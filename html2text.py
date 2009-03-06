import re

def html2text(html):
    html=re.sub(r"\&[a-zA-Z]{1,10};",'',html)
    html=re.sub(r"<[^>]*>",'',html)
    html=re.sub(r"[(\/>)<]",'',html)
    return html

if __name__ == '__main__':
    import urllib
    html=urllib.urlopen('http://www.douban.com/review/1054750/').read()
    print html2text(html)