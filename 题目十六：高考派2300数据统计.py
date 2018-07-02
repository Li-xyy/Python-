# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 11:07:54 2018
题目十六：高考派2300数据统计
@author: Administrator
"""

东北=['辽宁','吉林','黑龙江']
华东=['上海','江苏','浙江','安徽','福建','江西','山东']
华北=['北京','天津','河北','山西','内蒙古']
华中=['河南','湖北','湖南']
华南=['广东','广西','海南']
西南=['重庆','四川','贵州','云南','西藏']
西北=['陕西','甘肃','青海','宁夏','新疆']
area=['东北','华东','华北','华中','华南','西南','西北']

f=open("./全国招生计划表0206C正确.txt")
data=f.readlines()
import json
lm=[]
for i in range(142600):
    t=json.loads(data[i])
    lm.append(t)
a=0
b=0
c=0
d=0
e=0
f=0
g=0
for j in range(142600):
    if lm[j]['status']==1:
        le=len(lm[j]['data'])
        for k in range(le):
            if lm[j]['data'][k]['city']=='辽宁' or '吉林' or '黑龙江':
                a=a+int(lm[j]['data'][k]['plan'])
            elif lm[j]['data'][k]['city']=='上海' or '江苏' or '浙江' or '安徽' or '福建' or '江西' or '山东': 
                b=b+int(lm[j]['data'][k]['plan'])
            elif lm[j]['data'][k]['city']=='北京'or'天津'or'河北'or'山西'or'内蒙古': 
                c=c+int(lm[j]['data'][k]['plan'])
            elif lm[j]['data'][k]['city']=='河南'or'湖北'or'湖南': 
                d=d+int(lm[j]['data'][k]['plan'])
            elif lm[j]['data'][k]['city']=='广东'or'广西'or'海南': 
                e=e+int(lm[j]['data'][k]['plan'])
            elif lm[j]['data'][k]['city']=='陕西'or'甘肃'or'青海'or'宁夏'or'新疆': 
                f=f+int(lm[j]['data'][k]['plan'])
            elif lm[j]['data'][k]['city']=='东北'or'华东'or'华北'or'华中'or'华南'or'西南'or'西北': 
                g=g+int(lm[j]['data'][k]['plan'])
print('东北的招生人数：'.format(a))
print('华东的招生人数：'.format(b))
print('华北的招生人数：'.format(c))
print('华中的招生人数：'.format(d))
print('华南的招生人数：'.format(e))
print('西南的招生人数：'.format(f))
print('西北的招生人数：'.format(g))           

        
        
        