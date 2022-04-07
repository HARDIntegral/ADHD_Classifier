from sklearn.svm import NuSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def run_svm(data, labels, tests, test_labels):
    print('Support Vector Machines:')
    for k in ['rbf', 'poly', 'sigmoid']:
        y_pred = NuSVC(gamma='scale', kernel=k).fit(data, labels).predict(tests)
        print(f'\nSVM with {k.upper()} kernel\n')
        print(classification_report(test_labels, y_pred, target_names=['Control', 'ADHD']))

def run_knn(data, labels, tests, test_labels):
    print('Nearest Neighbors:')
    for k in range(3,8):
        clf = KNeighborsClassifier(n_neighbors=k).fit(data, labels)
        y_pred = clf.predict(tests)
        print(f'\nk-Nearest Neighbors with {k} Voters\n')
        print(classification_report(test_labels, y_pred, target_names=['Control', 'ADHD']))

def run_logreg(data, labels, tests, test_labels):
    clf = LogisticRegression(random_state=0).fit(data, labels)
    y_pred = clf.predict(tests)

    print("\nLogistic Regression\n")
    print(classification_report(test_labels, y_pred, target_names=['Control', 'ADHD']))
