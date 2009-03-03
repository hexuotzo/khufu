# encoding: utf-8
import ctypes
lib=ctypes.CDLL('/home/yanxu/tokyodystopia-0.9.9/libtokyodystopia.so')
idb=lib.tcidbnew()
ecode=lib.tcidbopen(idb,'khufu')
rnum=ctypes.c_int()
lib.tcidbsearch2.restype=ctypes.POINTER(ctypes.c_uint64)
result=lib.tcidbsearch2(idb,"严旭",ctypes.byref(rnum))
#print result,rnum.value
lib.tcidbget.restype = ctypes.c_char_p
for i in range(rnum.value):
    text = lib.tcidbget(idb,ctypes.c_int64(result[i]))
    print "text",text

