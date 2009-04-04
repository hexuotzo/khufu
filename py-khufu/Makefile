CC = gcc
CPPFLAGS = -I. -I/opt/local/include/python2.5 -I/usr/local/include/python2.5 -I/usr/local/include
CFLAGS = -g -O2 -std=c99 -Wall -fPIC -fsigned-char -DNDEBUG
LIBS = -ltokyodystopia -ltokyocabinet -lbz2 -lz -lpthread -lm -lc 
LDFLAGS = -L. -L/usr/local/lib -L/opt/local/lib
OS=$(shell uname)
objects = pykhufu.o pykhufu.so

ifeq ($(OS),Darwin)
	SHAREDFLAGS = -bundle -flat_namespace -undefined suppress
	PYSITEPACKAGE = /opt/local/lib/python2.5/site-packages/
else
	SHAREDFLAGS = -shared
	PYSITEPACKAGE = /usr/local/lib/python2.5/site-packages/
endif


pykhufu.so : pykhufu.o
	$(CC) $(CFLAGS) $(SHAREDFLAGS) -o $@ pykhufu.o \
		$(LDFLAGS) $(LIBS)


pykhufu.o : pykhufu.c
	$(CC) -c $(CPPFLAGS) $(CFLAGS) pykhufu.c


install :
	cp pykhufu.so $(PYSITEPACKAGE)


.PHONY : clean
clean :
	rm $(objects)