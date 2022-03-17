from scipy.io import loadmat
from random import choice
from data_manager.plotter import plot
from data_manager.data_grabber import split_data, bucket_data

def main():
    patient, testing = split_data(bucket_data('data_location.json'))

    patient = choice(patient)
    print(patient.is_ADHD)
    plot(patient.EEG_data[0:4] + patient.EEG_data[10:12] + patient.EEG_data[16:17])

if __name__ == '__main__':
    main()
