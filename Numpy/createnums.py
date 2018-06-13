#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : createnums.py
# @Time      : 2018/6/6 10:21
# @software  : PyCharm


import numpy as np


a = np.arange(10)

print(a)
b = np.arange(1, 9, 2)
print(b)
print('************************************')
c = np.linspace(0, 1, 6)
print(c)
d = np.linspace(0, 1, 5, endpoint=False)
print(d)

e = np.ones((3, 3))
print(e)

f = np.zeros((2, 2))
print(f)

g = np.eye(3)
print(g)

h = np.diag(np.array([1, 2, 3, 4]))
print(h)
m = np.random.rand(4)
n = np.random.randn(4)
print(m)

print(n)