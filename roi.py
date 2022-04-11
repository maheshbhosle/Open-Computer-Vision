#Region of Interest
#... to be continued
import cv2
class ROI:
    def __init__(self, source_img ):
        #Read the source_img from disk (path) and load it as a numpy.ndarray
        #Incase the source_img is not found/accessible then cv2.imread returns None
        self.memory_image = cv2.imread(source_img, cv2.IMREAD_COLOR)
        if self.memory_image is None:
            raise Exception(source_img + ' is not accessible')
        self.selection = []
        self.selection_state = 0

        print(self.memory_image.shape) #(height, width, bands_per_pixel)

    def on_mouse_event(self, event,x,y,flag, param):
        #event: the event like LEFT BUTTON DOWN, ...
        #x,y: co-ords of the event
        #flag: CTRL, SHIFT, ... key pressed along with the mouse event
        #param: any object that was sent while event registration or None

        if event == cv2.EVENT_LBUTTONDOWN:
            print('Mouse down at ', x, y)
            self.selection.clear() #wants to draw a new rect; hence clear the old coords
            self.selection_state = 1
            self.selection.append(x) #append x1 coord
            self.selection.append(y) #append y1 coord

        elif event == cv2.EVENT_LBUTTONUP:
            print('Mouse up at ', x, y)
            self.selection_state = 2
            self.selection.append(x) #append x2 coord
            self.selection.append(y) #append y2 coord

        if self.selection_state == 2:
            #mouse down and then up
            #x1,y1;x2,y2 are recorded
            #lets normalize
            if self.selection[0] > self.selection[2]:
                self.selection[0],self.selection[2]  = self.selection[2],self.selection[0]
            if self.selection[1] > self.selection[3]:
                self.selection[1], self.selection[3] = self.selection[3],self.selection[1]

            #correct the window bounds
            #self.memory_image.shape  -> (height, width, bands_per_pixel)
            self.selection[0] = max(self.selection[0], 0) #x1 = x1 or x1 = 0
            self.selection[1] = max(self.selection[1], 0) #y1 = y1 or y1 = 0
            self.selection[2] = min(self.selection[2], self.memory_image.shape[1]) #x2 = x2 or x2 = w
            self.selection[3] = min(self.selection[3], self.memory_image.shape[0]) #y2 = y2 or y2 = h

            #normalized now
            self.selection_state = 3

    def define_roi(self):
        #Create a window
        cv2.namedWindow('ROI')
        #Register with cv2 for mouse event (on window) notifications
        cv2.setMouseCallback('ROI', self.on_mouse_event)

        refresh_flag = True
        while refresh_flag:

            #Render the image in the window
            cv2.imshow('ROI', self.memory_image)

            if self.selection_state == 3:
                # rectangle(img, pt1, pt2, color, thickness)
                cv2.rectangle(self.memory_image, pt1=(self.selection[0],self.selection[1]), pt2=(self.selection[2], self.selection[3]), color=(255, 0, 0), thickness=2)

            if cv2.waitKey(100)== 27: #waits for 100 ms to read a key press. If the key pressed is ESC (27) then set the refresh_flag = False
                refresh_flag = False

        #Dispose the window and recover the memory
        cv2.destroyWindow('ROI')

obj = ROI('d:/images/small_kids.jpg')
obj.define_roi()