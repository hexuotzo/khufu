#!/usr/bin/python
# -*- coding: utf8 -*-
import urllib
import urllib2
import re
import os
import time
import sys

url = "http://baby.sina.com.cn"

index_dic_type_one = {
    "zhyq":{'url':'zb.html','re':('<ul class="jk_menu_1">(.*?)</ul>',),'link':('<a href="(.*?)">(.*?)</a>',),},
    "fmq":{'url':'sc.html','re':('<ul class="jk_menu_1">(.*?)</ul>',),'link':('<a href="(.*?)">(.*?)</a>',),},
    "xlq":{'url':'zb.html','re':('<ul class="jk_menu_1">(.*?)</ul>',),'link':('<a href="(.*?)">(.*?)</a>',),},
}

index_dic_type_two = {
    "hyq":{'url':'eq/fy.html','re':('<ul class="jk_menu_1">(.*?)</ul></div>',),'link':('<a href="(.*?)">(.*?)</a>',),},
    "xsr":{'url':'1_w/zb.html','re':('<ul class="jk_menu_1">(.*?)</ul></div>',),'link':('<a href="(.*?)">(.*?)</a>',),},
    "yrq":{'url':'1_3/zb.html','re':('<ul class="jk_menu_1">(.*?)</ul></div>',),'link':('<a href="(.*?)">(.*?)</a>',),},
    "yourq":{'url':'1_2/lc.html','re':('<ul class="jk_menu_1">(.*?)</ul></div>',),'link':('<a href="(.*?)">(.*?)</a>',),},
}

def reg(reg,html):
    p = re.compile(reg)
    return p.findall(html)

def getHtml(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; zh-CN; rv:1.9.0.1) Gecko/2008070206 Firefox/3.0.1')
    request.add_header('Accept','application/x-shockwave-flashapplication/x-shockwave-flash,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    l_proxy_info = {
        'host' : "localhost",
        'port' : 8000
    }
    l_proxy_support = urllib2.ProxyHandler({"http" : \
        "http://%(host)s:%(port)d" % l_proxy_info})
    l_opener = urllib2.build_opener(l_proxy_support, urllib2.HTTPHandler)
    urllib2.install_opener(l_opener)
    # opener = urllib2.build_opener()
    feeddata = l_opener.open(request).read()
    return feeddata

def analyzier(url):
    return getHtml(url).replace("\r","").replace("\n","").replace("\t","")

def getDatalinks(html):
    datalinks_reSyntax = r'data_p\[\d+\]\[0]=\'(.*?)\';data_p\[\d+\]\[1]=\'(.*?)\';'
    return reg(datalinks_reSyntax, html)

def getData(title,url):
    html = analyzier(url)
    data_reSyntax = r'<!--.*BEGIN-->(.*?)<!--.*END-->'
    return reg(data_reSyntax, html)
    
def analy_list(lists):
    for data_list in lists:
        try:
            print '\t\t\t'+data_list[0].decode('gbk'), "http://baby.sina.com.cn"+data_list[1]
        except:
            print '\t\t\t'+data_list[0], "http://baby.sina.com.cn"+data_list[1]
        #开始抓每页内容
        try:
            print getData(data_list[0],"http://baby.sina.com.cn"+data_list[1])[0].decode('gbk')
        except:
            continue
        # break