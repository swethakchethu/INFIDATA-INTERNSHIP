#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#violin plot
#loading dataset
df=sns.load_dataset("iris")
#creating a violan plot
sns.violinplot(x='species',y='sepal_width',data=df)
plt.show()