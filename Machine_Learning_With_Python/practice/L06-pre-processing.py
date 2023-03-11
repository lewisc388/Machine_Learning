# L06-pre-processing.py
#
# --------[Lesson 6: Prepare for Modeling by Pre-Processing Data]--------
# Your raw data may not be setup to be in the best shape for modeling. Sometimes you need to
# pre-process your data in order to best present the inherent structure of the problem in your
# data to the modeling algorithms. In today’s lesson, you will use the pre-processing capabilities
# provided by the scikit-learn.
# The scikit-learn library provides two standard idioms for transforming data. Each are useful
# in different circumstances: Fit and Multiple Transform and Combined Fit-And-Transform.
# There are many techniques that you can use to prepare your data for modeling, for example try
# out some of the following:
# ✓ Standardize numerical data (e.g. mean of 0 and standard deviation of 1) using the scale
#   and center options.
# ✓ Normalize numerical data (e.g. to a range of 0-1) using the range option.
# ✓ Explore more advanced feature engineering such as Binarizing.

from sklearn.preprocessing import StandardScaler, Normalizer, Binarizer
from pandas import read_csv
import numpy

url = 'https://goo.gl/bDdBiA'
colnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(url, names= colnames)
array = dataframe.values

X = array[:,0:8]
Y = array[:,8]
#print(f"X: {X}\n")

# Standardize
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

numpy.set_printoptions(precision= 3)
print(f"Standardized:\n{rescaledX[0:5,:]}\n")

# Normalize
X_normalized = Normalizer().fit(X)
normed_X = X_normalized.transform(X)

print(f"Normalized:\n{normed_X[0:5,:]}")

# Binarize
X_binarized = Binarizer(threshold=0.5).fit(X)
binary_X = X_binarized.transform(X)

print(f"Binarized:\n{binary_X[0:5,:]}")