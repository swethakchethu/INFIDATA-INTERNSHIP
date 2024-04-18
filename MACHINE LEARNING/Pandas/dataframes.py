import pandas as  pd
#how to convert distionary to dataframe

data=pd.DataFrame({
    "name":["ali","khan","mahi","vinit"],
    "age":[20,25,30,25],
    "branch":["cse","me","ise","ece"],
    "place":["bnglr","tmk","delhi","mysore","pandi"]
})

print(data)
data.to_csv('id.csv',index=False)