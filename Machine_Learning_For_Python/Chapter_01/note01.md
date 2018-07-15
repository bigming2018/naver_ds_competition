# 머신러닝을 위한 Pyyhon

===========================================

## Intro

- 이 강좌에서 배우는 것 : 파이썬, 데이터 전처리, 머신러닝

- sklearn

```
>>> from sklearn import linear_model
>>> reg = linear_model.LinearRegression()
>>> reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
>>> reg.coef_
array([0.5, 0.5)]
```