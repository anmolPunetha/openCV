import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('image.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # pytesseract takes RGB values not BGR so we convert
hImg, wImg, _ = img.shape

# print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_boxes(img))

'''
# Detecting characters (solely character, no words)
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255), 2)
    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(80,80,255),2)
'''


# to detect the data(not characters rather words out of the image
cong = '--oem 3 --psm 6 outputbase digits'  # not working, some issue
boxes = pytesseract.image_to_data(img, config=cong)
for x,b in enumerate(boxes.splitlines()):  # enumerate is just an alt of count = 0 wala method
    if x!=0:
        b = b.split()
        print(b)
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255), 2)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(80,80,255),2)

cv2.imshow('Image',img)
cv2.waitKey(0)