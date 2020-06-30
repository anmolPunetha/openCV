import cv2
import numpy as np

vid = cv2.VideoCapture(0)
whT = 320  # width, height is same as in the file
confThreshold = 0.5
nmsThreshold = 0.3

# accessing the classes names from the file
classesNames = []
classesFile = 'coco.names'                   # contains 80 classes used by the yolo cnn
with open(classesFile, 'rt') as f:
    classesNames = f.read().rstrip('\n').split('\n')
# print(classesNames)
# print(len(classesNames))

# importing the models
# tiny one has lower resolution so high processing speed
# the 320 one has low processing power but high resolution so confidence is greater
modelConfiguration = 'yolov3-tiny.cfg'
modelWeights = 'yolov3-tiny.weights'

# setting the network
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def findObjects(outputs, img):
    hT, wT, cT = img.shape
    confs = []
    classIds = []
    bbox = []
    for output in outputs:
        for det in output:
            scores = det[5:]  # choosing the max probability from 6th to 85th elements
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2]*wT), int(det[3]*hT)
                x, y = (int(det[0]*wT)-w/2), (int(det[1]*hT)-h/2)
                bbox.append([x,y,w,h])
                confs.append(float(confidence))
                classIds.append(classId)

    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)  # to remove the overlapping boxes on same object
    print(len(indices))
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
        #print(x,y,w,h)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255),2)
        cv2.putText(img, f'{classesNames[classIds[i]].upper()} {int(confs[i]*100)}%',(x, y-10), cv2.FONT_HERSHEY_COMPLEX,
                    0.6, (255,0,255),2)


while True:
    _, img = vid.read()
    # direct image cant be sent to network, blob format is used
    blob = cv2.dnn.blobFromImage(img, 1/255, (whT,whT), [0,0,0],1,crop=False)
    net.setInput(blob)

    # extracting the names of output layers
    # .getUnconnectedOutLayers gives index(starting from 1) of output layers
    layerNames = net.getLayerNames()                   # all layers
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]
    # print(outputNames)
    outputs = net.forward(outputNames)
    # print(outputs[0].shape) # out of these 85, first five are centre-x,c-y,w,h,max probability.
    # print(outputs[1].shape) # rest 80 are the probability of the 80 classes
    # print(outputs[2].shape)

    findObjects(outputs, img)

    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
