import os
import requests,json
import pyttsx3
import speech_recognition as ss
import pyjokes
def takeQuery():
    try:
        sr = ss.Recognizer()                         ##this will return an object of class Recognizer
        sr.pause_threshold = 1                      ##this gap
        #print("speak")
        with ss.Microphone() as m:                   ##we are getting microphone object and returns an object of class AudioData
            sr.adjust_for_ambient_noise(m)
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='en-IN')
            return query
    except Exception:
        return "Error! Some problem with device!"

def weather(city):
    url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='+city
    response=requests.get(url)
    res=response.json()
    print(response)
    print(res)


pyttsx3.speak("Hello! My name is Aude, your personal assistant")
print("1. Speech\n2. Text")
pyttsx3.speak("to give me command select an input method")
n=int(input())
if n==2:
    print("What can I do for you?",end=": ")
    s=input()
    
else:
    pyttsx3.speak("Speak now")
    print("Speak now")
    s=takeQuery()

while(True):
        #print(s)
        l=s.split()
        if "Error" in s:
            pyttsx3.speak("Sorry! Some error occurred. please try again")
        elif s=="":
            pyttsx3.speak("Say Again!Speech not recognized!")
        elif "open" in l:
            x=l[l.index('open')+1]
            pyttsx3.speak("Opening"+x+"for you")
            r=os.system(x)
            if r==1:
                pyttsx3.speak("please enter valid application name")
        elif "videos" in l or "video" in l or "YouTube" in l:
            pyttsx3.speak("Opening youtube for you")
            pyttsx3.speak("press enter to continue")
            os.system("start chrome youtube.com")
            input()
        elif "linkedin" in l or "LinkedIn" in l:
            pyttsx3.speak("Opening linkedin for you")
            pyttsx3.speak("press enter to continue")
            os.system("start chrome linkedin.com")
            input()
        elif "facebook" in l or "Facebook" in l:
            pyttsx3.speak("Opening facebook for you")
            pyttsx3.speak("press enter to continue")
            os.system("start chrome facebook.com")
            input()
        elif "search" in l or "google" in l:
            pyttsx3.speak("please enter search query")
            if n==1:
                q=takeQuery()
            else:
                q=input()
            pyttsx3.speak("Opening google chrome for you")
            pyttsx3.speak("press enter to continue")
            os.system("start chrome https://www.google.com/search?q="+q)
            input()
        elif "google" in l:
            pyttsx3.speak("Opening google for you")
            pyttsx3.speak("press enter to continue")
            os.system("start chrome google.co.in")
            input()
        elif "Gmail" in l or "mail" in l:
            pyttsx3.speak("Opening gmail for you")
            pyttsx3.speak("press enter to continue")
            os.system("start chrome gmail.com")
            input()
        elif "joke" in l or "jokes" in l:
            joke=pyjokes.get_joke()
            print(joke)
            pyttsx3.speak(joke)
        elif "repeat" in l or "say again" in s or "come again" in s:
            print(joke)
            pyttsx3.speak(joke)
        elif "end" in l or "exit" in l or "goodbye" in l or "standby" in l:
            pyttsx3.speak("going for a nap! good bye!")
            break
        else:
            pyttsx3.speak("Sorry! could not understand. please try again")
        if n==1:
            pyttsx3.speak("Speak now")
            print("Speak now")
            s=takeQuery()
        else:
            print("What can I do for you?",end=": ")
            s=input()
