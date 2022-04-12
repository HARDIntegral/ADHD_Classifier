from data_manager.data_grabber import split_data
from SVM.svm import SVM

def run(adhd, ctrl):
    for i in range(0,1):
        #print(f'\nModel #{i+1}:\n')
        
        # split data into training and testing sets
        training, testing = split_data(adhd, ctrl)
        
        # models
        test_c = SVM(training, testing)
        test_c.fit(0, 0.1414)
        test_c.test()
        test_rbf = SVM(training, testing)
        test_rbf.fit(1, 0.1414)
        test_rbf.test()