import numpy as np
from scipy.io import loadmat
from random import choice
from data_manager.plotter import data_plotter_1d, data_plotter_2d, data_plotter_3d, eeg_plot
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import RestrictType, labels, avg_slope, avg_value, extremes, restrict_frontal

from models.run_models import run_svm

def main():
    adhd, ctrl, testing = split_data(bucket_data('data_location.json'))
    
    # Formatting 3-D training data
    a1_3d = [                                                           \
        avg_slope(adhd, restrict=RestrictType.IVRS, norm=False),        \
        avg_value(adhd, restrict=RestrictType.NONE, norm=False),        \
        extremes(adhd, 250, restrict=RestrictType.IVRS, norm=False)     \
    ] 
    c1_d3 = [                                                           \
        avg_slope(ctrl, restrict=RestrictType.IVRS, norm=False),        \
        avg_value(ctrl, restrict=RestrictType.NONE, norm=False),        \
        extremes(ctrl, 250, restrict=RestrictType.IVRS, norm=False)     \
    ]
    adhd_train_set_3d = np.swapaxes(np.array(a1_3d), 0, 1).tolist()
    ctrl_train_set_3d = np.swapaxes(np.array(c1_d3), 0, 1).tolist()
    
    training_set_3d = np.array(adhd_train_set_3d + ctrl_train_set_3d)
    training_labels_3d = labels(adhd) + labels(ctrl)

    # Formatting 3-D testing data
    t_3d = [                                                            \
        avg_slope(testing, restrict=RestrictType.IVRS, norm=False),     \
        avg_value(testing, restrict=RestrictType.NONE, norm=False),     \
        extremes(testing, 250, restrict=RestrictType.IVRS, norm=False)  \
    ]
    testing_set_3d = np.swapaxes(np.array(t_3d), 0, 1)
    testing_labels_3d = labels(testing)

    run_svm(training_set_3d, training_labels_3d, testing_set_3d, testing_labels_3d)

    '''
    # Mess with this more, cannot find a good sperating pattern yet
    data_plotter_3d(
        avg_slope(adhd, restrict=RestrictType.IVRS, norm=False), avg_value(adhd, restrict=RestrictType.NONE, norm=False), extremes(adhd, 250, restrict=RestrictType.IVRS, norm=False),
        avg_slope(ctrl, restrict=RestrictType.IVRS, norm=False), avg_value(ctrl, restrict=RestrictType.NONE, norm=False), extremes(ctrl, 250, restrict=RestrictType.IVRS, norm=False),
        labels = ['AVG Slope', 'AVG Value', 'Extremes'], legend = ['ADHD', 'Control']
    )
    # Use this for the logistic regression, not an ideal data set tho
    #data_plotter_1d(extremes(adhd, 250, restrict=RestrictType.IVRS, norm=False)+extremes(ctrl, 250, restrict=RestrictType.IVRS, norm=False), adhd+ctrl, label='AVG Slope')
    '''

if __name__ == '__main__':
    main()
