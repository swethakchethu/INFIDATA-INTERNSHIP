import pandas as pd
data=pd.DataFrame({
    "calories":[420,399,288],
    "duration":[10,20,30]
})
print("first coloum of data is:\n",data['calories'])
print("first coloum of data is:\n",data.calories)

