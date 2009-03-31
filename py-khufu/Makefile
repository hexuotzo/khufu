CC = gcc
CPPFLAGS = -I. -I/opt/local/include/python2.5 -I/usr/local/include/python2.5
CFLAGS = -g -O2 -std=c99 -Wall -fPIC -fsigned-char -O2
LIBS = -ltokyodystopia -ltokyocabinet -lbz2 -lz -lpthread -lm -lc 
LDFLAGS = -L. -L/usr/local/lib -L/opt/local/lib

objects = pykhufu.o pykhufu.so

pykhufu.so : pykhufu.o
	$(CC) $(CFLAGS) -bundle -o $@ \
		$(LDFLAGS) $(LIBS)

pykhufu.o : pykhufu.c
	$(CC) -c $(CPPFLAGS) $(CFLAGS) pykhufu.c


.PHONY : clean
clean :
	rm $(objects)