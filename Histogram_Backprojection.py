import cv2
import numpy as np
from matplotlib import pyplot as plt

#Histogram Backprojection
#Histogram Backprojection is a technique used for finding objects of interest in
#an image.


class HistogramBackprojection:
    def __init__(self, source_image, roi):
        #load the source image
        self.source_img = cv2.imread(source_image, cv2.IMREAD_COLOR)
        #load the roi
        self.roi = cv2.imread(roi, cv2.IMREAD_COLOR)
        #test
        if self.source_img is None:
            raise Exception('Couldnt load '+ source_image)
        if self.roi is None:
            raise Exception('Couldnt load ' + roi)


    def backprojection(self):
        #switch the color space from BGR to HSV
        hsv_source_image = cv2.cvtColor(self.source_img, cv2.COLOR_BGR2HSV)
        hsv_roi = cv2.cvtColor(self.roi, cv2.COLOR_BGR2HSV)

        #calculate a 2 channel (hue:0 and saturation:1) histogram (distribution of values (pixel intensities) over a dataset (image).
        hist_hsv_roi = cv2.calcHist(images = [hsv_roi], channels=[0,1], mask=None, histSize= [180,256], ranges = [0,179,0,255])

        #histogram backprojection
        # It creates an image of the same size (as that of the input image) but single channel.
        # Each pixel of histogram backprojection corresponds to the probability of that pixel
        # belonging to object of interest (being searched).
        # The output image will have the object of interest in more white compared to remaining part.

        hist_bkp = cv2.calcBackProject(images=[hsv_source_image], channels=[0,1],hist= hist_hsv_roi, ranges=[0,179,0,255], scale=1)

        #Lets enhance the histogram backprojection image to transforms the intensities
        #of its pixel according to the intensities of the neighboring pixels.
        #i.e. Convolution using kernel
        kernel = np.ones((7,7), dtype=np.uint8)
        hist_bkp = cv2.filter2D(hist_bkp, -1, kernel)

        #Hightlight the findings (hist_bkp)
        #The image and histogram backprojection are to be 'anded',
        #but the image is 3 channel and histogram backprojection is single channel
        #so convert the histogram backprojection to 3 channels.
        hist_bkp = cv2.merge((hist_bkp, hist_bkp, hist_bkp))
        findings = cv2.bitwise_and(self.source_img, hist_bkp)

        #render
        cv2.imshow('Source', self.source_img)
        cv2.imshow('ROI', self.roi)
        cv2.imshow('Backprojection', hist_bkp)
        cv2.imshow('Findings', findings)
        plt.plot(hist_hsv_roi)

        plt.show()
        #cv2.waitKey(0)
        cv2.destroyAllWindows()

hb = HistogramBackprojection('d:/images/alphabets_digits_symbols.jpg', 'd:/images/roi.png')
hb.backprojection()
