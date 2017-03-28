#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

# Import classifier SVC from sklearn.svm
from sklearn.svm import SVC
clf = SVC(C=10000., kernel="rbf")

# Use smaller training dataset
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100]  

# Train (fit) classifier with training data
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "seconds"

# Use trained classifier to predict labels on feature test set
t1 = time()
labels_pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "seconds"
print "prediction for element 10 is", labels_pred[10]
print "prediction for element 26 is", labels_pred[26]
print "prediction for element 50 is", labels_pred[50]

# Import and use accuracy_score to measure accuracy
from sklearn.metrics import accuracy_score
percent_accuracy = accuracy_score(labels_test, labels_pred)
print percent_accuracy
#########################################################


