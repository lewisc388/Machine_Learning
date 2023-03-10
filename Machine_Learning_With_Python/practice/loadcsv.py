# loadcsv.py

from pandas import read_csv
import numpy

url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas', 'pres', 'skin', 'mass', 'pedi', 'age', 'class']
data = read_csv(url, names= names)

print(data)

