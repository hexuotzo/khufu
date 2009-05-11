# import twill

cmd = '''
go http://www.douban.com/login
fv 2 form_email zaojiao100@gmail.com
fv 2 form_password 123456
submit
go http://www.douban.com%snew_topic
fv 2 rev_title "%s"
fv 2 rev_text "%s"
submit
'''

groups = ['/group/yuer/', '/group/Babymamy/', '/group/38772/', '/group/youngman/', '/group/17444/', '/group/mother/', '/group/babyangel/', '/group/73952/', '/group/baobao/', '/group/hunxuebaobao/', '/group/mamab/', '/group/16020/', '/group/16086/', '/group/34832/', '/group/babe/', '/group/159320/']


