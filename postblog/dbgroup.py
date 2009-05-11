import re
html = open('g.html').read()
regx = re.findall(r'<dd><a href="(.*)">(.*)</a> <span>(.*)</span>',html)
print [url for url,gname,p in regx]
