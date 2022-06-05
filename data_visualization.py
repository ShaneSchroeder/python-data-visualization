import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris.data', header=None)
df.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class']

groupedByClass = df.groupby(df.Class)

setosa = groupedByClass.get_group("Iris-setosa")
versicolor = groupedByClass.get_group("Iris-versicolor")
virginica = groupedByClass.get_group("Iris-virginica")

plt.scatter(setosa["Sepal Length"], setosa["Sepal Width"], color='b', marker='o')
plt.scatter(versicolor["Sepal Length"], versicolor["Sepal Width"], color='g', marker='*')
plt.scatter(virginica["Sepal Length"], virginica["Sepal Width"], color='r', marker='p')

plt.show()