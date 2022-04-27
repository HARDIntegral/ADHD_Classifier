from data_manager.data_manipulation import moving_average
from data_manager.element import Element
from scipy.io import loadmat
from random import shuffle
from json import load as asJSON

FREQUENCY = 128
SMOOTHENING_BIAS = 127


def bucket_data(path):
    '''
    Load ADHD / Control data as buckets
    
    Parameters
    ----------
    path : str
        Path to the list of dataset paths
    
    Returns
    -------
    ADHD : array
        Bucket of ADHD data elements
    Control : array
        Bucket of Control data elements
    '''
    
    with open(path) as file:
        
        locations = asJSON(file)
        folder = list(locations.items())[0][-1]

        ADHD    = [ Element(True ,load_data(folder + '/' + path)) for path in locations['ADHD']    ]
        Control = [ Element(False,load_data(folder + '/' + path)) for path in locations['Control'] ]

        return ( ADHD , Control )


def load_data(path):
    
    raw = list(loadmat(path).items())[-1][1].transpose()
    
    return [ interpret(value) for value in raw ]


def interpret(value):
    return moving_average(value,int((len(value) / FREQUENCY) * SMOOTHENING_BIAS))


def split_data(a,b):

    shuffle(a)
    shuffle(b)

    return ( a[12:] + b[12:] , a[:12] + b[:12] )