import numpy as np
import pandas as pd

exem1_data=pd.DataFrame({'x':[0,1,2,3,4],
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

new_user_input=float(input("enter value of x:"))
new_user_input+[[new_user_input]]
new_output=linear_regression.predict((new_user_input))[0]
print(f"when x ={new_user_input},y={new_output}")

sigma=1/(1+np.exp(-new_output[0]))
print(f"sigma value={sigma}")



