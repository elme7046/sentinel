import cv2
import face_recognition as fr  
import os
import pickle


def buildDatabase():
    DBEncodings = []
    DBNames = []
    DBdir = '/home/senorita/Documents/sentinel/sentinel/python/sentinel_database'
    for root, dirs, files, in os.walk(DBdir):
        for name in files:
            if '.png' in name and name != 'default.png' and '.u' not in name:
                print(name)
                fullfileName = os.path.join(root,name)
                personImg = fr.load_image_file(fullfileName)
                personEncoding = fr.face_encodings(personImg,model='large')[0]
                DBEncodings.append(personEncoding)

                personName = os.path.splitext(name)[0]
                DBNames.append(personName)

    
    print(DBNames)

    with open('DBTrain.pkl','wb') as f:
        pickle.dump(DBNames,f)
        pickle.dump(DBEncodings,f)



def appendDatabase(imagePath,name):
    DBEncodings = []
    DBNames = []
    if os.path.isfile('DBTrain.pkl'):
        with open('DBTrain.pkl','rb') as f:
            DBNames = pickle.load(f)
            DBEncodings = pickle.load(f)
    personImg = fr.load_image_file(imagePath)
    personEncoding = fr.face_encodings(personImg,model='large')
    DBEncodings.append(personEncoding)
    personName = os.path.splitext(name)[0]
    DBNames.append(personName)
    with open ('DBTrain.pkl','wb') as f:
        pickle.dump(DBNames,f)
        pickle.dump(DBEncodings,f)
