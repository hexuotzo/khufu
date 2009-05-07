#encoding: utf-8

import pycabinet
import random
import os

changedate = "2009-05-08"
dbpath = "infodb/infodb"
scmd = 'tctmgr put infodb/infodb %s "title" "%s" "savedate" "%s" "tag1" "%s"'
data = pycabinet.search(dbpath,"savedate","2009-05-05",20000)
for i in range(100):
    obj = random.choice(data)
    cmd = scmd % (obj['kid'],obj['title'],changedate,obj["tag1"])
    print cmd
    os.popen(cmd)
