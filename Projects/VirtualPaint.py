'''
With this project we will be able to make a virtual pen system. How?
We will first get the HSV values of the color pens we will use using the mask. We will draw the contours
around them. After finding it's centre, we will draw same color's tip which will draw as per we move.
'''


import cv2
import numpy as np

web = cv2.VideoCapture(0)
web.set(3, 640)
web.set(4, 480)
web.set(10, 50)

myColors = [[42,46, 0, 87 , 255, 255],   # green
             [0, 26, 89, 59, 255, 255],  # orange
            [74,79, 0,123, 158, 255]]    # blue

myColorValues = [[0, 255, 0],
                 [0, 165, 255],
                 [255, 0, 0]]

myPoints = []   # x, y, colorId


def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for clr in myColors:
        lower = np.array(clr[0:3])   # the three minimums
        upper = np.array(clr[3:6])   # the three max
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getcontours(mask)
        cv2.circle(imgResult, (x,y), 10,myColorValues[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
    return newPoints
        #cv2.imshow(str(clr[0]),mask)


def getcontours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:  # as a threshold to avoid noise
            #cv2.drawContours(imgResult, cnt, -1 , (0,255,255),3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y  # passing the centre


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    var, img = web.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints :
            myPoints.append(newP)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow('Result', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break