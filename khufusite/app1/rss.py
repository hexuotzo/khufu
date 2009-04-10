# encoding: utf-8

from django.contrib.syndication.feeds import Feed
from django.utils import feedgenerator

class RssSiteNewsFeed(Feed):
    title = "早教知识网-全国唯一的早教知识查询、搜索网站 育儿 早教 健康 胎教 怀孕"
    link = "/feeds/rss/"
    description = "早教知识网是全国唯一的早教知识查询网站.为父母提供权威,安全,免费的怀孕分娩,胎教,育儿,保健,喂养,常见病护理知识,早教知识.年轻父母可以在这里找到与婴幼儿发育,成长,教育有关的全部知识和咨询。"

    def items(self):
        return ['1','2','3']
    def item_link(self, item):
        return "/%s/"%item