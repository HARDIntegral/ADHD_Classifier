from models.svm import SVM

def run_svm(data, labels, tests, test_labels):
    svm = SVM()
    svm.fit(data, labels)
    y_pred = svm.predict(tests)
    print(f'Accuracy is:{sum(test_labels==y_pred)/test_labels.shape[0]}')
