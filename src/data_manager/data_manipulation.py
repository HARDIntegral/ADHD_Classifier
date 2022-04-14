from enum import Enum
import numpy as np

###################################################################################################
# These are helper functions

def moving_average(data, avg_period):
    weights = np.ones(avg_period) / avg_period
    return np.convolve(data, weights, mode='valid')

def data_avg(data):
    return sum(data)/len(data)

###################################################################################################
# These are ideas as to what I can do to feed data into the models

# First Idea:
# Return the average slopes of the channels over time
def avg_slope(elements):
    slopes = [] 
    for element in elements:
        slopes.append([ round((i[-1] - i[0])/len(i), 2) for i in element.EEG_data ])
    return slopes

# Second Idea:
# Return the average value of the values of a channel over time
#   if that makes sense
def avg_value(elements):
    values = []
    for element in elements:
        values.append([ round(sum(i)/len(i), 2) for i in element.EEG_data ])
    return values