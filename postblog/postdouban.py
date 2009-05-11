from twill import *
import random
import cmemcache as memcache

def randompages():
    data = pycabinet.search(dbpath,"tag1","怀孕",20000)
    for i in range(2):
        mc = memcache.Client(['boypark.cn:11211'])
        obj = random.choice(data)
        d = mc.get(obj['kid'])
        yield d['title'],d['text']

cmd = '''
go http://www.douban.com/login
fv 2 form_email zaojiao100@gmail.com
fv 2 form_password 123456
submit
go http://www.douban.com%snew_topic
fv 2 rev_title "%s"
fv 2 rev_text "%s"
submit
'''

groups = ['/group/yuer/', '/group/Babymamy/', '/group/38772/', '/group/youngman/', '/group/17444/', '/group/mother/', '/group/babyangel/', '/group/73952/', '/group/baobao/', '/group/hunxuebaobao/', '/group/mamab/', '/group/16020/', '/group/16086/', '/group/34832/', '/group/babe/', '/group/159320/']

for g in groups:
    for title,text in randompages():
        print title
    # print execute_string( cmd % (g,title,text) )

