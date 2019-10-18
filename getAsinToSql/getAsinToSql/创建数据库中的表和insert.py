# @File  : test02-创建数据库和insert.py
# @Author: Jie Wei
#@time: 2019/8/26 15:04
import pymysql

# 打开数据库连接  在同一个数据中创建不同的表。

connection = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        password='1234',
        db='amazon_jp',  ## 同不同数据库，针对不同的表  例如："hanxin"
        charset='utf8')  # 连接数据库
cursor = connection.cursor()  #创建游标

# 使用cursor()方法获取操作游标

# 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql= """CREATE TABLE  amazon_jp_link(
            link_id int primary key auto_increment,
            keyword VARCHAR(255),
            link_detail VARCHAR(255),
            search_num VARCHAR(255),
            url VARCHAR(255)
        )default charset=utf8;"""
#  utf8上没有双引号  #最后一条是没有逗号的。。
print(sql)
cursor.execute(sql )  #执行了之后 要提交事务
# cursor.execute(sql_3)
#提交
connection.commit() # 数据库连接提交事务
# 先关闭游标
cursor.close()
# 关闭数据库连接
connection.close()

