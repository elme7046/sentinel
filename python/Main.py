import mailer
from facial_recog import testopendbthread
from facial_recog import database


while True:

    print("Please wait while database is being built/rebuilt")
    database.buildDatabase()
    perInfo, perName = testopendbthread.recognition()
    if perInfo != '':
        subject = "Someone is at your door"
        body = perName + " is at your front door"
        recipients = ["mitc1520@kettering.edu"]
        mailer.send_email(subject, body, recipients)
        
