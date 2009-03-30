#!/usr/local/bin/python

#e.g:
#http://www.zaojiao.com/education/2008/0516/article_1630.html
#web/www.zaojiao.com/education/2008/0516/article_1630.html > key

import sys
import hashlib
import string

url = "web/%s" % sys.argv[1][7:]
key = hashlib.md5(url).hexdigest()
kid = string.atoi(key[:10],16)
print kid