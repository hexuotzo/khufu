#encoding: utf-8
from scrapy import log
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.xpath.selector import HtmlXPathSelector
from scrapy.item import ScrapedItem
from zaojiao_bot.items import ZaojiaoBotItem
from datetime import date
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
        "http://www.zaojiao.com/education/",
        "http://www.zaojiao.com/zhidao/",
        "http://forum.zaojiao.com/index.php",
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow=('article_\.html',),), \
                callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=('viewthread\.php',),), \
                callback='parse_item_forum'),
    )
    def save_to_tt(self,item):
        v = {
            'text':item.body.encode('utf8'),
            'url':item.url,
            'title':item.title.encode('utf8'),
            'addpinyin':item.body.encode('utf8'),
            'savedate':item.savedate,
            'kid':item.uuid,
        }
        pb.put4("114.113.30.29",11213,item.uuid,v,0)
        
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
            'savedate':item.savedate,
            'kid':item.uuid,
            'tag1':random.choice(menus)
        }
        pb.put4("114.113.30.29",11214,item.uuid,info_v,0)
    
    def parse_item_forum(self,response):
        hxs = HtmlXPathSelector(response)
        item = ScrapedItem()
        item.title = cn(hxs.x('//h2/text()').extract()[0])
        item.body = cn(hxs.x('//div[@class="t_msgfont"]').extract()[0])
        item.url = response.url
        item.savedate = str(date.today())
        item.uuid = str(abs(hash(response.url)))

        self.save_to_tt(item)
    
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = ScrapedItem()
        item.title = cn(hxs.x('//h1/text()').extract()[0])
        item.body = cn(hxs.x('//div[@id="content"]').extract()[0])
        item.url = response.url
        item.savedate = str(date.today())
        item.uuid = str(abs(hash(response.url)))
        
        self.save_to_tt(item)
        
        return [item]

SPIDER = ZaojiaoSpider()
