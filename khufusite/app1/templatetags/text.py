#encoding: utf-8

from django import template

register = template.Library()

@register.filter
def removetext(text):
    text=text.encode("utf8")
    text=text.replace("-育儿早教-中国早教网","")
    text=text.replace("-怀孕胎教-中国早教网","")
    return text

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
    html_tmpl = '''
	<ul class="margin_left">
		<li><h5><a href="/keyword/?insearch=%(m)s">%(m)s</a></h5></li>
		<li><a href="/keyword/?insearch=%(m)s&amp;type_class=%(n)s">%(n)s</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=%(n)s">%(n)s</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=%(n)s">%(n)s</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=%(n)s">%(n)s</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=%(n)s">%(n)s</a></li><li><a href="/keyword/?insearch=%(m)s&amp;type_class=%(n)s">%(n)s</a></li>
	</ul>
    '''
    html = ''
    for m in menu:
        for n in l:
            html += html_tmpl % dict(m=m,n=n)
    return html
