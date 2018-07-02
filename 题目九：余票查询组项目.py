# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:16:17 2018

@author: Administrator
"""



import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-26&leftTicketDTO.from_station=CQW&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
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

for x in range(9):
    sp=data[x]
    sp=sp.split('|')
    if sp[3].startswith("G"):
        ls=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
        for i in ls:
            print(str(i).replace("[","").replace("]","").replace("'","").replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
        print("\n")
for x in range(9):
    sp=data[x]
    sp=sp.split('|')
    if sp[3].startswith("K"):
        ls=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
        for i in ls:
            print(str(i).replace("[","").replace("]","").replace("'","").replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
        print("\n")
for x in range(9):
    sp=data[x]
    sp=sp.split('|')
    if sp[3].startswith("T"):
        ls=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
        for i in ls:
            print(str(i).replace("[","").replace("]","").replace("'","").replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
        print("\n")
for x in range(9):
    sp=data[x]
    sp=sp.split('|')
    if sp[3].startswith("Z"):
        ls=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
        for i in ls:
            print(str(i).replace("[","").replace("]","").replace("'","").replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
        print("\n")    

