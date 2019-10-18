# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonAsinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # keyword = scrapy.Field()
    # search_num = scrapy.Field()
    # link_detail = scrapy.Field()  # 放详情页链接。


    ASIN = scrapy.Field()  # 备份的ASIN。
    keyword = scrapy.Field()  # 备份的ASIN。
    commodity_item = scrapy.Field()  # 商品名称。
    brandName = scrapy.Field()  # #品牌卖家
    price = scrapy.Field()  # 价格
    comments = scrapy.Field()  # 评论数。
    star_level = scrapy.Field()  # 星级
    ranking = scrapy.Field()  # 排名
    DATE = scrapy.Field()  # ASIN码。
    pass
