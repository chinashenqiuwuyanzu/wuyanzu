#!/usr/bin/python
# -*- coding: UTF-8 -*-
# qian = input('>>>')
# qian = int(qian)
# goods = [
#     {"name": '电脑', "price": 1999},
#     {"name": '鼠标', "price": 10},
#     {"name": '游艇', "price": 20},
#     {"name": '美女', "price": 998},
# ]
# ccc=[]
# for i in goods:
#  print(i["name"],i["price"])
# print('1:电脑, 2:鼠标,  3:游艇, 4:美女')
# q = int(input('请输入编号：'))
# ccc.append(q)
# print(ccc)
# qian = input('>>>')
# qian = int(qian)
# while True:
#     jine=input('按y结算')
#     if jine=='y':
#         break
#
# for j in goods:
#         if j["price"]>qian:
#             print('余额不足')
#             break
#         else:
#             print('购买成功')
#             break
# for  k in goods:
#        if k["price"]>qian:
#             print('余额不足,充值请继续')
#             c=int(input('>>>'))
#             b=c+qian
#             print('充值成功',b)
#             break
#        # else:
#        #      print('购买成功')









goods = [
    {"name": '电脑', "price": 1999},
    {"name": '鼠标', "price": 10},
    {"name": '游艇', "price": 20},
    {"name": '美女', "price": 998},
]
ccc=[]
while True:
     for i in goods:
        print(i["name"],i["price"])
     print('1:电脑, 2:鼠标,  3:游艇, 4:美女')
     q = int(input('请输入编号：'))
     print('加入购物车')
     aa=input('(y)查看，(m)继续购买')
     if aa=='y':
         print(q)
     qq=input('请输入不买的序号，(m)继续购买')
     if qq!='m':
         list(q).remove(qq)
     ccc.append(q)
     print(ccc)
     break
qian = input('请输入资金')
qian = int(qian)
while True:
    jine=input('按y结算')
    if jine=='y':
        break

for j in goods:
        if j["price"]>qian:
            print('余额不足')
            break
        else:
            print('购买成功')
            break
while True:
    for  k in goods:
           if k["price"]>qian:
                print('充值请继续')
                c=int(input('充钱'))
                qian=c+qian
                print('充值成功',qian)
                break
    else:
       f = input('确认购物吗？，请输入y or n：')
       if f == 'y':
           zzz=qian-k["price"]
           print('购买成功',zzz)
       break











# goods = [
#     {"name": '电脑', "price": 1999},
#     {"name": '鼠标', "price": 10},
#     {"name": '游艇', "price": 20},
#     {"name": '美女', "price": 998},
# ]
# ccc=[]
# while True:
#      for i in goods:
#         print(i["name"],i["price"])
#      print('1:电脑, 2:鼠标,  3:游艇, 4:美女')
#      q = int(input('请输入编号：'))
#      print('加入购物车成功')
#      aa=input('(y)查看购物车，(n)继续购买')
#      if aa=='y':
#          print(q)
#      qq=input('请输入不买的序号，(n)继续购买')
#      if qq!='n':
#          list(q).remove(qq)
#      ccc.append(q)
#      print(ccc)
#      break
# qian = input('请输入资金')
# qian = int(qian)
# while True:
#     jine=input('按y结算')
#     if jine=='y':
#         break
#
# for j in goods:
#         if j["price"]>qian:
#             print('余额不足')
#             break
#         else:
#             print('购买成功')
#             break
# for  k in goods:
#        if k["price"]>qian:
#             print('充值请继续')
#             c=int(input('充钱'))
#             b=c+qian
#             print('充值成功',b)
#             # break
#
#        if k["price"]<qian:
#             print('购买成功')
#             break




# num=eval(input('请输入金额：'))#只能输入数字
# goods=[
#        {'name':"电脑",'price':1999},
#        {'name':"鼠标",'price':10},
#        {'name':"游艇",'price':20},
#        {'name':"美女",'price':998},
#        ]
# print('请输入要购买的商品：')
# print('0：电脑\n1：鼠标\n2：游艇\n3：美女')
# num_goods=eval(input('请输入序号：'))#只能输入多个，输入多个时中间用逗号隔开
# sum=0
# if isinstance(num_goods,int):
#     sum+=goods[num_goods]['price']
# else:
#     for i in range(len(num_goods)):
#         if num_goods[i]>4:
#             print('请输入0~3中的数字，该商品无效，已删除')
#         else:
#             sum+=goods[num_goods[i]]['price']
#
# if num>sum:
#     flag=input('确认购物吗？，请输入y or n：')
#     if flag =='y':
#         remained=num-sum
#         print('购物成功！剩余金钱为:',remained)
#     else:
#         print('请继续购物或删除商品！')
# else:
#     while(num<sum):
#         chongzhi=eval(input('您的余额不足！请充值：'))
#         num=chongzhi+num
#         print('充值成功！')
#     flag=input('确认购物吗？，请输入y or n：')
#     if flag =='y':
#         remained=num-sum
#         print('购物成功！剩余金钱为:',remained)