#!/usr/bin/env python3

from data_manager.data_grabber import split_data, bucket_data
from data_manager.data_manipulation import avg_slope, avg_value
from SVM.svm import Kernels, SVM
import sys

def main():
    
    locations = 'Data/ADHD/Dataset.json'
    
    if len(sys.argv) > 1 and sys.argv[1] == 'research':
        locations = 'Data/Locations.json'
        
    print('Using locations file:',locations);
    
    # load the data
    
    adhd , control = bucket_data(locations)

    # assign features to the data
    
    assignFeatures(adhd)
    assignFeatures(control)
    
    # split data into training and testing sets
    
    training , testing = split_data(adhd,control)
    
    model = SVM(training,testing)
    model.fit(Kernels.RBF.value)
    model.test()
    model.fit(Kernels.M_RBF.value)
    model.test()
    model.fit(Kernels.M_POLY.value)
    model.test()
    model.fit(Kernels.M_RBF_POLY.value)
    model.test()


def assignFeatures(dataset):
    for element , features in zip(dataset,packFeatures(dataset)):
        element.add_features(features[0] + features[1])
        

def packFeatures(dataset):
    return list(zip(avg_slope(dataset),avg_value(dataset)))


if __name__ == '__main__':
    main()