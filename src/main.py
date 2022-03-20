from scipy.io import loadmat
from random import choice
from data_manager.plotter import data_plotter, eeg_plot
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import avg_slope, avg_value, extremes, restrict_frontal

def main():
    adhd, ctrl, testing = split_data(bucket_data('data_location.json'))
    
    data_plotter(avg_slope(adhd, restrict=True, norm=True), avg_value(adhd, restrict=True, norm=True), avg_slope(ctrl, restrict=True, norm=True), avg_value(ctrl, restrict=True, norm=True))
    #data_plotter(avg_slope(adhd, True), extremes(adhd, 100, True), avg_slope(ctrl, True), extremes(ctrl, 100, True))
    #data_plotter(avg_value(adhd, True), extremes(adhd, 100, True), avg_value(ctrl, True), extremes(ctrl, 100, True))

    '''
    patient = choice(testing)
    print(patient.is_ADHD)
    eeg_plot(restrict_frontal(patient.EEG_data))
    '''

if __name__ == '__main__':
    main()
