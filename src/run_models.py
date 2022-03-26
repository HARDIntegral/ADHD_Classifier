from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

def run_svm(data, labels, tests, test_labels):
    clf = svm.NuSVC(gamma="auto")
    clf.fit(data, labels)
    y_pred = clf.predict(tests)
    print(f'Accuracy is:{sum(test_labels==y_pred)/test_labels.shape[0]}')

def run_knn(data, labels, tests, test_labels):
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(data, labels)
    y_pred = clf.predict(tests)
    print(f'Accuracy is:{sum(test_labels==y_pred)/test_labels.shape[0]}')