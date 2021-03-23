#!/usr/bin/env python
# coding: utf-8

# In[33]:


import cv2 
from matplotlib import pyplot 

# Opening normal image
# "0" for grayscale processing, however I got a green hue on my image? 
# Might be a problem with the RGB/BGR color channels in cv2?

img = cv2.imread('Image.jpeg', 0) 

# Pixel Matrix
def myimage(image):
    pyplot.imshow(image)
    
    print('Image size: ', image.shape)
    print('Pixel matrix:\n', image)
    pyplot.show()
    print('X & Y axis on the plot, are showing the pixel count.')

# Resize, cause of assignment description because why not I guess.
SIZE = 320
img = cv2.resize(img, (SIZE, SIZE))
myimage(img)


# In[34]:


import numpy as np
import skimage.measure

# Using prior Pixel Matrix from Grayscale
a = np.array([
      [ 81, 21, 27, 44, 44, 44],
      [117, 38, 16, 44, 44, 44],
      [121, 63, 10, 45, 45, 45],
      [ 39, 36, 37,  9,  7, 17],
      [ 38, 35, 35, 10,  8,  5],
      [ 38, 34, 34, 10, 21, 17],
    
])

# Using block_reduce to downsample and max-pool.
skimage.measure.block_reduce(a, (2,2), np.max)


# In[37]:


# Defining parameters of edges and lines in my Grayscale Image.
gray = cv2.imread('Image.jpeg', 0)
edges_param = cv2.Canny(img,50,150, apertureSize = 3)

newLinesImage = cv2.imwrite('ImageEdge.jpeg', edges_param)
minLineLength = 100

Line_Param = cv2.HoughLinesP(image=edges_param,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), 
minLineLength=minLineLength,maxLineGap=80)


# In[38]:


# Opening the result. (sorry for the small picture)
# Will open the outdrawn edges and lines of the my grayscale image with your preferred image editor in your OS.
from PIL import Image

image = Image.open('ImageEdge.jpeg')
image.show()

# TO THE REVIEWER: If you have any idea on how to implement the Stride function, I would greatly appreciate some input on that. Thanks a bunch!

