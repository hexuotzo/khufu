# encoding : utf-8
from html2text import html2text
import os

def getbody(html):
    bodytxt=[]
    try:
        txt = html2text(html.decode('utf8'))
    except:
        txt = html2text(html.decode('gbk'))    
    try:
        txt = txt.encode('utf8').split('\n')
    except:
        txt = txt.encode('gbk').split('\n')
    for r in txt:
        r = r.strip()
        if r == '':continue
        elif r[0] == '[':
            if len(bodytxt) >= 5:break
            else:pass
        elif ']' in r[-4:] and len(bodytxt) < 5:pass
        elif r[:4] == '****':break
        elif r[5:]<chr(127):pass
        elif r[0].isdigit() and r[2] > chr(127):bodytxt.append(r)
        elif r[0] == '#' and r[1] != '#':
            try:
                if bodytxt[-1][0] == '#':bodytxt=[]
                else:bodytxt.append(r)
            except:
                bodytxt.append(r)
        elif r[:2] == '**':bodytxt.append(r)
        elif r[0] > chr(127):bodytxt.append(r)
        elif r[0] == '#' and len(bodytxt) >= 5:break
    return '\n'.join(bodytxt)
if __name__ == '__main__':
    url = "http://baby.sina.com.cn/edu/09/1303/0800133263.shtml"
    #url = "http://www.zaojiao.com/education/2007/1210/article_1308.html"
    #url = "http://news.163.com/09/0313/10/549ESDIR000136K8.html"
    #url = "http://wow.duowan.com/0903/100883030207.html"
    #testweblist:zaojiao,sina,163,wow
    html = os.popen("curl --compressed %s" % url).read()
    print getbody(html)