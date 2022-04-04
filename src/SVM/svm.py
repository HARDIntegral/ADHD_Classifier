import numpy as np
import SVM.c_opt as co

class SVM():
    def __init__(self):
        pass

    def fit(self, training_set):
        dummy = co.opt(training_set, 0)
        print(dummy)

    def test(self, testing_set):
        pass