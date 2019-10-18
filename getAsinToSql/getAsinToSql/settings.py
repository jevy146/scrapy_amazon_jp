# -*- coding: utf-8 -*-

# Scrapy settings for getAsinToSql project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'getAsinToSql'

SPIDER_MODULES = ['getAsinToSql.spiders']
NEWSPIDER_MODULE = 'getAsinToSql.spiders'


import pandas as pd
def open_to_excel(path):  # 搜索关键字的文件。
   df_file = pd.read_excel(path,sheet_name=0,encoding="utf-8")  # 这样就把表头读取成了第一行了
     # 将关键字这一列提取出来，，转成列表。
   return list(df_file.search_word.values)

Path = "./seed_words/词频.xlsx"
# df_file = pd.read_csv(Path)  # 这样就把表头读取成了第一行了
# print(df_file.result_word.values)
KEYWORD = open_to_excel(Path)  # 设置为字段列表的形式。
KEYWORDS = KEYWORD[3800:3900]
print("KEYWORDS:",KEYWORDS)
# KEYWORDS = ["Winterhandschuhe"]
MAX_PAGE = 3


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'getAsinToSql (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

RANDOMIZE_DOWNLOAD_DELAY = True
'''
https://www.cnblogs.com/xueli/p/7250537.html  对setting的解释
'''
# from scrapy.contrib.throttle import AutoThrottle
AUTOTHROTTLE_ENABLED = True
#起始的延迟
AUTOTHROTTLE_START_DELAY = 5
#最小延迟
DOWNLOAD_DELAY = 3
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
CONCURRENT_REQUESTS = 3#类似于线程数量。。默认是16，一下子提交16个强求。。


DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',

}

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
#    'getAsinToSql.middlewares.GetasintosqlSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html

# HTTP_PROXY = 'http://127.0.0.1:8123'

DOWNLOADER_MIDDLEWARES = {
   'getAsinToSql.middlewares.GetasintosqlDownloaderMiddleware': 543,
   # 'getAsinToSql.middlewares.ProxyMiddleware': 410,  #这个是使用8123的端口。。
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}  #开启中间件的，，放cookie和IP还有浏览器头部的。。


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html


ITEM_PIPELINES = {
   # 'getAsinToSql.pipelines.GetasintosqlPipeline': 300,
   # 'getAsinToSql.pipelines.saveToMysql': 400,
   'getAsinToSql.pipelines.SaveToCsv': 400,
}

# MYSQL_HOST = '192.168.31.104'
# MYSQL_DBNAME = 'amazon_jp'
# MYSQL_USER = 'root'
# MYSQL_PASSWD = '1234'
# MYSQL_PORT = 3306
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
