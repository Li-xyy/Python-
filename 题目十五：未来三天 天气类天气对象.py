# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 08:50:02 2018

@author: Administrator




题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法
"""




class Weather:
    def __init__(self,temp,description,pre):
        self.temp=temp
        self.description=description
        self.pre=pre
    def msg(self):
        print("temp:"+self.temp,"decription:"+self.description,"pre:"+self.pre)
day1=Weather('30','晴','800')
day2=Weather('31','晴','900')        
day3=Weather('31','晴','1000')
day1.msg()   
day2.msg()
day3.msg()

###################################method2
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=mianyang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
l=len(data['list'])

class Weather:
    def __init__(self,temp,description,pre):
        self.temp=temp
        self.description=description
        self.pre=pre
    def msg(self):
        print("temp:"+self.temp,"decription:"+self.description,"pre:"+self.pre)
for i in range(l):
    a=data['list'][i]['main']['temp']
    c=data['list'][i]['main']['pressure']
    b=data['list'][i]['weather'][0]['description']        
    day1=Weather(str(a),b,str(c))
    day1.msg()
