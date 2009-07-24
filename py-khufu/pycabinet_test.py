# encoding: utf-8
import pycabinet as pb

v = {'title':'hi','savedate':'2009-07-21','tag1':'备孕'}
pb.put4("114.113.30.29",11214,"test_1",v)
# for r in pycabinet.search("../infodb/infodb","tag1","备孕",10):
#     print r["title"]