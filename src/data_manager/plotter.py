import matplotlib.pyplot as plt
import numpy as np
from data_manager.data_manipulation import normalize, labels, data_avg, avg_slope, avg_value, extremes

CHANNEL_LABELS = ['Fp1', 'Fp2', 'F3 ', 'F4 ', 'F7 ', 'F8 ', 'Fz ']

# This plotter serves the purpose of determining which set of data is optimal 
#   for a logistic regression
def data_plotter_1d(data, elements, label='Class 1'):
    fig = plt.figure().add_subplot()
    try:
        x = [ data_avg(i) for i in data ]
    except TypeError:
        x = data
    y = labels(elements)
    fig.scatter(x, y)
    fig.set_xlabel(label)
    plt.show()

def data_plotter_2d(x1, y1, x2, y2, labels=['Class 1', 'Class 2'], legend=['Data 1', 'Data 2']):
    fig = plt.figure().add_subplot()
    fig.scatter(x1, y1, c='#ff0000')
    fig.scatter(x2, y2, c='#0000ff')
    fig.set_xlabel(labels[0])
    fig.set_ylabel(labels[1])
    plt.legend(legend, loc=4)
    plt.show()

def data_plotter_3d(x1, y1, z1, x2, y2, z2, labels=['Class 1', 'Class 2', 'Class 3'], legend=['Data 1', 'Data 2']):
    fig = plt.figure().add_subplot(projection='3d')
    fig.scatter(x1, y1, z1, c='#ff0000')
    fig.scatter(x2, y2, z2, c='#0000ff')
    fig.set_xlabel(labels[0])
    fig.set_ylabel(labels[1])
    fig.set_zlabel(labels[2])
    plt.legend(legend, loc=4)
    plt.show()

def eeg_plot(data):
    data = normalize(data)
    [ plt.plot(i, label=f"Plot: {label}") for label,i in enumerate(data) ]
    plt.legend(CHANNEL_LABELS, loc=4)
    plt.show()