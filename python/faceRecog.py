import face_recognition as fr
import cv2

cam = cv2.VideoCapture(0)
count = 0
faceLocs = [(0, 0, 0, 0)]
countIndex = 0
while(True):
    ret,Img = cam.read()
    Img = cv2.resize(Img, (0, 0), fx=0.25, fy=0.25)
    ImgRGB = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)

    count += 1
    
    if(count >= 10):
        faceLocs = fr.face_locations(ImgRGB)
        cv2.imwrite('opencv' + str(countIndex)+'.png', Img)
        count = 0
        countIndex += 1
    
    for (top, right, bottom, left) in faceLocs:
        Img = cv2.rectangle(Img, (left, top), (right, bottom), (0, 0, 255), 2)
        

    cv2.imshow('faceWin', Img)
    cv2.moveWindow('faceWin', 10, 10)
    if(cv2.waitKey(1) == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()