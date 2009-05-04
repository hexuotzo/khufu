# encoding: utf-8
from django.contrib.sitemaps import Sitemap
from datetime import datetime
import pycabinet
import random

class KhufuSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        menus = [
            "备孕",
            "怀孕",
            "产后",
            "0-1岁",
            "1-2岁",
            "2-3岁",
            "3-6岁",
            "专家咨询",
        ]
        dbname = '/home/yanxu/khufu/infodb/infodb'
        res = []
        for m in menus:
            data = pycabinet.search(dbname,'tag1',m,5000)
            for obj in data:
                res.append(obj)
        return res

    def location(self,obj):
        return "/v/%s/" % obj["kid"]

    def lastmod(self, obj):
        return datetime.strptime(obj["savedate"],'%Y-%m-%d')


