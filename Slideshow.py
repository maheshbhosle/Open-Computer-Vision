#Slideshow with video_export

import cv2
from os import path, listdir

class SlideShow:
    #A special method of the class.
    #It is auto invoked as object of the class is created.
    #It is used to initialize the object to its first state
    def __init__(self, source, filter = ['.jpg', '.jpeg', '.png']):
        if not path.exists(source):
            raise Exception('Path not found: ' + source)
        if not path.isdir(source):
            raise Exception('Not a directory: '+ source)

        self.contents = [source+ '/' +x for x in listdir(source) if path.splitext(x.lower())[1] in filter ]

    #A object processing method
    def play(self):
        #Create a window
        cv2.namedWindow('SlideShow')
        #Set up a std size for every image
        std_size = (1200, 800)
        i = 0
        l = len(self.contents)
        mem_img = None
        flag = True
        while flag:
            if mem_img is None:
                #load the image
                mem_img = cv2.imread(self.contents[i], cv2.IMREAD_COLOR)
                #resize (upscale/downscale) it to a std size
                mem_img = cv2.resize(mem_img, std_size)
            else:
                mem_img = next_img

            #render
            cv2.imshow('SlideShow', mem_img)
            #delay of 1 second
            cv2.waitKey(1000)
            i+=1 #next
            if i < l: #not a last slide
                #load the next slide
                next_img = cv2.imread(self.contents[i], cv2.IMREAD_COLOR)
                #resize it to a std size
                next_img= cv2.resize(next_img, std_size, interpolation=cv2.INTER_AREA)
                #blend to create a transition
                for x in range(1, 101):
                    alpha = 0.01 * x
                    beta = 1 - alpha
                    blend = cv2.addWeighted(next_img, alpha, mem_img, beta, 0)
                    #render the blend
                    cv2.imshow('SlideShow', blend)
                    cv2.waitKey(10)
            else:
                flag = False

        cv2.waitKey(1000)
        cv2.destroyWindow('SlideShow')


    #A object processing method
    def video_export(self, target = 'd:/images/output.avi'):
        print('Beginning Export...')
        #Set up a std size for every image
        frame_size = (1200, 800)

        #codec for video writing in .avi form
        fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

        #frames per second
        fps = 30

        #initialize a video writer
        v_out = cv2.VideoWriter(target, fourcc, fps, frame_size)

        i = 0
        l = len(self.contents)
        mem_img = None
        flag = True


        while flag:
            if mem_img is None:
                #load the image
                mem_img = cv2.imread(self.contents[i], cv2.IMREAD_COLOR)
                #resize (upscale/downscale) it to a std size
                mem_img = cv2.resize(mem_img, frame_size)
            else:
                mem_img = next_img

            for seconds in range(3):
                # write the image fps times to generate 1 second video
                for q in range(fps):
                    v_out.write(mem_img)

            i+=1 #next
            if i < l: #not a last slide
                #load the next slide
                next_img = cv2.imread(self.contents[i], cv2.IMREAD_COLOR)
                #resize it to a std size
                next_img= cv2.resize(next_img, frame_size, interpolation=cv2.INTER_AREA)
                #blend to create a transition
                for x in range(1, 101):
                    alpha = 0.01 * x
                    beta = 1 - alpha
                    blend = cv2.addWeighted(next_img, alpha, mem_img, beta, 0)
                    #write the blend as well
                    v_out.write(blend)

            else:
                flag = False

        #close the video writer
        v_out.release()
        print('Slideshow Exported: ', target)


ss = SlideShow('d:/images')#init is called
#ss.play() 
ss.video_export()

