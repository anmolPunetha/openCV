# chap1- read image, video, webcam

# installing the package
import cv2
print("package installed")

# reading the image
img = cv2.imread('../Resources/picture.jpg')
cv2.imshow('window', img)  # window's name,image
cv2.waitKey(10)  # 0: infinite time, else that many milliseconds

# reading the video
# video is read as a cluster of images
# we keep storing the images and set a key for quit
vid = cv2.VideoCapture('Resources/video.mp4')
while True:
    success, img = vid.read()      # success here is a boolean(image shown or not)
    cv2.imshow('window',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# using the webcam
# a similar code base is used as video, only we don't set sny path
# 0 is set for first webcamm
# .set for size where 4 is for height, 3 for width, 10 for brightness

web = cv2.VideoCapture(0)
web.set(3, 640)
web.set(4, 480)
web.set(10, 50)
while True:
    var, img = web.read()
    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break