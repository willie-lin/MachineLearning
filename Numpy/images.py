#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : images.py
# @Time      : 2018/6/6 10:50
# @software  : PyCharm

import numpy as np
import matplotlib.pyplot as plt

image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
# plt.show()