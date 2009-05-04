#!/usr/bin/python
# -*- coding: utf8 -*-
from conf import *
from html2text import html2text
import cPickle as pickle

	
if __name__ == '__main__':
	c1 = pickle.load(open('../newtags/results.pickle'))
    
	for title,dic in index_dic_type_one.items():
		spiderUrl = '%s/%s/%s'%(url, title, dic.get('url'))
		# spiderUrl = 'http://baby.sina.com.cn/fmq/sc.html'
		# spiderUrl = 'http://localhost:82/index_er.html'
		analy_html = analyzier(spiderUrl)
		bar_reSyntax = dic.get('re')[0]
		bar_html = ''.join(reg(bar_reSyntax,analy_html))

		bar_link_reSyntax = dic.get('link')[0]
		bar_link_lists = reg(bar_link_reSyntax, bar_html)
		
		now_reSyntax = r'<li class="cur">(.*?)</'
		now_title = reg(now_reSyntax, bar_html)
		#分析当前数据
		analy_now_dateaUrl = spiderUrl
		analy_now_dateaTitle = now_title[0]
		
		print analy_now_dateaTitle.decode('gbk'),analy_now_dateaUrl
		data_lists = getDatalinks(analy_html)
		for title,url,body in analy_list(data_lists):
			url = "http://%s" % url
			body = html2text(body)
			dtype = c1.classify(body)
			print "t1",title,url,dtype
		
		for links in bar_link_lists:
			spiderUrl = url+links[0]
			print links[1].decode('gbk'), spiderUrl
			analy_html = analyzier(spiderUrl)
			bar_reSyntax = dic.get('re')[0]
			bar_html = ''.join(reg(bar_reSyntax,analy_html))
			data_lists = getDatalinks(analy_html)
			for title,url,body in analy_list(data_lists):
				url = "http://%s" % url
				body = html2text(body)
				dtype = c1.classify(body)
				print "t2",title,url
		
		
		