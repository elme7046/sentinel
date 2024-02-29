import mailer
from facial_recog import recognitioncode
from facial_recog import database
import os
import sys
import threading

database.buildDatabase()
perInfo = "f"
perName = ""
while True:

    
    perInfo, perName = recognitioncode.recognition()
    print(perInfo,perName)
    if perInfo == 'f' and os.path.isfile('DBTrain.pkl'):
        pass
    elif perInfo == 'f' and not os.path.isfile('DBTrain.pkl'):
        database.buildDatabase()
    elif perInfo != 'f':
        #Whitelist

        subject = "Someone is at your door"
        body = perName + " is at your front door"
        recipients = ["mitc1520@kettering.edu"]
        os.system("python3.7 /home/senorita/sentinel/python3.7/TextToSpeech.py -script \"" + body + "\"")
        os.system("mpg123 ./goodput.mp3")
        #mailer.send_email(subject, body, recipients)
        print("Mail Sent")
        #database.buildDatabase()
    perInfo = "f"
    perName = ""
        
    
        
