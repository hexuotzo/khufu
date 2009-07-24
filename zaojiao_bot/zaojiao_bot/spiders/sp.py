#encoding: utf-8
from scrapy import log
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.xpath.selector import HtmlXPathSelector
from scrapy.item import ScrapedItem
from zaojiao_bot.items import ZaojiaoBotItem
from datetime import datetime
import random
import pycabinet as pb

def safecn(i):
    try:
        return unichr(int(i))
    except:
        return i

cn = lambda s:"".join( 
        map(lambda x:safecn(x.replace("&#","")),
                s.strip().split(";")) 
        )

class ZaojiaoSpider(CrawlSpider):
    domain_name = "zaojiao.com"
    start_urls = [
        "http://www.zaojiao.com/pregnancy/",
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow=('\.html',),), \
                callback='parse_item'),
    )
    def parse_item(self, response):
        log.msg("response.url",response.url)
        hxs = HtmlXPathSelector(response)
        item = ScrapedItem()
        item.title = cn(hxs.x('//h1/text()').extract()[0])
        item.body = cn(hxs.x('//div[@id="content"]').extract()[0])
        item.url = response.url
        item.uuid = str(abs(hash(response.url)))
        
        '''
        in data db
        '''
        v = {
            'text':item.body.encode('utf8'),
            'url':item.url,
            'title':item.title.encode('utf8'),
            'addpinyin':item.body.encode('utf8'),
            'savedate':str(datetime.now()),
            'kid':item.uuid,
        }
        pb.put4("114.113.30.29",11213,item.uuid,v)
        
        menus = (
            "备孕",
            "怀孕",
            "产后",
            "0-1岁",
            "1-2岁",
            "2-3岁",
            "3-6岁",
            "专家咨询",
        )
        info_v = {
            'title':item.title.encode('utf8'),
            'savedate':str(datetime.now()),
            'kid':item.uuid,
            'tag1':random.choice(menus)
        }
        pb.put4("114.113.30.29",11214,item.uuid,info_v)
        
        return [item]

SPIDER = ZaojiaoSpider()