#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#violin plot
#loading dataset
df=sns.load_dataset("iris")
#creating a violan plot
sns.stripplot(x='species',y='sepal_width',color="blue",data=df)
plt.show()