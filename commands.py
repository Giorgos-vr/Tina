import os
import playsound
import speech_recognition as sr
from gtts import gTTS as gt


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
                Command.user_said = " "
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
        shapeSelect = ["σχήμα", "σχήματα", "σχηματάκι", "σχηματάκια"]
        colourSelect = ["χρώμα", "χρώματα", "χρωματάκι", "χρωματάκια"]
        letterSelect = ["γράμμα", "γράμματα", "γραμματάκια", "γραμματάκι", "άλφα", "βήτα", "αλφαβήτα"]
        numberSelect = ["νούμερο", "νούμερα", "αριθμός", "αριθμοί", "αριθμούς"]
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
            Command.sel = None


'''class Game:

    def __init__(self) -> None:
        pass

    def tenRandShapes():
        for x in range(3):

            random_shape = {"τετράγωνο": 'shapes/square.png', "τρίγωνο": 'shapes/triangle.png', "κύκλος": 'shapes/circle.png'}
            random_shape_key, random_shape_value = random.choice(list(random_shape.items()))
            #print(random_shape_value)
            Command.say(random_shape_key)
            return Image(source=random_shape_value)


    def ShapeGame(self):
        rand_shape = str()
        for x in range(3):

            random_shape = {"τετράγωνο":'shapes/square.png', "τρίγωνο":'shapes/triangle.png', "κύκλος":'shapes/circle.png'}
            random_shape_key, random_shape_value = random.choice(list(random_shape.items()))
            #print(random_shape_value)
            Command.say(random_shape_key)
            self.rand_shape = Image(source=random_shape_value)
            return self.rand_shape
'''

#Game.tenRandShapes()



# def test():
    

# test()

