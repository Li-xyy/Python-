# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:16:37 2018

@author: Administrator
"""
for i in range(0,13):
    import urllib.request as r
    req=r.Request('https://www.qiushibaike.com/8hr/page/{}'.format(i),headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
    myurl=r.urlopen(req)
    print(myurl.getcode())
    data=myurl.read().decode('utf-8')
    import re
    ls=re.compile('<h2>(.*?)</h2>',re.S).findall(data)
    ls1=re.compile('<span>(.*?)</span>',re.S).findall(data)
    ls2=ls1[0:24]
    for i in range(24):
        ls3=ls[i]
        ls4=ls2[i]
        print("作者:{}\n内容：{}".format(ls3,ls4))
  
    
        