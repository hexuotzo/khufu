#encoding: utf-8
from twill import *
import random
import cmemcache as memcache
import pycabinet
import cjson

def removetext(text):
    text=text.encode("utf8")
    text=text.replace("-育儿早教-中国早教网","")
    text=text.replace("-怀孕胎教-中国早教网","")
    text=text.replace("-新闻资讯-中国早教网","")
    text=text.replace("-中国早教网","")
    return text


def randompages():
    data = pycabinet.search('../infodb/infodb',"tag1","怀孕",20000)
    for i in range(2):
        mc = memcache.Client(['boypark.cn:11211'])
        obj = random.choice(data)
        d = cjson.decode(mc.get(obj['kid']))
        yield obj['kid'],removetext(d['title']),d['body'].encode("utf8")

def login():
    return '''
go http://www.douban.com/login
showforms
fv 2 form_email zaojiao100@gmail.com
fv 2 form_password 123456
submit
    '''

cmd = '''
go http://www.douban.com%snew_topic
fv 2 rev_title "%s"
fv 2 rev_text """http://www.zaojiao100.com/v/%s/\n%s"""
showforms
submit
'''

groups = ['/group/yuer/', '/group/Babymamy/', '/group/38772/', '/group/youngman/', '/group/17444/', '/group/mother/', '/group/babyangel/', '/group/73952/', '/group/baobao/', '/group/hunxuebaobao/', '/group/mamab/', '/group/16020/', '/group/16086/', '/group/34832/', '/group/babe/', '/group/159320/']

execute_string( login() )
for kid,title,text in randompages():
    print title,text[:20]
    for g in groups:
        print cmd%(g,title,kid,text) 
        print execute_string( cmd % (g,title,kid,text) )
