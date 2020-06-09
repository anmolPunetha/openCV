# chap6- joining images (simple method but has limitations)
import cv2
import numpy as np

img = cv2.imread("../Resources/picture.jpg")
img = cv2.resize(img, (440,300))

imgH = np.hstack((img, img, img))  # horizontally joining
imgV = np.vstack((img, img))   # vertically joining

#cv2.imshow('image', imgH)

# chap7 - color detection
# we use trackbar to use hue, sat, val
# hue has max value of 360, but in opencv it is 179


def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", (480,240))
cv2.createTrackbar("Hue Min", "TrackBars", 0,179,empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179,179,empty)
cv2.createTrackbar("Sat Min", "TrackBars", 95,255,empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255,255,empty)
cv2.createTrackbar("Val Min", "TrackBars", 96,255,empty)
cv2.createTrackbar("Val Max", "TrackBars", 255,255,empty)

while True:

    lemo = cv2.imread("../Resources/lemo.jfif")
    lemoHSV = cv2.cvtColor(lemo, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(lemoHSV, lower, upper)

    # now we use 'and' function to seek pixels which are common in mask and image
    lemoResult = cv2.bitwise_and(lemo, lemo, mask=mask)

    tog = np.hstack((lemo, lemoResult))

    cv2.imshow("HSV image",lemoHSV)
    cv2.imshow("MASK image", mask)
    cv2.imshow("Result", tog)
    cv2.waitKey(1)