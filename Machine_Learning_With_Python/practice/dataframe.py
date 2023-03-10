# dataframe.py

import numpy
import pandas

myarray = numpy.array([['Apple','Orange','Banana'], ['Carrot','Lettuce','Broccoli']])
rowname = ['Fruits', 'Vegetables']
colname = ['one', 'two', 'three']

mydataframe = pandas.DataFrame(myarray, index= rowname, columns= colname)

print(mydataframe)