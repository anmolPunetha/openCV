import cv2
import face_recognition

imgElon = face_recognition.load_image_file("Images/elon.jpg")
imgElon = cv2.resize(imgElon, (580, 480))
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_RGB2BGR)  # conversion necessary cz we need bgr this function gives rgb

imgTest = face_recognition.load_image_file("Images/elon test.png")
imgTest = cv2.resize(imgTest, (400, 400))
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_RGB2BGR)

# finding the faces and it's encodings
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]  # encodings are 128 measurements of face
cv2.rectangle(imgElon,(faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 0), 2)

# comparing the above two through linear SVM algo at back end
results = face_recognition.compare_faces([encodeElon], encodeTest)
faceDis = face_recognition.face_distance([encodeElon],encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results}:{round(faceDis[0],2)}', (25, 25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0, 255),1)


cv2.imshow("Elon Musk",imgElon)
cv2.imshow("Elon Test",imgTest)
cv2.waitKey(0)
