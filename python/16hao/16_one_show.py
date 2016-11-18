#!D:\python\python.exe
# -*- coding: UTF-8 -*-

print "Content-type:textml;charset=UTF-8"
print                               # 空行，告诉服务器结束头部

from db import*
#CGL处理模块
import cgi,cgitb
#创建fieldstorsge 的模块
form = cgi.FieldStorage()
#正则
import re
# 获取数据
username = form.getvalue('username')
userpwd  = form.getvalue('userpwd')
usercell  = form.getvalue('usercell')
userphone  = form.getvalue('userphone')
userid  = form.getvalue('userid')
userqq  = form.getvalue('userqq')
#对用户名进行验证
a=re.compile('^[0-9a-z]{5,9}$')
q=a.match(username)
if(q):
    print(ok)
else:
    print("必须由5到10位数字或者字母组成，不允许数字开头")
# #对密码进行验证
# b=re.compile('^\w{6}$')
# w=b.match(userpwd)
# if(w):
#     print(ok)
# else:
#     print("密码必须在6位以上")
# #对手机号进行验证
# c=re.compile('^1[538][0-9]{9}$')
# e=c.match(usercell)
# if(e):
#     print(ok)
# else:
#     print("必须是11位数字组成，以15,18,13开头")
# #对电话进行验证
# d=re.compile('^\d{3}-\d{8}$')
# r=d.match(userphone)
# if(r):
#     print(ok)
# else:
#     print("必须是010-68801717，前面是三位的区号，后面8位的电话号，中间是-")
#  #对身份证号进行验证   
# e=re.compile('^\d{13}$')
# t=e.match(userid)
# if(t):
#     print(ok)
# else:
#     print("必须是13数字组成，18位的数字")
#  #对qq号进行验证   
# f=re.compile('^\d{8,11}$')
# y=f.match(userqq)
# if(y):
#     print(ok)
# else:
#     print("必须是8到11位数字组成")
#执行添加操作
sql = "INSERT INTO users (username,userpwd,usercell,userphone,userid,userqq) values ("+"'"+username+"'"+","+"'"+userpwd+"'"+","+"'"+usercell+"'"+","+"'"+userphone+"'"+","+"'"+userid+"'"+","+"'"+userqq+"'"+")"
# print sql
one=DB()
print(one.my_add(sql))