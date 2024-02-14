#Used With Face Recognition

import cv2
import face_recognition as fr  
import pickle

#cam = cv2.VideoCapture('rtsp://192.168.1.3:554')
cam = cv2.VideoCapture("rtsp://10.0.0.58:554")
#cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cam.set(cv2.CAP_PROP_BUFFERSIZE,1)
test = True

while True:

    ret, img = cam.read()
    imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    if test:
        imgrgb = cv2.resize(imgrgb,(0,0),fx=0.20,fy=0.20)
        facelocs = fr.face_locations(imgrgb,model="cnn")

        for(top,right,bottom,left) in facelocs:
            top *= 5
            right *= 5
            bottom *= 5
            left *= 5
            img = cv2.rectangle(img,(left,top),(right,bottom),(0,0,255),2)
    test = not test
    cv2.imshow('facewin',img)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
