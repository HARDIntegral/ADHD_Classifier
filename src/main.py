from scipy.io import loadmat
from data_manager.plotter import plot
from data_manager.data_grabber import split_data, load_data

def main():
    training, testing = split_data(load_data('data_location.json'))
    print(training[3].is_ADHD)
    plot(training[3].EEG_data)

if __name__ == '__main__':
    main()
