import tushare as ts
import os


#filename = "C:/Users/Tsutomu/Desktop/财经分析/data/test.csv"
#for code in ['000875', '600848', '000981']:
#    df = ts.get_hist_data(code)
#    if os.path.exists(filename):
#        df.to_csv(filename, mode='a', header=None)
#    else:
#        df.to_csv(filename)
#code,代码
#name,名称
#arturnover,应收账款周转率(次)
#arturndays,应收账款周转天数(天)
#inventory_turnover,存货周转率(次)
#inventory_days,存货周转天数(天)
#currentasset_turnover,流动资产周转率(次)
#currentasset_days,流动资产周转天数(天)
yingyun = ts.get_operation_data(2014,3)
# 选中，代码，名称和流动资产周转率


#a1=data.copy()
#print a1[a1['y'].isin(['6','10'])]    #表显示满足条件：列y中的值包含'6','8'的所有行。
code = ['600605','002649']
cllect = yingyun[['code','name','currentasset_turnover']]

al = yingyun.copy()
a = al[al['code'].isin(code)]
b = a[['code','name','currentasset_turnover']]


