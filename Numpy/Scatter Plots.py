#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : Scatter Plots.py
# @Time      : 2018/6/6 11:12
# @software  : PyCharm

# import numpy as np
# import matplotlib.pyplot as plt
#
# n = 1024
# X = np.random.normal(0, 1, n)
# Y = np.random.normal(0, 1, n)
# # T = np.arctan2(X, Y)
# # plt.axes([0.025, 0.025, 0.095, 0.095])
# plt.scatter(Y, X, s=75, alpha=.5)
# # plt.xlim(-1.5, 1.5), plt.xticks([])
# # plt.ylim(-1.5, 1.5), plt.yticks([])

import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())
plt.ylim(-1.5, 1.5)
plt.yticks(())

plt.show()