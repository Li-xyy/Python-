# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:29:06 2018

@author: Administrator
"""

#第三题
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/weather?q=mianyang&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode("utf-8")
import json
data=json.loads(data)
print("绵阳天气是:"+str(data['main']['temp']))
print("绵阳气压是:"+str(data['main']["pressure"]))
print("绵阳天气情况是:"+str(data['weather'][0]["description"]))
print("程序结束")