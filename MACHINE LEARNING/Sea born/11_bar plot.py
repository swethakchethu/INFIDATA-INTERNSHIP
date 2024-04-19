#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df=sns.load_dataset("iris")
#creating a violan plot
sns.barplot(x='species',y='sepal_width',color='purple',data=df)
plt.show()