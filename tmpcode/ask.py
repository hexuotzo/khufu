#encoding: utf-8
import re
from html2text import html2text

def ask(html):
    #问题:
    st = {
        '问题':[r'<div class="f14B">(\S+)</div>',0],
        '问题补充':[r'<div class="f14">(\S+)</div>',0],
        '答案':[r'<div class="f14">(\S+)</div>',1],
        '提问者':[r'提问者：(.*)',0],
        '提问时间':[r'提问时间：(.*)',0],
        '回答者':[r'回答者：(.*)',0],
        '回答时间':[r'回答时间：(.*)',0],
    }
    result = {}
    for k,v in st.items():
        t = html2text(re.findall(v[0],html)[v[1]].decode("utf8"))
        result[k] = t
    return result

if __name__ == '__main__':
    import urllib2
    url = 'http://www.zaojiao.com/ask/q38729.html'
    html = urllib2.urlopen(url).read()
    for k,v in ask(html).items():
        print k,v
        print