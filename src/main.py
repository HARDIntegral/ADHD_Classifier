from scipy.io import loadmat
from data_manager.plotter import plot
from data_manager.data_grabber import split_data, load_data

def main():
    training, testing = split_data(load_data('data_location.json'))
    plot(training[0].EEG_data)

if __name__ == '__main__':
    main()
