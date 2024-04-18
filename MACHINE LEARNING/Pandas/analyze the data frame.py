import pandas as pd
df=pd.read_csv("diabetes.csv")

#head
print("accessing from the dataset from first 10 row\n",df.head(10))
print("accessing from the dataset from first 5 row\n",df.head())

#tail
print("accessing from the dataset from last 5 row\n",df.tail())
print("accessing from the dataset from last 10 row\n",df.head(10))

print(df.shape) #rows and column values
print(df.columns[df.isna().any()])

#information data
print("basic info:\n",df.info)

#basic statastical information
print("statistical info:\n",df.describe())