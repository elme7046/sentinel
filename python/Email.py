from email.message import EmailMessage
import smtplib
from email.mime.text import MIMEText
import sys

subject = ""
recipients = []
body = ""	
file = ""
for i in range(1, len(sys.argv)-1):
	if(sys.argv[i] == "-s"):
		subject = sys.argv[i+1]
	elif(sys.argv[i] == "-r"):
		recipients.append(sys.argv[i+1])
	elif(sys.argv[i] == "-b"):
		body = sys.argv[i+1]
	elif(sys.argv[i] == "-f"):
		file = sys.argv[i+1]
	else:
		pass

#body = "https://forums.developer.nvidia.com/c/agx-autonomous-machines/jetson-embedded-systems/70"
sender = "sentinel.homeguard@gmail.com"
password = "wjgm admi grgi rxwr"

def send_email(subject, body, sender, recipients, password, file=None):
	msg = EmailMessage()
	msg.set_content(body)
	msg["Subject"] = subject
	msg["From"] = sender
	msg["To"] = ", ".join(recipients)
	if(file != None):
		with open(file, 'rb') as fp:
			img_data = fp.read()
		msg.add_attachment(img_data, maintype='image',
									subtype='png')
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
		smtp_server.login(sender, password)
		smtp_server.sendmail(sender, recipients, msg.as_string())
	print("Message sent!")
	
send_email(subject, body, sender, recipients, password, file)