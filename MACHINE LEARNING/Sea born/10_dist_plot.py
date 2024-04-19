#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df=sns.load_dataset("iris")
#creating a violan plot
sns.displot(df['sepal_width'],color='b')
plt.show()