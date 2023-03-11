# L03-loadcsv.py

# --------[Lesson 3: Load Data From CSV]--------
# Machine learning algorithms need data. You can load your own data from CSV files but when
# you are getting started with machine learning in Python you should practice on standard
# machine learning datasets. Your task for todays lesson are to get comfortable loading data into
# Python and to find and load standard machine learning datasets. There are many excellent
# standard machine learning datasets in CSV format that you can download and practice with on
# the UCI machine learning repository.
# • Practice loading CSV files into Python using the CSV.reader() function in the standard
#   library.
# • Practice loading CSV files using NumPy and the numpy.loadtxt() function.
# ✓ Practice loading CSV files using Pandas and the pandas.read csv() function.


from pandas import read_csv
import numpy

url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas', 'pres', 'skin', 'mass', 'pedi', 'age', 'class']
data = read_csv(url, names= names)

print(data)

