#!D:\python\python.exe
# -*- coding: UTF-8 -*-
# print "Content-type:text/html;charset=gbk"
print 
from db import*
import urllib2
import urllib
import re
db=DB()
# 封装类库
class News:

    #init
    def __init__(self):
        self.url = "http://news.baidu.com/"

    #convert div to ''
    def tranTags(self, x):
        pattern = re.compile('<div.*?</div>')
        res = re.sub(pattern, '', x)
        return res

    #抓取整个页面
    def getPage(self):
        url = self.url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    #抓取整个导航
    def getNavCode(self):
        page = self.getPage()
        pattern = re.compile('(<div id="menu".*?)<i class="slogan"></i>', re.S)
        navCode = re.search(pattern, page)
        return navCode.group(1)
    def removerdiv(self,div):
        newsres = re.sub('<div class=".*?">.*?</div>',"",div)
        return newsres
    #再次筛选导航内容
    def getNav(self):
        navCode = self.getNavCode()
        pattern = re.compile('<a href=("http://.*?/).*?>(.*?)</a>', re.S)
        itmes = re.findall(pattern, navCode)
        newitems=self.getTitles(itmes)
        return self.removerdiv(newitems)
     #抓取整个新闻内容的标题
    def getTitle(self):
        result=self.getPage()
        pattern = re.compile('<div id="pane-news".*?>(.*)<div class=".*?" id="tupianxinwen">', re.S)
        res = re.search(pattern, result)
        return res.group()
		#再次赛选标题内容
    def getChild(self):
        result=self.getTitle()
        pattern = re.compile('<span class="dot"></span>.*?<a href=("http://.*?/).*?>(.*?)</a>', re.S)
        itmes = re.findall(pattern,result)
        return self.getTitles(itmes)
    def getTitles(self,res):
        string=''
        for index in res:
            string+="("+"'"+index[0].lstrip('"')+"'"+","+"'"+index[1]+"'"+")"+","
            # string+="("+"'"+index[0].lstrip('"')+"'"+","+"'"+index[1]+"'"+")"+","
        return string.rstrip(',')    

news = News()
res=news.getNav()
# print res
sql="insert into baidunews (url,name) values"+res
# print sql
print db.my_add(sql)
# print sql
# 采集整个新闻内容的标题 入库











# 简单的方法
# User='User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2914.3 Safari/537.36'
# response = urllib2.urlopen("http://news.baidu.com/")
# content = response.read()
# pattern = re.compile('(<div id="menu".*?)<i class="slogan"></i>', re.S)
# nav = re.search(pattern, content)
# print nav.group()