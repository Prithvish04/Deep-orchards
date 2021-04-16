#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os
import math

path1=os.path.abspath('..') 
rootdir=os.path.join(path1+'/almonds/annotations')

for root, dirs, files in os.walk(rootdir):
        print("root", root)  # 当前目录路径
        print("dirs", dirs)  # 当前路径下所有子目录
        print("files", files)  # 当前路径下所有非目录子文件    
for name in files:
    if name[-3:] == 'csv':
        csvFile = os.path.join(root,name)
        xmlname = name[:-3] + 'xml'
        xmlroot = '../data/VOCdevkit2007/VOC2007/Annotations'
        xmlFile = os.path.join(xmlroot,xmlname)
        
        csvData = csv.reader(open(csvFile))
        xmlData = open(xmlFile, 'w')
        # there must be only one top-level tag
        xmlData.write('<annotation>' + "\n")
        xmlData.write('<size>' + "\n")
        xmlData.write('    ' + '<width>' \
                                  + '300' + '</width>' + "\n")
        xmlData.write('    ' + '<height>' \
                                  + '300' + '</height>' + "\n")
        xmlData.write('    ' + '<depth>' \
                                  + '3' + '</depth>' + "\n")
        xmlData.write('</size>' + "\n")
        rowNum = 0
        for row in csvData:
            if rowNum == 0:
                tags = row
                # replace spaces w/ underscores in tag names
                for i in range(len(tags))[1:]:
                    tags[i] = tags[i].replace(' ', '_')
            
            else:     
                xmlData.write('<object>' + "\n")
                xmlData.write('<name>' \
                                  + 'almonds' + '</name>' + "\n")
                xmlData.write('<pose>' \
                                  + '0' + '</pose>' + "\n")
                xmlData.write('<difficult>' \
                                  + '0' + '</difficult>' + "\n")                    
                xmlData.write('<truncated>' \
                                  + '0' + '</truncated>' + "\n")
                xmlData.write('<bndbox>' + "\n")
                for i in range(len(tags))[1:]:
                    if i == 1:
                        value = math.ceil(float(row[i]))+1
                        if value <1:
                              print("warning")
                        xmlData.write('    ' + '<xmin>' \
                                          + str(value) + '</xmin>' + "\n")
                    if i == 2:
                        value = math.ceil(float(row[i]))+1
                        if value <1:
                              print("warning")
                        xmlData.write('    ' + '<ymin>' \
                                          + str(value) + '</ymin>' + "\n") 
                    if i == 3:
                        value = math.ceil(float(row[i])+float(row[i-2]))+1
                        if value >299:
                          
                            value = 299
                        xmlData.write('    ' + '<xmax>' \
                                          + str(value) + '</xmax>' + "\n")         
                    if i == 4:
                        value = math.ceil(float(row[i])+float(row[i-2]))+1
                        if value>299:
                        
                            value = 299
                        xmlData.write('    ' + '<ymax>' \
                                          + str(value) + '</ymax>' + "\n")                 
                xmlData.write('</bndbox>' + "\n")
                xmlData.write('</object>' + "\n")
        
                    
            rowNum +=1
        
        xmlData.write('</annotation>' + "\n")
        xmlData.close()

#        for i in range(len(tags))[1:]:
#           xmlData.write('    ' + '<' + tags[i] + '>' \
#                          + row[i] + '</' + tags[i] + '>' + "\n")
