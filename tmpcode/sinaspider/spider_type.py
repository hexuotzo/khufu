#!/usr/bin/python
# -*- coding: utf8 -*-
from conf import *
	
if __name__ == '__main__':
	for title,dic in index_dic_type_two.items():
		spiderUrl = '%s/%s/%s'%(url, title, dic.get('url'))
		print spiderUrl
		#spiderUrl = 'http://localhost:82/index_er.html'
		analy_html = analyzier(spiderUrl)
		bar_reSyntax = dic.get('re')[0]
		bar_html = ''.join(reg(bar_reSyntax,analy_html))
		test = r'<li><a href="#" id="m\d+\d+-\d+" onClick="TAB_switch\(\d+\);return false".*?>(.*?)</a></li><ul.*?>(.*?)</ul>'
		analy_lists = reg(test, bar_html)
		for analylist in analy_lists:
			analy_one_cag_title = analylist[0].decode('gbk')
			analy_two_cag_lists = analylist[1]
			print '一级分类:',analy_one_cag_title
			analy_two_cag_lists =  reg(r'<a href="(.*?)">(.*?)</a>', analy_two_cag_lists)
			for links in analy_two_cag_lists:
				spiderUrl = url+links[0]
				print "\t",'二级分类:',links[1].decode('gbk'), spiderUrl
				analy_html = analyzier(spiderUrl)
				data_lists = getDatalinks(analy_html)
				analy_list(data_lists)
				break
			break
			print '+++++++++++++++++++++'
		break
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
