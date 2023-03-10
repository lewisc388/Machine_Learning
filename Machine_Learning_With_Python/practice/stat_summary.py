# stat_summary.py

from pandas import read_csv

url = 'https://goo.gl/bDdBiA'
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = read_csv(url, names= colnames)

print(f"First lines:\n{data.head()}\n")
print(f"Data Dimensions: {data.shape}\n")
print(f"Data Types:\n{data.dtypes}\n")
print(f"Description:\n{data.describe()}\n")
print(f"Pairwise Correlation:\n{data.corr()}\n")