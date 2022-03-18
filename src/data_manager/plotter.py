import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import normalize, avg_slope, avg_value, extremes

CHANNEL_LABELS = ['Fp1', 'Fp2', 'F3 ', 'F4 ', 'F7 ', 'F8 ', 'Fz ']

def plot(data):
    #data = normalize(data)
    [ plt.plot(np.gradient(np.gradient(i)), label=f"Plot: {label}") for label,i in enumerate(data) ]
    plt.legend(CHANNEL_LABELS, loc=4)

    print('\n AVG Slope')
    [ print(f"\tAVG {i[0]} : \t{i[1]}") for i in zip(CHANNEL_LABELS, avg_slope(data)) ]
    print('AVG Value')
    [ print(f"\tAVG {i[0]} : \t{i[1]}") for i in zip(CHANNEL_LABELS, avg_value(data)) ]

    plt.show()