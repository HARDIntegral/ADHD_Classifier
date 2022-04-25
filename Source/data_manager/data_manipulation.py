from enum import Enum
from numpy import ones , convolve


###################################################################################################
# These are helper functions

def moving_average(data,avg_period):
    
    weights = ones(avg_period) / avg_period
    
    return convolve(data,weights,mode = 'valid')

def data_avg(data):
    return sum(data) / len(data)


###################################################################################################
# These are ideas as to what I can do to feed data into the models

# First Idea:
# Return the average slopes of the channels over time
def avg_slope(elements):
    return flatten([ calcSlope(element) for element in elements ])
    
def calcSlopes(element):
    return [ calcSlope for value in element.EEG_data ]

def calcSlope(value):
    return round((value[-1] - value[0]) / len(value),2)

    


# Second Idea:
# Return the average value of the values of a channel over time
#   if that makes sense
def avg_value(elements):
    return flatten([ calcValues for element in elements ])
    
def calcValues(element):
    return [ calcValue(value) for value in element.EEG_data ]
    
def calcValue(value):
    return round(sum(value) / len(value),2)
    
    
    
def flatten(list):
    return [ item for sublist in list for item in sublist ]