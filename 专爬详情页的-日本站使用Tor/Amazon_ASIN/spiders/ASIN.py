# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from Amazon_ASIN.items import AmazonAsinItem

import copy
import urllib.parse
import random

''' 使用Tor 洋葱头代理服务器，实现伪装IP '''
from stem import Signal
from stem.control import Controller
import socket
import socks
import requests
import time
controller = Controller.from_port(port=9151)  # 9151
controller.authenticate()
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)  # 8123  9150
socket.socket = socks.socksocket


class AsinSpider(scrapy.Spider):
    name = 'ASIN'
    allowed_domains = ['amazon.co.jp']
    def start_requests(self):
        commodity_item = AmazonAsinItem()  # 实例化对象 后面进行传递即可。。
        count=0
        for keyword_link_detail in self.settings.get('LINK_DETAIL'):
            if len(keyword_link_detail[1]) != 28:
                print("准备获取{}的内容".format(keyword_link_detail[1]))
                url = keyword_link_detail[1]
                commodity_item['ASIN']=url.split("/")[-1]
                commodity_item['keyword']=keyword_link_detail[0]

                ip = requests.get("http://checkip.amazonaws.com").text
                print("第", count + 1, "次IP：", ip)  # 查看包装的IP是
                count+=1
                controller.signal(Signal.NEWNYM)

                yield scrapy.Request(url=url, dont_filter=True,
                                         callback=self.parse_detail_page,
                                     meta={'item': copy.deepcopy(commodity_item)}
                                         )
                time.sleep(0)

    def parse_detail_page(self, response):

        commodity_info = response.meta['item']

        if response.status == 503:
            ip = requests.get("http://checkip.amazonaws.com").text
            print("503回调IP：", ip)  # 查看包装的IP是

            controller.signal(Signal.NEWNYM)
            yield scrapy.Request(url="https://www.amazon.co.jp/dp/" + commodity_info["ASIN"],
                                 meta={'item': copy.deepcopy(commodity_info), },
                                 callback=self.parse_detail_page, dont_filter=True,

                                 )
            time.sleep(random.randint(1, 4))

        elif response.status == 200:

            selector = Selector(response)
                # 详情页链接的在上一个函数已经提交到items了

            try:
                address = selector.xpath('//*[@id="glow-ingress-line2"]/text()').extract_first()  # 获取邮编的地址，，
                print("查看详情页的邮编。", address)  # 查看邮编地址。。。
            except:
                address="null"

            try:
                warning_text =selector.xpath('/html/body/center/span/text()').extract_first()
            except:
                warning_text=None
            print('warning_text:',warning_text)
            '''+++++++++++++++++++++++++++++++++++++++++++++++++++++增加一次代理'''
            if address == None or address == "null":
                # print("详情页代理重新运行。。",proxies)
                print("详情页链接重新运行。。",commodity_info["ASIN"] )

                if warning_text !=None:
                    print("18禁的内容")
                    return

                else:

                    ip = requests.get("http://checkip.amazonaws.com").text
                    print("回调IP：", ip)  # 查看包装的IP是

                    controller.signal(Signal.NEWNYM)
                    yield scrapy.Request(url="https://www.amazon.co.jp/dp/" + commodity_info["ASIN"],
                                     meta={'item': copy.deepcopy(commodity_info), },
                                     callback=self.parse_detail_page, dont_filter=True,

                                     )
                    time.sleep(random.randint(1, 4))
                    return


            try:
                commodity_item = selector.xpath('//span[@id="productTitle"]/text()').extract_first().replace("\n"," ").strip()  # 商品名称 将.strip()去掉了。
            except:
                commodity_item="null"

            if commodity_item=="null":
                print("产品为空的ASIN。", commodity_info["ASIN"])
                print("产品为空，，程序结束")
                ''' 判断是那种大海报类型的详情页，，程序结束。'''
                return

            commodity_info["commodity_item"] = commodity_item  # 商品名称

            try:
                brandName = selector.xpath('//a[@id="bylineInfo"]/text()').extract_first()  # 品牌名称
            except:
                brandName = "null"
            commodity_info["brandName"] = brandName  # 品牌卖家
                #print(111, brandName)
            try:
                price = selector.xpath('//*[@id="priceblock_dealprice"]/text()').extract_first()  # 并去掉特殊字符。。

                if price:
                    # print("正常。。。")
                    pass
                else:
                    print("价格位置··",price)  #price=None，，
                    price = selector.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first()
                    if price:
                        pass
                    else:
                        price = selector.xpath(
                            '//*[@id="olp_feature_div"]//span[@class="a-color-price"]/text()').extract_first()

                price="".join(price.split())  #去掉\xa0
            except:

                price = "null"

            commodity_info["price"] = price  # 商品价格

            try:
                comments = selector.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first()  # 评论数
            except:
                comments = "null"

            commodity_info["comments"] = comments  # 品论数量
            try:
                star_level = selector.xpath('//*[@id="reviewsMedley"]//span[@class="a-declarative"]/a/span/text()').extract_first()  # 星级 第二种写法，在页面上面的星级。
            except:
                star_level = 'null'

            commodity_info["star_level"] = star_level  # 品论数量
            '''
            total = selector.css('#prodDetails > div > div.column.col2 > div:nth-child(1) > div.secHeader > span').css("::text").extract_first()
            print("total=2=", total)  # 判断网页结构的
            '''
            try:
                total = selector.css("#prodDetails > h2").css("::text").extract_first()
                #print("结构标题", total)  # 判断网页结构的
            except:
                total = selector.css("#prodDetails > div.wrapper.DElocale > div.column.col2 > div:nth-child(1) > div.secHeader > span").css("::text").extract_first()
                #print("结构标题", total)  # 判断网页结构的 双保险的结构。

            if total != None:

                #右边的网络结构。
                try:
                    ranking = selector.css("#SalesRank > td.value").css("::text").extract_first().replace("\n"," ").strip()
                    print("++++++右边+++++++", ranking)
                    if ranking == "":
                        try:
                            ranking = selector.xpath('//*[@id="SalesRank"]//span[@class="zg_hrsr_rank"]').css(
                                "::text").extract_first()
                        except:
                            ranking = "null"
                except:
                    ranking = "null"
                commodity_info["ranking"] = ranking  # 排名

                try:
                    DATE = selector.xpath('//*[@id="prodDetails"]/div/div[2]//div[@class="pdTab"]/table/tbody/tr[@class="date-first-available"]/td[2]/text()').extract_first()
                except:
                    DATE = "null"
                #print(888, DATE)
                commodity_info["DATE"] = DATE  # 日期

            else:
                #左边的网络结构。。日本站的还没弄好。。
                try:
                    ranking = selector.css("#SalesRank::text").extract()[1].replace("\n"," ").strip()   #extract_first()获取第一个文本
                    print("-----左边------",ranking)
                    if ranking=="":
                        try:
                            ranking = selector.xpath('//*[@id="SalesRank"]//span[@class="zg_hrsr_rank"]').css(
                            "::text").extract_first()
                        except:
                            ranking = "null"
                except:
                    ranking="null"  #有种类似于海报的广告，，没有排名的。
                commodity_info["ranking"] = ranking  # 排名
                ul_lis = selector.xpath(
                    '//div[@id="detail_bullets_id"]//td[@class="bucket"]/div[@class="content"]//li')
                if ul_lis:
                    data_doc=ul_lis.xpath("./text()").extract()
                    list_clean = []
                    for each in data_doc:
                        each = each.strip()
                        if each != '':
                            list_clean.append(each)
                    print(list_clean)
                    commodity_info["DATE"] = list_clean  #将

                else:
                    commodity_info["DATE"] = 'null'

            yield commodity_info















