# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GetasintosqlPipeline(object):
    def process_item(self, item, spider):
        return item


import csv
import os
class SaveToCsv(object):
    def __init__(self):
        os.chdir("./detail_page")  #新建一个文件夹，用来保存爬取的详情页信息的，
        self.file = csv.writer(open('amazon_jp_0918_550.csv', 'a', newline='', encoding='utf-8'))
        ## 设置文件名称，进行保存。。
        # self.file.writerow('keyword，url，search_num，link_detail'.split('，'))
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
# from getAsinToSql import settings
# class saveToMysql(object):
#     def __init__(self):
#         self.connection = pymysql.connect(
#             host=settings.MYSQL_HOST,
#             user='root',
#             port=3306,
#             password='1234',
#             db=settings.MYSQL_DBNAME,  #amazon_jp 提前将数据库中的表建好
#             charset='utf8')
#         self.cursor = self.connection.cursor()
#         # sql = 'create table jobInfo(id int(11) primary key auto_increment,jobname varchar(50),company varchar(100),address varchar(50),salary  varchar(50),pdate    varchar(50))default charset utf8;'
#         # self.cursor.execute(sql)
#         # self.connection.commit()
#
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
#         sql_4 = "insert into amazon_jp_link(keyword,link_detail,search_num,url) values ('%s','%s','%s','%s')" % (
#             data_3["keyword"], data_3['link_detail'], data_3['search_num'], data_3['url'], )
#         print("在保存MySQL，，")
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