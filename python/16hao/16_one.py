#!D:\python\python.exe
# -*- coding: UTF-8 -*-

print "Content-type:textml"
print                               # 空行，告诉服务器结束头部
# CGI处理模块
import cgi, cgitb 
#数据库模块
import MySQLdb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
username = form.getvalue('username')
userpwd  = form.getvalue('userpwd')
usertpwd  = form.getvalue('usertpwd')
useremail  = form.getvalue('useremail')
usercell  = form.getvalue('usercell')
userphone  = form.getvalue('userphone')
userid  = form.getvalue('userid')
userqq  = form.getvalue('userqq')
# 打开数据库连接
db = MySQLdb.connect("127.0.0.1","root","root","python" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO users (username,userpwd,usertpwd,useremail,usercell,userphone,userid,userqq) values ("+"'"+username+"'"+","+"'"+userpwd+"'"+","+"'"+usertpwd+"'"+","+"'"+useremail+"'"+","+"'"+usercell+"'"+","+"'"+userphone+"'"+","+"'"+userid+"'"+","+"'"+userqq+"'"+")"
try:
   # 执行sql语句
   if(cursor.execute(sql)):
   		print("<script>alert('添加成功');location.href='./16_one_show.py'</script>")
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()

