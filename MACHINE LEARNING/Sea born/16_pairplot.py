#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df=sns.load_dataset("iris")

sns.pairplot(df,hue='species')
plt.show()