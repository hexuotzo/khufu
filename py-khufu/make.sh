#!/bin/sh
gcc -c -I. -I/usr/local/include -I/home/yanxu/include -I/usr/local/include -DNDEBUG -D_GNU_SOURCE=1 -D_TD_PREFIX="\"/usr/local\"" -D_TD_INCLUDEDIR="\"/usr/local/include\"" -D_TD_LIBDIR="\"/usr/local/lib\"" -D_TD_BINDIR="\"/usr/local/bin\"" -D_TD_LIBEXECDIR="\"/usr/local/libexec\"" -D_TD_APPINC="\"-I/usr/local/include\"" -D_TD_APPLIBS="\"-L/usr/local/lib -ltokyodystopia -ltokyocabinet -lbz2 -lz -lpthread -lm -lc \"" -std=c99 -Wall -fPIC -fsigned-char -O2 mydystopia.c


LD_RUN_PATH=/lib:/usr/lib:/usr/local/lib:/home/yanxu/lib:/usr/local/lib:/usr/local/lib:. gcc -std=c99 -Wall -fPIC -fsigned-char -O2 -o mydystopia mydystopia.o -L. -L/usr/local/lib -L/home/yanxu/lib -L/usr/local/lib  -ltokyodystopia -ltokyocabinet -lbz2 -lz -lpthread -lm -lc

chmod a+x mydystopia
