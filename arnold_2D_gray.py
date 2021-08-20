# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:03:58 2021

@author: PRIYANSI

GRAY IMAGE 2D ARNOLD SCRAMBLING

Input : 256 X 256 Grayscale Lena Image

For N X N sized Grayscale Image
Periodicity of Arnold is expressed as P_N = (N/64) * (P_64)
where P_64 = Arnold Periodicity of 64 X 64 Grayscale Image

"""
from PIL import Image
import numpy as np

def arnold_2D_GRAY(r,image_arr):
     N = image_arr.shape[0]
     x,y = np.meshgrid(range(N),range(N))
     x_map = (x + y) % N
     y_map = (2*x + y) % N
     for t in range(0,r):
         image_arr = image_arr[x_map,y_map]
     return image_arr


imgname = "lena.tif"
P = 192 #Periodicity of image
r = 101
'''
Scrambling with 101 iterations....
'''
image_arr = np.array(Image.open(imgname))
out_image =  Image.fromarray(arnold_2D_GRAY(r,image_arr))
out_image.save('Scrambled.bmp')
'''
Unscrambling with P - r iterations...
'''
image_s_arr = np.array(Image.open('Scrambled.bmp'))
org_image =  Image.fromarray(arnold_2D_GRAY( P - r, image_s_arr))
org_image.save('Unscrambled.bmp')