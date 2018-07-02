# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:51:20 2018

@author: Administrator
"""



f=open('./qz.csv','w')
f.write("商品名,商品价格,付款人数,店铺,地址\n")
for i in range(0,100):
    import urllib.request as r
    a=44*i
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&loc=%E5%93%88%E5%B0%94%E6%BB%A8&s=0&s={}&ajax=true'.format(a)
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    if data=='':
        print()
        continue
    q=len(data['mods']['itemlist']['data']['auctions'])
    for x in range(0,q):
        a=data['mods']['itemlist']['data']['auctions'][x]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][x]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][x]['nick']
        e=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
        f.write("{},{},{},{},{}\n".format(a,b,c,d,e))
        
    print('第{}页已获取数据'.format(i+1))
f.close()




