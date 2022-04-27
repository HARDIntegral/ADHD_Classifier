#!/usr/bin/env python3

from numpy.random import randint
from scipy.io import savemat
from shutil import rmtree
from time import sleep
from json import dumps
from os import mkdir , path

folder = 'Data/ADHD'
index = {}


def generateSamples(count):
    
    global index;
    
    index = {
        'file_path' : folder ,
        'Control' : [] ,
        'ADHD' : []
    }
    
    if path.isdir(folder):
        rmtree(folder)
    
    sleep(0.1);
    
    mkdir(folder)
    mkdir(folder + '/ADHD/')
    mkdir(folder + '/Control/')
    
    for i in range(count):
        generateSample('ADHD',i)
        generateSample('Control',i)
        
    generateIndex();
    

def generateSample(type,id):
    
    data = generateMatrix()
    
    mat = { 'v1p' : data }
    
    path = type + '/' + str(id) + '.mat'

    index[type].append(path)
    
    savemat(folder + '/' + path,mat)


def generateMatrix():
    return randint(-1000,1000,size = (10000,19),dtype = int)
    
    
def generateIndex():
    
    json = dumps(index,indent = 4)
    
    file = open(folder + '/Dataset.json','w')
    file.write(json)
    file.close()
    

if __name__ == '__main__':
    generateSamples(3)