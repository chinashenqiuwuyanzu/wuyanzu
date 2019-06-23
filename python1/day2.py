#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import copy
# c = [4,5,6]
# a = [ 12,31,c,1000]
# ff= copy.deepcopy(a)
# c.append(100)
# print(a)
# print(ff)
# a = (2, 3, 4, 2, 'sdf')
# b = a.count()
# print(len(a))
# b = [21, 3, 243, 3453]
# a.extend(b)
# a[1] = 13000
# ff = a.copy()
# print(ff)
# a = {'name': '小明', 'age': 16}
# a['sex'] = 'nan'
# a.pop('name')
# a.popitem()
# b = {'c':123,'x':456}
# b.update(a)
# print(b)
# a = {12, 23, 34, 45}
# a.add(('qew',123))
# a.pop()
# b = {21, 23, 43, 54}
# a.remove(12)
# a.update(b)
# print(a | b)
# print(a)

# a = input('请输入:')
# print(a)
# a = 'qwert '
# print(a[0:2])
# a = '123'
# print(type(a))
# a = tuple(a)
# print(a)
# a = 'qw23weeqqwr'
# print(a[::3])
# print(a[::5])
# import copy
# c = [9, 6]
# a = [1, 2, 3, c,'wqeq']
# ff= copy.deepcopy(a)
# print(ff)
# a = input('>>>')
# a =int(a)
# if a > 3:
#  print('hello')
# if a < 3:
#  print('sorry')
# a = 2
# if a > 3:
#     print('hello')
# else:
#    print('sorry')
# a =  90
# if a > 3 and a > 10:
#     print('hello')
# elif a < 2:
#     print('sorry')
# a = input('>>>')
# a = int(a)
# if a > 90:
#     print('优秀')
# elif 90 > a > 80:
#     print('良')
# elif 80 > a > 70:
#     print('及格')
# a = input('>>>')
# a = int(a)
# if a%2==0:
#     if a%3==0:
#      print('hello world')
#     # else:
#     #    print('hello')
# if a%2==0 and a%3!=0:
#                   print('hello')
# elif a%3==0:
#        print('world')
# else:
#     print(123)
# a = [212,23, 432,234,'2213']
# for i in a:
#     print(i)
# a = 100
# for i in range(1, 99, 5):
#     print(i)
# num = 0
# for i in range(1,100,2):
#  num = num + i
# sum = 0
# for c in range(2,100,2):
#     sum = sum +c
# b=num - sum
# print(b)
# num=0
# for i in range(100):
#    if i % 2 == 0:
#        num = num - i
#    else:
#        num= num + i
# print(num)
# for i in range(10):
#     if i > 5:
#         print('恭喜')
#     else:
#         print(100)
# for i in range(2):
#     for j in range(2):
#         print('小循环')
#     print('大循环')
#三次猜数字
# import random
# a = random.randrange(1,10)
# for i in range(3):
#   i = input('>>>')
#   i = int(i)
#   if  i > a:
#     print('大了')
#   elif i < a:
#     print('小了')
#
#   elif i == a:
#     print('恭喜')
#   else:
#    print('菜')
# a = [12,32,21]
# for i in (a):
#    print(i)
# for i in range(1,10):
#    for j in range(1,10):
#     print("%d*%d=%d" % (i, j, i*j), end=' ')
#     if i ==j:
#       break
#    print( ' ')
# sum=0
# for i in range(2,100):
#
#     for j in range(2,i):
#
#      if (i % j == 0):
#       break
#     else:
#       sum=sum+i
# print(sum)

# for i in range(100,999):
#     x=i//100
#     y=i//10%10
#     z=i%10
#     if i == x**3 + y**3 + z**3:
#      print(i)

# for i in range(2,1000):
#     num=0
#     for j in range(1,i):
#       if i%j==0:
#        num+=j
#     if num==i:
#        print(i)
# print('i\'m ok.')
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j !=k :
#                   print(i,j,k)
# a = 1
# b = 0
# c = input('>>>')
# c = int(c)
# for i in range(1, c+1):
#     a *= 1
#     b += a
#     print(b)
#查看是不是回文数
# a=input('>>>')
# for i in range(len(a)//2):
#    if  a[i] != a[-(i+1)]:
#        print('不是个回文')
#        break
# else:
#     print('是个回文')
# a =0
# # c = 0
# # while (a < 101):
# #     c= c+a
# #     a = a + 1
# # print(c)
# a=0
# for i in range(1,101):
#     a= a+i
# print(a)
#
# while True:
#  a = input('>>>')
#  a= a.split(',')
#  for i,j in enumerate(a):
#   a [i] = int(j)
#  k=sum(a)//len(a)
#  if a[0] < 0 :
#        break
#  print('平均数为{}'.format(k))
#  for c in a:
#     if c < k:
#       print('低于平均分{}'.format(c))
# a = []
# for i in range(6):
#     a.append(i)
# print(a)
# b = [i for  i in range(6) ]
# print(b)
#键盘上输入若干个学生的成绩，统计出平均成绩并输出低于平均分的学生成绩，用输入负数结束输入
# while True:
#  a = input('>>>')
#  a= a.split(',')
#  b=[int(i)  for i in a]
#  # for i,j in enumerate(a):
#  #  a [i] = int(j)
#  x=sum(a)/ len(a)
#  if a[0] < 0 :
#       break
#  print('平均数为{}'.format(x))
#  z = [ c for c in a if c < x]
#  # for c in a:
#  #    if c < k:
#  print('低于平均分{}'.format(z))
# 去重
# a = [12,13,13,12,13,14,15]
# for i in a:
#   b= a.count(i)
#   if b>1:
#       for j in range(b-1):
#           a.remove(i)
# print(a)
# a = [12,13,12,13,14,15]
# b = []
# for i in a :
#    if i not in b:
#        b.append(i)
# print(b)
#文件夹创建 九九乘法表
# f = open(‪'C:\\Users\\Wushuai\\Desktop\\55.txt','w',encoding='utf-8')
# f = open(r'a.txt','r',encoding='utf-8')
# for i in f:
#   for j in range(1,i+1):
#      f.write('"%d*%d=%d"\t' % (i, j, i*j) )
#   f.write('\n')
# b=f.readline()
# c=f.readline()
# d=f.readline()
# print(b)
#   f.write('abckdg')
#   f.write('asgjgsjh\n')
# b= f.startwith('abc')
# print(b)
# f.close()
#过滤15到20 行
# f = open('a.txt','r',encoding='utf-8')
# b = f.readlines()
# for i in b:
#    if i[:3]==('abc'):
#     print(i)
# for i in range(1,21):
#     if i < 15:
#         f.readline()
#     else:
#      b = f.readline()
#      print(b)
#打印列表中所有第一大和第二大的数
# a=input('>>.')
# b = [12,13,14,15,16,17]
# # b=a.split(',')

# b=[int(i) for i in b]
# b.sort()
# o=[]
# f=b.count(b[-1])
# for k in range(1,f+1):
#     o.append(b[-1])
#     b.remove(b[-1])
# d=b.count(b[-1])
# for j in range(1,d+1):
#     o.append(b[-1])
# print(o)


# a = [12,13,14,15,16,17]
# a.reverse()
# b=a[0]
# c=a[1]
# print(b,c)
#阶乘之和
# a=0
# b=1
# for i in range(1,4):
#     b=i*b
#     a=a+b
# print(a)
#公鸡是i  j是母鸡  小鸡是k
# for i in range(1,100):
#     for j in range(1,100):
#         k=100-j-i
#         if (2*i+ j + k/2 ==100):
#          print(i,j,k)
# a = input('>>>')
# print(a[0])
# print(a[-1])
#三角形
# a=input('>>>')
# b=input('>>>')
# c=input('>>>')
# a=int(a)
# b=int(b)
# c=int(c)
# if a+b>c and a+c>b and b+c>a:
#     print('shi')
# else:
#     print('bushi')
#冒泡排序
# a=[15,13,14,38,49,27]
# for i in range(0, len(a)):
#     for j in range(0,len(a)-1):
#         if a[j] >  a[j+1]:
#            a[j],a[j+1]= a[j+1],a[j]
#     print(a)
# l=len(a)
# for i in range(0,l):
#     for j in range(0,l-1):
#         if a[i] >= a[j]:
#            a[i],a[j]=a[j],a[i]
#
# print(a)
# a=['adsa','asfdsa','asfsaf','asfsdf',]
# a.pop(0)
# a.append('adsa')
# print(a)
# a='1232'
# b=int(a)
# print(hex(b))
# for i in range(1,10000000000000):
#     a=0
#     for j in range(1,i):
#        if i%j==0:
#            a=a+j
#     if a==i:
#         print(a)
# f=open('abc.png','rb')
# b=f.read()
# ff=open('abc1.png','wb')
# ff.write(b)
# f.close()
# with open('a.txt','r+',encoding='utf-8') as f:
#     f.write('我')
#     b=f.read()
# print(b)
# def a():
#     b=0
#     for i in range(1,101):
#         b=b+i
#     print(b)
# a()
# a=input('>>>')
# for i in range(len(a)//2):
#     if a[i]==a[-(i+2)]:
#         print('no')
#         break
# else:
#         print('yes')
# a=input('>>>')
# a=a.split(',')
# for i in range(0,len(a)):
#     for j in range(0,i):
#         if a[i] >= a[j]:
#             t=a[i]
#             a[i]=a[j]
#             a[j]=t
# print(a)
# num=0
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#            break
#     else:
#          num=num+i
# print(num)
# a=input('>>>')
# b=a.split(',')
# b=[int(i) for i in b]
# for i in b:
#     for j in b:
#         for k in b:
#             print(i,j,k)
# a=[]
# for i in range(4):
#     a.append(i)
# print(a)
# 不用int将字符串变成整数
#  1*100     2*10       3*1
#  1*10**2   2*10**1   3*10**0
# a='123'
# b=a[::-1]              #反转成'321'
# c=0
# for i in range(len(a)):   #len(a)=3  所以i的取值就是 0,1,2
#     for j in range(10):   #j是数字0-9
#         if str(j)==b[i]:  #假如j=3 即str(j)='3'
#             c+=j*10**i    #此时没有str的j还是数字j
# print(c)
# a=input('>>>')
# for i in range(len(a)//2):
#     if a[i]!=a[-(i+1)]:
#         print('no')
#         break
# else:
#     print('yes')
# for i in range(1,10):
#     for j in range(1,10):
#         print("%d*%d=%d" % (i, j, i * j), end=' ')
# a = [12, 13, 14, 15]
# a.append(11)
# a.sort()
# print(a)
# a=[]
# c=int(input('>>>')
# while True:
#     for i  in c:
#        if i==0:
#            break
#        else:
#            a=a.append(c)
#            a.sert()
#            print(a)
# b = 1
# def a():
#     global b
#     b=0
#     print(b)
# a()
# print(b)
# def lksfdh(x):
#     print('hello')
#     print(x)
# lksfdh('sarfghks' )
# b=sum(range(1,101))
# print(b)
# def ppp(b,c):
#     print(b)
# ppp(12,17)       #占位
# ppp(c=12,b=17)   #仔细看打印结果
# def ppp(b=100):
#     a=0
#     for i in range(b+1):
#         a=a+i
#     print(a)
# ppp()
#质数之和
# num=0
# def ppp(a,b):
#   for i in range(2,100):
#     for j in range(2,i):
#       if i%j==0:
#           break
#     else:
#       num+=i
# print(num)
# # ppp(2,100)
# def  ppp(**b):
#     print(b)
# ppp(name=123,age=1,sex='nan')
# def ppp(* args):
# def pp(**kwargs):

# a=input('>>>')
# a=int(a)
# def ppp(b):
#     a=0
#     for i in range(1,b+1):
#         a+=i
#     print(a)
#     return  a
# ppp(100)
# c=ppp(100)+2
# print(2)
# def ppp(x):
#      a=0
#      for i in range(1,x+1):
#         a+=i
#      return a
# for i in range(10,41,10):
#     c=ppp(i)+2
#     print(c)
# def jia(x,y):
#     l = x + y
#     c = x - y
#     z =  x * y
#     q = x // y
#     print(l,c,z,q)
# jia(4,2)
# # def jian(x,y):
# #     c=x-y
# #     print(c)
# # jian(113,11)
# a=int(input('x'))
# b=input('>>>')
# c=int(input('y'))
# def jia(c):
#
#      if b=="+":
#       print()
# a=lambda :3+4
# print(a())
# a=lambda x,y:x+y
# b=lambda x,y:x-y
# c=lambda x,y:x*y
# d=lambda x,y:x//y
# s=input('>>>')
# while True:
#   if '+'in s:
#     d=s.split('+')
#     print(b(int(d[0]),int(d[1])))
#   elif '-' in s:
#     d = s.split('-')
#     print(b(int(d[0]), int(d[1])))
#   elif '*' in s:
#     d = s.split('*')
#     print(b(int(d[0]), int(d[1])))
#   elif '//' in s:
#      d = s.split('//')
#      print(b(int(d[0]), int(d[1])))
#   else:
#      break
# def shan(x,y,z):
#      x=list(x)
#      for i in range(y,y+z):
#          # for j in range(y,i):
#             x.pop(y)
#             # x.pop(y+z)
#             # if
#             #    break
#      x=str(x)
#      b=''.join(x)
#      print(x)
# shan('qwerty',2,2)
# def a(x,y,z):
#     x=list(x)
#     if y+z>len(x):
#         y+z == len(x)
#     for i in range(y,y+z):
#         x.pop(y)
#     x=str(x)
#     b=''.join(x)
#     print(b)
# a('asfdsf',2 ,1)
# a=[12,23,34,45]
# c=11
# for i in range(0,len(a)):
#     if a[0] > c:
#
#         break
#
# d=a[:i] + [c]+ a[i:]
# print(d)
# a=[12,32,34,54,65]
# d=a[:1]
# b=a[1:]
# print(d)
# print(b)
# a=[76,56,34,32,11]
# a=[12,23,34,53,24]
# c=int(input('>>>'))
# a.append(c)
# # for i in range(1,len(a)):
# #     for j in range(1,i):
# #         if a[j] > a[j+1]:
# #             t=a[j]
# #             a[j]=a[j+1]
# #             a[j+1]=t
# # print(a)
# for i in range(0,len(a)):
#     for j in range(0,i):
#         if a[i] >= a[j]:
#             t=a[i]
#             a[i]=a[j]
#             a[j]=t
#
# print(a)
# def ppp(a,b):
#     for i in range(0,len(a)):
#         if a[0]+a[i]==b:
#             break
#         else:
#           print('no')
#           print(a[0],a[i])
#     return
# ppp([12,23,34],35)
# 一个函数，传两个参数a,b，a是数组，b是一个数字，找出a数组中两数只和等于b，打印出来这两个数
# def ppp(a,b):
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if a[i]+a[j]==b and i!=j:
#                print(a[i],a[j])
# ppp([12,23,34],35)
#将列表中最大的放在最后一位，最小的放在第一位
# a=[12,23,34,45,11,24]
# for i in a:
#     for j in range(len(a)):
#         if i < a[j]:
#             i=a[j]
# a.remove(i)
# a.insert(a[-1],i)
# for c in a:
#     for j in range(len(a)):
#         if c > a[j]:
#            c=a[j]
# a.remove(c)
# a.insert(0,c)
# print(a)
#将列表中的元素向左挪一位
# a=[12,45,23,46,78]
# for i in a:
#     if i==a[0]:
#         break
# a.remove(i)
# a.append(i)
# print(a)
#十进制转十六进制
# a=int(input('>>>'))
# ff = [str(i) for i in range(10)] +['a','b','c','d','e','f']
# c=''
# while True:
#     b = a % 16
#     c = c + ff[b]
#     a = a//16
#     if a==0:
#         break
# print(c[::-1])
#十进制转八进制
# a=int(input('>>>'))
# ff = [str(i) for i in range(7)]
# c=''
# while True:
#     b = a % 8
#     c = c + ff[b]
#     a = a//8
#     if a==0:
#         break
# print(c[::-1])
# goods = [['电脑',1999],
#          ['鼠标',10],
#          ['游艇',20],
#          ['美女',998],
#     ]
# car = []
# money = input('输入金额')
# if not money.isdigit():
#     exit()
# qian = int(money)
# yuer = qian
# for i in goods:
#     print(i)
# buyindex = ''
# while True:
#     buy = input("输入'no'退出，请输入购买")
#     if buy.isdigit():
#         buyindex = int(buy)
#         if buyindex < 1 or buyindex > len(goods):
#             print('没有符合')
#             continue
#     elif buy == 'q':
#         if len(car) < 1:
#             print("没有购买")
#             exit()
#         for j in car:
#             print(car)
#             print("已经购买,剩余余额：%d" % yuer)
#             exit()
#     price = goods[buyindex - 1][1]
#     price = int(price)
#     if (price > yuer):
#         print('余额不足,请充值')
#         chong = int(input('充值金额'))
#         yuer += chong
#         if chong > 0:
#             print('充值成功')
#             print('剩余金额:%d' % yuer)
#     elif (price <= yuer):
#         yuer = yuer - price
#         car.append(goods[buyindex-1])
#         print('购买成功')
# a=[12,23,34,12,23,45,56]
# # b=[]
# # for i in a:
# #     if i not in b:
# #         b.append(i)
# # print(b)
# for i in a:
#        b=a.count(i)
#        if b>1:
#           for j in range(b-1):
#               a.remove(i)
# print(a)
# def ppp(a,b):
#     num = 0
#     for i in range(a,b+1):
#        for j in range(a,i):
#            if i%j==0:
#                break
#        else:
#             num=num+i
#     print(num)
# ppp(2,100)
#因数之和
# l=[]
# for i in range(1,1000):
#    num = 0
#    for j in range(1,i):
#        if (i%j==0):
#           num+=j
#    if i==num:
#        l.append(i)
# print(l)
# def asd():
#     print('hello')
# def qwe():
#     print('123')
# if __name__=='__main__':
#   for i in range(10):
#       print(i)
# try:
#     a= 123 + 'qwe'
#     print(a)
# except:
#     print(123456)
# try:
#     a=1111+'qwewq'
#     print(a)
# except :
#     print(666)
# else:
#     print('hello')
# finally:
#     print(123)
# try:
#     f=[i for i in range(10)]
#     print(f)
# except:
#     print(123)
# import xlwt
# # 创建一个空的excel文件
# f=xlwt.Workbook()
# # 添加一个标签页  括号中是标签页的名称
# sheet=f.add_sheet('python_test')
# # 写入数据 需要固定写入的单元格 x,y
# #第一个数字代表行
# #第二个数字代表，列
# #第三个内容代表 写入的内容
# for i in range(1,100):

#
#      sheet.write(i,1,i+1)
# #保存文件
# f.save('aaaa.xls')

# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('python_test')
# for i in range(1,10):
#     for j in range(1,i+1):
#      sheet.write(i-1, j-1, ("%d*%d=%d" % (i, j, i*j) ) )
# f.save('aaaa.xls')


# import xlrd
# f = xlrd.open_workbook('aaaa.xls')
# # sheet = f.sheets()[0]
# # sheet1 = f.sheets()[1]
# # b=f.nsheets
# # print(b)# b=f.sheet_names()
# # print(b)
# sheet=f.sheet_by_name('python_test')
# # b=sheet.nrows
# b=sheet.ncols
# print(b)
# # for i in range(b):
# # c=sheet.col_values(0)
# c=sheet.cell(8,8).value
# print(c)
# import xlrd
# f = xlrd.open_workbook('aaaa.xls')
# sheet=f.sheet_by_name('python_test')
# for i in range(3,8):
#     for j in range(0,i):
#         c = sheet.cell(i,j).value
# print(c)
# import xlrd
# f=xlrd.open_workbook('aaa.xls')
# print(f)
# with open('qqq.txt','r+',encoding='utf-8') as f:
#    a=f.read()
#    print(a)
# b = a.split(',')
# print(b)
# import xlwt
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('ccc')
# # b=a.split(',')
# for i in range(0,3):
#     for j in range(0,4):
#         if b[i]//2:
#           sheet.write(j,i,b)
# ff.save('aaa.xls')                                                                                                                                                                                                                              
#
# # b=a.split(',')







import xlwt
import xlrd
with open('qqq.txt','r+',encoding='utf-8') as f:
   a=f.readlines()
c=[]
ff=xlwt.Workbook()
sheet=ff.add_sheet('ccc')
for i in range(5):
    b=a[i]
    b = b.split(',')
    c.append(b)
print(c)
f.close()
for j in range(len(c)):
    for k in range(4):
         sheet.write(j,k,(c[j][k]))
ff.save('aaa.xls')
# # #
# # # # b=a.split(',')
#
# import xlwt
# import xlrd
# with open('qqq.txt','r+',encoding='utf-8') as f:
#    a=f.readlines()
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('ccc')
# for i in range(5):
#     b=a[i]
#     b = b.split(',')
#     # print(b)
#     for k in range(5):
#
#  def asd(x):
#     a=0
#     for i in range(x+1):
#         a+=i
#     return a
# b=asd(100)
# print(b)
# import pymysql
# db=pymysql.connect('localhost', port='3306', user='root', passwd='123465', db='nobi3',charset='utf8')
# cursor=db.cursor()
# try:
#   cursor.execute("DROP DATABASE PyTest")
# except Exception as e:
#     print(e)
# finally:
#     pass
# import os
# print(os.getcwd())
#
# os.chdir(r'D:\Xmind_8_Pro')
# print(os.getcwd())
# b=os.popen('route print')
# print(b.read())
#print(os.listdir(r''))
# os.mkdir('aaa')


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('192.168.0.90',3000))
# while True:
#        client,addr=s.recvfrom(1024)
#        print(client.decode('utf-8'))
#        msg=input('>>>')
#        s.sendto(msg.encode('utf-8'),addr)

# import smtplib
# import email.mime.multipart as mul
# import email.mime.text as text
# ww=['316986133@qq.com','465105918@qq.com']
# message = mul.MIMEMultipart()
# message['Subject'] = 'python_test'
# message['From'] = '15660513120@163.com'
# message['To'] = '.'.join(ww)
# txt="""你好 中国你好
#     世界你好
# """
# tet = text.MIMEText(txt)
# message.attach(tet)
# smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('15660513120@163.com','A123456')
# smtp123.sendmail('15660513120@163.com',ww,message.as_string())
# smtp123.close()
# print(hex(333))
# print(oct(333))
# print(bin(333))
# print(int(0b101001101))
# print(ord('\\'))
# a=[123,2345,435,46,5436,54]
# print(max(a))
# a,b=divmod(100,16)
# print(a,b)
# import lianxi
# # lianxi.Ccc().vvv()
# # lianxi.Ccc().bbb()
# lianxi.ccc.vvv()