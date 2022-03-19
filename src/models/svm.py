from sklearn import svm

def svm_model(adhd, ctrl, test):
    clf = svm.SVC(kernel='linear')
    clf.fit(adhd, ctrl)
