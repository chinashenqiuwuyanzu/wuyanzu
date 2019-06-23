# # import day2
# # day2.asd()
# # day2.qwe()
# # from day2 import qwe,asd
# # qwe()
# # asd()
# from day2  import *
# import random
# import copy
#
# # qwe()

# import paramiko
# with paramiko.SSHClient() as ssh123:
#     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh123.connect(hostname='192.168.0.233',port=22,username='root',password='123456')
#     a,b,c = ssh123.exec_command('ls -al /home')
# # while True:
# #     x=input('>>>')
# #     if x == exit:
# #         break
#     print(b.read().decode())
# qq = paramiko.Transport(('192.168.0.233',22))
# qq.connect(username='root',password='123456')
# sftp = paramiko.SFTPClient.from_transport(qq)
# # sftp.get('/home/zz.sh','b.sh')
# sftp.put('day1.py','/etc/day1.py')

# 发送邮件 smtp    接收邮件 pop3 imap
import smtplib
import email.mime.multipart as mul
import email.mime.text as text
message = mul.MIMEMultipart()
message['Subject'] = 'python_test'
message['From'] = '15660513120@163.com'
message['To'] = '316986133@qq.com'
txt = """刘旭舔狗！
         跨界石东方航空！
         阿斯顿发
"""
tet = text.MIMEText(txt)
message.attach(tet)
smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)

att1 = text.MIMEText(open('qqq.txt', 'rb').read(), 'base64', 'utf-8')
 
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="ccc"'
message.attach(att1)

smtp123.login('15660513120@163.com','A123456')
smtp123.sendmail('15660513120@163.com','316986133@qq.com',message.as_string())
smtp123.close()

# import socket
# while True:
#     s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     host = ('192.168.0.90',3000)
#     msg=input('>>>')
#     s.sendto(msg.encode('utf-8'),host)
#     reg = s.recv(1024)
#     print(reg.decode('utf-8'))
# import re
# a = 'q22weer123erw\n789'
# # b = re.compile('123(.*?)789')
# b = re.compile('123(.*)789',re.S)
# c = b.findall(a)
# print(c)
# import re
# a = ['wqer123wqrw789','wergdsfg123']
# # b = re.findall('123(.*)789', a)
# for i in a:
#     c=re.sub('[0-9]+','abc',i)
#     print(c)
# import re
# with open('t.txt','r')as f:
#      ff=f.read()
#      b = re.compile('123(.*)789',re.S)
#      c=b.findall(ff)
#      print(c)



# target=int(input('>>'))
# res=0
# a,b=1,1
# for i in range(target-1):
#     a,b=b,a+b
# print(a)

# for i in range(1000):
# 	for j in range(1000):
# 		for k in range(1000):
# 			if (i+100)==j*j and (j+168)==k*k:
# 				print(i)

# def asd(a):
#     for i in range(a):
#         num=0
#         for j in range(i):
#             if i%j==0:
#                 num+=i
#             if i==j:
#                 print(i)
# asd(1000)
# def asd(a):
#     l = []
#     for i in range(1,a):
#         k = 0
#         for j in range(1,i):
#             if (i % j == 0):
#                 k += j
#         if i == k:
#             l.append(i)
#     print(l)
# asd(1000)
































