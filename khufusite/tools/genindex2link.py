#!/usr/local/bin/python
#encoding: utf-8
#用来生成首页2级菜单全部链接的工具脚本
l = [
    "生活提示",
    "母胎变化",
    "适时胎教",
    "营养保健",
    "疾病护理",
    "常见问题"
]
menu = [
    "备孕",
    "怀孕",
    "产后",
    "0-1岁",
    "1-2岁",
    "2-3岁",
    "3-6岁",
    "专家咨询",
]
html = '<li><a href="/keyword/?insearch=%s&amp;type_class=%s">%s</a></li>'

for i in menu:
    print "".join([html%(i,v,v) for v in l])
    print 