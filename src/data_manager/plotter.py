import matplotlib.pyplot as plt
from data_manager.data_grabber import split_data, load_data

def plot(data):
    [plt.plot(i) for i in data.tolist()]
    plt.show()