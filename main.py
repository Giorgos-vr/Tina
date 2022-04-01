import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import StringProperty
from commands import *


class IntroWindow(Screen):
    pass

class MenuWindow(Screen):
    once = False #intro dialogue is only meant to play once
    def on_enter(self, *args):
        while MenuWindow.once == False:
            Command.start()
            Command.introMenu()
            while MenuWindow.once == False:
                if Command.sel == "shapes":
                    self.parent.current = "shapes"
                    MenuWindow.once = True
                elif Command.sel == "items":
                    self.parent.current = "items"
                    MenuWindow.once = True
                elif Command.sel == "numbers":
                    self.parent.current = "numbers"
                    MenuWindow.once = True
                elif Command.sel == "letters":
                    self.parent.current = "letters"
                    MenuWindow.once = True
                else:
                    MenuWindow.once = True
            

        return MenuWindow.once #intro counter doesn't reset

class ShapeGame(Screen):
    rand_shape = StringProperty()
    # These counters control the amount of repetitions of question dialogues and must be consistent
    # with one another.
    count1 = 0 #count1 is for image selection (on_pre_enter)
    count2 = 0 #count2 is for user responce (on_enter)
    #note2self it may be possible to combine these 2 counters into one but I'm not sure how, more testing needed.

    def on_pre_enter(self, *args):        
        def callback_pre_image(dt):
            if ShapeGame.count1 < 5:
                if ShapeGame.count1 < 5:
                    Command.say("Τι είναι?")
                    #here's the brilliant part!
                    #acceptable answers and image paths are stored as dict key:value pairs.
                    random_shape = {('μαύρο', 'άδειο', 'σκοτεινό'):'shapes/black.png',
                        ('μπλε', 'γαλάζιο', 'γαλανό'):'shapes/blue.png', ("πράσινο", "πρασινάκι"):'shapes/green.png',
                        ("ροζ", "κόκκινο"):'shapes/pink.png', ("μωβ", "φούξια"):'shapes/purple.png',
                        ("κόκκινο", "ροζ", "κοκκινάκι"):'shapes/red.png', ("άσπρο", "λευκό"):'shapes/white.png',
                        ("κίτρινο", "κιτρινάκι", "καναρινί"):'shapes/yellow.png',
                        ("παραλληλόγραμμο", "τραπέζιο", "τραπέζι", "τετράγωνο", "τραπεζοειδές"):'shapes/trapezoid.png',
                        ("διαμάντι", "ρόμβος", "παραλληλόγραμο", "τετράγωνο"):'shapes/diamond.png',
                        ("ορθογώνιο", "παραλληλόγραμμο"):'shapes/rectangle.png', ("οβάλ", "στεφάνι"):'shapes/oval.png',
                        ("αστέρι", "αστεράκι", "άστρο"):'shapes/star.png', ("τετράγωνο", "τετραγωνάκι"):'shapes/square.png',
                        ("τρίγωνο", "τριγωνάκι"):'shapes/triangle.png', ("κύκλος", "στρογγυλό", "κυκλάκι"):'shapes/circle.png'}
                    #answer:image dict item is picked at random
                    random_shape_key, random_shape_value = random.choice(list(random_shape.items()))
                    print(random_shape_key) #key is printed for debugging purposes
                    self.rand_shape_key = random_shape_key
                    self.rand_shape = random_shape_value #value is assigned to instance to be used by .kv
                                                         #and allow kivy to display the image
                    ShapeGame.count1 += 1   #update
                    return ShapeGame.count1 #and return counter
                elif ShapeGame.count1 >= 5: #this is probably pointless
                    pass
            elif ShapeGame.count1 >=5:      #cancel callback once max reps is reached
                Clock.unschedule(callback_pre_image)
                ShapeGame.count1 = 0 #reset counter
                return ShapeGame.count1

        Clock.schedule_once(callback_pre_image) #schedule callback
        Clock.schedule_interval(callback_pre_image, 10) #setup interval (10 seconds in this case)

        
    def on_enter(self, *args):
        def callback_on_image(dt):
            if ShapeGame.count2 < 5:
                if ShapeGame.count2 < 5:
                    #on_enter the user responce is captured, broken down into individual words
                    #and these words are placed in a list with a space separator
                    input = Command.audioIn().lower().split(' ')
                    if Command.user_said == None:
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
                    #and here's the other brilliant part, the user responce list gets compared
                    #with the accepted responces list found in the dict key list previously randomly selected
                    elif any(word in input for word in self.rand_shape_key):
                        Command.say("πολύ σωστά!")#if correct
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
                    elif Command.bad_read == False:
                        Command.say("Λάθος!")#if wrong (and not a bad read)
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
                    else:
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
            elif ShapeGame.count2 >=5:
                Clock.unschedule(callback_on_image)
                ShapeGame.count2 = 0 #reset counter
                Command.say(f"Μπράβο {Command.user_name}!") #"well done" confirms loop completion
                return ShapeGame.count2

        Clock.schedule_once(callback_on_image)
        Clock.schedule_interval(callback_on_image, 10)

    
class ItemGame(Screen):
    rand_item = StringProperty()
    count1 = 0
    count2 = 0

    def on_pre_enter(self, *args):        
        def callback_pre_item(dt):
            if ItemGame.count1 < 10:
                if ItemGame.count1 < 10:
                    Command.say("Τι είναι?")
                    random_item = {("αρκούδα", "αρκουδάκι", "αρκουδίτσα", "καφέ"):'items/bear.png',
                    ("γουρούνι", "γουρουνάκι"):'items/pig.png', ("ποντίκι", "ποντικάκι", "αρουραίος", "χάμστερ"):'items/mouse.png',
                    ("ψάρι", "ψαράκι"):'items/fish.png', ("σκυλί", "σκύλος", "σκυλάκι"):'items/dog.png',
                    ("ελάφι", "ελαφάκι"):'items/deer.gif', ("γάτα", "γατούλα", "γατάκι", "γατίτσα"):'items/cat.png',
                    ("πουλί", "περιστέρι", "περιστεράκι", "πουλάκι"):'items/bird.png', ("ανανάς", "ανανά"):'items/pineapple.png',
                    ("πορτοκάλι", "πορτοκαλάκη", "πορτοκαλάκι"):'items/orange.png', ("λεμόνι", "λεμονάκι"):'items/lemon.png',
                    ("κεράσι", "κερασάκι", "κεράσια", "κερασάκια"):'items/cherry.png', ("μπανάνα", "banana", "μπανανίτσα", "μπανανούλα"):'items/banana.png',
                    ("μήλο", "μηλαράκι"):'items/apple.png'}
                    random_item_key, random_item_value = random.choice(list(random_item.items()))
                    print(random_item_key)
                    self.rand_item_key = random_item_key
                    self.rand_item = random_item_value
                    ItemGame.count1 += 1
                    return ItemGame.count1
                elif ItemGame.count1 >= 10:
                    pass
            elif ItemGame.count1 >=10:
                Clock.unschedule(callback_pre_item)
                ItemGame.count1 = 0
                return ItemGame.count1

        Clock.schedule_once(callback_pre_item)
        Clock.schedule_interval(callback_pre_item, 10)

        
    def on_enter(self, *args):
        def callback_on_item(dt):
            if ItemGame.count2 < 10:
                if ItemGame.count2 < 10:
                    input = Command.audioIn()
                    select = input.lower().split(' ')
                    if Command.user_said == None:
                        ItemGame.count2 += 1
                        return ItemGame.count2
                    elif any(word in select for word in self.rand_item_key):
                        Command.say("πολύ σωστά!")
                        ItemGame.count2 += 1
                        return ItemGame.count2
                    elif Command.bad_read == False:
                        Command.say("Λάθος!")
                        ItemGame.count2 += 1
                        return ItemGame.count2
                    else:
                        ItemGame.count2 += 1
                        return ItemGame.count2
            elif ItemGame.count2 >=10:
                Clock.unschedule(callback_on_item)
                ItemGame.count2 = 0
                Command.say(f"Μπράβο {Command.user_name}!")
                return ItemGame.count2

        Clock.schedule_once(callback_on_item)
        Clock.schedule_interval(callback_on_item, 10)

class NumberGame(Screen):
    rand_number = StringProperty()
    count1 = 0
    count2 = 0

    def on_pre_enter(self, *args):        
        def callback_pre_number(dt):
            if NumberGame.count1 < 5:
                if NumberGame.count1 < 5:
                    Command.say("Τι είναι?")
                    random_number = {("μηδενικό", "zero", "0"):'numbers/0.png', ("1", "άσσος"):'numbers/1.png',
                    ("2", "δύο", "διπλό", "δυάρι"):'numbers/2.png', ("3", "τριάρι", "τριπλό"):'numbers/3.png', ("4", "τεσσάρι", "τετραπλό"):'numbers/4.png',
                    ("5", "πεντάρι", "πενταπλό"):'numbers/5.png', ("6", "εξάρι", "εξαπλό"):'numbers/6.png',
                    ("7", "επτά", "εφτάρι", "7άρι"):'numbers/7.png', ("8", "οκτώ", "οχτώ", "8άρι"):'numbers/8.png', ("9", "εννιά", "εννιάρι", "εννέα"):'numbers/9.png'}
                    random_number_key, random_number_value = random.choice(list(random_number.items()))
                    print(random_number_key)
                    self.rand_number_key = random_number_key
                    self.rand_number = random_number_value
                    NumberGame.count1 += 1
                    return NumberGame.count1
                elif NumberGame.count1 >= 5:
                    pass
            elif NumberGame.count1 >=5:
                Clock.unschedule(callback_pre_number)
                NumberGame.count1 = 0
                return NumberGame.count1

        Clock.schedule_once(callback_pre_number)
        Clock.schedule_interval(callback_pre_number, 10)

        
    def on_enter(self, *args):
        def callback_on_number(dt):
            if NumberGame.count2 < 5:
                if NumberGame.count2 < 5:
                    input = Command.audioIn().lower().split(' ')
                    if Command.user_said == None:
                        NumberGame.count2 += 1
                        return NumberGame.count2
                    elif any(word in input for word in self.rand_number_key):
                        Command.say("πολύ σωστά!")
                        NumberGame.count2 += 1
                        return NumberGame.count2
                    elif Command.bad_read == False:
                        Command.say("Λάθος!")
                        NumberGame.count2 += 1
                        return NumberGame.count2
                    else:
                        NumberGame.count2 += 1
                        return NumberGame.count2
            elif NumberGame.count2 >=5:
                Clock.unschedule(callback_on_number)
                NumberGame.count2 = 0
                Command.say(f"Μπράβο {Command.user_name}!")
                return NumberGame.count2

        Clock.schedule_once(callback_on_number)
        Clock.schedule_interval(callback_on_number, 10)

class LetterGame(Screen):
    rand_letter = StringProperty()
    count1 = 0
    count2 = 0

    def on_pre_enter(self, *args):        
        def callback_pre_letter(dt):
            if LetterGame.count1 < 5:
                if LetterGame.count1 < 5:
                    Command.say("Τι είναι?")
                    random_letter = {}
                    random_letter_key, random_letter_value = random.choice(list(random_letter.items()))
                    print(random_letter_key)
                    self.rand_letter_key = random_letter_key
                    self.rand_letter = random_letter_value
                    LetterGame.count1 += 1
                    return LetterGame.count1
                elif LetterGame.count1 >= 5:
                    pass
            elif LetterGame.count1 >=5:
                Clock.unschedule(callback_pre_letter)
                LetterGame.count1 = 0
                return LetterGame.count1

        Clock.schedule_once(callback_pre_letter)
        Clock.schedule_interval(callback_pre_letter, 10)

        
    def on_enter(self, *args):
        def callback_on_letter(dt):
            if LetterGame.count2 < 5:
                if LetterGame.count2 < 5:
                    input = Command.audioIn().lower().split(' ')
                    if Command.user_said == None:
                        LetterGame.count2 += 1
                        return LetterGame.count2
                    elif any(word in input for word in self.rand_letter_key):
                        Command.say("πολύ σωστά!")
                        LetterGame.count2 += 1
                        return LetterGame.count2
                    elif Command.bad_read == False:
                        Command.say("Λάθος!")
                        LetterGame.count2 += 1
                        return LetterGame.count2
                    else:
                        LetterGame.count2 += 1
                        return LetterGame.count2
            elif LetterGame.count2 >=5:
                Clock.unschedule(callback_on_letter)
                LetterGame.count2 = 0
                Command.say(f"Μπράβο {Command.user_name}!")
                return LetterGame.count2

        Clock.schedule_once(callback_on_letter)
        Clock.schedule_interval(callback_on_letter, 10)

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    

    def build(self):
        return Builder.load_file('Main.kv')

if __name__ == '__main__':
    MainApp().run()