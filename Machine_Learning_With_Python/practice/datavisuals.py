# datavisuals.py

import matplotlib.pyplot as plt
from pandas import read_csv
from pandas.plotting import scatter_matrix

url = 'https://goo.gl/bDdBiA'
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = read_csv(url, names= colnames)

data.hist(column=colnames)

plt.plot(kind='box', data=data)

scatter_matrix(data)
plt.show()