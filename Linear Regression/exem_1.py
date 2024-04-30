import numpy as np
import pandas as pd

exem1_data=pd.DataFram({'x':[0,1,2,3,4],
                        'y':[1,2,3,4,5]})
print(exem1_data)
x=exem1_data['x'].values.reshape(-1,1)
y=exem1_data['y'].values.reshape(-1,1)

from sklearn.linear_model import LinearRegression
linear_regression=LinearRegression()
linear_regression.fit(x,y)
print('[info] linear regression model training complete...')

m=linear_regression.coef_[0][0]
c=linear_regression.intercept_[0]

print(f"m value is:{m}")
print(f"c value is:{c}")
print(f"equation of line is:y={m}x+{c}")