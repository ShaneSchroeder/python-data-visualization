import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris.data', header=None)
df.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class']

# group the data by class
df_setosa = df[df['Class'] == 'Iris-setosa']
df_versicolor = df[df['Class'] == 'Iris-versicolor']
df_virginica = df[df['Class'] == 'Iris-virginica']

# plot df_setosa with blue color and circle shape
plt.scatter(df_setosa['Sepal Length'], df_setosa['Sepal Width'], color='blue', marker='o')

#plot df_versicolor with green color and star shape
plt.scatter(df_versicolor['Sepal Length'], df_versicolor['Sepal Width'], color='green', marker='*')

#plot df_virginica with red color and square shape
plt.scatter(df_virginica['Sepal Length'], df_virginica['Sepal Width'], color='red', marker='s')

plt.show()