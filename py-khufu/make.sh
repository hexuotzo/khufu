#!/bin/sh
# gcc -c -g -I. -I/usr/local/include -I/opt/local/include/python2.5 -I/usr/local/include -DNDEBUG -D_GNU_SOURCE=1 -D_TD_PREFIX="\"/usr/local\"" -D_TD_INCLUDEDIR="\"/usr/local/include\"" -D_TD_LIBDIR="\"/usr/local/lib\"" -D_TD_BINDIR="\"/usr/local/bin\"" -D_TD_LIBEXECDIR="\"/usr/local/libexec\"" -D_TD_APPINC="\"-I/usr/local/include\"" -D_TD_APPLIBS="\"-L/usr/local/lib -ltokyodystopia -ltokyocabinet -lbz2 -lz -lpthread -lm -lc \"" -std=c99 -Wall -fPIC -fsigned-char -O2 pykhufu.c

gcc -fno-common -c -I. -I/usr/local/include -I/opt/local/include/python2.5 -I/usr/local/include -DNDEBUG -D_GNU_SOURCE=1 -D_MYBIGEND -D_TD_PREFIX="\"/usr/local\"" -D_TD_INCLUDEDIR="\"/usr/local/include\"" -D_TD_LIBDIR="\"/usr/local/lib\"" -D_TD_BINDIR="\"/usr/local/bin\"" -D_TD_LIBEXECDIR="\"/usr/local/libexec\"" -D_TD_APPINC="\"-I/usr/local/include\"" -D_TD_APPLIBS="\"-L/usr/local/lib -ltokyodystopia -ltokyocabinet -lbz2 -lz -lpthread -lm -lc \"" -g -O2 -std=c99 -Wall -fsigned-char -O2 pykhufu.c


gcc -g -O2 -bundle -flat_namespace -undefined suppress -o pykhufu.so pykhufu.o -L. -L/opt/local/lib -L/Users/yanxu/lib -L/usr/local/lib -ltokyocabinet -ltokyodystopia -lbz2 -lz -lpthread -lm -lc
	  
# LD_RUN_PATH=/lib:/usr/lib:/usr/local/lib:/home/yanxu/lib:/usr/local/lib:/usr/local/lib:/opt/local/lib:.
# gcc -O2 -dynamiclib -o pykhufu.dylib pykhufu.o -L. -L/usr/local/lib -L/opt/local/lib  -ltokyodystopia -ltokyocabinet -lbz2 -lz -lpthread -lm -lc

