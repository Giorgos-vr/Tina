from fileinput import filename
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS as gt
from kivy.uix.screenmanager import ScreenManager, Screen


class Command:

    def __init__(self):
        Command.user_said = ""
        Command.user_name = ""
        Command.sel = ""

    
    def say(text):
        tts = gt(text=text, lang="el")
        filename = "say.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)




    def audioIn():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            

            try:
                Command.user_said = r.recognize_google(audio, language = "el-GR")
                print(Command.user_said)
            except sr.UnknownValueError:
                Command.say("Δεν σε κατάλαβα, συγνώμη!")
            except sr.RequestError:
                Command.say("Αδυναμία σύνδεσης!")
        
        return Command.user_said


    def greetUser():
        Command.user_name = Command.user_said
        Command.say(f"Γειά σου {Command.user_name}")
        
        return Command.user_name



    def start():
        Command.say("Γειά σου, με λένε Τίνα, από το Ρομποτίνα. Εσένα πως σε λένε;")
        Command.audioIn()
        Command.greetUser()

    def gameSelection():
        Command.say(f"{Command.user_name} ποιό παιχνίδι θέλεις να παίξουμε?")
        input = Command.audioIn().lower().split(' ')
        print(input)
        shapeSelect = ["σχήμα", "σχήματα"]
        colourSelect = ["χρώμα", "χρώματα"]
        letterSelect = ["γράμμα", "γράμματα"]
        numberSelect = ["νούμερο", "νούμερα", "αριθμός", "αριθμοί"]
        if any(word in input for word in shapeSelect):
            Command.say("Πάμε για σχήματα!")
            Command.sel = "shapes"
        elif any(word in input for word in colourSelect):
            Command.say("Πάμε για χρώματα!")
            Command.sel = "colours"
        elif any(word in input for word in letterSelect):
            Command.say("Πάμε για γράμματα!")
            Command.sel = "letters"
        elif any(word in input for word in numberSelect):
            Command.say("Πάμε για αριθμούς!")
            Command.sel = "numbers"
        else:
            Command.say("Δεν σε κατάλαβα. Αν θέλεις διάλεξε από το μενού!")
            Command.sel = None

        return Command.sel

    def introMenu():
        Command.say(f"{Command.user_name} θέλεις να παίξουμε?")
        input = Command.audioIn().lower().split(' ')
        print(input)
        positive_input = ["ναι", "αμέ", "αχά"]
        if any(word in input for word in positive_input):
            Command.say("Τέλεια!")
            Command.gameSelection()
        else:
            Command.say("Κρίμα!")