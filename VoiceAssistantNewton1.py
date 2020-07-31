import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):	
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir! I am Newton2.0, How may I help you?")

def takeCommand():
#it takes input from microphone and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_treshhold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again Please.")
        return "None"
    return query

def sendMail(to,content):
    server = smtplib.SMTP('smtp.live.com',400)
    server.ehlo()
    server.starttls()
    server.login('sender_id@hotmail.com','password')
    server.sendmail('sender_id@hotmail.com', to, content)
    server.close()




if __name__=='__main__':
    #speak("Ananya is a good girl.")
    wishme()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks as per "query".
        if 'wikipedia' in query:
            print("Searching in Wikipedia........")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Please wait! I'm opening YouTube.com")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("Please wait! I'm opening Google.com")
            webbrowser.open("https://www.google.com")
        elif 'open stackoverflow' in query:
            speak("Please wait! I'm opening Stackoverflow")
            webbrowser.open("https://www.stackoverflow.com")
        elif 'play music' in query:
            music_dir ='D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[2]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! the time is {strTime}")
        elif 'mail to sanjiv' in query:
            speak("What I've to say?")
            content = takeCommand()
            to = 'reciver_id@gmail.com'
            sendMail(to,content)
            speak("Email has been send.")







