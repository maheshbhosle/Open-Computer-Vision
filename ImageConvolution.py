#Image Processing using Convolution 

import cv2
import numpy as np

class ImageConvolution:
    def __init__(self, img_path):
        self.mem_image = cv2.imread(img_path, cv2.IMREAD_COLOR)
        if self.mem_image is None:
            raise Exception('No Image Found: ' + img_path)

        #self.mem_image = cv2.resize(self.mem_image, (1200,800))

    #blur an image
    def blur(self):
        #way 1
        #resultant_image = cv2.blur(self.mem_image, (9,9))

        #way2
        #a) design the blurring kernel
        kernel = np.ones((9,9))/81
        #b)convolution
        resultant_image = cv2.filter2D(self.mem_image, -1, kernel)

        #render
        cv2.imshow('Original Image', self.mem_image)
        cv2.imshow('Blurred Image', resultant_image)
        cv2.waitKey(0) #waits for a key press
        cv2.destroyAllWindows()



    #edge detection
    def edge_detection(self):
        # a) design the edge detection kernel
        kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
        # b)convolution
        resultant_image = cv2.filter2D(self.mem_image, -1, kernel)

        # render
        cv2.imshow('Original Image', self.mem_image)
        cv2.imshow('Edge Highlighted Image', resultant_image)
        cv2.waitKey(0)  # waits for a key press
        cv2.destroyAllWindows()

    #sharpen
    def sharpen(self):
        # a) design the edge detection kernel
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        # b)convolution
        resultant_image = cv2.filter2D(self.mem_image, -1, kernel)

        # render
        cv2.imshow('Original Image', self.mem_image)
        cv2.imshow('Sharpened Image', resultant_image)
        cv2.waitKey(0)  # waits for a key press
        cv2.destroyAllWindows()

    #outline
    def outline(self):
        # a) design the edge detection kernel
        kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
        #b) convert the src image into grayscale image
        gray_scale_image = cv2.cvtColor(self.mem_image, cv2.COLOR_BGR2GRAY)


        #c)convolution for edge detection
        resultant_image = cv2.filter2D(gray_scale_image, -1, kernel)

        #d)binary not
        resultant_image = cv2.bitwise_not(resultant_image)

        # render
        cv2.imshow('Original Image', self.mem_image)
        cv2.imshow('Outline Image', resultant_image)
        cv2.waitKey(0)  # waits for a key press
        cv2.destroyAllWindows()

    #sobel_edge
    def sobel(self):
        # a) design 2 edge detection kernels
        #kernel source https://www.projectrhea.org/rhea/index.php/An_Implementation_of_Sobel_Edge_Detection
        kernel_h = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        kernel_v = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

        #c)convolution for edge detection
        resultant_image_h = cv2.filter2D(self.mem_image, -1, kernel_h)
        resultant_image_v = cv2.filter2D(self.mem_image, -1, kernel_v)

        #d)merge the two resultant images
        resultant_image = cv2.bitwise_or(resultant_image_h, resultant_image_v)

        #render
        cv2.imshow('Original Image', self.mem_image)
        cv2.imshow('Sobble Edge Detection', resultant_image)
        cv2.waitKey(0)  # waits for a key press
        cv2.destroyAllWindows()


ic = ImageConvolution('d:/images/temple.png')
#ic.blur()
#ic.edge_detection()
#ic.sharpen()
#ic.outline()
ic.sobel()

#FYI
#Kernel: Kernel (also called as a convolution matrix or a mask) is a small
#square matrix containing preset values. It (kernel) represents how much part of
#surrounding pixels (neighbours) values should be used (during convolution) to
#calculate the intensity value of the current pixel. Usually kernels are square
#matrices of odd length like 3x3, 5x5, ...
#It is used for image blurring, sharpening, embossing, edge detection, and more.

#Convolution: Convolution is a mathematical process in which the elements of a
#sub matrix (of the same size as that of the kernel) from the source image, are
#multiplied with the corresponding elements of the kernel. Further addition is
#performed on the previous computation to calculate a new intensity for the current
#pixel.

#Refer: https://en.wikipedia.org/wiki/Kernel_(image_processing)