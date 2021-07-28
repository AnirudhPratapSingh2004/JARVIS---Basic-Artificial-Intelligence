import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import pyjokes
from requests import get
import cv2
import requests
from bs4 import BeautifulSoup
import speedtest
import operator
import pyautogui
import pywhatkit
from pytz import timezone
import keyboard
from PyDictionary import PyDictionary as dict
import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I Am Jarvis, How May I Help You")

def takecommand():
    # It Takes Microphone Input From The User And Returns String Output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say That Again Please...")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aditisingh14205@gmail.com', 'pass@2020')
    server.sendmail('aditisingh14205@gmail.com', to, content)
    server.close()


def screenshot():
    speak("Ok Sir , What Should I Name This File ?")
    path = takecommand()
    path1name = path + ".jpg"
    path1 = "C:\\SCREEN SHOTS"+ path1name
    kk = pyautogui.screenshot()
    kk.save (path1)
    os.startfile("C:\\SCREEN SHOTS")
    speak("Here Is Your ScreenShot")
 


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        # Logic For Executing Tasks Based On Query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            url = 'youtube.com'
            chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)

        elif 'open the flawless' in query:
            speak("OK Sir, This Is What I Found For Your Search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=The+Flawless'
            webbrowser.open(web)
            speak("Done Sir")

        elif 'open ocean of games' in query:
            speak("ok sir, opening your website")
            oceanofgames = 'https://oceansofgamess.com/'
            webbrowser.open(oceanofgames)   


        elif 'open google' in query:
            speak("ok sir, opening google")
            google = 'google.com'
            chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)

        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir, rd))

             
        elif 'set alarm' in query:
            speak("Sir, please tell me the time to set alarm")
            time = takecommand()

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time To Wake Up Sir")
                    playsound('Ultra Instinct Goku.mp3')
                    speak("Alarm Closed")

                elif now>time:
                   break   
                

        elif 'the time' in query:
            ind_time = datetime.datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
            print(ind_time)
            speak(f"Sir, The Time Is {ind_time}s")

        elif 'open vs code' in query:
            codepath = "C:\\Users\\ANIRUDH PRATAP SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open notepad' in query:
            notepath = "C:\\Windows\\system32\\notepad"
            os.startfile(notepath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open this pc' in query:
            os.system("start This PC")    

        elif 'open control panel' in query:
            os.system("start control panel")

        elif 'open epic games' in query:
            epicgameslauncher = "C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher"
            os.startfile(epicgameslauncher)

        elif 'play songs on youtube' in query:
            speak("what song should i play sir ?")
            cm = takecommand().lower()
            pywhatkit.playonyt(f"{cm}")
            speak("enjoy sir")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"sir, your ip address is {ip}")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'take screenshot' in query:

            screenshot()    

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'send whatsapp message' in query:
            pywhatkit.sendwhatmsg("+918800664538", "hi anirudh", 2, 33)

        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'volume up' in query:
            pyautogui.press("volume up")

        elif 'volume down' in query:
            pyautogui.press("volume down")       

        elif 'temperature' in query:
            search = "temperature in gurugram"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(temp)

        elif 'can you calculate' in query:
            r = sr.Recognizer()
            with sr.Microphone()as source:
                speak("Sir, what you wanted to calculate ?")
                print("Listenning")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add, # Addition
                    '-' : operator.sub, # Subtraction
                    'x' : operator.mul, # Multiply
                    'divided' :operator.__truediv__, # Division
                    }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
            print(speak)            

        elif 'internet speed' in query:

            try:
                os.system('cmd /k "speedtest"')
                speak(audio)
            except:
                speak("sorry i am not able to find your internet speed")   

        elif 'email to papa' in query:
            try:
                speak("What Should I Say Sir ?")
                content = takecommand().lower()
                to = "chandrasingh0804@gmail.com"
                sendEmail(to, content)
                speak("Your Email Has Been Sent !")

            except Exception as e:
                print(e)
                speak("Sorry Sir, Your Email Has Not Been Sent !")

        elif 'email to mom' in query:
            try:
                speak("What Should I Say Sir ?")
                content = takecommand().lower()
                to = "nishacpsc@gmail.com"
                sendEmail(to, content)
                speak("Your Email Has Been Sent !")

            except Exception as e:
                print(e)
                speak("Sorry Sir, Your Email Has Not Been Sent !")


        # Interactions With Jarvis    
        elif 'hi jarvis' in query:
            speak("hi sir")

        elif 'how are you jarvis' in query:
            speak("im fine sir, what about you ?")

        elif 'i am good' in query or 'i am also fine' in query:
            speak("that's a good thing sir !")

        elif 'are you a human' in query:
            speak("no sir, i'm not human, i'm your artificial intelligence assistant")

        elif 'what are you' in query:
            speak("i'm an artificial intelligence assistant")

        elif 'badhiya bhai' in query:
            speak("haa bhai")                               


        # To Close Any Application

        elif 'close notepad' in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'close command prompt' in query:
            speak("okay sir, closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif 'close youtube' in query:
            speak("okay sir, closing youtube")
            os.system("taskkill /f /im chrome.exe")

        elif 'close google' in query:
            speak("okay sir, closing google")
            os.system("taskkill /f /im chrome.exe")        

        elif 'close control panel' in query:
            os.system("taskkill /f /im ControlPanel.Ink")

        elif 'close vs code' in query:
            speak("okay sir, closing vs code")
            os.system("taskkill /f /im code.exe")    

        elif 'stop playing music' in query:
            os.system("taskkill /f /im GrooveMusic.exe")       

        # To Get Jokes

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke(language='en')
            speak(joke)

        elif 'shutdown' in query:
            speak('thanks for using me sir')
            sys.exit(1)

        elif 'pause' in query:
            keyboard.press("spacebar")

        elif 'play' in query:
            keyboard.press("spacebar")

        elif 'full screen' in query:
            keyboard.press("f")

        elif 'cinema mode' in query:
            keyboard.press("t")

        elif 'skip' in query:
            keyboard.press("1")

        elif 'open new window' in query:
            keyboard.press_and_release("ctrl + n")

        elif 'open new tab' in query:
            keyboard.press_and_release("ctrl + t")

        elif 'open history' in query:
            keyboard.press_and_release("ctrl + h")

        elif 'open downloads' in query:
            keyboard.press_and_release("ctrl + j")

        elif 'repeat my words' in query:
            speak("start speaking sir !")
            jj = takecommand()
            speak(f"you said : {jj}")

        elif 'open dictionary' in query:
            speak("Tell Me The Problem Sir !")
            prob1 = takecommand()

            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("jarvis","")
            prob1 = prob1.replace("of","")
            prob1 = prob1.replace("meaning of","")
            result = dict.meaning(prob1)
            print(result)
            speak(f"The Meaning For {prob1} is {result}") 
                                                        