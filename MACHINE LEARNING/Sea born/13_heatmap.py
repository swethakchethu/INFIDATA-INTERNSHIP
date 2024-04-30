#importing packages
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
df['species']=df['species'].map({'setosa':1,
                                 'versicolor':2,
                                 'virginica':3})
correlation=df.corr()
sns.heatmap(correlation,cbar=True,
            annot=True,linewidths=0.5,
            cmap='Blues')
plt.show()