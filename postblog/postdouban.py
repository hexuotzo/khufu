import twill

cmd = '''
go http://www.douban.com/login
fv 2 form_email zaojiao100@gmail.com
fv 2 form_password 123456
submit
go http://www.douban.com/group/yuer/new_topic
fv 2 rev_title "Welcome:)"
fv 2 rev_text "http://www.zaojiao100.com/"
submit
'''