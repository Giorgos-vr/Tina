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
    once = False
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
                elif Command.sel == "letters":
                    self.parent.current = "letters"
                    MenuWindow.once = True
                elif Command.sel == "numbers":
                    self.parent.current = "numbers"
                    MenuWindow.once = True
                else:
                    MenuWindow.once = True
            

        return MenuWindow.once


                
        

class ShapeGame(Screen):
    rand_shape = StringProperty()
    count1 = 0
    count2 = 0

    def on_pre_enter(self, *args):        
        def callback_pre_image(dt):
            if ShapeGame.count1 < 5:
                if ShapeGame.count1 < 5:
                    Command.say("Τι είναι?")
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
                    random_shape_key, random_shape_value = random.choice(list(random_shape.items()))
                    print(random_shape_key)
                    self.rand_shape_key = random_shape_key
                    self.rand_shape = random_shape_value
                    ShapeGame.count1 += 1
                    return ShapeGame.count1
                elif ShapeGame.count1 >= 5:
                    pass
            elif ShapeGame.count1 >=5:
                Clock.unschedule(callback_pre_image)
                ShapeGame.count1 = 0
                return ShapeGame.count1

        Clock.schedule_once(callback_pre_image)
        Clock.schedule_interval(callback_pre_image, 10)

        
    def on_enter(self, *args):
        def callback_on_image(dt):
            if ShapeGame.count2 < 5:
                if ShapeGame.count2 < 5:
                    input = Command.audioIn().lower().split(' ')
                    if Command.user_said == None:
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
                    elif any(word in input for word in self.rand_shape_key):
                        Command.say("πολύ σωστά!")
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
                    elif Command.bad_read == False:
                        Command.say("Λάθος!")
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
                    else:
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
            elif ShapeGame.count2 >=5:
                Clock.unschedule(callback_on_image)
                ShapeGame.count2 = 0
                Command.say(f"Μπράβο {Command.user_name}!")
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
                    ("πορτοκάλι", "πορτοκαλάκι"):'items/orange.png', ("λεμόνι", "λεμονάκι"):'items/lemon.png',
                    ("κεράσι", "κερασάκι", "κεράσια", "κερασάκια"):'items/cherry.png', ("μπανάνα", "μπανανίτσα", "μπανανούλα"):'items/banana.png',
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

class LetterGame(Screen):
    pass

class NumberGame(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    

    def build(self):
        return Builder.load_file('Main.kv')

if __name__ == '__main__':
    MainApp().run()