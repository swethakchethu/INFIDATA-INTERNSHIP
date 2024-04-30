#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df=sns.load_dataset("iris")
#creating a violan plot
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species',size='species')
plt.show()
