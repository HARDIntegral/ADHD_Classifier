import numpy as np

def moving_average(data, avg_period):
    weights = np.ones(avg_period) / avg_period
    return np.convolve(data, weights, mode='valid')

# Returns only the channels that read from the frontal lobe
def restrict_frontal(data):
    return data[0:4]+data[10:12]+data[16:17]

def normalize(data):
    return data/np.linalg.norm(data)

#####################################################################
# These are ideas as to what I can do to feed data into the models

# First Idea:
# Return the average slopes of the channels over time
def avg_slope(elements, restrict=False):
    slopes = [] 
    for element in elements:
        slopes += [ (i[-1] - i[0])/len(i) for i in element.EEG_data ]
    return slopes

# Second Idea:
# Return the average value of the values of a channel over time
#   if that makes sense
def avg_value(elements, restrict=False):
    values = []
    for element in elements:
        values += [ sum(i)/len(i) for i in element.EEG_data ]
    return values

# Third Idea:
# Return the number of peaks and troughs from each channel over a
#   period of time
def second_gradient(list):
    return np.gradient(np.gradient(list))

def extremes(elements, sensitivity, restrict=False):
    extremes = []
    for element in elements:
        curve_extremes = []
        data = element.EEG_data
        upper_max = max([ max(second_gradient(i)) for i in data ])
        lower_min = min([ min(second_gradient(i)) for i in data ])
        extr_sensitivity = (upper_max + lower_min)/(2*sensitivity)

        for i in data:
            num_extremes = 0
            for j in second_gradient(i):
                if abs(j)<extr_sensitivity:
                    num_extremes +=1
            curve_extremes.append(num_extremes)
        extremes += curve_extremes
    return extremes