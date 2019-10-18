# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class AmazonAsinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
import random
from fake_useragent import UserAgent

import base64
import time
    # 代理服务器
# proxyServer = "http://http-dyn.abuyun.com:9020"
#
#
# # 代理隧道验证信息
# proxyUser = "HIX9H33N87639FSD"
# proxyPass = "580D452C7B02267E"
#
#     # for Python3
# proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")
#




import json




# from scrapy.conf import settings


class AmazonAsinDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    def read_cookies(self):
        # 设置cookies前必须访问一次百度的页面
        # driver.get("http://www.baidu.com")
        # jar = RequestsCookieJar()
        with open(r"E:\杨杰伟传来文件\0906-日本站已整理好\0906-日本站已整理好\getAsinToSql\getAsinToSql\cookies_17.txt", "r") as fp:
            cookies = json.load(fp)
            cookie = [item["name"] + ":" + item["value"] for item in cookies]
            cookMap = {}
            for elem in cookie:
                str = elem.split(':')
                cookMap[str[0]] = str[1]
            print(f"在CookiesMiddleware使用的cookMap = {cookMap}")
            return cookMap


    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        ua = UserAgent()
        USER_AGENT = ua.chrome # 任意头文件
        # print(USER_AGENT)
        request.headers['User-Agent'] = USER_AGENT


        ## 增加IP地址。
        # request.meta["proxy"] = proxyServer
        # # print("IP", proxyServer)
        # request.headers["Proxy-Authorization"] = proxyAuth

        '''使用Tor代理服务器,伪装本地的IP
        a = requests.get("http://checkip.amazonaws.com").text
          # a的格式是IP   ，端口默认是9151
        port=9151
        proxy = 'http://' + '%s:%s' % (a.strip(), port)  #输出的格式为 {'http': '64.113.32.29:9150'}
        print("正在使用的IP：", proxy)
        request.meta['proxy']=proxy
        
        不是这么使用的。。
            '''



        # print("代理Tor IP",settings.get('HTTP_PROXY'))

        # request.meta['proxy'] = settings.get('HTTP_PROXY')


        # cookies = self.read_cookies()
        # cookie_jar = cookies
        # # print("cookie_jar", cookie_jar)
        # request.cookies = cookie_jar

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        print('DownloaderMiddleware返回状态码：', response.status)
        time.sleep(1.5)
        if response.status==200:
            return response
        else:
            return

        # else:
        #     print('DownloaderMiddleware重新请求：')
        #     ua = UserAgent()
        #     USER_AGENT = ua.chrome  # 任意头文件
        #     print(USER_AGENT)
        #     request.headers['User-Agent'] = USER_AGENT
        #     return request




    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        print('代理%s，访问%s出现异常:%s' % (request.meta['proxy'], request.url, exception))

        time.sleep(1)
        # proxy = self.get_random_ip() #重新选一个IP用。
        # request.meta['proxy'] = proxy
        # request.meta["proxy"] = proxyServer
        # # print("重新增加IP", proxyAuth)
        # request.headers["Proxy-Authorization"] = proxyAuth

        ua = UserAgent()
        USER_AGENT = ua.chrome  # 任意头文件
        print(USER_AGENT)
        request.headers['User-Agent'] = USER_AGENT
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)






