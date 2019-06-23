# import os
# os.makedirs(r'aaa\bbb')
# 将路径与文件分隔开
# b=os.path.split(r'‪E:\19.4.20\wu.py')
# print(b)
# 判断是否是普通文件
# b = os.path.isfile(r'‪‪‪C:\Users\Wushuai\Desktop\新建文本文档 (2).txt')
# print(b)
# b = os.path.splitext(r'‪‪E:\19.4.20\wu.py')
# b=os.listdir()
# for i in b:
# 	b=str(i)
#     d=b.endswith('.py')
# 	if d==ture:
# 	    print(i)


# import pymysql
# conn=pymysql.connect(host='192.168.0.233',
#                      port=3306,
#                      user='root',
#                      passwd='12300'
#                      )
# m=conn.cursor()
# sql=('use nobi5')
# m.execute(sql)
# sql =("create table user(id int,name char(25),age char(30))")
# m.execute(sql)
# # cur.execute('insert into user values(1,"张三"),(2,"李四");')
# m.execute('create database nobi5')
# sql = ("create table user(id int,name char(20));")
# sql="INSERT INTO user(name, account, saving) VALUES ( '%s', '%s', %.2f )"
# # data = ('雷军', '13512345678', '100'）
# m.execute(sql)
# m.execute("create table user(id int,name char(20));")
# sursor.close
# conn.close
# row = cur.execute('show tables')
# print(row)
# import xlrd
# import xlwt

# f=open('qqq.txt','r',encoding='utf-8')
# # with open('qqq.txt','r+',encoding='utf-8') as f:、
# a=f.readlines()
# print(a)
# c=[]
# f=xlwt.Workbook()
# sheet=f.add_sheet('ccc')
# for i in range(5):
# 	b=a[i]
# 	b=b.split(',')
# 	c.append(b)
# print(c)
# for j in conn:
# f=xlrd.open_Workbook('aaa.xls')

# import paramiko
# ssh123 = paramiko.SSHCLinet()
# ssh123 = connect(hostname='192.168.0.233',port=22,username='root',password='12300')
import  smtplib #封装了smtp协议
import  email.mime.multipart as mul #制作邮件
import  email.mime.text as text #对邮件的正文进行处理
#ff='15660513120@163.com'
#ww='316986133@qq.com'
#创建一个空邮件
message=mul.MIMEMultipart()
#标题
message['Subject']='pythone_test'
#发件人
message['From']='15660513120@163.com'
#收件人
message['To']='316986133@qq.com'
#正文  多行数据
txt="""
刘旭先生 恭喜你 获得了s10世界赛冠军  希望您于十日内交2w元钱到拳头公司   我将为您把您的冠军奖杯邮寄过去
并为您制作s10冠军皮肤
"""
#对正文进行处理
tet = text.MIMEText(txt)
#将处理过后的正文添加到邮件里
message.attach(tet)
#定义一个邮件服务器
smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
#带有附件的邮件
att1 = text.MIMEText(open('qqq.txt', 'rb').read(), 'base64', 'utf-8')
#附件的字段 固定的
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="冠军杯"'
message.attach(att1)

#登陆服务器  用户名 密码   不是你的邮箱密码是授权码
smtp123.login('15660513120@163.com','A123456')
#发送邮件   发件人  收件人  邮件
smtp123.sendmail('15660513120@163.com','316986133@qq.com',message.as_string())
#断开连接
smtp123.close()
# import socket
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('192.168.0.90',3000))
# while Ture:
# 	  client,addr=s.recvfrom(1024)
#  	  print(client.decode('utf-8'))
#       msg='welcome'
#       s.sendto(msg.encode('utf-8'),addr)
# num=0
# while True:
# 	if a<101:
# 		num+=a
# 		break
# print(num)
# num=0
# a=1
# while a<100:
# 	num+=a
# 	a+=1
# print(num)
# a=122
# f=[str(i)  for i in range(10)] +['a','b','c','d','e','f']
# c=''
# while True:
# 	b= a%16
# 	c=c+f[b]
# 	a=a//16
# 	if a==0:
# 	    break
# print(c[::-1])
# c=[]	
# def asd(a):
# 	for i in range(1,a):
# 		num=0
# 		for j in range(1,i):
# 			if i%j==0:
# 				num+=j
# 		if i==num:
# 			c.append(i)

# 	print(c)
# asd(101)
# a='123'
# b=a[::-1]
# print(b)
# c=0
# for i in range(len(a)):
# 	for j in range(10):
# 		if b[i]==str(j):
# 			c+=j*10**i
# print(c)
# import re
# a='vasv3qsjbsb23j1233bkj2b675dfs4123sdfd54'
# b=re.compile('[0-9][0-9]+')
# c=b.findall(a)
# print(len(c))
# print(c)
# a=[12,12,23,34,23,45,12]
# for i in a:
# 	# print(i)
# 	b=a.count(i)
# 	# print(b)
# 	if b>1:
# 		for j in range(b-1):
# 			a.remove(i)
# print(a) 
# a=[12,23,34,456,56,678,32]
# for i in a:
# 	for j in range(len(a)):
# 		if i<a[j]:
# 			i=a[j]
# a.remove(i)
# a.insert(a[-1],i)
# print(a)
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print("%d*%d = %d" % (i,j,i*j), end='\t')
# 		if i==j:
# 			break
# 	print('')
# import time
# # t=time.time()
# # print("当前时间:",t)
# # localtime = time.localtime(time.time())
# # print('本地时间：',localtime)
# # localtime = time.asctime(time.localtime(time.time()))
# # # print('本地时间：',localtime)
# # time.sleep(10)
# # print('本地时间：',localtime)
# for i in range(4):
#     # print(str(int(time.time()))[-2:])
#     # time.sleep(2)
#     print(str(int(time.time()))[-           2:])
# a='qweqweer123wer'
# b=a.split('w')
# print(b)
# c=''.join(b)
# print(c)
# a='hello %s,我今年%d岁' % ('qwe',100)
# # b=a%('qwe',100)
# print(a)

# b= '%d*%d=%d' % (9,9,9*9)
# print(b)
# a=[12,23,34,45]
# b=[876,567,543]
# a.extend(b)
# print(a)
# import requests
# import  re
# class  FreeBuf():
#     def send_request(self):
#         url = 'https://www.freebuf.com/page/2'
#         #发送请求
#         res = requests.post(url)
#         #读取结果  1.text  以文本的方式接收,结果是个字符串
#         #content  以字节方式接收
#         hh = res.content.decode('utf-8')
#         return  hh
#     def  guolv(self,x):
#         patt = re.compile('')
#         items = patt.findall(x)
# fr = FreeBuf()
# hh = fr.send_request()
# fr.guolv(hh)return context.wrap_socket(sock, server_hostname=server_hostname
import requests
import  re
class  FreeBuf():
    def send_request(self):
        url = 'https://www.freebuf.com/page/2'
        #发送请求
        res = requests.post(url)
        #读取结果  1.text  以文本的方式接收,结果是个字符串
        #content  以字节方式接收
        hh = res.content.decode('utf-8')
        return  hh
    def  guolv(self,x):
        patt = re.compile('')
        items = patt.findall(x)
fr = FreeBuf()
hh = fr.send_request()
fr.guolv(hh)