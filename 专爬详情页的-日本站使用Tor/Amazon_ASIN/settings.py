# -*- coding: utf-8 -*-

# Scrapy settings for Amazon_ASIN project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Amazon_ASIN'

SPIDER_MODULES = ['Amazon_ASIN.spiders']
NEWSPIDER_MODULE = 'Amazon_ASIN.spiders'


# import pymysql
# # 打开数据库连接
# connection = pymysql.connect(
#     host = '192.168.31.104',
#     #host='localhost',
#     user='root',
#     password='1234',
#     db='amazon_jp',  ## 同不同数据库，针对不同的表  例如："hanxin"
#     charset='utf8')  # 连接数据库
# cursor = connection.cursor()  # 创建游标
# sql_1 = "select keyword,link_detail from amazon_jp_link limit 0,20;"  #从第一行开始截取3个，1,2,3，
# cursor.execute(sql_1)
# LINK_DETAIL = cursor.fetchall()  ## 获取所有数据 返回的是一个元组
# LINK_DETAIL=LINK_DETAIL[10:13]
# # LINK_DETAIL=(('bluetooth+イヤホン', 'https://www.amazon.co.jp/dp/B07PZ6SL49'), ('bluetooth+イヤホン', 'https://www.amazon.co.jp/dp/B077JN968F'))
#
# print(LINK_DETAIL)

import pandas as pd
def open_csv(path):  # 搜索关键字的文件。
    file_china = open(path,encoding='utf-8') #路径里面有中文。。
    df_file = pd.read_csv(file_china)  # 这样就把表头读取成了第一行了
    link_detail =zip(df_file.keyword.values,df_file.link_detail.values)    # 将关键字这一列提取出来，，转成列表。
    return link_detail

Path = r"E:\杨杰伟传来文件\0906-日本站已整理好\0906-日本站已整理好\getAsinToSql\getAsinToSql\detail_page\amazon_jp_0918_50.csv"
link_detail = open_csv(Path)  # 将详情页的链接获取下来。相关信息从中解析。
LINK_DETAIL = list(link_detail)[34500:35000]

print(LINK_DETAIL)








DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',

}

#对失败的HTTP进行重新请求（重试）会减慢爬取速度，因此可以禁止重试。在配置文件中编写：

RETRY_ENABLED = False
#生成随机数，浮点类型
#a = random.uniform(2, 4)
#控制随机数的精度round(数值，精度)
#print(round(a, 2))
#DOWNLOAD_DELAY = round(a, 2)  # 延缓爬取的时间。。有两位小数
RANDOMIZE_DOWNLOAD_DELAY = True
'''
https://www.cnblogs.com/xueli/p/7250537.html  对setting的解释
'''
# from scrapy.contrib.throttle import AutoThrottle
AUTOTHROTTLE_ENABLED = True
#起始的延迟
AUTOTHROTTLE_START_DELAY = 4
#最小延迟
DOWNLOAD_DELAY = 2
#最大延迟
AUTOTHROTTLE_MAX_DELAY = 10
#每秒并发请求数的平均值，不能高于 CONCURRENT_REQUESTS_PER_DOMAIN或CONCURRENT_REQUESTS_PER_IP，调高了则吞吐量增大强奸目标站点，调低了则对目标站点更加”礼貌“
#每个特定的时间点，scrapy并发请求的数目都可能高于或低于该值，这是爬虫视图达到的建议值而不是硬限制
AUTOTHROTTLE_TARGET_CONCURRENCY = 5 # 平均每秒并发数 原先值为16
#调试
AUTOTHROTTLE_DEBUG = True
CONCURRENT_REQUESTS_PER_DOMAIN = 5 #单个域名的请求数，，原先值为16
CONCURRENT_REQUESTS_PER_IP =5    # 单个IP的并发请求数，原先值为16

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 配置Scrapy执行的最大并发请求（默认值：16）
CONCURRENT_REQUESTS = 4 #类似于线程数量。。默认是16，一下子提交16个强求。。

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Amazon_ASIN (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# RANDOMIZE_DOWNLOAD_DELAY = True
#
# COOKIES_ENABLED = False  #不启用cookie
#
# '''https://blog.csdn.net/ZF98095/article/details/87624578,设置爬取的速度'''
# #遵守robots协议
# ROBOTSTXT_OBEY = False
# #并发请求个数（越小越慢）
# CONCURRENT_REQUESTS = 1
# #下载延迟时间（越大请求越慢）
# DOWNLOAD_DELAY = 5
# #默认False;为True表示启用AUTOTHROTTLE扩展
# AUTOTHROTTLE_ENABLED = True
# #默认3秒;初始下载延迟时间
# AUTOTHROTTLE_START_DELAY = 5
# #默认60秒；在高延迟情况下最大的下载延迟
# AUTOTHROTTLE_MAX_DELAY = 15
# #使用httpscatch缓存
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 1
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'







# from scrapy.contrib.throttle import AutoThrottle
# AUTOTHROTTLE_ENABLED = True
#起始的延迟
# AUTOTHROTTLE_START_DELAY = 5
#最小延迟
# DOWNLOAD_DELAY = 3
#最大延迟
# AUTOTHROTTLE_MAX_DELAY = 15
#每秒并发请求数的平均值，不能高于 CONCURRENT_REQUESTS_PER_DOMAIN或CONCURRENT_REQUESTS_PER_IP，调高了则吞吐量增大强奸目标站点，调低了则对目标站点更加”礼貌“
# #每个特定的时间点，scrapy并发请求的数目都可能高于或低于该值，这是爬虫视图达到的建议值而不是硬限制
# AUTOTHROTTLE_TARGET_CONCURRENCY = 5  # 平均每秒并发数 原先值为16
# #调试
# AUTOTHROTTLE_DEBUG = True
# CONCURRENT_REQUESTS_PER_DOMAIN = 5  #单个域名的请求数，，原先值为16
# CONCURRENT_REQUESTS_PER_IP = 5    # 单个IP的并发请求数，原先值为16

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 配置Scrapy执行的最大并发请求（默认值：16） 类似于线程数
# CONCURRENT_REQUESTS = 2


# DEFAULT_REQUEST_HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'max-age=0',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
#
# }


# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Amazon_ASIN.middlewares.AmazonAsinSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html




# HTTP_PROXY = 'http://127.0.0.1:9150'  这个方法行不通。。

DOWNLOADER_MIDDLEWARES = {
   'Amazon_ASIN.middlewares.AmazonAsinDownloaderMiddleware': 543,
   # 'Amazon_ASIN.middlewares.ProxyMiddleware': 410,
}


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'Amazon_ASIN.pipelines.AmazonAsinPipeline': 300,
   'Amazon_ASIN.pipelines.saveToCsv': 400,
   # 'Amazon_ASIN.pipelines.saveToMysql': 300,  #数值越大越优先。。。
}

MYSQL_HOST = '192.168.31.104'
MYSQL_DBNAME = 'amazon_jp'
MYSQL_USER = 'root'
MYSQL_PASSWD = '1234'
MYSQL_PORT = 3306
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
