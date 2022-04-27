
from sklearn.metrics import classification_report
from SVM.c_opt import opt , test
from random import shuffle
from numpy import average , array
from enum import Enum

class Kernels(Enum):
    RBF                 = 0
    M_RBF               = 1
    M_POLY              = 2
    M_RBF_POLY          = 3

class SVM():
    
    def __init__(self,training_set,testing_set):
        self.training_set = training_set
        self.testing_set = testing_set


    def fit(self,kernel,C=1):
        
        shuffle(self.training_set)
        
        self.kernel = kernel
        
        ( self.alphas , self.b ) = opt(self.training_set,self.kernel,C)


    def test(self):
        
        ( self.pred , self.true ) = test(self.training_set,self.testing_set,self.alphas,self.b,self.kernel)
        
        avg_value = average(array(self.pred))
        
        self.pred = [ i / avg_value for i in self.pred ]
        self.pred = [ 1 if i > 1 else 0 for i in self.pred ]
        

        match (self.kernel):
            case 0:
                print('USING RBF KERNEL')
            case 1:
                print('USING MASKED RBF KERNEL')
            case 2: 
                print('USING POLYNOMIAL KERNEL')
            case 3:
                print('USING RBF POLYNOMIAL HYBRID KERNEL')
            case _:
                pass
            
        print(classification_report(self.true,self.pred))