# encoding: utf-8
import pycabinet
for r in pycabinet.search("../infodb/infodb","tag1","备孕",10):
    print r["title"]