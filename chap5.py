# chap5- warp perspective (changing image to bird-eye view)...changing the orientation

import cv2
import numpy as np

img = cv2.imread('../Resources/pic2.jpg')
img = cv2.resize(img, (500, 450))

width, height = 250, 350
pts1 = np.float32([[63,77], [191,0], [300,450], [400,375]])  # manually calculated
pts2 = np.float32([[0,0], [width,0], [0, height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix,(width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)
