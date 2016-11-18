#!D:\python\python.exe
# -*- coding: UTF-8 -*-

#把配置文件读取过来
from config import *
#数据库模块
import MySQLdb
# python的数据库类
class DB:
	mydb = ''
	#自动化链接数据库
	def __init__( self ):
			#数据库的链接地址
			db_connect = dbconfig['HOST']
			#链接数据库的用户名
   			db_username = dbconfig['ROOT']
   			#链接数据库的密码
   			db_password = dbconfig['PWD']
   			#数据库的名称
   			db_base = dbconfig['DATABASE']
   			if( DB.mydb == '' ):
   				db = MySQLdb.connect(db_connect, db_username, db_password, db_base)
   				DB.mydb=db
   	#获取操作游标
   	def my_cursor( self ):
   			cursor = self.mydb.cursor()
   			return cursor
   	#执行sql语句
   	#参数需要
   	def my_exe( self, sql ):
   			cursor=self.my_cursor()
   			res=cursor.execute( sql )
   			return res
   	#查询所有
   	def my_all( self,table):
   			sql="SELECT * FROM %s" % table
   			res=self.my_exe(sql)
   			#result=res.fetchall()
   			return res
   	#修改数据
   	def my_save( self,sql):
   			res=self.my_exe(sql)
   			return res
   	def my_add(self,sql):
   			res = self.my_exe(sql)
   			return res
