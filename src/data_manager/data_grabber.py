from data_manager.element import Element
from data_manager.data_manipulation import moving_average
from scipy.io import loadmat
from tqdm import tqdm                       # for progress bars
import json

FREQUENCY = 128
SMOOTHENING_BIAS = 127

def load_data(path):
    raw_data = list(loadmat(path).items())[-1][1].transpose()
    return [ moving_average(i, int((len(i)/FREQUENCY)*SMOOTHENING_BIAS)) for i in raw_data ]

def bucket_data(path_to_data):
    with open (path_to_data) as f:
        p_locations     = json.load(f)
        parent_path     = list(p_locations.items())[0][-1]
    
        ADHD_bucket     = [ Element(True, load_data(parent_path+i)) for i in tqdm(p_locations["ADHD"]) ]
        Control_bucket  = [ Element(False, load_data(parent_path+i)) for i in tqdm(p_locations["Control"]) ]

        return (ADHD_bucket, Control_bucket)

def split_data(buckets):
    # pre-generated random numbers
    adhd_test_rand      = [15, 26, 24, 55, 44, 32, 14, 22, 33, 56, 58, 43]
    control_test_rand   = [36, 40, 53, 12, 18, 17, 28, 41, 32, 27, 38, 25]
    # filler numbers
    adhd_train_fill     = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, \
                           13, 16, 17, 18, 19, 20, 21, 23, 25, 27, 28, 29, \
                           30, 31, 34, 35, 36, 37, 38, 39, 40, 41, 42, 45, \
                           46, 47, 48, 49, 50, 51, 52, 53, 54, 57, 59, 60]
    control_train_fill  = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 13, \
                           14, 15, 16, 19, 20, 21, 22, 23, 24, 26, 29, 30, \
                           31, 33, 34, 35, 37, 39, 42, 43, 44, 45, 46, 47, \
                           48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59]
    
    training_set    = [ buckets[0][i] for i in adhd_train_fill ] + [ buckets[1][j] for j in control_train_fill ]
    testing_set     = [ buckets[0][i] for i in adhd_test_rand ] + [ buckets[1][j] for j in control_test_rand ]

    return (training_set, testing_set)
