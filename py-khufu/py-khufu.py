# encoding: utf-8
from ctypes import *

class PyDystopia(object):
    """Tokyo Dystopia Python Interface"""
    def __init__(self, dbname='khufu'):
        self.dbname = dbname
        self.lib=CDLL('libtokyodystopia.so')
        self.idb=self.lib.tcidbnew()
        ecode=self.lib.tcidbopen(self.idb,self.dbname)
    def search(self,text,returntext=False):
        """search text"""
        lib = self.lib
        idb = self.idb
        rnum=c_int()
        lib.tcidbsearch2.restype=POINTER(c_uint64)
        result=lib.tcidbsearch2(idb,text,byref(rnum))
        for i in range(rnum.value):
            if returntext:
                lib.tcidbget.restype = c_char_p
                text = lib.tcidbget(idb,c_int64(result[i]))
                yield result[i],text
            yield result[i]

if __name__ == '__main__':
    pd = PyDystopia()
    for kid in pd.search('严旭'):
        print "kid",kid

