import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import smtplib
import random
import pyjokes
import urllib.parse
from wikipedia.wikipedia import search

# set voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# Creating a speak function to speak data
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Creating wishme function to greeting user
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hy, I am Jarvis your assistant.")

def takeCommand():
    # it take microphone input from the user and return strings output
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query} \n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    
    return query
def sendEmail(to,contant):
    server = smtplib.SMTP('smtp.google.com',587)
    server.ehlo()
    server.starttls()
    server.login("yourgmail@gmail.com","yourpassword")
    server.sendmail('yourgmail@gmail.com',to,contant)
    server.close()

# main function
if __name__ == "__main__":
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('chrome_path'))
    WishMe()
    speak("what's your name")
    name = takeCommand().lower()
    speak(f"Hello,{name} how may i help you")
    
    
    while True:
        query = takeCommand().lower()

        # logic for executing task based on query
        if 'what is your owner name' in query:
            print(f"My owner name is {name}")
            speak(f"My owner name is {name}")

        elif 'how are you' in query:
            print("Fine. How are you !")
            speak("fine. How are you")

        elif 'fine' in query:
            print("that's great!. How may i help you")
            speak("that's great how may i help you")

        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab("youtube.com")
            exit()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab("google.com")
            exit()

        elif 'open my portfolio site' in query:
            webbrowser.get('chrome').open_new_tab("palashcv.ml")
            exit()

        elif 'play music' in query:
            music_dir = 'music folder path'
            songs = os.listdir(music_dir)
            ran = random.choice(songs)
            index = songs.index(ran)
            os.startfile(os.path.join(music_dir,songs[index]))
            exit()

        elif 'play movie' in query:
            movie_dir = 'movie folder path'
            movies = os.listdir(movie_dir)
            ran = random.choice(movies)
            index = movies.index(ran)
            os.startfile(os.path.join(movie_dir,movies[index]))
            exit()

        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir the time is {strTime}")
            speak(f"sir the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "vs code path"
            os.startfile(codePath)
            exit()

        elif 'send mail to palash' in query:
            try:
                print("whats should i say?")
                speak("whats should i say?")
                contant = takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to,contant)
                print("Email has been Send!")
                speak("Email has been Send!")

            except Exception as e: 
                print(e)
                speak("Email sending fali")
                exit()

        elif 'alarm' in query:
            os.system('cmd /k "explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App"')
            exit()

        elif 'joke' in query:
            for i in range(5):
                print(pyjokes.get_jokes()[i])
                speak(pyjokes.get_jokes()[i])

        elif 'search youtube' in query:
            speak("What do you want to search on youtube?")
            print("What do you want to search on youtube?")
            text = takeCommand()
            query = urllib.parse.quote(text)
            url = "https://www.youtube.com/results?search_query=" + query
            webbrowser.get('chrome').open_new_tab(url)
            exit()

        elif 'location' in query:
            speak("What is your location?")
            location = takeCommand()
            url = 'https://google.nl/maps/place/'+location+'/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location'+location)
            exit()

        elif 'shutdown' in query:
            os.system('shutdown /p /f')
        
        elif 'search' in query:
            speak('what do you want to search for ?')
            search = takeCommand()
            url = 'https://google.com/search?q='+search
            webbrowser.get('chrome').open_new_tab(url)
            speak('here is what I found for '+search)
            exit()
        
        elif 'close' in query:
            exit()