# L02-dataframe.py

# --------[Lesson 2: Get Around In Python, NumPy, Matplotlib and Pandas]--------
# You need to be able to read and write basic Python scripts. As a developer you can pick-up new
# programming languages pretty quickly. Python is case sensitive, uses hash (#) for comments
# and uses white space to indicate code blocks (white space matters). Todays task is to practice
# the basic syntax of the Python programming language and important SciPy data structures in
# the Python interactive environment.
# 1. Practice assignment, working with lists and flow control in Python.
# 2. Practice working with NumPy arrays.
# 3. Practice creating simple plots in Matplotlib.
# 4. Practice working with Pandas Series and DataFrame.

import numpy
import pandas

myarray = numpy.array([['Apple','Orange','Banana'], ['Carrot','Lettuce','Broccoli']])
rowname = ['Fruits', 'Vegetables']
colname = ['one', 'two', 'three']

mydataframe = pandas.DataFrame(myarray, index= rowname, columns= colname)

print(mydataframe)