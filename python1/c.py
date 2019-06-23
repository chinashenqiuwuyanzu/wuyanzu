# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 服务器：可以提供某种服务的产品，软件
# # s=socket.socket()
# s.bind(('192.168.0.90',3000))
# s.listen(3)
# while True:
# 	  client,addr=s.accept()
# 	  reg=client.recv(1024)
# 	  print(reg.decode('utf-8'))
# 	  msg='刘旭吃mai'
# 	  client.send(msg.encode('utf-8'))
# a=0
# for i in range(1,5):
# 	for j in range(1,5):
# 		for k in range(1,5):
# 			if i!=j!=k:
# 				print(i,j,k)
# 				a+=1
# print(a)
 
# n=0
# while (n+1)**2-n*n<=168:
#     n+=1
# print(n)
# for i in range((n+1)**2):
#     if i**0.5==int(i**0.5) and (i+168)**0.5==int((i+168)**0.5):
#         print(i-100)

# for i in range(1000):
# 	for j in range(1000):
# 		for k in range(1000):
# 			if (i+100)==j*j and (j+168)==k*k:
# 				print(i)
# a=0
# b=1
# while b<1000:
# 	print(b)
# 	a,b=b,a+b
 
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print("%d*%d=%d" % (i,j,i*j),end='\t')
# 		if i==j:
# 			break
# 	 print('')
                                                                                                                                                                                                                                                                                                                                                                                                                                                     
# a=1
# b=1
# print(a)
# print(b)
# for i in range(10):
#     a=a+b
#     print(a)
#     b=a+b
#     print(b)
# a=[]
# for i in range(100,200):
# 	for j in range(2,i):
# 		if i%j==0:
# 			break
# 	if i==j+1:
# 		a.append(i)
# print(a)
# import os
# # result = os.getcwd()
# # print(result)
# os.popen('')


# import pymysql
# conn=pymysql.connect(host='192.168.0.233',port=3306,user='root',passwd='12300')
# m=conn.cursor()
# # m.execute('use nobi5')
# m.execute('use nobi5')
# m.execute('create database python_sql;')
# m.execute('show databases;')
# m.execute('show tables;')
# b = m.fetchall()
# print(b)
# import xlwt
# import xlrd
# with open('qqq.txt','r', encoding ='utf-8') as f:
# 	a=f.read()
# 	print(a)
# ff=xlwt.Workbook(zzz.xls)
# sheet = ff.add_sheet('python_test') .. 



# import xlwt
# import xlrd
# with open('qqq.txt','r+',encoding='utf-8') as f:
#    a=f.readlines()
# c=[]
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('ccc')
# for i in range(5):
#     b=a[i]
#     b = b.split(',')
#     c.append(b)
# print(c)
# f.close()
# for j in range(len(c)):
#     for k in range(4):
#          sheet.write(j,k,(c[j][k]))
# ff.save('aaa.xls')
# a=[1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
# a.sort()
# b=[]
# for i in a:
# 	if i not in b:
# 		b.append(i)

# # last=a[-1]
# # for i in range(len(a)-2,-1,-1):
# # 	if last==a[i]:
# # 		del a[i]
# # 	else:last=a[i]

# print(b)
# print(sum(range(1, 101)))
# import socket
# while True:
# 	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 	sock.connect(('192.168.0.29',3000))
# 	qq=input('>>>')
# 	sock.send(qq.encode('utf-8'))
# 	ww=sock.recv(1024)
# 	print(ww.decode('utf-8'))
# 	sock.close()
# import requests
# import re
# url='http://www.zhipin.com/c101210100-p100301/?page=2&ka=page-2'
# head = {
#     'User=Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#     }
# res = requests.post(url,headers=head)
# html = res.content.decode('utf-8')
# a=[]
# p_ul = re.compile(r'<ul>[\s]+<li>[\s]+<div\sclass=\"job-primary\">[\s\S]+</div>[\s]+</li>[\s]+</ul>')
# ite = p_ul.findall(html)
# p_li = re.compile(r'<li>[\s\S]+?<\/li>')
# content_list = p_li.findall(ite.group())
# self.deal_page(content_list)
# self.write_page()
# a.extend(ite)
# print(a)




# import requests
# import re
# class zhuabao():
# 	def pa(self,j):
# 			url='http://www.qiushibaike.com/text/page/{}/'.format(j)
# 			head={
# 			     'User=Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# 			}
# 			res = requests.get(url,headers=head)
# 			hh = res.content.decode('utf-8')
# 			return hh
# 	def guolv(self,x):
# 			a = re.compile('<h2>(.*?)</h2>',re.S)
# 			aa =a.findall(x)
# 			print(aa)
# for j in range(1,4):
# 	fr=zhuabao()
# 	hh=fr.pa(j)
# 	yy=fr.guolv(hh)	

# list1 = ['Google', 'Runoob', 'Taobao']
# list_pop=list1.pop(1)
# print("删除的项为 :", list_pop)
# print("列表现在为 : ", list1)		









# from selenium import webdriver
# from time import sleep
# dr = webdriver.Chrome()
# dr.get('http://www.baidu.com')
# sleep(2)
# print(dr.title)
# if dr.title =='百度一下，你就知道':
# 	print('yes')
# print(dr.current_url)
# dr.set_window_size(800,800)
# dr.set_window_position(100,800)
# dr.get('https://www.jd.com')
# sleep(2)
# dr.back()
# sleep(2)
# dr.forward()
# dr.find_element_by_id('kw').send_keys('python')  #send_keys 是输入
# sleep(2)
# dr.find_element_by_id('su').click()    #找到百度一下的id  ，click 是点击确定的意思

#通过name属性来定位
# 通过class属性来定位
#不论采用任何方式的定位  一定要保证定位的唯一性
# dr.find_element_by_class_name('s_ipt').send_keys('开封大学')
# dr.find_element_by_id('su').click()
# sleep(2)
# dr.find_element_by_class_name('c-showurl').click()
# 通过link_text属性来定位    文本定位
# dr.find_element_by_link_text('新闻').click()
# partial_link_text属性来定位   模糊文本
# dr.find_element_by_partial_link_text('新').click()
#通过tag name属性来定位  根据标签名称定位
# print(dr.find_element_by_tag_name('title'))
#通过xpath属性来定位  根据路径定位（可以用相对路径或绝对路径）      xptah 路径标记语言
# dr.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
# #通过css_selector属性来定位    根据css定位
# dr.find_element_by_css_selector('#u1 > a:nth-child(1)').click()

# a=0
# for i in range(x):
# 	a=a+i
# 	print(a)	

import requests
import re


url='http://www.qiushibaike.com/text/page/2/'
res=requests.get(url)
hh=res.content.decode('utf-8')
 	# return hh

patt=re.compile('<h2>(.*)</h2>',re.S)
items=patt.findall(hh)
print(items)
# a=[]
# for i in items:
# 	aa=re.findall('tidle="(.*?)",i')
# 	tit.append(aa[0])
# 	print(tit)







