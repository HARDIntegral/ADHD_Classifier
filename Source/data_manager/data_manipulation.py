
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
    slopes = [] 
    [ slopes.append(calculate_slopes(element)) for element in elements ]
    return slopes

def calculate_slopes(element):
    return [ calculate_slope(value) for value in element.EEG_data ]

def calculate_slope(data):
    return round((data[-1] - data[0])/len(data), 2) 


# Second Idea:
# Return the average value of the values of a channel over time
#   if that makes sense
def avg_value(elements):
    values = []
    [ values.append(calculate_avg_values(element)) for element in elements ]
    return values

def calculate_avg_values(element):
    return [ calculate_avg_value for value in element.EEG_data ]

def calculate_avg_value(data):
    return round(sum(data)/len(data), 2)