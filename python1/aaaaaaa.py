# import requests
# import re
# url='http://www.qiushibaike.com/imgrank/page/2/'
# head = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#     }
# res = requests.post(url, headers=head)
# html = res.content.decode('utf-8')
# print(html)
# patt = re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"' )
# ite = patt.findall(html)
# print(len(ite))
# a=0
# # for i in ite:
#     j='https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#     # print(j)
#     msg=requests.get(j,headers=head)
#     hh = msg.content
#     with open('{}.jpg'.format(a),'wb')as f:
#         f.write(hh)
#     a += 1
# import requests
# import re
# class pacha():
#     def qiushi(self):
#         url='http://movie.douban.com/top250'
#         head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#
#         }
#         res = requests.post(url, headers=head)
#         hh = res.content.decode('utf-8')
#         return hh
#     def  guolv(self,x):
#         patt = re.compile('<span class="title">(.*?)</span>',re.S)
#         itesms = patt.findall(x)
#         print(itesms)
#     #     tit=[]
#     #     #     for i in itesms:
#     #     #         aa=re.findall('title="(.*?)"',i)
#     #     #         tit.append(aa[0])
#     #     #     print(tit)
#     #     #     return tit
#     #     #
#     #     # def save(self, y):
#     #     #     with open('t.txt','a',encoding='utf-8') as ff:
#     #     #         for i in y:
#     #     #             ff.write(i+'\n')
# fr = pacha()
# hh = fr.qiushi()
# yy = fr.guolv(hh)
# # fr.save(yy)
import requests
import re
url = 'https://movie.douban.com/top250?qq-pf-to=pcqq.group'
head = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/73.0.3683.103 Safari/537.36'
        }
res = requests.get(url,headers = head)
html = res.content.decode('utf-8')
print(html)
a=[]
patt = re.compile('<img width="100" alt="(.*?)" ')#src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class="">') #(过滤)
itesms = patt.findall(html)
a.extend(itesms)
p = re.compile('src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class=""')
h = p.findall(html)
b=0
for i in h:
    j = 'https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg'.format(i[0],i[1])
    msg = requests.get(j,headers=head)
    hh = msg.content
    with open('{}.jpg'.format(a[b]),'wb') as f:
        f.write(hh)
    b = b + 1