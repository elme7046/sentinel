import cv2

detector=cv2.CascadeClassifier('/home/senor/Documents/Sentinel1.0/sentinel/python/facial_recog/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('rtsp://10.0.0.58:554')
#cap = cv2.VideoCapture(0)
txtFont = cv2.FONT_HERSHEY_SIMPLEX

while(True):

  ret,img = cap.read()
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces = detector.detectMultiScale(gray,1.3,5)
  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img,'Person',(x,y+h+25),txtFont,1,(0,255,0),2)
  cv2.imshow('capture',img)
  key = cv2.waitKey(1)
  if key == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()