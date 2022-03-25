from scipy.io import loadmat
from random import choice
from data_manager.plotter import data_plotter_1d, data_plotter_2d, data_plotter_3d, eeg_plot
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import RestrictType, avg_slope, avg_value, extremes, restrict_frontal

def main():
    adhd, ctrl, testing = split_data(bucket_data('data_location.json'))

    data_plotter_2d(extremes(adhd, 250, restrict=RestrictType.IVRS, norm=False), extremes(adhd, 25, restrict=RestrictType.NORM, norm=False), extremes(ctrl, 250, restrict=RestrictType.IVRS, norm=False), extremes(ctrl, 25, restrict=RestrictType.NORM, norm=False), labels = ['AVG Slope IVRS', 'AVG Slope NORM'], legend = ['ADHD', 'Control'])
    '''
    # Mess with this more, cannot find a good sperating pattern yet
    data_plotter_3d(
        avg_slope(adhd, restrict=RestrictType.IVRS, norm=False), avg_value(adhd, restrict=RestrictType.NONE, norm=False), extremes(adhd, 250, restrict=RestrictType.IVRS, norm=False),
        avg_slope(ctrl, restrict=RestrictType.IVRS, norm=False), avg_value(ctrl, restrict=RestrictType.NONE, norm=False), extremes(ctrl, 250, restrict=RestrictType.IVRS, norm=False),
        labels = ['AVG Slope', 'AVG Value', 'Extremes'], legend = ['ADHD', 'Control']
    )
    # Use this for the logistic regression, not an ideal data set tho
    data_plotter_1d(extremes(adhd, 250, restrict=RestrictType.IVRS, norm=False)+extremes(ctrl, 250, restrict=RestrictType.IVRS, norm=False), adhd+ctrl, label='AVG Slope')
    '''

if __name__ == '__main__':
    main()
