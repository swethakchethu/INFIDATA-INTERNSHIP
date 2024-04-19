#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

#loading data set
df=sns.load_dataset("iris")
print(df)

sns.lineplot(x="sepal_length",y="sepal_width",data=df)
#setting the title using matplotlib
plt.title('title sing Matplotlib Function')
plt.show()