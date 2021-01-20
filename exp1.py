# # resizing the image
# # original = 2456,2052
# # after resizing = 859,718
import cv2
import numpy as np
img = cv2.imread('/Users/niharikasoni/Desktop/1.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 35 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# #  removing noise and distortion from the image 

edges = cv2.Canny(resized, 100, 2500, apertureSize=5)
cv2.imshow("edge image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

#  mouse event
eventpoints = [ ]
# print(events)
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        eventpoints.append((x,y))
        print(x,', ',y)
        if True:
            if len(self.pts) > 0:
                cv2.circle(self.resized, self.pts[-1], 3, (0, 0, 255), 1)
                font=cv2.FONT_HERSHEY_SIMPLEX
                strXY= str(x) + ', ' + str(y)
                cv2.putText(img,strXY, (x,y), font, 1, (255,255,0),2 )
                # cv2.imshow("image",img)
                cv2.namedWindow(figure_title)
                cv2.setMouseCallback(figure_title, click_event) #call calibration_func

    while True:
        cv2.imshow(figure_title,resized)
        key = cv2.waitKey(0)
        if key == 27:
            cv2.destroyAllWindows()
            break
# cv2.setMouseCallback("image",click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 
# #  drawing a horizontal line to get the dsitance between 2 points 

# start_point = (200, 200)
# end_point = (1000, 1000)
# color = (255, 0, 0) 
# thickness = 5
# line = cv2.line(edges, start_point, end_point, color, thickness) 
# # line = cv2.line(edges,(0,0), (width,height), (0,0,255), thickness)
# cv2.imshow("line_image",line)
# cv2.imwrite("/Users/niahrikasoni/Documents/1.jpg",line)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
 
# # image = cv2.imread('C:/Users/N/Desktop/test.jpg')
 
# height = edges.shape[0]
# width = edges.shape[1]
 
# # cv2.line(edges, (20,10), (100,10), (255,0,0), 2)
# cv2.line(edges, (500,500), (width, height), (255,0,0), 5)
 
# cv2.imshow("Image", edges)
    
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# coordinates 
# indices = np.where(edges != [0])
# coordinates = zip(indices[0], indices[1])
# print(coordinates)