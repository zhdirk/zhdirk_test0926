# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:44:05 2019

@author: zhdirk
"""
import pandas as pd
df = pd.read_csv('d:/data2.csv')

df.sort_values(['num',],ascending=0,inplace=True )
test1 = df.head(10)
df.sort_values(['sum',],ascending=0,inplace=True )
test2 = df.head(15)
test = pd.concat([test1,test2],ignore_index=True).drop_duplicates()
dict1 = pd.DataFrame({'label':[1 for i in range(30)]})
test_all = pd.concat([test,dict1],axis =1)