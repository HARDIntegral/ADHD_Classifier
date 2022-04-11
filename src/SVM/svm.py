
from sklearn.metrics import classification_report
import numpy as np
import SVM.c_opt as co

class SVM():
    def __init__(self):
        pass

    def fit(self, training_set, rbf, C):
        (self.w, self.b) = co.opt(training_set, rbf, C)

    def test(self, testing_set):
        (self.pred, self.true) = co.test(testing_set, self.w, self.b)
        print(classification_report(self.true, self.pred))