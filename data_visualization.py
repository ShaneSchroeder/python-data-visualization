import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import plotly.express as px

## Part 1 of Water Potability Analysis

data = pd.read_csv("water_potability.csv")
print(data.head())

data = data.dropna()
print(data.isnull().sum())

plt.figure(figsize=(15, 10))
sns.countplot(data.Potability)
plt.title("Distribution of Unsafe and Safe Water")
plt.show()


## Part 2 of Water Potability Analysis
data = data
figure = px.histogram(data, x = "ph",
                      color = "Potability",
                      title = "Factors Affecting Water Potability: pH")
figure.show()


### PROJECT 1 ###

# df = pd.read_csv('iris.data', header=None)
# df.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class']

# # group the data by class
# df_setosa = df[df['Class'] == 'Iris-setosa']
# df_versicolor = df[df['Class'] == 'Iris-versicolor']
# df_virginica = df[df['Class'] == 'Iris-virginica']

# # plot df_setosa with blue color and circle shape
# plt.scatter(df_setosa['Sepal Length'], df_setosa['Sepal Width'], color='blue', marker='o')

# #plot df_versicolor with green color and star shape
# plt.scatter(df_versicolor['Sepal Length'], df_versicolor['Sepal Width'], color='green', marker='*')

# #plot df_virginica with red color and square shape
# plt.scatter(df_virginica['Sepal Length'], df_virginica['Sepal Width'], color='red', marker='s')

# plt.show()