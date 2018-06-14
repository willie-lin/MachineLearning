#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : 05_Classification_with_SKLEARN_K_Nearest_Neighbor_Algorithm.py
# @Time      : 2018/6/13 16:20
# @software  : PyCharm

import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

df = pd.read_csv('./SampleFiles/breast-cancer-wisconsin.txt')
df.replace('?', -9999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.20)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print('Accuracy:', accuracy)

exapple_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1],[4, 3, 1, 2, 1, 2, 1, 2, 4]])
exapple_measures = exapple_measures.reshape(len(exapple_measures), -1)

pridiction = clf.predict(exapple_measures)
print('Pridiction:', pridiction)