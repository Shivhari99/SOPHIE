import numpy
import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import pyaudio
import subprocess
import pyjokes 
from playsound import playsound
import keyboard
from tkinter import *
import wikipedia
import webbrowser
import os
import smtplib
import socket
name_assistant = "SOPHIE"
socket.getaddrinfo('localhost', 8080)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning!")

    elif hour >= 12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")

    speak("I am SOPHIE one point O, SOPHIE stands for Series One Processor Hyper Intelligent Encrypter, Please tell me how may I assist you")

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def takeCommand():
    '''
    it takes microphone input from the user and gives string output.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtplib.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('tewariaman1899@gmail.com','Shivhari@99')
    server.sendmail('tewarisaman1899@gmail.com',to,content)
    server.close()

def change_name():
    pass

def change():
    pass

def info():
    pass
def main_screen():

    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("100x250")
    screen.iconbitmap('app_icon.ico')


    name_label = Label(text = name_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
    name_label.pack()


    microphone_photo = PhotoImage(file = "E:\\virtual_assistant.png")
    microphone_button = Button(image=microphone_photo, command = takeCommand)
    microphone_button.pack(pady=10)    
    
if __name__=="__main__":
    wishMe()
    query = takeCommand().lower()

if 'wikipedia' in query:
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences= 10)
    speak("According to wikipedia")
    speak(results)
if 'note this' in query:    
    statement = query.replace("note this", "")
    note(statement) 
if 'joke' in query:
    speak(pyjokes.get_joke())

elif 'open youtube' in query:
    webbrowser.open("https://www.youtube.com/")
elif'will you marry me' in query:
    speak('we are not allowed to marry our creators, I am trying on Siri hahaha')
elif 'what do you look like' in query:
    speak('What do you think I look like, a beautiful woman !!!')
elif 'do you love me' in query:
    speak('I love every creation of GOD, of course I love you !!!')
elif 'open google' in query:
    webbrowser.open("https://www.google.co.in/")
elif 'open stack overflow' in query:
    webbrowser.open("https://stackoverflow.com/")
elif 'open amazon' in query:
    webbrowser.open("https://www.amazon.in/")
elif 'the date' in query:
    today = date.today()
    strDate = today.strftime("%d/%m/%Y")
    speak(f"Sir, the date is{strDate}")
elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the Time is{strTime}")
elif 'open maps' in query:
    webbrowser.open("https://www.google.com/maps")

elif 'open code' in query:
    codePath = "C:\\Users\\tewar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))
elif 'i am worried' in query:
    webbrowser.open("https://www.youtube.com/watch?v=zSioX0v5iPQ")

elif 'open Gmail' in query:
    webbrowser.open("gmail.com")

elif 'send email' in query:
    try:
        speak("What should I say?")
        content = takeCommand()
        to = "tewarishivhari999@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent")
    except Exception as e:
        print(e)
        speak("Sorry Sir, I can't send this email at the moment ")
elif 'thank you' in query:
    speak("always at your service SIR")
