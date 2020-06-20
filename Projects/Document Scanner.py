import cv2
import numpy as np

web = cv2.VideoCapture(0)
web.set(3, 640)
web.set(4, 480)
web.set(10, 50)


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5),1)
    imgCanny = cv2.Canny(imgBlur, 200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations= 2)
    imgThres = cv2.erode(imgDial, kernel, iterations=1)
    return imgThres


def getcontours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>200:
            #cv2.drawContours(imgContour, cnt, -1 , (0,0,255),3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    cv2.drawContours(imgContour, biggest, -1, (0, 0, 255), 20)
    # print(biggest)
    return biggest


def reorder(myPoints):
    myPoints = myPoints.reshape(4,2)   # as the prev shape is 4,1,2
    myPointsNew = np.zeros((4,1,2), np.int32)
    add = np.sum(myPoints, axis=1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew


def getWarp(img, biggest):
    biggest = reorder(biggest)
    print(biggest.shape)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [480, 0], [0, 640], [480, 640]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (480, 640))

    imgCropped = imgOutput[20:imgOutput.shape[0]-20, 20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped, (480, 640))

    return imgCropped


while True:
    var, img = web.read()
    img = cv2.resize(img, (640, 480))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getcontours(imgThres)  # apply an if command to set what happens when no biggest is seen
    imgCropped = getWarp(img, biggest)
    cv2.imshow('webcam', imgCropped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break