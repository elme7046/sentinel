import cv2
import face_recognition as fr 
import pickle
import os
import threading
import datetime
import time
import mailer
import datetime
from facial_recog import database

DBEncodings = []
DBNames = []
personName = 'Unknown Person'
personInfo = 'u'

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
        else:
            personInfo = 'u'
            personName = 'Unknown Person'
    pass
def recognition():
    global DBNames, DBEncodings,personInfo,personName
    counter = 0
    empty_time = time.time()
    known_time = time.time()
    unknown_time = time.time()
    personName = 'Unknown Person'
    personInfo = 'u'

    known_email_timeout = False
    unknown_email_timeout = False
    known_persons = []
    unknown_persons = []
    known_timeout = 0


    if os.path.isfile('DBTrain.pkl'):
        with open('DBTrain.pkl','rb') as f:
            DBNames = pickle.load(f)
            DBEncodings = pickle.load(f)
    #cam = cv2.VideoCapture('rtsp://192.168.1.3:554') #School router
    #cam = cv2.VideoCapture("rtsp://10.0.0.58:554") #Home router
    #cam = cv2.VideoCapture("rtsp://172.20.10.5:554") #Stephen's hotspot
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)    
    while True:
        ret, unknownIm = cam.read()
        unknownIm = cv2.resize(unknownIm,(0,0),fx=0.75,fy=0.75)
        imgRGB = cv2.cvtColor(unknownIm,cv2.COLOR_BGR2RGB)
        imgRGB = cv2.resize(imgRGB,(0,0),fx=0.25,fy=0.25)
        
        faceLoc = fr.face_locations(imgRGB,model='cnn')
        faceEncod = fr.face_encodings(imgRGB,faceLoc)

       #if counter % 30 == 0:
        try:
            threading.Thread(target=faceCheck,args=(faceLoc,faceEncod)).start()
        except ValueError:
            pass
        #counter += 1


        for (top, right, bottom, left) in faceLoc:
            left = left * 4
            top = top * 4
            bottom = bottom * 4
            right = right * 4
            if DBNames != []:
                if personInfo == 'w':
                    #cv2.rectangle(unknownIm,(left,top),(right,bottom),(0,255,0),2)
                    #cv2.putText(unknownIm,personName,(left,top-6),font,0.7,(0,255,255),2) 
                    
                    cam.release()
                    cv2.destroyAllWindows()      
                    return personInfo, personName  
                        
                elif personInfo == 'k':
                    cv2.rectangle(unknownIm,(left,top),(right,bottom),(0,255,0),2)
                    cv2.putText(unknownIm,personName,(left,top-6),font,0.7,(0,255,255),2) 
                    known_persons.append(personName)
                elif personInfo == 'u':
                    cv2.rectangle(unknownIm,(left,top),(right,bottom),(0,0,255),2)
                    cv2.putText(unknownIm,personName,(left,top-6),font,0.7,(0,255,255),2)
                    unknown_persons.append(personName)


            else:
                cv2.rectangle(unknownIm,(left,top),(right,bottom),(0,0,255),2)
                cv2.putText(unknownIm,'Initialize Database!',(left,top-6),font,0.7,(0,255,255),2)

        #TODO timeout when no face 
        if(known_email_timeout == False):
            if(len(known_persons) > 0):
                print("email known")
                known_email_timeout = True
                known_time = time.time()
                unknown_time = time.time()
        else:
            t = time.time() - known_time
            if(len(known_persons) == 0):
                if(t > 10):
                    known_time = time.time()
                    known_email_timeout = False
            else:
                if(t > 900):
                    known_time = time.time()
                    known_email_timeout = False

        if(len(known_persons) == 0):
            if(len(unknown_persons) > 0):
                if(unknown_email_timeout == False):
                    temp, betterimg = cam.read()
                    if os.path.isfile('DBTrain.pkl'):
                        cT = datetime.datetime.now()
                        imName = "Unknown_Person_" + cT.strftime("%Y_%m_%d_%H_%M.") + "u.png"
                        path = '/home/senorita/Documents/sentinel/sentinel/python/sentinel_database'
                        cv2.imwrite(os.path.join(path,imName),betterimg)
                        database.appendDatabase(os.path.join(path,imName),imName)
                    print("email unknown")
                    unknown_time = time.time()
                    unknown_email_timeout = True
                else:
                    t = time.time() - unknown_time
                    if(t > 900):
                        unknown_time = time.time()
                        unknown_email_timeout = False
            else:
                pass
        else:
            unknown_time = time.time()
        known_persons = []
        unknown_persons = []
                



        unknownIm = cv2.resize(unknownIm,(0,0),fx=2,fy=2)
        cv2.imshow('img',unknownIm)
        cv2.moveWindow('img',0,0)
        if cv2.waitKey(1)==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
