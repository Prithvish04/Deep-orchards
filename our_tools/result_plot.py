#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:47:44 2021

@author: tfh
"""

import pickle
import os
import numpy as np
from matplotlib import pyplot as plt
import cv2

with open('../data/VOCdevkit2007/VOC2007/ImageSets/Main/test.txt_annots.pkl', 'rb') as f:
    data = pickle.load(f)

with open ('../data/VOCdevkit2007/VOC2007/ImageSets/Main/test.txt', "r") as myfile:
    data_name = myfile.read().splitlines()

for i in data_name:
    dir=os.path.join('../data/VOCdevkit2007/VOC2007/JPEGImages/'+i+'.jpg')
    image = cv2.imread(dir)
    fig, ax = plt.subplots() 
    ax.imshow(image)
    for j in data[i]:
        x = j['bbox']
        rectangle = plt.Rectangle((x[0],x[1]), x[2]-x[0], x[2]-x[1], linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rectangle)    
    plt.show()

