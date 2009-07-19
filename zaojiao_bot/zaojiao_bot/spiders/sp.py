from scrapy import log
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.xpath.selector import HtmlXPathSelector
from scrapy.item import ScrapedItem
from zaojiao_bot.items import ZaojiaoBotItem
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
        col='title\t%s\turl\t%s\ttext\t%s\taddpinyin\t%s\tkid\t%s'
        v = col % (item.title.encode('utf8'),item.url,item.body.encode('utf8'),item.body.encode('utf8'),item.uuid)
        pb.put3('datadb.tct',item.uuid,v)
        
        return [item]

SPIDER = ZaojiaoSpider()