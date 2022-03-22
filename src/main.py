from scipy.io import loadmat
from random import choice
from data_manager.plotter import data_plotter_1d, data_plotter_2d, data_plotter_3d, eeg_plot
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import avg_slope, avg_value, extremes, restrict_frontal

def main():
    adhd, ctrl, testing = split_data(bucket_data('data_location.json'))

    data_plotter_2d(avg_value(adhd, restrict=False, norm=True), avg_slope(adhd, restrict=False, norm=True), avg_value(ctrl, restrict=False, norm=True), avg_slope(ctrl, restrict=False, norm=True), labels = ['AVG Value', 'Extremes'], legend = ['ADHD', 'Control'])
    '''
    data_plotter_3d(    \
        avg_value(adhd, restrict=True, norm=True), avg_slope(adhd, restrict=True, norm=True), extremes(adhd, 100, restrict=True, norm=True),    \
        avg_value(ctrl, restrict=True, norm=True), avg_slope(ctrl, restrict=True, norm=True), extremes(ctrl, 100, restrict=True, norm=True),    \
        labels = ['AVG Value', 'AVG Slope', 'Extremes'], legend = ['ADHD', 'Control']  \
    )

    patient = choice(testing)
    print(patient.is_ADHD)
    eeg_plot(restrict_frontal(patient.EEG_data))
    '''
    #data_plotter_1d(avg_value(adhd, restrict=True, norm=True)+avg_value(ctrl, restrict=True, norm=True), adhd+ctrl, label = 'AVG Value')

if __name__ == '__main__':
    main()
