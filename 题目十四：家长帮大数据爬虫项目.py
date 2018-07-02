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
  
m=[]   
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html '
    data='id={}&type=2&city=62&state=1'.format(ls[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html '
        data='id={}&type=2&city=62&state=1'.format(ls[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))
        continue
f=open('./rs1.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close()





    
    
    
