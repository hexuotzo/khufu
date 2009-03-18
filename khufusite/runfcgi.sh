#!/bin/sh
echo "Resting......"

PROJDIR="/home/yanxu/khufu/khufusite"
#PIDFILE="/tmp/khufu.pid"
#SOCKET="/tmp/khufu.sock"

cd $PROJDIR
#if [ -f $PIDFILE ]; then
#    kill `cat -- $PIDFILE`
#    rm -f -- $PIDFILE
#fi

#/usr/local/bin/python $PROJDIR/manage.py runfcgi method=prefork socket=$SOCKET pidfile=$PIDFILE daemonize=false
#/usr/sbin/chown nobody $SOCKET

kill `cat /tmp/khufu.pid`
/usr/local/bin/python manage.py runfcgi method=threaded host=127.0.0.1 port=3033 pidfile=/tmp/khufu.pid


