import pyttsx3
import datetime
import os 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("C:\\Irfan-Projects\\SARA-Ai\\Sara-Main\\Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("C:\\Irfan-Projects\\SARA-Ai\\Sara-Main\\Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("sara","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak(" Your Alarm is ringing sir")
            os.startfile("C:\\Irfan-Projects\\SARA-Ai\\Sara-Main\\music.mp3") 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)
