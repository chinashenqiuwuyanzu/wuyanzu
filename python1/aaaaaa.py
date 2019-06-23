# a = [12,13,13,12,13,14,15]
# for i in a:
#   b= a.count(i)
#   if b>1:
#       for j in range(b-1):
#           a.remove(i)
# print(a)


# 自动登录QQ空间
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()

dr.get('https://www.baidu.com/')
sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
dr.find_element_by_id('kw').send_keys('qq空间')
sleep(2)
dr.find_element_by_id('su').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
sleep(5)
dr.find_element_by_xpath('//*[@id="nick_465105918"]').click()
sleep(5)

# def cc(x):
# 	a=0
# 	for i in range(x):
# 		a=a+i
# 		print(a)
# cc(100)