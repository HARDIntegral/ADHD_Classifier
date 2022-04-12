from data_manager.data_grabber import split_data
from SVM.svm import SVM

def run(adhd, ctrl):
    for i in range(0,25):
        print(f'\nModel #{i+1}:\n')
        
        # split data into training and testing sets
        training, testing = split_data(adhd, ctrl)
        
        # models
        test_rbf = SVM()
        test_rbf.fit(training, 1, 1.414)
        test_rbf.test(testing)
        test_c = SVM()
        test_c.fit(training, 0, 1.414)
        test_c.test(testing)