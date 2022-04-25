# A wrapper for a element in either the training or testing set
class Element():
    def __init__(self, is_ADHD, EEG_data):
        self.is_ADHD = is_ADHD      # whether or not this element represents a child with ADHD or not
        self.EEG_data = EEG_data    # the EEG recording in the format of a numpy array 

    def add_features(self, features):
        self.features = features    # once their features are extracted, the features are assigned to themselves
