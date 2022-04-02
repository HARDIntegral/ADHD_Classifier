import numpy as np
from scipy.io import loadmat
from data_manager.plotter import data_plotter_1d, data_plotter_2d, data_plotter_3d, eeg_plot
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import RestrictType, labels, data_avg, avg_slope, avg_value, extremes, restrict_frontal

def main():
    adhd, ctrl, testing = split_data(bucket_data('data_location.json'))

if __name__ == '__main__':
    main()