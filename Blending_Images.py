#Blend 2 images 
import cv2

img1 = cv2.imread('d:/images/farm.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('d:/images/kids.jpg', cv2.IMREAD_COLOR)

std_size = (1200, 800)
img1 = cv2.resize(img1, std_size)
img2 = cv2.resize(img2, std_size)

#blend = cv2.add(img1, img2)
alpha = 0.95
beta = 1 - alpha

#per pixel
#target = img1*alpha + img2*beta + gamma
blend = cv2.addWeighted(img1, alpha, img2, beta, 0)

cv2.imshow('WIN', blend)
cv2.waitKey(0)
