
from sklearn.metrics import classification_report
import numpy as np
import SVM.c_opt as co
from random import shuffle

class SVM():
    def __init__(self, training_set, testing_set):
        self.training_set = training_set
        self.testing_set = testing_set

    def fit(self, rbf, C):
        shuffle(self.training_set)
        self.rbf = rbf
        (self.alphas, self.b) = co.opt(self.training_set, self.rbf, C)
        print(self.alphas, self.b)

    def test(self):
        (self.pred, self.true) = co.test(self.training_set, self.testing_set, self.alphas, self.b, self.rbf)
        print(self.pred, self.true)
        avg_value = np.average(np.array(self.pred))
        self.pred = [ i/avg_value for i in self.pred ]
        self.pred = [ 1 if i>1 else 0 for i in self.pred ]

        if self.rbf:
            print('USING RBF KERNEL')
        else:
            print('USING CUSTOM KERNEL') 
        print(classification_report(self.true, self.pred))