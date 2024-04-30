#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df=sns.load_dataset("iris")
#creating a violan plot
sns.lmplot(x='sepal_length',y='petal_width',data=df)
plt.show()