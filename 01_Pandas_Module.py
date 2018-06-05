#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : 01_Pandas_Module.py
# @Time      : 2018/6/5 16:11
# @software  : PyCharm


import pandas as pd

data = {'col1': [1, 2], 'col2': [3, 4], 'col3': [4, 2]}

dataframe = pd.DataFrame(data=data)

print("DATAFRAME \n", dataframe)

print("\nOnly COLUMN1, 3 data\n", dataframe[['col1', 'col3']])

dataframe['col4'] = dataframe['col1'] * dataframe['col2']
print(dataframe
)