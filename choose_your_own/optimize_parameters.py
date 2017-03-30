from __future__ import print_function

from prep_terrain_data import makeTerrainData
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

print(__doc__)

# Make training and testing data
features_train, labels_train, features_test, labels_test = makeTerrainData()

# Set the parameters by cross-validation
tuned_parameters = {'n_estimators': [1, 10, 50, 100], 'max_depth': [1, 10, 50, 100],
                     'min_samples_split': [2, 10, 50, 100], 'min_samples_leaf': [1, 10, 50, 100],
						'max_features': [1, 2]}

scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(RandomForestClassifier(), tuned_parameters, cv=5,
                       scoring='%s_macro' % score)
    clf.fit(features_train, labels_train)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = labels_test, clf.predict(features_test)
print(classification_report(y_true, y_pred))
print()