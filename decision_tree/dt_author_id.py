#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("C:/Users/Bryan/Documents/machine-learning/ud120-projects/tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

# Import and train Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(min_samples_split = 40)
clf.fit(features_train, labels_train)

# Predict with trained DT Classifier
labels_pred = clf.predict(features_test)

# Measure accuracy of predictions relative to actual test labels
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_pred, labels_test)
print acc


#########################################################


