from scipy.io import loadmat
from random import choice
from data_manager.plotter import data_plotter, eeg_plot
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import avg_slope, avg_value, extremes, restrict_frontal

def main():
    adhd, ctrl, testing = split_data(bucket_data('data_location.json'))
    
    #data_plotter(avg_slope(adhd), avg_value(adhd), avg_slope(ctrl), avg_value(ctrl))
    #data_plotter(avg_slope(adhd), extremes(adhd, 100), avg_slope(ctrl), extremes(ctrl, 100))
    #data_plotter(avg_value(adhd), extremes(adhd, 100), avg_value(ctrl), extremes(ctrl, 100))

    '''
    patient = choice(testing)
    print(patient.is_ADHD)
    eeg_plot(restrict_frontal(patient.EEG_data))
    '''

if __name__ == '__main__':
    main()
