import pandas as pd
import pandas as ps

df=pd.read_csv('data.csv')
print('[info] data loaded successfully...')

print('[info] checking for nan values...')
print(df.columns[df.isna().any()])

print('[info] removing nan values...')
df=df.dropna()

print('[info] checking for nan values again...')
print(df.columns[df.isna().any()])