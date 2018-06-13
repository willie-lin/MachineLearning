#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : BasicVisualize.py
# @Time      : 2018/6/6 10:37
# @software  : PyCharm

import numpy as np
import matplotlib.pyplot as plt

# plt.plot(x, y)
# plt.plot()

x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y)
plt.plot(x, y, 'o', color='red')
plt.show()