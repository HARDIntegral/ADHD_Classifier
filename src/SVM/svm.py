import numpy as np
import SVM.c_opt as co

class SVM():
    def __init__(self):
        pass

    def fit(self, training_set, rbf):
        (self.w, self.b) = co.opt(training_set, rbf)
        print(self.w, self.b)

    def test(self, testing_set):
        pass