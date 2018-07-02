# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:40:21 2018

@author: Administrator
"""

import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=mianyang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
##########中文版第一问

for x in range(0,20,2):
    a=data["city"]['name']
    b=data["list"][x]['dt_txt']
    c=data["list"][x]["main"]["temp"]
    d=data["list"][x]["weather"][0]["description"]
    e=data["list"][x]["main"]["pressure"]
    f=data["list"][x]["main"]["temp_max"]
    g=data["list"][x]["main"]["temp_min"]
    print("{},{},天气是：{}".format(a,b,d))
    if d=="大雨":
        print("请带伞！")
    elif d=="中雨":
        print("请带伞！")
    elif d=="小雨":
        print("请带伞！")
    else:
        print("玩开心~")
    
    
    
for i in range(10):
    if i==1:
        print("◐"*7)
    elif i==2:
        print("☞****你****☜")
    elif i==3:
        print("☞****的****☜")
    elif i==4:
        print("☞****贴****☜") 
    elif i==5:
        print("☞****心****☜")
    elif i==6:
        print("☞****小****☜")
    elif i==7:
        print("☞****管****☜")
    elif i==8:
        print("☞****家****☜")
    elif i==9:
        print("◐"*7)
 

    
