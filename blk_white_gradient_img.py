#create a black and white gradient
import numpy as np
import cv2

#define an array of 256 elements having values evenly distributed (stepped) in the range 0-255
#arr = np.linspace(0,255,256, dtype=np.uint8)
#arr = np.tile(arr, (256,1))
#print(arr)

#create a 2d array of size 256*256, each element filled with zeros
arr = np.zeros((256,256), dtype=np.uint8)
#add i to each row
for i in range(0,256):
    arr[i] +=i
print(arr)
cv2.imshow('WIN', arr)
cv2.waitKey(0)