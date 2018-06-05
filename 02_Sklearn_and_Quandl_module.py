#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : 02_Sklearn_and_Quandl_module.py
# @Time      : 2018/6/5 16:22
# @software  : PyCharm

import pandas as pd
import quandl, math

df = quandl.get('WIKI/GOOGL')
# df = quandl.get('WIKI/')

# df = df[['Adj. Open', 'Adj. Height', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
#
# df['HighLow Percent'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
# df['Percent Chang'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
# df = df['Adj. Close', 'HighLow Percent', 'Percent Chang', 'Adj. Volume']
# use a dataframe data stucture to hold features
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HighLow Percent'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close'] * 100.0
df['Percent Change'] = (df['Adj. Close'] - df['Adj. Open'])/ df['Adj. Open'] * 100.0
df['Percent College'] = (df['Adj. Low'] - df['Adj. Volume'])/ df['Adj. Volume'] * 100.0
df = df[['Adj. Close', 'HighLow Percent', 'Percent Change', 'Percent College', 'Adj. Volume']]


forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['Forecast'] = df[forecast_col].shift(-forecast_out)

print(df.head(5))
