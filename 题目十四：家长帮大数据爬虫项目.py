# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:54:44 2018

@author: Administrator
"""

#1
f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
ls=re.compile('jianjie-(.*?).html').findall(s)
ls1=re.compile('(.*?)http').findall(s)
for i in range(2300):
    print("编号：{} 学校：{}".format(ls[i],ls1[i]))

f=open('./c.csv','w')
for i in range(2300):
    f.write(ls[i])

f.close()

#2.
req=r.Request('http://www.gaokaopai.com/daxue-zhaosheng-477.html ',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
myurl=
data=urlopen(req).read().decode('utf-8')
import re
ls1=re.compile('data-val="(.*?)" data-id="2"').findall(data)
ls2=re.compile(".setVar\S'claimCity', (.*?)\S\S>").findall(data)
for i in range(len(ls2)):
    print('省份:{},编号:{}'.format(ls1[i],ls2[i]))


 
 #3
import urllib.request as r
import json
f=open('./rs.txt','w')
for i in ls:
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html '
    data='id={}&type=2&city=61&state=1'.format(i).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    f.write(d+'\n')
f.close()


f=open('./rs1.txt','w')
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html '
    data='id={}&type=2&city=61&state=1'.format(ls[i]).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    print('{}'.format(i))
    f.write(d+'\n')
f.close()

f=open('./rs3.txt','w')
for i in range(2300):
    try:
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html '
        data='id={}&type=2&city=61&state=1'.format(ls[i]).encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d=r.urlopen(req).read().decode('utf-8','ignore')
        ls3=json.loads(d)
        for i in range(len(ls3['data'])):
            a1=ls3['data'][i]
            f.write('{}'.format(a1))
        f.write('\n')
    except Exception as err:
        print('')    
f.close()






    
    
    
