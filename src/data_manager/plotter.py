import matplotlib.pyplot as plt
import numpy as np
from data_manager.data_manipulation import normalize, avg_slope, avg_value, extremes

CHANNEL_LABELS = ['Fp1', 'Fp2', 'F3 ', 'F4 ', 'F7 ', 'F8 ', 'Fz ']

def data_plotter_2d(x1, y1, x2, y2, labels=['Class 1', 'Class 2'], Legends=['Data 1', 'Data 2']):
    fig = plt.figure().add_subplot()
    fig.scatter(x1, y1, c='#ff0000')
    fig.scatter(x2, y2, c='#0000ff')
    fig.set_xlabel(labels[0])
    fig.set_ylabel(labels[1])
    plt.legend(Legends, loc=4)
    plt.show()

def data_plotter_3d(x1, y1, z1, x2, y2, z2, labels=['Class 1', 'Class 2', 'Class 3'], Legends=['Data 1', 'Data 2']):
    fig = plt.figure().add_subplot(projection='3d')
    fig.scatter(x1, y1, z1, c='#ff0000')
    fig.scatter(x2, y2, z2, c='#0000ff')
    fig.set_xlabel(labels[0])
    fig.set_ylabel(labels[1])
    fig.set_zlabel(labels[2])
    plt.legend(Legends, loc=4)
    plt.show()

def eeg_plot(data):
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