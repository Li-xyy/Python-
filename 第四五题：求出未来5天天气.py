# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:38:07 2018

@author: Administrator
"""

import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=mianyang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
##########中文版第一问
#21日6点
a=data["city"]['name']
b=data["list"][0]['dt_txt']
c=data["list"][0]["main"]["temp"]
d=data["list"][0]["weather"][0]["description"]
e=data["list"][0]["main"]["pressure"]
f=data["list"][0]["main"]["temp_max"]
g=data["list"][0]["main"]["temp_min"]
a1=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#21日12点
a=data["city"]['name']
b=data["list"][2]['dt_txt']
c=data["list"][2]["main"]["temp"]
d=data["list"][2]["weather"][0]["description"]
e=data["list"][2]["main"]["pressure"]
f=data["list"][2]["main"]["temp_max"]
g=data["list"][2]["main"]["temp_min"]
a2=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#21日18点
a=data["city"]['name']
b=data["list"][4]['dt_txt']
c=data["list"][4]["main"]["temp"]
d=data["list"][4]["weather"][0]["description"]
e=data["list"][4]["main"]["pressure"]
f=data["list"][4]["main"]["temp_max"]
g=data["list"][4]["main"]["temp_min"]
a3=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#22日6点
a=data["city"]['name']
b=data["list"][8]['dt_txt']
c=data["list"][8]["main"]["temp"]
d=data["list"][8]["weather"][0]["description"]
e=data["list"][8]["main"]["pressure"]
f=data["list"][8]["main"]["temp_max"]
g=data["list"][8]["main"]["temp_min"]
a4=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#22日12点
a=data["city"]['name']
b=data["list"][10]['dt_txt']
c=data["list"][10]["main"]["temp"]
d=data["list"][10]["weather"][0]["description"]
e=data["list"][10]["main"]["pressure"]
f=data["list"][10]["main"]["temp_max"]
g=data["list"][10]["main"]["temp_min"]
a5=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#22日18点
a=data["city"]['name']
b=data["list"][12]['dt_txt']
c=data["list"][12]["main"]["temp"]
d=data["list"][12]["weather"][0]["description"]
e=data["list"][12]["main"]["pressure"]
f=data["list"][12]["main"]["temp_max"]
g=data["list"][12]["main"]["temp_min"]
a6=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#23日6点
a=data["city"]['name']
b=data["list"][16]['dt_txt']
c=data["list"][16]["main"]["temp"]
d=data["list"][16]["weather"][0]["description"]
e=data["list"][16]["main"]["pressure"]
f=data["list"][16]["main"]["temp_max"]
g=data["list"][16]["main"]["temp_min"]
a7=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#23日12点
a=data["city"]['name']
b=data["list"][18]['dt_txt']
c=data["list"][18]["main"]["temp"]
d=data["list"][18]["weather"][0]["description"]
e=data["list"][18]["main"]["pressure"]
f=data["list"][18]["main"]["temp_max"]
g=data["list"][18]["main"]["temp_min"]
a8=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#23日18点
a=data["city"]['name']
b=data["list"][20]['dt_txt']
c=data["list"][20]["main"]["temp"]
d=data["list"][20]["weather"][0]["description"]
e=data["list"][20]["main"]["pressure"]
f=data["list"][20]["main"]["temp_max"]
g=data["list"][20]["main"]["temp_min"]
a9=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#24日6点
a=data["city"]['name']
b=data["list"][24]['dt_txt']
c=data["list"][24]["main"]["temp"]
d=data["list"][24]["weather"][0]["description"]
e=data["list"][24]["main"]["pressure"]
f=data["list"][24]["main"]["temp_max"]
g=data["list"][24]["main"]["temp_min"]
a10=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#24日12点
a=data["city"]['name']
b=data["list"][26]['dt_txt']
c=data["list"][26]["main"]["temp"]
d=data["list"][26]["weather"][0]["description"]
e=data["list"][26]["main"]["pressure"]
f=data["list"][26]["main"]["temp_max"]
g=data["list"][26]["main"]["temp_min"]
a11=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#24日18点
a=data["city"]['name']
b=data["list"][28]['dt_txt']
c=data["list"][28]["main"]["temp"]
d=data["list"][28]["weather"][0]["description"]
e=data["list"][28]["main"]["pressure"]
f=data["list"][28]["main"]["temp_max"]
g=data["list"][28]["main"]["temp_min"]
a12=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#25日6点
a=data["city"]['name']
b=data["list"][32]['dt_txt']
c=data["list"][32]["main"]["temp"]
d=data["list"][32]["weather"][0]["description"]
e=data["list"][32]["main"]["pressure"]
f=data["list"][32]["main"]["temp_max"]
g=data["list"][32]["main"]["temp_min"]
a13=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#25日12点
a=data["city"]['name']
b=data["list"][34]['dt_txt']
c=data["list"][34]["main"]["temp"]
d=data["list"][34]["weather"][0]["description"]
e=data["list"][34]["main"]["pressure"]
f=data["list"][34]["main"]["temp_max"]
g=data["list"][34]["main"]["temp_min"]
a14=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#25日16点
a=data["city"]['name']
b=data["list"][36]['dt_txt']
c=data["list"][36]["main"]["temp"]
d=data["list"][36]["weather"][0]["description"]
e=data["list"][36]["main"]["pressure"]
f=data["list"][36]["main"]["temp_max"]
g=data["list"][36]["main"]["temp_min"]
a15=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#######英文版
#21日6点
a=data["city"]['name']
b=data["list"][0]['dt_txt']
c=data["list"][0]["main"]["temp"]
d=data["list"][0]["weather"][0]["main"]
e=data["list"][0]["main"]["pressure"]
f=data["list"][0]["main"]["temp_max"]
g=data["list"][0]["main"]["temp_min"]
a1=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#21日12点
a=data["city"]['name']
b=data["list"][2]['dt_txt']
c=data["list"][2]["main"]["temp"]
d=data["list"][2]["weather"][0]["main"]
e=data["list"][2]["main"]["pressure"]
f=data["list"][2]["main"]["temp_max"]
g=data["list"][2]["main"]["temp_min"]
a2=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#21日18点
a=data["city"]['name']
b=data["list"][4]['dt_txt']
c=data["list"][4]["main"]["temp"]
d=data["list"][4]["weather"][0]["main"]
e=data["list"][4]["main"]["pressure"]
f=data["list"][4]["main"]["temp_max"]
g=data["list"][4]["main"]["temp_min"]
a3=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#22日6点
a=data["city"]['name']
b=data["list"][8]['dt_txt']
c=data["list"][8]["main"]["temp"]
d=data["list"][8]["weather"][0]["main"]
e=data["list"][8]["main"]["pressure"]
f=data["list"][8]["main"]["temp_max"]
g=data["list"][8]["main"]["temp_min"]
a4=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#22日12点
a=data["city"]['name']
b=data["list"][10]['dt_txt']
c=data["list"][10]["main"]["temp"]
d=data["list"][10]["weather"][0]["main"]
e=data["list"][10]["main"]["pressure"]
f=data["list"][10]["main"]["temp_max"]
g=data["list"][10]["main"]["temp_min"]
a5=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#22日18点
a=data["city"]['name']
b=data["list"][12]['dt_txt']
c=data["list"][12]["main"]["temp"]
d=data["list"][12]["weather"][0]["main"]
e=data["list"][12]["main"]["pressure"]
f=data["list"][12]["main"]["temp_max"]
g=data["list"][12]["main"]["temp_min"]
a6=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#23日6点
a=data["city"]['name']
b=data["list"][16]['dt_txt']
c=data["list"][16]["main"]["temp"]
d=data["list"][16]["weather"][0]["main"]
e=data["list"][16]["main"]["pressure"]
f=data["list"][16]["main"]["temp_max"]
g=data["list"][16]["main"]["temp_min"]
a7=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#23日12点
a=data["city"]['name']
b=data["list"][18]['dt_txt']
c=data["list"][18]["main"]["temp"]
d=data["list"][18]["weather"][0]["main"]
e=data["list"][18]["main"]["pressure"]
f=data["list"][18]["main"]["temp_max"]
g=data["list"][18]["main"]["temp_min"]
a8=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
a=data["city"]['name']
b=data["list"][20]['dt_txt']
c=data["list"][20]["main"]["temp"]
d=data["list"][20]["weather"][0]["main"]
e=data["list"][20]["main"]["pressure"]
f=data["list"][20]["main"]["temp_max"]
g=data["list"][20]["main"]["temp_min"]
a9=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#24日6点
a=data["city"]['name']
b=data["list"][24]['dt_txt']
c=data["list"][24]["main"]["temp"]
d=data["list"][24]["weather"][0]["main"]
e=data["list"][24]["main"]["pressure"]
f=data["list"][24]["main"]["temp_max"]
g=data["list"][24]["main"]["temp_min"]
a10=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#24日12点
a=data["city"]['name']
b=data["list"][26]['dt_txt']
c=data["list"][26]["main"]["temp"]
d=data["list"][26]["weather"][0]["main"]
e=data["list"][26]["main"]["pressure"]
f=data["list"][26]["main"]["temp_max"]
g=data["list"][26]["main"]["temp_min"]
a11=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#24日18点
a=data["city"]['name']
b=data["list"][28]['dt_txt']
c=data["list"][28]["main"]["temp"]
d=data["list"][28]["weather"][0]["main"]
e=data["list"][28]["main"]["pressure"]
f=data["list"][28]["main"]["temp_max"]
g=data["list"][28]["main"]["temp_min"]
a12=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#25日6点
a=data["city"]['name']
b=data["list"][32]['dt_txt']
c=data["list"][32]["main"]["temp"]
d=data["list"][32]["weather"][0]["main"]
e=data["list"][32]["main"]["pressure"]
f=data["list"][32]["main"]["temp_max"]
g=data["list"][32]["main"]["temp_min"]
a13=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#25日12点
a=data["city"]['name']
b=data["list"][34]['dt_txt']
c=data["list"][34]["main"]["temp"]
d=data["list"][34]["weather"][0]["main"]
e=data["list"][34]["main"]["pressure"]
f=data["list"][34]["main"]["temp_max"]
g=data["list"][34]["main"]["temp_min"]
a14=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))
#25日16点
a=data["city"]['name']
b=data["list"][36]['dt_txt']
c=data["list"][36]["main"]["temp"]
d=data["list"][36]["weather"][0]["main"]
e=data["list"][36]["main"]["pressure"]
f=data["list"][36]["main"]["temp_max"]
g=data["list"][36]["main"]["temp_min"]
a15=print("The city： "+str(a),"time："+str(b),"temp："+str(c),"description："+str(d),"pressure："+str(e),"temp_max："+str(f),"temp_min："+str(g))

###第三问
#21日6点
a=data["city"]['name']
b=data["list"][0]['dt_txt']
c=data["list"][0]["main"]["temp"]
d=data["list"][0]["weather"][0]["description"]
e=data["list"][0]["main"]["pressure"]
f=data["list"][0]["main"]["temp_max"]
g=data["list"][0]["main"]["temp_min"]
a1=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))

#21日12点
a=data["city"]['name']
b=data["list"][2]['dt_txt']
c=data["list"][2]["main"]["temp"]
d=data["list"][2]["weather"][0]["description"]
e=data["list"][2]["main"]["pressure"]
f=data["list"][2]["main"]["temp_max"]
g=data["list"][2]["main"]["temp_min"]
a2=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#21日18点
a=data["city"]['name']
b=data["list"][4]['dt_txt']
c=data["list"][4]["main"]["temp"]
d=data["list"][4]["weather"][0]["description"]
e=data["list"][4]["main"]["pressure"]
f=data["list"][4]["main"]["temp_max"]
g=data["list"][4]["main"]["temp_min"]
a3=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
b1=print("建议：小雨，出门备伞，出门前关好门窗，穿衬衣")
#22日6点
a=data["city"]['name']
b=data["list"][8]['dt_txt']
c=data["list"][8]["main"]["temp"]
d=data["list"][8]["weather"][0]["description"]
e=data["list"][8]["main"]["pressure"]
f=data["list"][8]["main"]["temp_max"]
g=data["list"][8]["main"]["temp_min"]
a4=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#22日12点
a=data["city"]['name']
b=data["list"][10]['dt_txt']
c=data["list"][10]["main"]["temp"]
d=data["list"][10]["weather"][0]["description"]
e=data["list"][10]["main"]["pressure"]
f=data["list"][10]["main"]["temp_max"]
g=data["list"][10]["main"]["temp_min"]
a5=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#22日18点
a=data["city"]['name']
b=data["list"][12]['dt_txt']
c=data["list"][12]["main"]["temp"]
d=data["list"][12]["weather"][0]["description"]
e=data["list"][12]["main"]["pressure"]
f=data["list"][12]["main"]["temp_max"]
g=data["list"][12]["main"]["temp_min"]
a6=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
b2=print("建议：出门最好备伞，出门前关好门窗，建议穿短袖")
#23日6点
a=data["city"]['name']
b=data["list"][16]['dt_txt']
c=data["list"][16]["main"]["temp"]
d=data["list"][16]["weather"][0]["description"]
e=data["list"][16]["main"]["pressure"]
f=data["list"][16]["main"]["temp_max"]
g=data["list"][16]["main"]["temp_min"]
a7=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#23日12点
a=data["city"]['name']
b=data["list"][18]['dt_txt']
c=data["list"][18]["main"]["temp"]
d=data["list"][18]["weather"][0]["description"]
e=data["list"][18]["main"]["pressure"]
f=data["list"][18]["main"]["temp_max"]
g=data["list"][18]["main"]["temp_min"]
a8=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#23日18点
a=data["city"]['name']
b=data["list"][20]['dt_txt']
c=data["list"][20]["main"]["temp"]
d=data["list"][20]["weather"][0]["description"]
e=data["list"][20]["main"]["pressure"]
f=data["list"][20]["main"]["temp_max"]
g=data["list"][20]["main"]["temp_min"]
a9=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
b3=print("建议：有雨，出门备伞，出门前关好门窗，注意增添衣物")
#24日6点
a=data["city"]['name']
b=data["list"][24]['dt_txt']
c=data["list"][24]["main"]["temp"]
d=data["list"][24]["weather"][0]["description"]
e=data["list"][24]["main"]["pressure"]
f=data["list"][24]["main"]["temp_max"]
g=data["list"][24]["main"]["temp_min"]
a10=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#24日12点
a=data["city"]['name']
b=data["list"][26]['dt_txt']
c=data["list"][26]["main"]["temp"]
d=data["list"][26]["weather"][0]["description"]
e=data["list"][26]["main"]["pressure"]
f=data["list"][26]["main"]["temp_max"]
g=data["list"][26]["main"]["temp_min"]
a11=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#24日18点
a=data["city"]['name']
b=data["list"][28]['dt_txt']
c=data["list"][28]["main"]["temp"]
d=data["list"][28]["weather"][0]["description"]
e=data["list"][28]["main"]["pressure"]
f=data["list"][28]["main"]["temp_max"]
g=data["list"][28]["main"]["temp_min"]
a12=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
b4=print("建议：整天都有雨，出门备伞，出门前关好门窗，不建议进行户外运动")
#25日6点
a=data["city"]['name']
b=data["list"][32]['dt_txt']
c=data["list"][32]["main"]["temp"]
d=data["list"][32]["weather"][0]["description"]
e=data["list"][32]["main"]["pressure"]
f=data["list"][32]["main"]["temp_max"]
g=data["list"][32]["main"]["temp_min"]
a13=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#25日12点
a=data["city"]['name']
b=data["list"][34]['dt_txt']
c=data["list"][34]["main"]["temp"]
d=data["list"][34]["weather"][0]["description"]
e=data["list"][34]["main"]["pressure"]
f=data["list"][34]["main"]["temp_max"]
g=data["list"][34]["main"]["temp_min"]
a14=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
#25日16点
a=data["city"]['name']
b=data["list"][36]['dt_txt']
c=data["list"][36]["main"]["temp"]
d=data["list"][36]["weather"][0]["description"]
e=data["list"][36]["main"]["pressure"]
f=data["list"][36]["main"]["temp_max"]
g=data["list"][36]["main"]["temp_min"]
a15=print("城市是"+str(a),"时间是"+str(b),"温度是"+str(c),"天气情况是"+str(d),"气压是"+str(e),"最高温度是"+str(f),"最低温度是"+str(g))
b5=print("建议：有雨，出门备伞，出门前关好门穿，穿短衣短裤")

###############函数
def msg(x):
    a=data["city"]['name']
    b=data["list"][x]['dt_txt']
    c=data["list"][x]["main"]["temp"]
    d=data["list"][x]["weather"][0]["description"]
    e=data["list"][x]["main"]["pressure"]
    f=data["list"][x]["main"]["temp_max"]
    g=data["list"][x]["main"]["temp_min"]
    print("城市是{},时间是{},温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{}".format(a,b,c,d,e,f,g))

msg(0)
msg(2)
msg(4)
msg(8)
msg(10)
msg(12)
msg(16)
msg(18)
msg(20)
msg(24)
msg(26)
msg(28)
msg(32)
msg(34)
msg(36)
c1=data["list"][0]["main"]["temp"]
c2=data["list"][2]["main"]["temp"]
c3=data["list"][4]["main"]["temp"]
c4=data["list"][8]["main"]["temp"]
c5=data["list"][10]["main"]["temp"]
c6=data["list"][12]["main"]["temp"]
c7=data["list"][16]["main"]["temp"]
c8=data["list"][18]["main"]["temp"]
c9=data["list"][20]["main"]["temp"]
c10=data["list"][24]["main"]["temp"]
c11=data["list"][26]["main"]["temp"]
c12=data["list"][28]["main"]["temp"]
c13=data["list"][32]["main"]["temp"]
c14=data["list"][34]["main"]["temp"]
c15=data["list"][36]["main"]["temp"]
print(int(c1)*"-")
print(int(c2)*"-")
print(int(c3)*"-")
print(int(c4)*"-")
print(int(c5)*"-")
print(int(c6)*"-")
print(int(c7)*"-")
print(int(c8)*"-")
print(int(c9)*"-")
print(int(c10)*"-")
print(int(c11)*"-")
print(int(c12)*"-")
print(int(c13)*"-")
print(int(c14)*"-")
print(int(c15)*"-")

######第四题
def msg(x):
    b=data["list"][x]["main"]["temp"]
    print(b)
  
msg(0)
msg(2)
msg(4)
msg(8)
msg(10)
msg(12)
msg(16)
msg(18)
msg(20)
msg(24)
msg(26)
msg(28)
msg(32)
msg(34)
msg(36)
    
print(int(26.27)*"-")
print(int(25.08)*"-")
print(int(23.51)*"-")
print(int(30.66)*"-")
print(int(23.97)*"-")
print(int(23.63)*"-")
print(int(29.23)*"-")
print(int(23.42)*"-")
print(int(22.73)*"-")
print(int(27.77)*"-")
print(int(23.21)*"-")
print(int(23.59)*"-")
print(int(27.74)*"-")
print(int(25.61)*"-")
print(int(23.4)*"-")





#####第五题
ls=[]
ls.append(26.27)
ls.append(25.08)
ls.append(23.51)
ls.append(30.66)
ls.append(23.97)
ls.append(23.63)
ls.append(29.23)
ls.append(23.42)
ls.append(22.73)
ls.append(27.77)
ls.append(23.21)
ls.append(23.59)
ls.append(27.74)
ls.append(25.61)
ls.append(23.4)
ls=sorted(ls)

ls1=reversed(ls)
print(ls1)
for i in ls1:
    print(i)
    

   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=chengdu,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c1=data["list"][0]["main"]["temp"] 
print(c1)
   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=shanghai,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c2=data["list"][0]["main"]["temp"] 
print(c2)

   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=beijing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c3=data["list"][0]["main"]["temp"] 
print(c3)
   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=tianjin,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c4=data["list"][0]["main"]["temp"] 
print(c4)
   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=qingdao,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c5=data["list"][0]["main"]["temp"] 
print(c5)
   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=xiamen,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c6=data["list"][0]["main"]["temp"] 
print(c6)
   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=fuzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c7=data["list"][0]["main"]["temp"] 
print(c7)
   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=guangzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c8=data["list"][0]["main"]["temp"] 
print(c8)
   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=guiyang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c9=data["list"][0]["main"]["temp"] 
print(c9)
   import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=hangzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
c10=data["list"][0]["main"]["temp"] 
print(c10)
ls=[]
ls.append(c1)
ls.append(c2)
ls.append(c3)
ls.append(c4)
ls.append(c4)
ls.append(c5)
ls.append(c6)
ls.append(c7)
ls.append(c8)
ls.append(c9)
ls.append(c10)
ls=sorted(ls)

ls1=reversed(ls)
print(ls1)
for i in ls1:
    print(i)

 




