from sklearn.svm import NuSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def run_svm(data, labels, tests, test_labels):
    clf = NuSVC(gamma="auto").fit(data, labels)
    y_pred = clf.predict(tests)

    print("\nSVM with RBF kernel\n")
    print(classification_report(test_labels, y_pred, target_names=['Control', 'ADHD']))

def run_knn(data, labels, tests, test_labels):
    clf = KNeighborsClassifier(n_neighbors=3).fit(data, labels)
    y_pred = clf.predict(tests)
    
    print("\nk-Nearest Neighbors\n")
    print(classification_report(test_labels, y_pred, target_names=['Control', 'ADHD']))

def run_logreg(data, labels, tests, test_labels):
    clf = LogisticRegression(random_state=0).fit(data, labels)
    y_pred = clf.predict(tests)

    print("\nLogistic Regression\n")
    print(classification_report(test_labels, y_pred, target_names=['Control', 'ADHD']))
