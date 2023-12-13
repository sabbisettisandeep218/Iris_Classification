# -*- coding: utf-8 -*-
"""Iris Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mL9VkrGNw6nrezRl_U4hqBS67dtZrX30
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

from sklearn.datasets import load_iris
iris=load_iris()

iris.keys()

print(iris["DESCR"])

iris["target_names"]

iris["feature_names"]

type(iris["data"])

iris["data"].shape

iris["data"[:5]]

iris["target"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(iris["data"],iris["target"],random_state=0)

x_train.shape

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train,y_train)

import numpy as np
x_new=np.array([[5,2.9,1,0.2]])
x_new.shape

prediction=knn.predict(x_new)
prediction

iris["target_names"][prediction]

knn.score(x_test,y_test)