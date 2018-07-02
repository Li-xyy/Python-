# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:19:19 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url="http://api.openweathermap.org/data/2.5/forecast?q=mianyang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"description":"(.*?)"').findall(data)
ls1=re.compile('"temp":(.*?),').findall(data)
ls2=re.compile('"pressure":(.*?),').findall(data)
for i in range(36):
    lsa=ls[i]
    lsb=ls1[i]
    lsc=ls2[i]
    print("天气:{} 温度:{} 气压:{}".format(lsa,lsb,lsc))
