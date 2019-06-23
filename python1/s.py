

# # def asd(a,b):
# # 	for i in range(len(a)):
# # 	    for j in range(len(a)):
# # 	    	if a[i]+a[j]==b and i!=j:
# # 	    	    print(a[i],a[j])

# # asd([12,23,12,45,21,45],24)
# a='123'
# b=a[::-1]
# # print(b)
# c=0
# for i in range(len(b)):
# 	for j in range(10):
# 		if str(j) == b[i]:
# 			c+=j*10**i
# print(c)
# import xlrd
# import xlwt
# with open('qqq.txt','r+',encoding='utf-8') as f:
#     a=f.readlines()
# print(a)
# c=[]
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('python_test')
# for i in range(5):
# 	b=a[i]
# 	b=b.split(',')
# 	c.append(b)
# print(c)
# f.close()
# for j in range(len(c)):
# 	for k in range(4):
# 		sheet.write(j,k,(c[j][k]))
		 
# ff.save('hhh.xls')
# print(x)

# b=[122,23,34,65,667,89]
# # b=[int(i) for i in b]
# b.sort()
# print(b)
# f=b.count(b[-1])
# print(f)
# o=[]
# for k in range(1,f+1):
# 	o.append(b[-1])
# 	b.remove(b[-1])
# d=b.count(b[-1])
# for j in range(1,d+1):
# 	o.append(b[-1])
# print(o)
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host = ('192.168.0.90',3000)
# msg='hello'
# s.sendto(msg.encode('utf-8'),host)
# reg = s.recv(1024)
# print(reg.decode('utf-8'))


# a='123'
# b=a[::-1]
# c=0
# for i in range(len(a)):
# 	for j in range(10):
# 		if str(j)==b[i]:
# 			c+=j*10**i
# print(c)

# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print("%d*%d=%d" % (i,j,i*j), end='\t')
# 		if i==j:
# 			break
# 	print('')

# import os
# import xlrd
# import xlwt
# os.mkdir('aaa')
# with open('a.txt','w+',encoding='utf-8') as f:
# 	f.write('1234\t' '12345\t')
# 	f.readlines()

# import socket
# s=socket.socket(socket.AT_INET,socket.SOCK_STREAM)
# s.bind('192.168.0.29',3000)
# s.listen(3)
# while True:
# 	a,c=s.accept()
# 	reg=a.recv(1024)
# 	print(reg.decode('utf-8'))
# 	msg=input('>>>')
# 	a.send(msg.encode('utf-8'))






# import requests
# import re

# class boss():
# 	def send_ceshi(self):
# 		url='http://www.lagou.com/zhaopin/ceshigongchengshi/2/?filterOption=2'
# 		head={
# 		      'User=Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# 		}
# 		res = requests.get(url,headers=head)
# 		hh=res.content.decode('utf-8')
# 		return hh
# 	def guolv(self,x):
# 		# a = re.compile('<div class="job-title">(.*?)</div>',re.S)
# 		a = re.compile('<ul class="item_con_list">(.*?)</div>',re.S)
# 		aa = a.findall(x)
		# print(aa)
	# 	tit=[]
	# 	for i in aa:
	# 		mm=re.findall('title="(.*?)"',i)
	# 		tit.append(mm[0])
	# 	print(tit)
	# 	return tit
	# def save(self,y):
	# 	with open('b.txt','a',encoding='utf-8') as ff:
	# 		for  i in y:
	# 			ff.write(i+'\n')
# fr=boss()
# hh=fr.send_ceshi()
# yy=fr.guolv(hh)
# fr.save(yy)
#  
# print(boss().send_ceshi())




# import requests
# import re
# import json
# import xlwt
# import xlrd
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('python_test')
# url='http://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.60664372&x-zp-page-request-id=713c694b77504ac6a03298a5a3e5a4f7-1557233071923-471678'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;    WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
# res=requests.get(url,headers=head)
# html=res.content.decode('utf-8')
# qqq=json.loads(html)
# c=[]
# d=['工作名称','公司名称','工资','地址']
# for z in range(len(d)):
#     sheet.write(0,z,d[z])
# for i in range(10):
#         a1=[]
#         b1=qqq['data']['results'][i]['jobName']
#         b2=qqq['data']['results'][i]['company']['name']
#         b3=qqq['data']['results'][i]['salary']
#         b4=qqq['data']['results'][i]['city']['display']
#         a1.append(b1)
#         a1.append(b2)
#         a1.append(b3)
#         a1.append(b4)
#         for t in range(len(d)):
#             sheet.write(i+1,t,'{}'.format(a1[t]))
#             if i+1==20:
#                 break
# f.save('bbb.xls')

# import pymysql
# import pymysql
# import xlwt
# import xlrd
# conn=pymysql.connect(host='192.168.0.211',
#                      port=3306,
#                      user='root',
#                      passwd='123456')
# m=conn.cursor()
# m.execute('use python_sql;')
# with open('b.txt' ,'r') as f:
# 	a=f.readlines()
# 	print(a)
# for i in range(len(a)):                                                                
#     b=a[i].split(",")
#     print(b)
#     if i == 0:
#        continue
#        m.execute('create table user111({} char(50),{} int,{} char(50),{} char(50));'.format(b[0],b[1],b[2],b[3]))
#     else:
#        m.execute('insert into user111 values("{}","{}","{}","{}")'.format(b[0],b[1],b[2],b[3]))
# m.execute('select * from user111;')


# a = [12,3,234,465]
# b = [145,4546,5667,1]
# a.extend(b)
# # a.append(b)
# print(a)

# import requests
# import re
# import xlwt
# url ='http://www.kuwo.cn/bang/index'
# head={
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;    WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
# }
# res = requests.get(url,headers=head)
# hh = res.content.decode('utf-8')
# # print(hh)
# a=[]
# # b=[]
# aa=re.compile('<a href=".*?" target="_blank">(.*?)</a>',re.S)
# aaa=aa.findall(hh)
# a.extend(aaa)
# print(b)

# import os
# import re
# a = os.getcwd()
# # print(a)
# b = os.listdir(a)
# aa=''.join(b)
# d=aa.split(',')
# print(aa)
# # db
# # print(b)
# # f = re.compile(py)
# # c = re.findall(aa)
# # print(c)
# # c=aa.endswith('.py')
# print(d)


import requests
import re
class qiushi():
	def pa(self):
		url='http://www.qiushibaike.com/text/page/2/'
		res=requests.get(url)
		hh=res.content.decode('utf-8')
		return hh
	def guo(self,x):
		patt=re.compile('<h2>(.*?)</h2>',re.S)
		a=patt.findall(x)
		
