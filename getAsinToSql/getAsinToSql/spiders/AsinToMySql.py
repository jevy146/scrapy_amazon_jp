# -*- coding: utf-8 -*-
import scrapy

from getAsinToSql.items import GetasintosqlItem
from scrapy.selector import Selector




'''要修改一下，，保存为csv文件，洋葱头方法要重写一下09-05'''


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

class AsintomysqlSpider(scrapy.Spider):
    name = 'AsinToMySql'
    allowed_domains = ['www.amazon.co.jp']
    # start_urls = ['http://www.amazon.de/']

    def start_requests(self):
        count = 0
        for index,keyword in enumerate(self.settings.get('KEYWORDS')):
            print("爬取第{}个关键字{}".format(index,keyword))
            keyword=keyword.replace(" ","+") #将空格替换成加号
            for page in range(1, self.settings.get('MAX_PAGE') + 1):  #MAX_PAGE=2
                url = f'https://www.amazon.co.jp/s?k={keyword}&page={page}&ref=nb_sb_noss'
                print("开始抓取首页网址：",url)

                ip = requests.get("http://checkip.amazonaws.com").text
                print("第", count + 1, "次IP：", ip)  # 查看包装的IP是
                count += 1
                controller.signal(Signal.NEWNYM)

                yield scrapy.Request(url=url, dont_filter=True,
                                     callback=self.parse,
                                     meta={'keyword': keyword,"url":url},

                                     )
                time.sleep(1)


    def parse(self, response):
        keyword = response.meta['keyword']
        url=response.meta['url']
        commodity_item = GetasintosqlItem()  # 实例化对象
        print("keyword=", keyword)
        commodity_item["keyword"] = keyword
        commodity_item["url"] = url
        if response.status == 200:
            selector = Selector(response)
            # 判断地址的
            address = selector.xpath('//*[@id="glow-ingress-line2"]/text()').extract_first()  # 获取邮编的地址，，
            print("首页的address=", address)  # 查看邮编地址。。。
            '''['01067\u200c Dresden']'''
            if address==None :
                print("重新加载首页，，，")
                yield scrapy.Request(url=commodity_item["url"],
                                     meta={'keyword': keyword, "url": url,},
                                     callback=self.parse, dont_filter=True,
                                     )
                time.sleep(2)
                return

            try:
                search_num=selector.css('#search > span > h1 > div > div.sg-col-14-of-20.sg-col-26-of-32.sg-col-18-of-24.sg-col.sg-col-22-of-28.s-breadcrumb.sg-col-10-of-16.sg-col-30-of-36.sg-col-6-of-12 > div > div > span:nth-child(1)').css("::text").extract_first()
                print("搜索量", search_num)
            except:
                search_num = "null"
            commodity_item["search_num"] = search_num
            # divs = selector.xpath(
            #     '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]//div[@class="a-section a-spacing-medium"]')

            divs = selector.xpath(
                    '//*[@id="search"]/div[@class="sg-row"]//div[@class="s-result-list s-search-results sg-row"]//div[@class="a-section a-spacing-medium"]')
            print("详情页链接的个数：", len(divs))  #有60个

            for num in  range(1,len(divs)+1):
                # 获取ASIN码
                ASIN=selector.xpath('//*[@id="search"]//div[@class="s-result-list s-search-results sg-row"]/div['+str(num)+']/@data-asin').extract()
                #print("ASIN",ASIN) # 编号从1开始。。
                #广告
                Advertisement=selector.xpath('//*[@id="search"]//div[@class="s-result-list s-search-results sg-row"]/div['+str(num)+']//span[@class="a-size-base a-color-secondary"]/text()').extract()

                if "スポンサー プロダクト" in Advertisement :  # 去掉广告，保留名牌产品。。
                    # print("----------",Advertisement)
                    # print("------ASIN-------", ASIN)
                    pass
                else:
                    # print("++++++++++++++++", Advertisement)
                    # print("+++++ASIN++++++", ASIN)
                    if ASIN[0] != '':
                        page_detail = "https://www.amazon.co.jp/dp/" + ASIN[0] #
                        commodity_item['link_detail'] = page_detail  # 保存 # 在item.py文件下。
                        yield commodity_item
                    # 在这里选出要爬取的详情页的链接个数。
                    # time.sleep(1)

