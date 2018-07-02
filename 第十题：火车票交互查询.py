# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:33:01 2018

@author: Administrator
"""



def hanzi_to_pin(s):
    ls=open('./火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc

import urllib.request as r#导入联网工具包，命令为r
data=input('请输入年月日')
from_station=input('出发站')#北京
from_station=hanzi_to_pin(from_station)
to_station=input('到达站')#成都
to_station=hanzi_to_pin(to_station)
print(data,from_station,to_station)

url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(data,from_station,to_station).replace("\n","")
print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data["data"]["result"]

p=" "
tit="车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注".format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
tit=tit.split(p)
for i in tit:
    print(i.center(10),end='')
print()

####按出发时间排序 
ls=[]
for x in range(9):
    sp=data[x].split('|')
    ls1=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
    ls.append(ls1)
mysort=lambda b:b[2][0]
ls.sort(key=mysort)
for i in range(9):
    ls11=ls[i]
    for i in ls11:
        print(str(i).replace("[","").replace("]","").replace(",","").replace("'","") .replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
    print("\n")

####按历史排序 
ls=[]
for x in range(9):
    sp=data[x].split('|')
    ls1=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
    ls.append(ls1)
mysort=lambda b:b[3]
ls.sort(key=mysort)
for i in range(9):
    ls11=ls[i]
    for i in ls11:
        print(str(i).replace("[","").replace("]","").replace(",","").replace("'","") .replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
    print("\n")
    





















    title=title.split(p)
    for i in title:
        print(i.center(12),end='')
    print()
    l=len(data)
    ls1=[]
    for w in range(l):
        s=data[w]
        ls=s.split('|')
        ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--','--','--','--','--','--',ls[26],'--',ls[1]]
        ls1.append(ls)
    ls1.sort(key=lambda x:x[2][0])
    l=len(ls1)
    for i in range(l):
        ls99=ls1[i]
        for b in ls99:
            print(str(b).center(15).replace('[','').replace(']',''),end='')
        print()











for x in range(9):
    sp=data[x].split('|')
    ls=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
    for i in ls:
        print(str(i).replace("[","").replace("]","").replace("'","") .replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
    print("\n")
    
 
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
####按历史排序 
ls=[]
for x in range(9):
    sp=data[x].split('|')
    ls1=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
    ls.append(ls1)
mysort=lambda b:b[3]
ls.sort(key=mysort)
for i in ls:
        print(str(i).replace("[","").replace("]","").replace("'","") .replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
        print("\n")
    
   
    
    
    











for a in range(0,l2):
    s=data[a]
    ls=s.split('|')
    c=map_station['{}'.format(ls[6])]
    d=map_station['{}'.format(ls[7])]
    ls9=['{}/{}'.format(c,d)]
    ls8=['{}/{}'.format(ls[8],ls[9])]
    if ls[32]=='':
        ls32='--'
    else:
        ls32=ls[32]
    if ls[31]=='':
        ls31='--'
    else:
        ls31=ls[31]
    if ls[30]=='':
        ls30='--'
    else:
        ls30=ls[30]
    if ls[23]=='':
        ls23='--'
    else:
        ls23=ls[23]
    if ls[28]=='':
        ls28='--'
    else:
        ls28=ls[28]
    if ls[29]=='':
        ls29='--'
    else:
        ls29=ls[29]
    if ls[26]=='':
        ls26='--'
    else:
        ls26=ls[26]
    ls1000=[ls[3],ls9[0],ls8[0],ls[10],ls32,ls31,ls30,'--',ls23,'--',ls28,'--',ls29,ls26,'--',ls[1]]
    ls100.append(ls1000)
    ls101.append(ls1000)
lishi=lambda x:x[3]
ls100.sort(key=lishi)















chufashi=lambda x:x[2].split('/')[0]
ls101.sort(key=chufashi)
print('按照出发时间排序：')
print()













    
    for i in ls:
        print(str(i).replace("[","").replace("]","").replace("'","") .replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
    print("\n")
        
    
    
    

ls1=[]
for x in range(9):
    sp1=data[x].split("|")[10]
    ls1.append(sp1) 
sorted(ls1)
  


ls=[28,30,10,10,10,10,39.9]
l=set(ls) 
myls=[]
for i in l:
    myls.append('{}-{}'.format(i,ls.count(i)))
mysort=lambda x:int(x.split('-')[1])
myls.sort(key=mysort,reverse=True)#降序，列表中的每个元素都会调用一次mysort函数
zhongshu=myls[0].split('-')
print('出现次数对多的元素是：{} 次数是：{}'.format(zhongshu[0],zhongshu[1]))
#























