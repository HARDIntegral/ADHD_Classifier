import matplotlib.pyplot as plt
from numpy.linalg import norm
from data_manager.data_grabber import split_data, load_data

def plot(data):
    [plt.plot(i/norm(i)) for i in data]
    plt.show()