# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:16:56 2019

@author: Tsutomu
"""

#import json
import pandas


with open('number.json','w') as A_obj:
    json.dump(res,A_obj)
df = pandas.read_json('number'+'.json', encoding = "utf-8")
df.to_csv('number'+'.csv', encoding = "utf_8_sig")

#fr=open("number.json","r")  #打开json文件
#ls=json.load(fr)  #将json格式的字符串转换成python的数据类型，解码过程
#data=[ list(ls[0].keys()) ]  #获取列名,即key
#for item in ls:
#    data.append(list(item.values()))  #获取每一行的值value
#fr.close()  #关闭json文件
#
#fw=open("number.csv","w")  #打开csv为文件
#for line in data:
#    fw.write(",".join(line)+"\n")  #以逗号分隔一行的每个元素，最后换行
#fw.close()  #关闭csv文件

