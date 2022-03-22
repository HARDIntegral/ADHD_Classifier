from scipy.io import loadmat
from random import choice
from data_manager.plotter import data_plotter_1d, data_plotter_2d, data_plotter_3d, eeg_plot
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import RestrictType, avg_slope, avg_value, extremes, restrict_frontal

def main():
    adhd, ctrl, testing = split_data(bucket_data('data_location.json'))
    data_plotter_2d(avg_value(adhd, restrict=RestrictType.IVRS, norm=True), extremes(adhd, 100, restrict=RestrictType.IVRS, norm=True), avg_value(ctrl, restrict=RestrictType.NORM, norm=True), extremes(ctrl, 100, restrict=RestrictType.NORM, norm=True), labels = ['AVG Value', 'Extremes'], legend = ['ADHD', 'Control'])
    
if __name__ == '__main__':
    main()
