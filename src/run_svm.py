import re
from sklearn.svm import NuSVC
from sklearn.metrics import classification_report
import numpy as np

def custom_kernel(Xi, Xj):
    print(Xi)
    return 1

def run_model(training, testing):
    # unpacking data
    training_features = [ i.features for i in training ]
    training_labels = [ i.is_ADHD for i in training ]
    testing_features = [ i.features for i in testing ]
    testing_labels = [ i.is_ADHD for i in testing ]

    # running the models
    for k in ['rbf', custom_kernel]:
        y_pred = NuSVC(gamma='scale', kernel=k).fit(training_features, training_labels).predict(testing_features)
        print(f'\nSVM with {k.upper()} kernel\n')
        print(classification_report(testing_labels, y_pred, target_names=['Control', 'ADHD']))