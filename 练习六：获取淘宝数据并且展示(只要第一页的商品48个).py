# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:07:01 2018

@author: Administrator
"""

import urllib.request as r
url='https://s.taobao.com/search?q=%E7%9F%AD%E8%A2%96&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180622&ie=utf8&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
for x in range(0,35):
        a=data['mods']['itemlist']['data']['auctions'][x]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][x]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][x]['nick']
        e=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
        print("商品名:{} 价格:{} 付款人数:{} 店铺:{} 地址:{}".format(a,b,c,d,e))

ls=[]
for x in range(0,35):
        b=data['mods']['itemlist']['data']['auctions'][x]['view_price']
        ls.append(float(b))
        sorted(ls)
print(ls)
ls1=reversed(ls)
for i in ls1:
    print(i)
    
    
    
    
    
ls=[]
for x in range(0,35):
        c=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        c1=c.replace("人付款","")
        ls.append(float(c1))
        sorted(ls)
print(ls)


for x in range(0,35):
    a=data['mods']['itemlist']['data']['auctions'][x]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][x]['view_price']
    c=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
    d=data['mods']['itemlist']['data']['auctions'][x]['nick'] 
    e=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
    f=data['mods']['itemlist']['data']['auctions'][x]['view_fee'] 
    
    
    if float(f)==0:
        try:
            g=data["mods"]["itemlist"]["data"]["auctions"][x]["icon"][1]["iconPopupComplex"]["subIcons"][0]["icon_content"]
        except Exception as err:
            if g=="15天退货":
                print("商品名:{} 价格:{} =====包邮 ======15天退换货".format(a,b))    
print("没有又包邮又15退货的商品")       
                
    print("商品名:{} 价格:{} =====包邮 ======15天退换货".format(a,b))    
            
    
 g=data["mods"]["itemlist"]["data"]["auctions"][x]["icon"][1]["iconPopupComplex"]["subIcons"][0]["icon_content"]
    print(g)

#mod>itemlist>data>auction[x]>icon[2]>iconPopupComplex[2]>subIcons[2]>icon_content
for x in range(0,35):
    g=["mod"]["itemlist"]["data"]["auction"][x]["icon"][1]["iconPopupComplex"]["subIcons"][0]["icon_content"]
    print(f)                    


