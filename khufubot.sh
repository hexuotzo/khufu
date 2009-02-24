#!/bin/sh

#e.g
#./khufubot.sh http://xxx.com/
#./khufubot.sh -P /tmp/ http://xxx.com/

wget -c -r -l 3 -U "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" --proxy on $*