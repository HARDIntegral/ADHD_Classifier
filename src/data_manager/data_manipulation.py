from enum import Enum
import numpy as np

class RestrictType(Enum):
    NONE = 0
    NORM = 1
    IVRS = 2

#####################################################################
# These are helper functions

def moving_average(data, avg_period):
    weights = np.ones(avg_period) / avg_period
    return np.convolve(data, weights, mode='valid')

# Returns only the channels that read from the frontal lobe
def restrict_frontal(data, restrict=RestrictType.NORM):
    if restrict == RestrictType.NORM:
        x = data[0:4].tolist()
        y = data[10:12].tolist()
        z = data[16:17].tolist()
    elif restrict == RestrictType.IVRS:
        x = data[4:10].tolist()
        y = data[12:16].tolist()
        z = data[17:-1].tolist()
    else:
        return data
    return x+y+z

def normalize(data):
    return data/np.linalg.norm(data)

def labels(elements):
    return [ 1 if i.is_ADHD else 0 for i in elements]

def data_avg(data):
    return sum(data)/len(data)

#####################################################################
# These are ideas as to what I can do to feed data into the models

# First Idea:
# Return the average slopes of the channels over time
def avg_slope(elements, restrict=RestrictType.NONE, norm=False):
    slopes = [] 
    for element in elements:
        slopes.insert(len(slopes), [                                                                                    \
            (restrict_frontal(i, restrict)[-1] - restrict_frontal(i, restrict)[0])/len(restrict_frontal(i, restrict))   \
            for i in (normalize(element.EEG_data) if norm else element.EEG_data)                                        \
        ])
    return slopes

# Second Idea:
# Return the average value of the values of a channel over time
#   if that makes sense
def avg_value(elements, restrict=RestrictType.NONE, norm=False):
    values = []
    for element in elements:
        values.insert(len(values), [                                                                                    \
            sum(restrict_frontal(i, restrict))/len(restrict_frontal(i, restrict))                                       \
            for i in (normalize(element.EEG_data) if norm else element.EEG_data)                                        \
        ])
    return values

# Third Idea:
# Return the number of peaks and troughs from each channel over a
#   period of time
def second_gradient(list):
    return np.gradient(np.gradient(list))

def extremes(elements, sensitivity, restrict=RestrictType.NONE, norm=False):
    extremes = []
    for element in elements:
        curve_extremes = []
        upper_max = max([                                                                                               \
            max(second_gradient(restrict_frontal(i, restrict)))                                                         \
            for i in (normalize(element.EEG_data) if norm else element.EEG_data)                                        \
        ])
        lower_min = min([                                                                                               \
            min(second_gradient(restrict_frontal(i, restrict)))                                                         \
            for i in (normalize(element.EEG_data) if norm else element.EEG_data)                                        \
        ])
        extr_sensitivity = (upper_max + lower_min)/(2*sensitivity)
        for i in (normalize(element.EEG_data) if norm else element.EEG_data):
            num_extremes = 0
            for j in second_gradient(restrict_frontal(i, restrict)):
                if abs(j)<extr_sensitivity:
                    num_extremes +=1
            curve_extremes.append(num_extremes)
        extremes.insert(len(extremes), (curve_extremes))
    return extremes