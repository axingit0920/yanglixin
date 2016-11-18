#!D:\python\python.exe
# -*- coding: UTF-8 -*-

print "Content-type:textml"
print   

import urllib2,urllib 
url = 'http://api.k780.com:88/?app=weather.future&weaid=1&&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json' 
data={'status':'read','rating':3,'tag':'小说'} 
data = urllib.urlencode(data) 
url2 = url + '?' + data # 跟post不同的只有这一句，使用?把url和data的内容连接起来，结果是https://api.douban.com/v2/book/user/ahbei/collections?status=read&rating=3&tag=小说 
response = urllib2.urlopen(url2) 
apicontent = response.read() 
print apicontent