# chap2 - basic functions in opencv
import cv2
import numpy as np

# converting to grayscale--.cvtColor
# blurring an image--GaussianBlur( ksize will be a pair os odd numbers only)
# edge detection-- Canny (2 thresholds are to be set)
# dilation- to increase the size of ede detection
# erosion --opposite of dilation

img = cv2.imread("../Resources/picture.jpg")
kernel = np.ones((5, 5), np.uint8)   # kernel is an array( here size is set with all values as one)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (11, 11), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("gray_image", imgGray)
cv2.imshow("blur_image", imgBlur)
cv2.imshow("Canny_image", imgCanny)
cv2.imshow("Dilation_image", imgDilation)
cv2.imshow("Eroded_image", imgEroded)


cv2.waitKey(0)