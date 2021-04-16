import cv2
import os
import csv
from matplotlib import pyplot as plt
import time 
import math

def a2i(x):
    return math.ceil(float(x))

def plot_vizualise(fruit):
    with os.scandir(fruit+'/images') as entries:
        for entry in entries:
            image = cv2.imread(fruit+'/images/'+entry.name)
            name = entry.name.split(".p")[0]
            
            # fruits annotation visualisation
            with open(fruit+'/annotations/'+name+'.csv', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                annote_list=[]
                fig, ax = plt.subplots() 
                ax.imshow(image) 
                
                # read through the csv file 
                for row in csv_reader:
                    if fruit == 'apples':
                        if row['c-x']:
                            circle = plt.Circle((a2i(row['c-x']), a2i(row['c-y'])), a2i(row['radius']), fill=False)
                            ax.add_patch(circle)
                    else:
                        if row['x']:
                            rectangle = plt.Rectangle((a2i(row['x']),a2i(row['y'])), a2i(row['dx']), a2i(row['dy']), linewidth=1, edgecolor='r', facecolor='none')
                            ax.add_patch(rectangle)
                plt.show()
                    
