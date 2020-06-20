import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_eye.xml")

web = cv2.VideoCapture(0)
web.set(3,640)
web.set(4, 480)
web.set(10, 80)

while True:
    _, img = web.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
