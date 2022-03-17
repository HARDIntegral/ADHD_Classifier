from data_manager.element import Element
from scipy.io import loadmat
import json

def load_data_locations(path_to_json):
    with open(path_to_json) as f:
        return json.load(f)

def load_data(locations):
    p_locations     = load_data_locations(locations)
    parent_path     = list(p_locations.items())[0][-1]
    
    ADHD_bucket     = [
        Element(True, list(loadmat(parent_path+i).items())[-1][1].transpose())
        for i in p_locations["ADHD"]
    ]
    Control_bucket  = [
        Element(False, list(loadmat(parent_path+i).items())[-1][1].transpose())
        for i in p_locations["Control"]
    ]

    return (ADHD_bucket, Control_bucket)

def split_data(buckets):
    # pre-generated random numbers
    adhd_test_rand      = [15, 26, 24, 55, 44, 32, 14, 22, 33, 56, 58, 43]
    control_test_rand   = [36, 40, 53, 12, 18, 17, 28, 41, 32, 27, 38, 25]
    # filler numbers
    adhd_train_fill     = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 23, 25, 27, 28, 29, 30, 31, 34, 35, 36, 37, 38, 39, 40, 41, 42, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 57, 59, 60]
    control_train_fill  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 26, 29, 30, 31, 33, 34, 35, 37, 39, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59]
    
    training_set    = [ buckets[0][i] for i in adhd_train_fill ] + [ buckets[1][j] for j in control_train_fill ]
    testing_set     = [ buckets[0][i] for i in adhd_test_rand ] + [ buckets[1][j] for j in control_test_rand ]

    return (training_set, testing_set)
