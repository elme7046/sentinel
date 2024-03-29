import sys
import os

if(sys.version[:5] != "3.7.5"):
    print("Using wrong python version!")
    exit()

from pathlib import Path
from openai import OpenAI

script = "placeholder script in case something goes wrong"
for i in range(1, len(sys.argv)-1):
	if(sys.argv[i] == "-script"):
		script = sys.argv[i+1]
	else:
		pass

if(type(script) != str):
	script = "script was not a string, so I changed it to a string"

client = OpenAI()

speech_file_path = Path("/home/senor/Documents/Sentinel1.0/sentinel/python/speaker/goodput.mp3").parent
response = client.audio.speech.create(model="tts-1", voice="alloy", input=script)

response.stream_to_file("./goodput.mp3")
os.system("mpg123 ./goodput.mp3")

