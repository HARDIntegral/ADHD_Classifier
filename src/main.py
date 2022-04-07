import numpy as np
from scipy.io import loadmat
from random import choice
from data_manager.plotter import data_plotter_1d, data_plotter_2d, data_plotter_3d, eeg_plot
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import RestrictType, labels, data_avg, avg_slope, avg_value, extremes, restrict_frontal

from run_models import run_svm, run_knn, run_logreg

def main():
    adhd, ctrl, testing = split_data(bucket_data('data_location.json'))


    training_labels = labels(adhd) + labels(ctrl)
    testing_labels = np.array(labels(testing))

    # Formatting 2-D training data
    a_2d = [                                                            \
        avg_slope(adhd, restrict=RestrictType.IVRS, norm=False),        \
        avg_value(adhd, restrict=RestrictType.NONE, norm=False),        \
        extremes(adhd, 250, restrict=RestrictType.IVRS, norm=False)     \
    ] 
    c_d2 = [                                                            \
        avg_slope(ctrl, restrict=RestrictType.IVRS, norm=False),        \
        avg_value(ctrl, restrict=RestrictType.NONE, norm=False),        \
        extremes(ctrl, 250, restrict=RestrictType.IVRS, norm=False)     \
    ]
    adhd_train_set_2d = np.swapaxes(np.array(a_2d), 0, 1).tolist()
    ctrl_train_set_2d = np.swapaxes(np.array(c_d2), 0, 1).tolist()
    
    training_set_2d = np.array([                                        \
        [data_avg(i[0])*data_avg(i[1]), data_avg(i[2])]                 \
        for i in (adhd_train_set_2d + ctrl_train_set_2d                 \
    )])

    # Formatting 3-D testing data
    t_2d = [                                                            \
        avg_slope(testing, restrict=RestrictType.IVRS, norm=False),     \
        avg_value(testing, restrict=RestrictType.NONE, norm=False),     \
        extremes(testing, 250, restrict=RestrictType.IVRS, norm=False)  \
    ]
    testing_set_2d = np.array([                                         \
        [data_avg(i[0])*data_avg(i[1]), data_avg(i[2])]                 \
        for i in np.swapaxes(np.array(t_2d), 0, 1).tolist()             \
    ])

    # Formating 1-D data
    a_1d = extremes(adhd, 250, restrict=RestrictType.IVRS, norm=False)
    c_1d = extremes(ctrl, 250, restrict=RestrictType.IVRS, norm=False)
    training_set_1d = np.array(a_1d+c_1d)
    testing_set_1d = np.array(extremes(testing, 250, restrict=RestrictType.IVRS, norm=False))

    # Running tests
    run_svm(training_set_2d, training_labels, testing_set_2d, testing_labels)
    run_knn(training_set_2d, training_labels, testing_set_2d, testing_labels)
    run_logreg(training_set_1d, training_labels, testing_set_1d, testing_labels)


if __name__ == '__main__':
    main()