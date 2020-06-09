# chap3,4 : resizing, cropping, adding shapes and text
# openCV convention:  x axis is same like in maths, but y axis is opposite of y in maths
import cv2
import numpy as np

# setting the size--first let know the size using .shape

img = cv2.imread('../Resources/picture.jpg')
print(img.shape)
imgResize = cv2.resize(img, (640, 400))
cv2.imshow('Image Resize', imgResize)

# cropping image (just array prop is used)....width x height here unlike above

imgCropped = imgResize[0:300, 150:600]
cv2.imshow('Cropped image', imgCropped)

# creating a image( 0 filled mtx implies black)

image = np.zeros((512, 512, 3), np.uint8)  # 256 characters

# giving image a color @ BGR
image[:] = 0, 255, 100  # green color, [:] implies to all else set [a,b :c,d]

# creating a line, rectangle, circle

cv2.line(image,(0,0),(image.shape[1],image.shape[0]),(255,0,0),3)
cv2.rectangle(image, (50, 50), (300, 300), (0, 0, 255), 2)  # write cv2.FILLED in thickness for filled rect.
cv2.circle(image,(200,100),20,(150,60,0), 3)

# writing text (scale-- size of text)

cv2.putText(image,'Hi buddy!', (200,400),cv2.FONT_HERSHEY_COMPLEX, 1.5, (150,150,150), 2)


cv2.imshow('Image', image)

cv2.waitKey(0)