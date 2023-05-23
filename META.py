import pyttsx3 
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib  
import sys
import pyautogui
from pynput.keyboard import Key , Controller
import time
import winsound
import cv2
import pyjokes


keyboard=Controller()


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",200)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#to convert text to speech
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=0.5)
        audio=r.listen(source)
    
    try:
        print("recognizing....")
        query=r.recognize_google(audio)
        print(f"user said: {query}\n")
    except Exception as e:
        print("repeat please")
        speak("repeat please")
        query=None
    return query
        
#to wish
def wishme():
    hour=int (datetime.datetime.now().hour)
    
    tt=time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"good morning, its {tt}")
    elif hour>=12 and hour<18:
        speak(f"good afternoon , its{tt}")
    else:
        speak(f"good evening, its {tt}")
    speak(" this is meta , how can i help you")
    #def sendemail
def sendemail(to,content):
        
        server=smtplib.SMTP("smtp.gmail.com",587,timeout=120)
        server.ehlo()
        server.starttls()  #to start email
        server.login("prims0509@gmail.com","Abcd@123")
        print("login success")
        server.sendmail('prims0508@gmail.com',to,content)
        server.close()

def send_whatsapp_message(msg: str):
    try:
        kit.sendwhatmsg_instantly(
            phone_no="+917587168936", 
            message=msg,
            tab_close=True
        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))  


def alarm(Timing):
    altime= str(datetime.datetime.now().strptime(Timing,"%H:%M %p"))

    altime=altime[11:-3]
    
    horeal=altime[:2]
    horeal=int(horeal)
    mireal=altime[3:5] 
    mireal=int(mireal)
    print(f"done ,alarm is set for {Timing}")
    while True:
        if horeal==datetime.datetime.now().hour:
            if mireal==datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif mireal<datetime.datetime.now().minute:
                break    

   




if __name__=="__main__" :
    wishme()
    
    while True:
        query=takecommand()
        if "notepad" in query:
            npath="C:\\Windows\\System32\\notepad.exe"

            os.startfile(npath)
            

            speak("opening notepad..")
        
        elif 'the time' in query.lower():
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {strtime}\n")
        elif "close notepad" in query.lower():
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")

        
        
        elif 'wikipedia' in query.lower() :
            speak('searching wikipedia..')
            query=query.replace('wikipedia','')
            result= wikipedia.summary(query,sentences=1)
            speak("according to wikipedia")
            speak(result)
            print(result)
        elif ' chrome' in query.lower():
            webbrowser.open("google.com")

        elif 'play' in query:
            song=query.replace('play','')
            speak('playing'+ song)
            kit.playonyt(song)
        elif 'college website' in query.lower():
             webbrowser.open("www.bitdurg.ac.in")

        elif 'open facebook' in query.lower():
            webbrowser.open("www.facebook.com")


        
        elif("open Google") in query.lower():
            speak("what should i search on google")
            cm=takecommand().lower()
            webbrowser.open("{cm}")

        elif 'how are you' in query:
            speak('im great, how about you')
        elif 'i am fine' in query.lower():
            speak('what can i do for you ')
        elif "tell me about yourself" in query.lower():
            speak("Im META,an artificial intelligence base voice assistant ,created by students of 3rd sem b I T durg capable of executing user commands ")
        elif "tell me a joke" in query.lower():
            joke=pyjokes.get_joke()
            speak(joke)
        
        
        elif 'date' in query:
            date=datetime.datetime.now().strftime('%d/%m/%y')
            speak( 'todays date  ' + date)
            print(date)

        elif 'send message' in query.lower():
            speak("what should i send ")
            msg=takecommand().lower()
            send_whatsapp_message(msg)
            speak("message sent successfully")
        
        elif 'weather' in query.lower():
            target="weather"
            kit.search(target)
            print("Searching...")

        elif 'news ' in query.lower():

            target1="news"
            kit.search(target1)
            print('searching')

        elif 'alarm' in query.lower():
            speak("please tell me the time to set alarm for example, set alarm at 5:30 am ")
            tt=takecommand() #set alarm to 5:30 am
            tt=tt.replace("set alarm at","") # 5:30am
            tt=tt.upper() #5:30AM
            alarm(tt)

        elif 'send email' in query.lower():
            try:
                speak("what should i send")
                content=takecommand().lower()
                to = "samruddhimetkar15@gmail.com"
                sendemail(to,content)
                speak("email has been sent to samruddhi")

            except Exception as e:
                print(e)
                speak("sorry problem in sending email")
        

        elif "switch window" in query.lower():
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif 'no thanks' in query:
            speak("thankyou for using me")
            sys.exit()

        elif 'bye' in query:
            speak("closing meta, bye")
            sys.exit()
        speak("do you have any other work")


            


 
            
        


        

    






         


    

