# L05-datavisuals.py

# --------[Lesson 5: Understand Data with Visualization]--------
# Continuing on from yesterdays lesson, you must spend time to better understand your data. A
# second way to improve your understanding of your data is by using data visualization techniques
# (e.g. plotting). Today, your lesson is to learn how to use plotting in Python to understand
# attributes alone and their interactions. Again, I recommend using the helper functions provided
# on the Pandas DataFrame.
# ✓ Use the hist() function to create a histogram of each attribute.
# ✓ Use the plot(kind=’box’) function to create box and whisker plots of each attribute.
# ✓ Use the pandas.scatter matrix() function to create pairwise scatter plots of all at-
#   tributes.


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import read_csv
from pandas.plotting import scatter_matrix

url = 'https://goo.gl/bDdBiA'
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(url, names= colnames)

data.hist(column=colnames)

data.plot(kind='box')

scatter_matrix(data)

plt.show()