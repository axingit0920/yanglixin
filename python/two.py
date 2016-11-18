#!D:\python\python.exe
# -*- coding: UTF-8 -*-

print "Content-type:textml"
print                               # 空行，告诉服务器结束头部

#数据库模块
import MySQLdb

# 连接数据库
db = MySQLdb.connect("127.0.0.1","root","root","python" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = "SELECT * FROM python_db"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      name = row[1]
      pwd = row[2]
      # 打印结果
      print "Name=%s,Password=%s" % \
             (name, pwd )
except:
   print "Error: unable to fecth data"