
from sklearn.metrics import classification_report
from SVM.c_opt import opt , test
from random import shuffle
from numpy import average , array

class SVM():
    
    def __init__(self,training_set,testing_set):
        self.training_set = training_set
        self.testing_set = testing_set


    def fit(self,rbf,C):
        
        shuffle(self.training_set)
        
        self.rbf = rbf
        
        ( self.alphas , self.b ) = opt(self.training_set,self.rbf,C)


    def test(self):
        
        ( self.pred , self.true ) = test(self.training_set,self.testing_set,self.alphas,self.b,self.rbf)
        
        avg_value = average(array(self.pred))
        
        self.pred = [ i / avg_value for i in self.pred ]
        self.pred = [ 1 if i > 1 else 0 for i in self.pred ]

        if self.rbf:
            print('USING RBF KERNEL')
        else:
            print('USING CUSTOM KERNEL')
            
        print(classification_report(self.true, self.pred))
