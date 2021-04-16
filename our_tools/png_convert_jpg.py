#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:03:36 2021

@author: tfh
"""

from PIL import Image
import os
import numpy as np

rootdir=os.path.join('./almonds/images/')
for root, dirs, files in os.walk(rootdir):
        print("root", root)  # 当前目录路径
        print("dirs", dirs)  # 当前路径下所有子目录
        print("files", files)  # 当前路径下所有非目录子文件   
    
for name in files:
    if name[-3:] == 'png':
        pngFile = os.path.join(root,name)
        img = Image.open(pngFile)
        rgb_img = img.convert('RGB')
        jpgname = name[:-3] + 'jpg'
        jpgroot = os.path.join('./data/VOCdevkit2007/VOC2007/JPEGImages/')
        jpgFile = os.path.join(jpgroot,jpgname)
        rgb_img.save(jpgFile)
        