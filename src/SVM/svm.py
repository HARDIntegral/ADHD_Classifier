
from sklearn.metrics import classification_report
import numpy as np
import SVM.c_opt as co
from random import shuffle

class SVM():
    def __init__(self):
        pass

    def fit(self, training_set, rbf, C):
        shuffle(training_set)
        self.rbf = rbf
        (self.w, self.b) = co.opt(training_set, self.rbf, C)

    def test(self, testing_set):
        (self.pred, self.true) = co.test(testing_set, self.w, self.b)
        avg_value = np.average(np.array(self.pred))
        self.pred = [ i/avg_value for i in self.pred ]
        self.pred = [ 1 if i>1 else 0 for i in self.pred ]
        if self.rbf:
            print('USING RBF KERNEL')
        else:
            print('USING CUSTOM KERNEL') 
        print(classification_report(self.true, self.pred))