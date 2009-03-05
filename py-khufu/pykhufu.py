# encoding: utf-8
from ctypes import *

class PyDystopia(object):
    """Tokyo Dystopia Python Interface"""
    def __init__(self, dbname='khufu'):
        self.dbname = dbname
        self.lib=CDLL('libtokyodystopia.so')
        self.idb=self.lib.tcidbnew()
        #IDBOWRITER | IDBOCREAT
        ecode=self.lib.tcidbopen(self.idb,self.dbname,6)
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
                stext = lib.tcidbget(idb,c_int64(result[i]))
                yield result[i],stext
            yield result[i]
    def put(self,kid,text):
        return self.lib.tcidbput(self.idb,c_int64(kid),text)
    def commit(self):
        return self.lib.tcidbclose(self.idb)
    def get(self,kid):
        self.lib.tcidbget.restype = c_char_p
        return self.lib.tcidbget(self.idb,c_int64(kid))

if __name__ == '__main__':
    pd = PyDystopia()
    for kid in pd.search('严旭'):
        print "kid",kid
    print pd.put(5,'用Python插入的')
    print pd.put(6,'zhmocean脱耦和求偶的心理学差异...风马牛不相及的事情却有着千丝万缕的联系...')
    print pd.commit()
    print pd.get(1)

