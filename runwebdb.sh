#!/bin/sh
kill `cat /home/yanxu/khufu/webdb/ttserver.pid`
sleep(2)

/usr/local/bin/ttserver -host 114.113.30.29 -port 11212 -thnum 8 -dmn -pid /home/yanxu/khufu/webdb/ttserver.pid -log /home/yanxu/khufu/webdb/ttserver.log -le -ulog /home/yanxu/khufu/webdb -ulim 128m -sid 1 -rts /home/yanxu/khufu/webdb/ttserver.rts /home/yanxu/khufu/webdb/khufu.tch#bnum=1000000

