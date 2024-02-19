import cv2
import face_recognition as fr 
import pickle
import threading

DBEncodings = []
DBNames = []
personName = 'Unknown Person'
personInfo = 'u'


with open('DBTrain.pkl','rb') as f:
    DBNames = pickle.load(f)
    DBEncodings = pickle.load(f)


font = cv2.FONT_HERSHEY_SIMPLEX



test = True

def faceCheck(location,encoding):
    global DBNames,DBEncodings,personName,personInfo
    for (top, right, bottom, left), encoding in zip(location,encoding):
        match = fr.compare_faces(DBEncodings,encoding)
        if True in match:
            match_idx = match.index(True)
            personName = DBNames[match_idx]
            personName = personName.replace('_',' ')
            if personName[-1] == 'w':
                personInfo = personName[-1]
                personName = personName.replace('.w','')
            elif personName[-1] == 'k':
                personInfo = personName[-1]
                personName = personName.replace('.k','')
            elif personName[-1] == 'u':    
                personInfo = personName[-1]
                personName = personName.replace('.u','')
    pass
def recognition():
    counter = 0
    #cam = cv2.VideoCapture("rtsp://10.0.0.58:554")
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)    
    while True:
        ret, unknownIm = cam.read()
        unknownIm = cv2.resize(unknownIm,(0,0),fx=0.5,fy=0.5)
        imgRGB = cv2.cvtColor(unknownIm,cv2.COLOR_BGR2RGB)
        imgRGB = cv2.resize(imgRGB,(0,0),fx=0.25,fy=0.25)
        
        faceLoc = fr.face_locations(imgRGB,model='cnn')
        faceEncod = fr.face_encodings(imgRGB,faceLoc)

        if counter % 30 == 0:
            try:
                threading.Thread(target=faceCheck,args=(faceLoc,faceEncod)).start()
            except ValueError:
                pass
        counter += 1


        for (top, right, bottom, left) in faceLoc:
            left = left * 4
            top = top * 4
            bottom = bottom * 4
            right = right * 4
            if DBNames != []:
                if personInfo == 'w':
                    cam.release()
                    cv2.destroyAllWindows()      
                    return personInfo, personName  
                            
                elif personInfo == 'k':
                    cv2.rectangle(unknownIm,(left,top),(right,bottom),(0,255,0),2)
                    cv2.putText(unknownIm,personName,(left,top-6),font,0.7,(0,255,255),2) 
                    #EMAIL with timeout
                    
                elif personInfo == 'u':
                    cv2.rectangle(unknownIm,(left,top),(right,bottom),(0,0,255),2)
                    cv2.putText(unknownIm,personName,(left,top-6),font,0.7,(0,255,255),2) 
            else:
                cv2.rectangle(unknownIm,(left,top),(right,bottom),(0,0,255),2)
                cv2.putText(unknownIm,'Initialize Database!',(left,top-6),font,0.7,(0,255,255),2)           


        unknownIm = cv2.resize(unknownIm,(0,0),fx=2,fy=2)
        cv2.imshow('img',unknownIm)
        cv2.moveWindow('img',0,0)
        if cv2.waitKey(1)==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
