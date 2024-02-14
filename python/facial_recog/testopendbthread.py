import cv2
import face_recognition as fr 
import pickle

DBEncodings = []
DBNames = []


with open('DBTrain.pkl','rb') as f:
    DBNames = pickle.load(f)
    DBEncodings = pickle.load(f)


font = cv2.FONT_HERSHEY_SIMPLEX

#cam = cv2.VideoCapture("rtsp://10.0.0.58:554")
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cam.set(cv2.CAP_PROP_BUFFERSIZE,1)
test = True
while True:
    ret, unknownIm = cam.read()
    unknownIm = cv2.resize(unknownIm,(0,0),fx=0.5,fy=0.5)
    imgRGB = cv2.cvtColor(unknownIm,cv2.COLOR_BGR2RGB)
    imgRGB = cv2.resize(imgRGB,(0,0),fx=0.25,fy=0.25)
    
    faceLoc = fr.face_locations(imgRGB,model='cnn')
    faceEncod = fr.face_encodings(imgRGB,faceLoc)

    for (top, right, bottom, left), faceEncod in zip(faceLoc,faceEncod):
        personName = 'Unknown Person'
        match = fr.compare_faces(DBEncodings,faceEncod)
        if True in match:
            match_idx = match.index(True)
            personName = DBNames[match_idx]

        left = left * 4
        top = top * 4
        bottom = bottom * 4
        right = right * 4

        newImg = cv2. rectangle(unknownIm,(left,top),(right,bottom),(0,0,255),2)
        newImg = cv2.putText(unknownIm,personName,(left,top-6),font,0.7,(0,255,255),2)
    unknownIm = cv2.resize(unknownIm,(0,0),fx=2,fy=2)
    cv2.imshow('img',unknownIm)
    cv2.moveWindow('img',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
