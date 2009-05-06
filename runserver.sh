#!/bin/sh
kill `cat /home/yanxu/khufu/meta/ttserver.pid`
sleep 2

/usr/local/bin/ttserver -host 114.113.30.29 -port 11211 -thnum 8 -dmn -pid /home/yanxu/khufu/meta/ttserver.pid -log /home/yanxu/khufu/meta/ttserver.log -le -ulog /home/yanxu/khufu/meta -ulim 128m -sid 1 -rts /home/yanxu/khufu/meta/ttserver.rts /home/yanxu/khufu/meta/khufu.tch

