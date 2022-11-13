# Importing Modules
import win32com.client as wincl
import datetime
import smtplib
import os
import webbrowser
import wikipedia
import speech_recognition as sr


# creating Function
def speak(text):
     speak = wincl.Dispatch("SAPI.SpVoice")
     speak.Speak(text)
     
def wishme():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morning!")
     elif hour == 12:
          speak("Good Noon!")
     elif hour>=12 and hour<18:
          speak("Good Afternoon!")
     else:
          speak("Good Evening!")
     speak("Hello my name is Hach It, How may I help you?")
     
def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("listening.....")
          r.pause_threshold = 1
          audio = r.listen(source)
          quarry = ""
     try:
          print("Recognizing...")
          quarry = r.recognize_google(audio, language="en-in")
          print(f"User said:{quarry}\n")
     except Exception as e:
          print("Exception: "+str(e))
          print("say that again please...")
          return "None"
     return quarry

def sendEmail(to, content):
     server = smtplib.SMTP('smpt.gmail.com', 587)
     server.shlo()
     server.starttls()
     server.login('your email@gmail.com','your password here')
     server.sendmail('your email@gmail.com', to, content)
     server.close()

#Main programm
if __name__=="__main__":
     print("Initializing Hatch It")
     wishme()
     while True:
          quarry = takeCommand().lower()
          if 'wikipedia' in quarry:
               speak("Searching wikipedia...")
               quarry = quarry.replace("wikipedia","")
               result = wikipedia.summary(quarry, sentences=2)
               speak("According to wikipedia")
               print(result)
               speak(result)

          elif 'open youtube' in quarry:
               webbrowser.open("youtube.com")

          elif 'open google' in quarry:
               webbrowser.open("google.com")

          elif 'open stackoverflow' in quarry:
               webbrowser.open("stackoverfllow.com")

          elif 'open facebook' in quarry:
               webbrowser.open("facebook.com")

          elif 'play music' in quarry:
               music_dir = "C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe"
               os.startfile(music_dir)

          elif 'the time' in quarry:
               strTime = datetime.datetime.now().strftime("%H:%M:%S")
               print(strTime)
               speak(f"Sir, the time is {strTime}")

          elif 'about yourself' in quarry:
               speak("i am Hatch It a voice assistant AI, I am under development but"
                     "still you can use me.")

          elif 'your creator' in quarry:
               speak("My creator is Rahul Das.")

          elif 'open programmers' in quarry:
               codePath = "C:\\Users\\RAHUL DAS\\OneDrive\\Desktop\\Programmers"
               os.startfile(codePath)

          elif 'email to someone' in quarry:
               try:
                    speak("What shoud I say?")
                    content = takeCommand()
                    to = "receiver's mail @gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
               except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to send this email.")

          elif 'open gmail' in quarry:
               webbrowser.open("gmail.com")

          elif 'good job' in quarry:
               speak("You are welcome")

          elif 'open code' in quarry:
               code_idle1 = "C:\\Users\\RAHUL DAS\\AppData\\Local\\Programs\\Python\\Python39\\pythonw.exe"
               code_idle2 = "C:\\Users\\RAHUL DAS\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
               os.startfile(code_idle1)
               os.startfile(code_idle2)
