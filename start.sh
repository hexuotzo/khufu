#!/bin/sh

KHUFU_PATH="/home/yanxu/khufu"

rm $KHUFU_PATH/meta/*.pid
rm $KHUFU_PATH/webdb/*.pid
$KHUFU_PATH/runserver.sh
$KHUFU_PATH/runwebdb.sh
$KHUFU_PATH/khufusite/runfcgi.sh
