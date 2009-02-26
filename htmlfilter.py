# encoding: utf-8
import os
import glob
import hashlib
from html2text import html2text
for d,subdir,files in os.walk('/home/hexuotzo/khufu/www.zaojiao.com'): 
    #dir:文件夹名 
    #subdir子文件夹 
    #files所有文件
    for f in files:
        fname = os.path.join(d,f)
        try:
            r=open(fname).read().decode('utf8')
        except:
            try:
                r=open(fname).read().decode('gbk')
            except:
                #print fname
                continue
        r= r.strip()
        text = html2text(r).replace('"','')
        key = hashlib.md5(fname).hexdigest()
        #print 'dystmgr put khufu 1%s "%s"'%(key,text.encode('utf8'))
        print os.popen('dystmgr put khufu 1%s "%s"'%(key,text.encode('utf8'))).read()
               