import cv2
import math
import numpy as np

# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (50, 50) 
  
# fontScale 
fontScale = 1

# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error opening camera")
    exit(0)
while(cap.isOpened()):
    ret, img = cap.read()
    cv2.rectangle(img, (600,600), (100,100), (0, 255, 0), 0)
    crop_img = img[100:600, 100:600]
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow("Thresholded",thresh1)
    
    contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = max(contours, key = lambda x: cv2.contourArea(x))
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img, (x,y), (x+w, y+h), (0,0,255), 5)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_img.shape, np.int8)
    cv2.drawContours(drawing, [cnt], 0, (0,255,0), 5)
    cv2.drawContours(drawing, [hull], 0, (0,255,0), 5)
    hull = cv2.convexHull(cnt, returnPoints = False)
    defects = cv2.convexityDefects(cnt, hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0,255,0), 10)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2+ (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2+ (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2+ (end[1] - far[1])**2)

        angelValue = (b**2 +c**2 - a**2)/(2*b*c)
        #print("angelValue " , str(angelValue))
        angle = math.acos(angelValue)*57
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img, far, 1, [0,0,255], -1)
        cv2.line(crop_img,start, end,[0,255,0],2)
    
    print(count_defects)
 

    if count_defects == 1:
        cv2.putText(img, "This is a Scissor", org, font, fontScale, color, thickness, cv2.LINE_AA)
    elif count_defects == 0:
        cv2.putText(img, "This is a Rock",org, font, fontScale, color, thickness, cv2.LINE_AA)
    elif count_defects == 4:
        cv2.putText(img, "This is a Paper", org, font, fontScale, color, thickness, cv2.LINE_AA)
    else:
        cv2.putText(img, "Not recognizing anything",  org, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Gesture", img)
    all_img = np.hstack((drawing, crop_img))
    k = cv2.waitKey(10)
    if k == 27:
        break
