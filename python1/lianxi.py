# a=int(input('>>>'))
# f=[]
# for i in range(int(a/2)+1):
#     for j in range(2,a):
#         if a%j==0:
#             f.append(j)
#             a=a//j
#             break
# print(f)


# import day1
# class Mnb():
#     def asd(self):
#         print(123)
#     def qwe(self):
#         print(456)
# class Ccc():
#     def vvv(self):
#         print('hello')
#         # self.__bbb()
#     def bbb(self):
#         print('123')
# # Ccc().bbb()
# # ccc=Ccc()
# # ccc.vvv()
# class qwe(Ccc,Mnb):
#     pass
# q=qwe()
# q.vvv()
# q.asd()
      # def vvv(self):
      #     print('hello')
      #     print(123)
      # pass
# a=qwe()
# a.vvv() b
# class Wu():
#     def __init__(self,name,xue,miao):
#         self.name=name
#         self.xue=xue
#         self.miao=miao
#     def  qqq(self,x):
#         self.xue -= 200
#         num=0
#         for i in range(x+1):
#             num+=i
#         print('{},还剩下{}血'.format(self.name,self.xue,self.miao))
#         print(num)
#         return 100
#     def  ccc(self):
#         self.miao += 8
#         print('{},经过{}秒才出来'.format(self.name,self.miao))
# q=Wu('刘旭',1000,10)
# q.qqq(100)
# q.ccc()

# class Qq():
#     def qqq(self):
#         a=int(input('>>>'))
#         ff = [str(i) for i in range(7)]
#         c=''
#         while True:
#             b = a % 8
#             c = c + ff[b]
#             a = a//8
#             if a==0:
#                 break
#         print(c[::-1])
# q=Qq()
# q.qqq()
# import requests
# import re
# class FreeBuF_():
#     def send_qingqiu(self):
#         url='http://www.freebuf.com/page/1'
#         head = {
#             'User=Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#
#         }
#         #发送请求
#         res = requests.post(url,headers=head)
#         #读取结果 1.text 以文本的方式接受，结果字符串
#         #         2.contnet 以字节的方式接受，结果是字节类型
#         # print(res.text)
#         hh=res.content.decode('utf-8')
#         return hh
#     def guolv(self,x):
#         patt = re.compile('<div class="news-info">(.*?)<dd>',re.S)
#         itesms = patt.findall(x)
#         # print(len(itesms))
#         tit=[]
#         for i in itesms:
#             aa=re.findall('title="(.*?)"',i)
#             tit.append(aa[0])
#         print(tit)
#         return tit
#         # print(tit)
#     def save(self,y):
#         with open('b.txt','a',encoding='utf-8') as ff:
#             for i in y:
#                 ff.write(i+'\n')
# fr = FreeBuF_()
# hh = fr.send_qingqiu()
# yy = fr.guolv(hh)
# fr.save(yy)
# # itesms
# import requests
# import re
# url='https://www.qiushibaike.com/imgrank/page/1/'
# head = {
#     'User=Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#     }
# res = requests.post(url, headers=head)
# html = res.content.decode('utf-8')
# patt = re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')
# ite = patt.findall(html)
# print(len(ite))

import requests
import re
url='http://www.zhipin.com/c101210100-p100301/?ka=search_100301'
head = {
    'User=Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
res = requests.post(url,headers=head)
html = res.content.decode('utf-8')
a=[]
patt = re.compile(r'<img width="100" alt="(.*?)"')
ite = patt.findall(html)
a.extend(ite)
print(ite)
p = re.compile('src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class=""')
c=p.findall(html)
b=0
# for i in c:
#     j='http://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg'.format(i[0],i[1])
#     msg=requests.get(j,headers=head)
#     hh = msg.content
#     with open('{}.jpg'.format(a[b]),'wb')as f:
#         f.write(hh)
#     b += 1