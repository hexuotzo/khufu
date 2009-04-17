# encoding: utf-8

from django.utils.encoding import smart_unicode,force_unicode,smart_str
from django.http import HttpResponse
from django.utils import feedgenerator
import os
import cjson
try:
    import cmemcache as memcache
except:
    import memcache

def removetext(text):
    text=smart_str(text,"utf8")
    text=text.replace("-育儿早教-中国早教网","")
    text=text.replace("-怀孕胎教-中国早教网","")
    return smart_unicode(text)

def rss(request):
    mc = memcache.Client(['boypark.cn:11211'])
    cmd = 'dystmgr search -nl -max 20 /home/yanxu/khufu/khufu 备孕'
    f = feedgenerator.Rss201rev2Feed(
        title = "早教知识网-全国唯一的早教知识查询、搜索网站 育儿 早教 健康 胎教 怀孕",
        link = "http://www.zaojiao100.com/rss/",
        description = "早教知识网是全国唯一的早教知识查询网站.为父母提供权威,安全,免费的怀孕分娩,胎教,育儿,保健,喂养,常见病护理知识,早教知识.年轻父母可以在这里找到与婴幼儿发育,成长,教育有关的全部知识和咨询。"
    )
    for kid in os.popen(cmd).read().split('\n'):
        obj=mc.get(kid)
        if obj==None:continue
        obj=cjson.decode(mc.get(kid))
        f.add_item(title=u"%s" % removetext(obj['title']),
                link=u"http://www.zaojiao100.com/v/%s/" % kid,
                description=u"%s" % obj['body']
        )
    return HttpResponse(f.writeString('UTF-8'))
