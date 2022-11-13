# -*- coding: utf-8 -*-
"""
Created on Thu May 13 00:40:28 2021

@author: brian
"""

from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression


X, y, coef = make_regression(n_samples = 124,n_features = 10, n_informative = 8, 
                             random_state = 15094, coef=True)
X_train, y_train = X[:100,:], y[:100]
X_test, y_test = X[100:,:], y[100:]
reg = LinearRegression().fit(X_train, y_train)
reg.score(X,y)

