# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:16:53 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url="http://www.baidu.com/s?wd=python&ie=utf-8&rsv_op=2aXSSd9KY2XQOIJfNML890WX42JQ9UVac7SPcVQ6fMWcaZV9KfQS50aPcY1UMQI7MPUZb6fV5L56X5dXK0VQ10R47Xg6XPff&tn=78040160_19_pg&ch=14&rsv_op=XLLQbJQPTZ90IWWgPPL9ZVMYZQbX7RYXeJcf6OUPUMedMQ6P4R5Je7M981JbYZ7370JKU2Q786cLVKPP2JPd126KMbh0fcdc"
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
ls1=re.compile('class="c-abstract">(.*?)</div>').findall(data)
ls2=re.compile('style="text-decoration:none;">(.*?)</a>').findall(data)
ls3=ls[4:13]
for i in range(9):
    lsa=ls3[i]
    lsb=ls1[i].replace("<em>","").replace("</em>","").replace("<font color=#CC0000>python<\/font>","")   
    lsc=ls2[i].replace("&nbsp","").replace(";","")
    print("标题:{}\n内容:{}\n网址:{}\n".format(lsa,lsb,lsc))

    