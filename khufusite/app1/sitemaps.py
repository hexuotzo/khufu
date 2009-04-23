# encoding: utf-8
from django.contrib.sitemaps import Sitemap
from datetime import datetime
import pycabinet
import random

class KhufuSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        dbname = '/home/yanxu/khufu/infodb/infodb'
        data = pycabinet.search(dbname,'tag1','怀孕',1000)
        res = []
        for i in range(20):
            obj = random.choice(data)
            res.append(obj)
        return res

    def location(self,obj):
        return "http://www.zaojiao100.com/v/%s/" % obj["kid"]

    def lastmod(self, obj):
        return datetime.strptime(obj["savedate"],'%Y-%m-%d')


