import speech_recognition as sr
from gtts import gTTS
import time
import os
import new
import pyowm
from datetime import datetime
r=sr.Recognizer()
mic=sr.Microphone()
def weather():
    owm = pyowm.OWM('3b8dc8474c4fdddfea2631f41f134a97')  
    obs = owm.weather_at_place("Chennai,in")  
    temperature=obs.get_weather().get_temperature('celsius')
    speak("The temperature is")
    speak(str(temperature['temp_max']))
    speak('celsius')
def news():
    new.ne()
    file=open('news.txt','r')
    for i in range(1,5):
            speak(file.readline())
    os.remove('news.txt')
def speak(s):
    tts=gTTS(text=s,lang='en')
    tts.save('temp.mp3')
    os.system('mpg321 -q temp.mp3')
    os.remove('temp.mp3')
def callback():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        os.system('clear')
        print("\t\t\t\t\t\tSpeak Now")
        os.system('mpg321 -q Notification.mp3')
        audio=r.listen(source)
    try:
        return(str.lower(str(r.recognize_google(audio))))
    except sr.UnknownValueError:
        print("Error")

if __name__=="__main__":
    os.system('cls')
    while(callback()=='jarvis'):
        print("\n \t\t\t\t\t\t\tWelcome  \n \t\t\t\t\t\t\tWhat can i do for you?\n \t\t\t\t\t\t\tThese are the things i can do for you\n \t\t\t\t\t\t1.Repeat \n \t\t\t\t\t\t2.Time\n \t\t\t\t\t\t3.Date\n \t\t\t\t\t\t4.Weather\n \t\t\t\t\t\t5.News\n ")
        speak('welcome  what can i do for you')
        speak(' Repeat')
        speak(' Time')
        speak(' Date')
        speak('Weather')
        speak(' News')
        case=callback()
        print "\t\t\t\t\t\tThis is what you said : " + case
        if(case=='time'):
            speak(time.strftime("%H:%M:%S\n"))
        elif(case=='date'):
            speak(time.strftime("%d:%m:%y\n"))
        elif(case=='repeat'):
            print("Say Now")
            print(callback()+'\n')
        elif(case=='good bye'or case=='goodbye'):
            print('good bye')
            speak('good bye')
            exit()
        elif(case=='weather'or case=='Weather'):
            weather()
        elif(case=='news'):
            news()
        else:
            print("Good Bye !")
            speak('goodbye')
            exit()
