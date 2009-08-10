# encoding: utf-8
from django.contrib.sitemaps import Sitemap
from django.conf import settings
from datetime import datetime
import pycabinet as pb
import random

class KhufuSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def _alldata(self):
        for m in settings.MENUS:
            for obj in pb.search(settings.MC_IP,settings.MC_INFO_PORT, \
                            'tag1',m,1000,0,0):
                yield obj
    def items(self):
        return list(self._alldata())

    def location(self,obj):
        return "/v/%s/" % obj["kid"]

    def lastmod(self, obj):
        return datetime.strptime(obj["savedate"],'%Y-%m-%d')


