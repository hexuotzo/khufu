#!/usr/local/bin/python
#encoding: utf-8

import pycabinet
import random
import os
from datetime import datetime

#changedate = "2009-05-15"
changedate = str(datetime.now().date())
dbpath = "/home/yanxu/khufu/infodb/infodb"
scmd = '/usr/local/bin/tctmgr put /home/yanxu/khufu/infodb/infodb %s "title" "%s" "savedate" "%s" "tag1" "%s"'
data = pycabinet.search(dbpath,"savedate","2009-05-05",20000)
for i in range(100):
    obj = random.choice(data)
    cmd = scmd % (obj['kid'],obj['title'],changedate,obj["tag1"])
    print cmd
    os.popen(cmd)
