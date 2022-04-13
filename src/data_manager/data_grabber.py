from data_manager.element import Element
from data_manager.data_manipulation import moving_average
from scipy.io import loadmat
import json, random

FREQUENCY = 128
SMOOTHENING_BIAS = 127

def load_data(path):
    raw_data = list(loadmat(path).items())[-1][1].transpose()
    return [ moving_average(i, int((len(i)/FREQUENCY)*SMOOTHENING_BIAS)) for i in raw_data ]

def bucket_data(path_to_data):
    with open (path_to_data) as f:
        p_locations     = json.load(f)
        parent_path     = list(p_locations.items())[0][-1]
    
        ADHD_bucket     = [ Element(True, load_data(parent_path+i)) for i in p_locations["ADHD"] ]
        Control_bucket  = [ Element(False, load_data(parent_path+i)) for i in p_locations["Control"] ]

        return (ADHD_bucket, Control_bucket)

def split_data(a, b):
    random.shuffle(a)
    random.shuffle(b)
    return (a[12:]+b[12:], a[:12]+b[:12])