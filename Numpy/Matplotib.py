#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Matplotib.py
# @Time      : 2018/6/6 10:59
# @software  : PyCharm

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)

plt.show()
