
from sklearn.metrics import classification_report
import numpy as np
import SVM.c_opt as co
from random import shuffle

class SVM():
    def __init__(self):
        pass

    def fit(self, training_set, rbf, C):
        shuffle(training_set)
        (self.w, self.b) = co.opt(training_set, rbf, C)

    def test(self, testing_set):
        (self.pred, self.true) = co.test(testing_set, self.w, self.b)
        avg_value = np.average(np.array(self.pred))
        self.pred = [ i/avg_value for i in self.pred ]
        self.pred = [ 1 if i>1 else 0 for i in self.pred ]
        print(self.pred)
        print(classification_report(self.true, self.pred))