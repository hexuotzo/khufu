#encoding: utf-8

from django import template
from django.utils.encoding import smart_unicode,force_unicode,smart_str

register = template.Library()

@register.filter
def removetext(text):
    text=smart_str(text,"utf8")
    text=text.replace("-育儿早教-中国早教网","")
    text=text.replace("-怀孕胎教-中国早教网","")
    text=text.replace("-新闻资讯-中国早教网","")
    text=text.replace("-专家指导-中国早教网","")
    text=text.replace("中国早教网","")
    return text

@register.filter
def cutstr(text,count):
    text=text.strip()
    return text[:count]

@register.simple_tag
def activemenu(word,text):
    if word==text:
        return 'class="active"'
    return ""

@register.simple_tag
def activemenu2(word,text):
    if word==text:
        return 'class="active2"'
    return ""

@register.simple_tag
def index2menu():
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
    html_tmpl = '''
	<ul class="margin_left">
		<li><h5><a href="/keyword/?insearch=%(m)s">%(m)s</a></h5></li>
		<li><a href="/keyword/?insearch=%(m)s&amp;type_class=生活提示">生活提示</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=母胎变化">母胎变化</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=适时胎教">适时胎教</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=营养保健">营养保健</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=疾病护理">疾病护理</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=常见问题">常见问题</a></li>
	</ul>
    '''
    html = ''
    for m in menu:
        html += html_tmpl % dict(m=m)
    return html
