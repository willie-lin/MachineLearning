#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : numpys.py
# @Time      : 2018/6/6 10:09
# @software  : PyCharm


import numpy as np

a = np.array([0, 1, 2, 3])

print(a.ndim)
print(a.shape)
print(len(a))
print('----------------------------------------')

b = np.array([
    [0, 1, 2 ],
    [3, 4, 5 ]]
)
print(b.ndim)
print(b.shape)
print(len(b))
print('****************************************')

c = np.array([[[1], [2]], [[3], [4]]])
print(c.ndim)
print(c.shape)
print('****************************************')