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
def avg_slope(data):
    return [ (i[-1] - i[0])/len(i) for i in data ]

# Second Idea:
# Return the average value of the values of a channel over time
#   if that makes sense
def avg_value(data):
    return [ sum(i)/len(i) for i in data ]

# Third Idea:
# Return the number of peaks and troughs from each channel over a
#   period of time
# Update: This idea is not worth going into since peaks are generally 
#   located in the same area with the same relative magnitude. If I
#   were to work on this, I would need to find a way to calculate a
#   shared extrema sensitivity and use that to filter out exteme areas
def extremes(data, sensitivity):
    extremes = []
    for i in data:
        gradients = np.gradient(np.gradient(i))
        extr_sensitivity = (max(gradients)+min(gradients))/(2*sensitivity)
        num_extremes = 0
        for j in i:
            if abs(j)>extr_sensitivity:
                num_extremes +=1
        extremes.append(num_extremes)
    return extremes