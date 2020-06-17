import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# we want to access images of att folder so that task is autonomous

# accessing the folder
path = "Images_Attendence"
images = []
classNames= []
myList = os.listdir(path)  # list of all images
#print(myList)

# accessing the images inside folder ang getting names
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])  # to remove jpg from name
#print(classNames)


# getting encodings of all images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendence(name):
    with open('Attendence.csv' ,'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # for faster speed
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # treating all the faces present in the webcam
    facesCurFrame = face_recognition.face_locations(imgS)  # multile faces can be there so no [0]
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

# checking with the saved database
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis) # returns index of min no

        if matches[matchIndex]:
            name = classNames[matchIndex]
            print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img, (x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img, (x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img, name,(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255),2)
            markAttendence(name)

    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
