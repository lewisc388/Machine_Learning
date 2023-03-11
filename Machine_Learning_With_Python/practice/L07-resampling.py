# L07-resampling.py

# --------[Lesson 7: Algorithm Evaluation With Resampling Methods]--------
# The dataset used to train a machine learning algorithm is called a training dataset. The dataset
# used to train an algorithm cannot be used to give you reliable estimates of the accuracy of the
# model on new data. This is a big problem because the whole idea of creating the model is to
# make predictions on new data. You can use statistical methods called resampling methods to
# split your training dataset into subsets, some are used to train the model and others are held
# back and used to estimate the accuracy of the model on unseen data.
# Your goal with todays lesson is to practice using the different resampling methods available
# in scikit-learn, for example:
# • Split a dataset into training and test sets.
# • Estimate the accuracy of an algorithm using k-fold cross-validation.
# • Estimate the accuracy of an algorithm using leave one out cross-validation.