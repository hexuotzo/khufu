# encoding: utf-8
import ctypes

def search(text,dbname='khufu'):
    lib=ctypes.CDLL('libtokyodystopia.so')
    idb=lib.tcidbnew()
    ecode=lib.tcidbopen(idb,dbname)
    rnum=ctypes.c_int()
    lib.tcidbsearch2.restype=ctypes.POINTER(ctypes.c_uint64)
    result=lib.tcidbsearch2(idb,text,ctypes.byref(rnum))
    # lib.tcidbget.restype = ctypes.c_char_p
    for i in range(rnum.value):
        # text = lib.tcidbget(idb,ctypes.c_int64(result[i]))
        # print "text",text
        yield result[i]

if __name__ == '__main__':
    for kid in search('严旭'):
        print "kid",kid

