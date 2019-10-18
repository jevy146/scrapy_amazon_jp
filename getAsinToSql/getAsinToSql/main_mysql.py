# @File  : main_mysql.py
# @Author: Jie Wei
#@time: 2019/8/28 15:11


from scrapy import cmdline
cmdline.execute("scrapy crawl AsinToMySql".split(" "))#有日志的输出。