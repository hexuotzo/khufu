#!/usr/local/bin/python
#encoding: utf-8
import re
import os
from html2text import html2text

def getbody(html):
    bodys = re.findall(r'''.*<!--正文-->(.*)<!--内容分页-->''',html,re.S|re.M|re.L)
    if len(bodys)>0:
        return html2text(bodys[0])
    return html2text(html)
if __name__ == '__main__':
    url = "http://www.zaojiao.com/education/2008/0516/article_1630.html"
    html = os.popen("curl --compressed %s" % url).read()
    print getbody(html)