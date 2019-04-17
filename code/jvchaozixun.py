# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:22:34 2019

@author: Tsutomu
"""

# http://webapi.cninfo.com.cn/api/stock/p_stock2303?scode=000039&access_token=4e464c611ccbba981646d0cf44ad6864
 
 
#      # -*- coding: UTF-8 -*- 
#                import httplib,urllib
#                import time,json
#
#def gettoken(client_id,client_secret):
#    url='http://api.before.com/api-cloud-platform/oauth2/token' #api.before.com需要根据具体访问域名修改
#    post_data="grant_type=client_credentials&client_id=%s&client_secret=%s"%(client_id,client_secret)
#    post_data = urllib.parse.urlencode(post_data).encode(encoding='UTF8')
#    req = urllib.request.urlopen(url, post_data)
#    responsecontent = req.read()
#    responsedict=json.loads(responsecontent)
#    token=responsedict["access_token"]
#    return token
#
#                def apiget(scode,tokent):
#                    url = "http://apitest2.com/api/stock/p_stock2100?scode=%s&access_token=%s" #apitest2.com需要根据具体访问域名修改
#                    conn = httplib.HTTPConnection("apitest2.com")
#                    conn.request(method="GET",url=url%(scode,tokent))
#                    response = conn.getresponse()
#                    rescontent= response.read()
#                    responsedict=json.loads(rescontent)
#                    resultcode=responsedict["resultcode"]
#                    print responsedict["resultmsg"],responsedict["resultcode"]
#                    if(responsedict["resultmsg"]=="success" and len(responsedict["records"])>=1):
#                        print responsedict["records"]  #接收到的具体数据内容
#                    else:
#                        print 'no data'
#                    return resultcode
#
#                def apipost(scode,tokent):
#                    url = "http://apitest2.com/api/stock/p_stock2100"  #apitest2.com需要根据具体访问域名修改
#                    post_data="scode=%s&access_token=%s"%(scode,tokent)
#                    req = urllib.urlopen(url, post_data)
#                    content = req.read()
#                    responsedict=json.loads(content)
#                    resultcode=responsedict["resultcode"]    
#                    print responsedict["resultmsg"],responsedict["resultcode"]
#                    if(responsedict["resultmsg"]=="success" and len(responsedict["records"])>=1):
#                        print responsedict["records"]  #接收到的具体数据内容
#                    else:
#                        print 'no data'
#                    return resultcode
#                       
#
#                if __name__=="__main__":
#                    client_id,client_secret="100001","c4c7de76a9364a37ba3885232345bddc" #client_id,client_secret通过我的凭证获取
#                    token=gettoken(client_id,client_secret)
#                    for i in range(0,3600): #注：3600为循环访问API的次数
#                        scode=str(300000+i) #股票代码，根据自己需要传入
#                        #resultcode=apiget(scode,token)   #以http get方法获取数据
#                        resultcode=apipost(scode,token) #以http post方法获取数据
#                        if resultcode==405: #token失效，重新获取
#                            token=gettoken(client_id,client_secret)
#                            apiget(scode,token)  #get请求
#                            #apipost(scode,token)#post请求
#                        time.sleep(1)

import urllib,http.client
import time,json
import pandas
#client_id,client_secret= #client_id,client_secret通过我的凭证获取
#tokent=gettoken(client_id,client_secret)
#
#code = ['000157','000425','000528','000666','000680','000821',
#        '000852','000923','000925','002008','002021','002031',
#        '600031','600055','600169','600262','600302','600343',
#        '600388','600499','600526','600582','600587','600761',
#        '600815','600843','600855','600860','600879','300056',
#        '002490','601106','002430','002435','002459','002526',
#        '300151','300156','601717','002278','002337','002353']

code = ['002430','002435','002459','002526',
        '300151','300156','601717','002278','002337','002353']
scode = '';
for str in code:
    scode = scode+str+'，'
    
#scode+='000158'



#scode = code[0]
for scode in code:
    tokent = 'c6194ecd76ae7733bb6fe1b5ac23c179'
    url = " http://webapi.cninfo.com.cn/api/stock/p_stock2303"  #apitest2.com需要根据具体访问域名修改
    #post_data="scode=%s&access_token=%s"%(scode,tokent)
    values = {"scode":scode,"access_token":tokent}
    post_data = urllib.parse.urlencode(values).encode(encoding='UTF8')
#    req = urllib.request.Request(url,post_data, headers=headers)
    req = urllib.request.urlopen(url, post_data)
#    req = urllib.request.urlopen(req)
    content = req.read()
    responsedict=json.loads(content)
    res = responsedict['records']
    with open(scode+'.json','w') as A_obj:
        json.dump(res,A_obj)
    df = pandas.read_json(scode+'.json', encoding = "utf-8")
    df.to_csv(scode+'.csv', encoding = "utf_8_sig")
    time.sleep(5)
#resultcode=responsedict["resultcode"]    
#print responsedict["resultmsg"],responsedict["resultcode"]
#if(responsedict["resultmsg"]=="success" and len(responsedict["records"])>=1):
#    print responsedict["records"]  #接收到的具体数据内容




# get

#url = "http://apitest2.com/api/stock/p_stock2100?scode=%s&access_token=%s" #apitest2.com需要根据具体访问域名修改
#conn = http.client.HTTPConnection("webapi.cninfo.com.cn")
#conn.request(method="GET",url=url%(scode,tokent))
#response = conn.getresponse()
#rescontent= response.read()
#responsedict=json.loads(rescontent)
#resultcode=responsedict["resultcode"]
#print responsedict["resultmsg"],responsedict["resultcode"]
#if(responsedict["resultmsg"]=="success" and len(responsedict["records"])>=1):
#    print responsedict["records"]  #接收到的具体数据内容
#else:
#    print 'no data'
#return resultcode


