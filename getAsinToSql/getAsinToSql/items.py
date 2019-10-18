# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetasintosqlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    keyword = scrapy.Field()
    url = scrapy.Field()
    search_num = scrapy.Field()
    link_detail = scrapy.Field()  # 放详情页链接。
    pass
