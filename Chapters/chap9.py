# chap9 -- face detection using viola and jones method using haar cascade detection method
# we need to train a model for that, but opencv has many inbuilt xml files for object detection

import cv2
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv2.imread("../Resources/face.jpeg")
img = cv2.resize(img,(480, 640))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4) # main detection of our image

# drawing rectangle around detected faces
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w,y+h),(255, 0, 0),2)

cv2.imshow("Face Detection", img)
cv2.waitKey(0)