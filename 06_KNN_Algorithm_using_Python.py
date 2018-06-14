#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : 06_KNN_Algorithm_using_Python.py
# @Time      : 2018/6/14 16:57
# @software  : PyCharm

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from math import sqrt
import warnings
from collections import Counter
import pandas as pd
import random

dataset = {'A': [ [1,2],[2,3],[3,1] ], 'B': [ [6,5],[7,7],[8,6] ]}
new_features = [1, 7]
# style.use('fivethirtyeight')
# plot1 = [2, 4]
# plot2 = [2, 7]
# euclidean_distance = sqrt((plot1[0] - plot2[0])**2 + (plot1[1] - plot2[1])**2)
# print('Euclidean Distance:', euclidean_distance)
# [[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
#
# plt.scatter(new_features[0], new_features[1])
# plt.show()


def k_nearest_neighbors(data, predict, k=5):
    if len(data) >= k:
        warnings.warn('k is set to a value less than total voting group')
    distances = []

    for group in data:
        for features in data[group]:
            euclidean_distance = sqrt((features[0] - predict[0])**2 + (features[1] - predict[1])**2)
            print("Euclidean Distance from point {2} to point {1} in class {3} = {0:.2f}".format(euclidean_distance, features, predict,group))
            distances.append([euclidean_distance, group])
    votes = [i[1] for i in sorted(distances)[:k]]
    print('Shortest distance when k={1} are: {0}'.format(sorted(distances)[:k], k))
    vote_result = Counter(votes).most_common(0)[0][0]
    print('Majority class in votes: ', vote_result)
    return vote_result


result = k_nearest_neighbors(dataset, new_features, k=3)
print("Result: {0} falls in class \'{1}\'".format(new_features, result))