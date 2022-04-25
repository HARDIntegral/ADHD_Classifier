
class Element():
    '''
    A wrapper for an element of the training / testing set
    
    Attributes
    ----------
    is_ADHD : bool
        Whether of not this element represents a child with ADHD or not
    EEG_data : numpy array
        The EEG recording in the format of a numpy array
    
    '''


    def __init__(self, is_ADHD, EEG_data):
        self.is_ADHD = is_ADHD
        self.EEG_data = EEG_data


    def add_features(self, features):
        '''once their features are extracted, the features are assigned to themselves'''
        self.features = features