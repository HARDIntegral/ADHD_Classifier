from data_manager.element import Element
from scipy.io import loadmat
import json

def load_data_locations(path_to_json):
    with open(path_to_json) as f:
        return json.load(f)

def load_data(locations):
    p_locations = load_data_locations(locations)
    parent_path = list(p_locations.items())[0][-1]

    ADHD_bucket = [ Element(True, list(loadmat(parent_path+i).items())[-1][1]) for i in p_locations["ADHD"] ]
    Control_bucket = [ Element(False, list(loadmat(parent_path+i).items())[-1][1]) for i in p_locations["Control"] ]

    return (ADHD_bucket, Control_bucket)
