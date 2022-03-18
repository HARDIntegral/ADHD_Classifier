from scipy.io import loadmat
from random import choice
from data_manager.plotter import plot
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import restrict_frontal

def main():
    training, testing = split_data(bucket_data('data_location.json'))

    patient = choice(training)
    print(patient.is_ADHD)
    plot(restrict_frontal(patient.EEG_data))

if __name__ == '__main__':
    main()
