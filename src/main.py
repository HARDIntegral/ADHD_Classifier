from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import avg_slope, avg_value
from SVM.svm import SVM
from sys import argv

def main():
    # load the data
    adhd, ctrl = bucket_data('data_location.json')

    # assign features to the data
    for e, d in zip(adhd, list(zip(avg_slope(adhd), avg_value(adhd)))):
        e.add_features(d[0] + d[1])
    for e, d in zip(ctrl, list(zip(avg_slope(ctrl), avg_value(ctrl)))):
        e.add_features(d[0] + d[1]) 

    # split data into training and testing sets
    training, testing = split_data(adhd, ctrl)
    model = SVM(training, testing)
    model.fit(int(argv[1]), 1)
    model.test()

if __name__ == '__main__':
    main()