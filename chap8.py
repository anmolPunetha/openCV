# chap8--contour / shape detection and some operations on it (area, perimeter, outline, corners, making a rec aarounf each shape)
# 1. draw canny image from grayscale of the org image
# 2. In a funcion, use .findContours and a retrieval mode along with a method
# 3. use a loop for accessing each item of the image, here u get
# 4. use .drawContours to draw outlines
import cv2


def getcontours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # mode in .findContours is the method of retrieval
    for cnt in contours:  # accessing each shape of the group
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:  # as a threshold to avoid noise
            cv2.drawContours(imgCopy, cnt, -1 , (0,0,255),3)  # drawing the contours, -1 bcz we are highlighting full shape
            perimeter = cv2.arcLength(cnt, True)
            print(perimeter)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            print(approx)  #tells the coordinates of corners of various shapes
            corner = (len(approx))
            x, y, w, h = cv2.boundingRect(approx)

            if corner == 3: objectType = "Tri"
            elif corner == 4 :
                aspRatio = w/float(h)
                if aspRatio>0.95 and aspRatio<1.05 : objectType = "Square"
                else : objectType = "Rect"
            elif corner >4 :objectType ="Circle"
            else : objectType="none"

            cv2.rectangle(imgCopy, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgCopy,objectType, (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))


img = cv2.imread('../Resources/shapes.jpg')
imgCopy = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(imgGray, 50, 50)

getcontours(imgCanny)

cv2.imshow("original",img)
cv2.imshow("Grayscale", imgGray)
cv2.imshow("Canny",imgCanny)
cv2.imshow('Detection and drawing', imgCopy)

cv2.waitKey(0)