# encoding: utf-8
import os
import glob
for d,subdir,files in os.walk('/home/hexuotzo/khufu/www.zaojiao.com'): 
    #dir:文件夹名 
    #subdir子文件夹 
    #files所有文件
    for f in files:
        fname = os.path.join(d,f)
        r=open(fname).read()
        