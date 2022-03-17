import matplotlib.pyplot as plt
from numpy.linalg import norm
from data_manager.data_grabber import split_data, bucket_data

def plot(data):
    [plt.plot(i, label=f"Plot: {label}") for label,i in enumerate(data)]
    plt.legend(['Fp1', 'Fp2', 'F3', 'F4', 'F7', 'F8', 'Fz'], loc=4)
    plt.show()