# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os
class AmazonAsinPipeline(object):
    def process_item(self, item, spider):
        return item


class saveToCsv(object):
    def __init__(self):
        os.chdir("./detail_page")  #新建一个文件夹，用来保存爬取的详情页信息的，
        self.file = csv.writer(open('detail_1007_28500.csv', 'a', newline='', encoding='utf-8'))
        ## 设置文件名称，进行保存。。
        # self.file.writerow('ASIN，keyword，commodity_item，brandName，price，comments，star_level，ranking，DATE'.split('，'))
    def process_item(self, item, spider): #不写表头了，
        data = []
        for each in dict(item).values():
            if each:
                data.append(each)
            else:
                data.append('null')
        self.file.writerow(data)
        return item

    #以下为固定地点监测写法,监测爬虫关闭
    def close_spider(self,spider):
        os.chdir("../")
        print('存储CSV文件结束')

# import pymysql
#
# from Amazon_ASIN import settings
# class saveToMysql(object):
#     def __init__(self):
#         self.connection = pymysql.connect(
#             host=settings.MYSQL_HOST,
#             user='root',
#             port=3306,
#             password='1234',
#             db=settings.MYSQL_DBNAME,
#             charset='utf8')
#         self.cursor = self.connection.cursor()
#         # sql = 'create table jobInfo(id int(11) primary key auto_increment,jobname varchar(50),company varchar(100),address varchar(50),salary  varchar(50),pdate    varchar(50))default charset utf8;'
#         # self.cursor.execute(sql)
#         # self.connection.commit()
#
#     count = 0
#
#     def process_item(self, item, spider):
#         data_3 = dict()
#         for key_1, value_1 in item.items():
#             if value_1:
#                 data_3[key_1] = value_1
#             else:
#                 #print(key_1, 'null')
#                 data_3[key_1] = 'null'
#         #print(data_3)
#
#         sql_4 = "insert into detail_out(ASIN,keyword,commodity_item,brandName,price,comments,star_level,ranking,`DATE`) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
#             data_3["ASIN"], data_3['keyword'], data_3['commodity_item'], data_3['brandName'], data_3['price'],
#             data_3['comments'], data_3['star_level'], data_3['ranking'], data_3['DATE'])
#         #print(sql_5)
#
#         try:
#             # 执行sql语句
#             self.cursor.execute(sql_4)  # 执行sql语句 游标执行
#             # 执行sql语句
#             self.connection.commit()  # 连接提交
#         except:
#             # 发生错误时回滚
#             self.connection.rollback()
#
#         return item
#
#     def close_spider(self, spider):
#         # self.connection.commit()  # 连接提交
#         self.cursor.close()
#         self.connection.close()
#         print('mysql 存储完成')