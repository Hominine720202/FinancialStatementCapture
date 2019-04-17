# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:25:25 2019

@author: Tsutomu
"""

import tushare as ts
import os
import pandas as pd


# 选中，代码，名称和流动资产周转率
res = pd.DataFrame()

code = ['000157','000425','000528','000666','000680','000821',
        '000852','000923','000925','002008','002021','002031',
        '600031','600055','600169','600262','600302','600343',
        '600388','600499','600526','600582','600587','600761',
        '600815','600843','600855','600860','600879','300056',
        '002490','601106','002430','002435','002459','002526',
        '300151','300156','601717','002278','002337','002353']
for year in range(2013,2019):
    for quarter in range(1,5):
        tmp = ts.get_operation_data(year,quarter)
        tmp2 = tmp[tmp['code'].isin(code)]
        tmp2 = tmp2[['code','name','currentasset_turnover']]
        tmp2['date']=str(year)+'/'+str(quarter)
        res=res.append(tmp2)
        
        
#quickratio,速动比率
res_qkrd = pd.DataFrame()

for year in range(2013,2019):
    for quarter in range(1,5):
        tmp = ts.get_debtpaying_data(year,quarter)
        tmp2 = tmp[tmp['code'].isin(code)]
        tmp2 = tmp2[['code','name','quickratio']]
        tmp2['date']=str(year)+'/'+str(quarter)
        res_qkrd=res_qkrd.append(tmp2)
        

# nav,净资产增长率
#targ,总资产增长率
#nprg,净利润增长率(%)
#ts.get_growth_data(2014,3)
res_jzj =  pd.DataFrame()   

for year in range(2013,2019):
    for quarter in range(1,5):
        tmp = ts.get_growth_data(year,quarter)
        tmp2 = tmp[tmp['code'].isin(code)]
        tmp2 = tmp2[['code','name','nav','targ','nprg']]
        tmp2['date']=str(year)+'/'+str(quarter)
        res_jzj=res_jzj.append(tmp2)
            



#esp,每股收益
#roe,净资产收益率(%)
#ts.get_report_data(2014,3)
res_roe  =  pd.DataFrame()  
 
for year in range(2013,2019):
    for quarter in range(1,5):
        tmp = ts.get_report_data(year,quarter)
        tmp2 = tmp[tmp['code'].isin(code)]
        tmp2 = tmp2[['code','name','roe','eps']]
        tmp2['date']=str(year)+'/'+str(quarter)
        res_roe=res_roe.append(tmp2) 