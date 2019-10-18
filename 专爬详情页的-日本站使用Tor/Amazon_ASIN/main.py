# @File  : main.py
# @Author: Jie Wei
#@time: 2019/8/1 15:35

from scrapy import cmdline
cmdline.execute("scrapy crawl ASIN".split(" "))#有日志的输出。

