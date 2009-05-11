#!/bin/sh

kcount=`ps ax|grep -c \`cat /tmp/khufu.pid\`|grep -vc grep`
if [ $kcount -lt 1 ]
then
    /home/yanxu/khufu/khufusite/runfcgi.sh
fi
