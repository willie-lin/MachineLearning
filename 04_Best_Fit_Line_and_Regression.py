#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : 04_Best_Fit_Line_and_Regression.py
# @Time      : 2018/6/13 11:04
# @software  : PyCharm

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


style.use('fivethirtyeight')


# prepare training data
x = np.array([1, 2, 3, 5, 7, 9], dtype=np.float64)
y = np.array([4, 5, 6, 7, 8, 10], dtype=np.float64)

# define a classifier/model = linear regression


def best_fit_slope_and_intercept(x, y):
    m = ((mean(x) * mean(y)) - (mean(x * y))) / (mean(x)**2 - mean(x**2))
    b = mean(y) - m*mean(x)
    return m, b


# 什么是平方误差？
# https    ://www.youtube.com/watch?v=6OvhLPS7rj4
# 为什么平方错误？
#     说你定义你的错误，
#     错误= PredictedValue - ActualValue。
# 
#     那么估计中的误差可以是两种，
# a        ）你低估了价值，在这种情况下你的错误将是负面的。
#         b）你高估的价值，在这种情况下，你的错误将是积极的。
# 
#     当你平均出来的时候，如果你低估了，你可能会得到一个非常低的错误
#     和平等高估，因为他们将互相取消。
# 
#     为了消除平均值的负值的影响，我们将它们平方。
# 
#     一个更好的问题是为什么不使用绝对差值而不是平方误差。
#     这没有确定的答案，因为它非常适用于特定的应用程序。
#     如果您想强调错误的传播，
#     基本上你想惩罚离平均值更远的错误（通常是机器学习中的0，统计中的用户参数）。在误差小于1的小尺度上，因为这些值本身很小，
#     只考虑绝对可能不会给算法提供最好的反馈机制。

def squared_error(y_original, y_line):
    return sum((y_line - y_original)**2)

# 什么是R平方或确定的Coeffcient？
#     R-squared是数据与拟合回归线有多接近的统计测量。
#     它也被称为决定系数
# 
#  R-squared =解释变异/总变异
# 
#  R平方是100之间总是0和％ -
#           0％表明该模型没有解释其平均值附近的响应数据的可变性。
#         100％表示该模型解释了其平均值附近响应数据的所有可变性。
# 
# 一般来说，R平方越高，模型越适合您的数据


def coefficient_of_determination(y_original, y_line):
    y_mean_line = [mean(y_original) for item in y_original]
    squared_error_regression = squared_error(y_original, y_line)
    squared_error_y_mean = squared_error(y_original, y_mean_line)

    return 1 - (squared_error_regression / squared_error_y_mean)


m,b = best_fit_slope_and_intercept(x, y)
regression_line = [(m*item)+b for item in x ]


predict_x = 12
predict_y = (m*predict_x)+b

r_squared = coefficient_of_determination(y, regression_line)
print('R-Squared', r_squared)


plt.scatter(x, y, c='red')
plt.scatter(predict_x, predict_y, c='green')
plt.plot(x, regression_line)
plt.show()