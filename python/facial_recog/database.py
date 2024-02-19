import cv2
import face_recognition as fr  
import os
import pickle


def buildDatabase():
    DBEncodings = []
    DBNames = []
    DBdir = os.getcwd() + '/python/facial_recog/images'
    for root, dirs, files, in os.walk(DBdir):
        for file in files:
            fullfileName = os.path.join(root,file)
            personImg = fr.load_image_file(fullfileName)
            personEncoding = fr.face_encodings(personImg,model='cnn')[0]
            DBEncodings.append(personEncoding)

            personName = os.path.splitext(file)[0]
            DBNames.append(personName)

        print(DBNames)

    with open('DBTrain.pkl','wb') as f:
        pickle.dump(DBNames,f)
        pickle.dump(DBEncodings,f)