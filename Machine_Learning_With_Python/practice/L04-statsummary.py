# L04-statsummary.py

# --------[Lesson 4: Understand Data with Descriptive Statistics]--------
# Once you have loaded your data into Python you need to be able to understand it. The better
# you can understand your data, the better and more accurate the models that you can build.
# The first step to understanding your data is to use descriptive statistics. Today your lesson is to
# learn how to use descriptive statistics to understand your data. I recommend using the helper
# functions provided on the Pandas DataFrame.
# ✓ Understand your data using the head() function to look at the first few rows.
# ✓ Review the dimensions of your data with the shape property.
# ✓ Look at the data types for each attribute with the dtypes property.
# ✓ Review the distribution of your data with the describe() function.
# ✓ Calculate pairwise correlation between your variables using the corr() function.


from pandas import read_csv

url = 'https://goo.gl/bDdBiA'
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = read_csv(url, names= colnames)

print(f"First lines:\n{data.head()}\n")
print(f"Data Dimensions: {data.shape}\n")
print(f"Data Types:\n{data.dtypes}\n")
print(f"Description:\n{data.describe()}\n")
print(f"Pairwise Correlation:\n{data.corr()}\n")