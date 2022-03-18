import matplotlib.pyplot as plt
import numpy as np
from data_manager.data_manipulation import normalize, avg_slope, avg_value, extremes

CHANNEL_LABELS = ['Fp1', 'Fp2', 'F3 ', 'F4 ', 'F7 ', 'F8 ', 'Fz ']

def plot(data):
    data = normalize(data)
    [ plt.plot(i, label=f"Plot: {label}") for label,i in enumerate(data) ]
    plt.legend(CHANNEL_LABELS, loc=4)

    print('\nAVG Slope')
    [ print(f"\tAVG {i[0]} : \t{i[1]}") for i in zip(CHANNEL_LABELS, avg_slope(data)) ]
    print('AVG Value')
    [ print(f"\tAVG {i[0]} : \t{i[1]}") for i in zip(CHANNEL_LABELS, avg_value(data)) ]
    print('Total Extreme Region Area')
    [ print(f"\t{i[0]}\t: \t{i[1]}") for i in zip(CHANNEL_LABELS, extremes(data, 100)) ]

    plt.show()