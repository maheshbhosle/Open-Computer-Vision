#Basic image operations using OpenCV
import cv2 #pip install opencv-python

#load an image in memory
mem_img = cv2.imread('d:/images/kids.jpg', cv2.IMREAD_COLOR)
#print(type(mem_img))
#print(mem_img.shape)

#Resize the image
#Resizing an image is upscaling or downsclaing  its dimensions (w,h).
#OpenCV provides the resize()
#resized_memory_image = resize(memory_image, destination_size, interpolation)

percentage = 20
h = mem_img.shape[0] * percentage //100
w = mem_img.shape[1] * percentage //100

if percentage < 100:
    #use the algo cv2.INTER_AREA if the image size is being reduced
    mem_img = cv2.resize(mem_img, (w,h), interpolation= cv2.INTER_AREA)
elif percentage > 100:
    # use the algo cv2.INTER_LINEAR or cv2.INTER_CUBIC (slow method) if the image size is being increased
    mem_img = cv2.resize(mem_img, (w,h), interpolation= cv2.INTER_LINEAR)


#crop an image
#use numpy array slicing array[rows, cols]
#example arr[0:10, 100:205] returns a matrix made from rows 0-9 and cols 100 to 204
#h = mem_img.shape[0]
#w = mem_img.shape[1]
#mem_img = mem_img[50:h-50, 50:w-50]


#image blur
#blurred_mem_image = cv2.blur(mem_image, ksize) convolves the image with a kernel. It simply takes the average of all the pixels under kernel area and replaces the central element with the average.
#mem_img = cv2.blur(mem_img, (7,7))
mem_img[200:320, 350:500] = cv2.blur(mem_img[200:320, 350:500], (20,20))

#Define a named window
cv2.namedWindow('WIN')
#Render the image in the window
cv2.imshow('WIN', mem_img)
#wait until any key is pressed
cv2.waitKey(0)



