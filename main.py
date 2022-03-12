from itertools import count
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.properties import StringProperty
from commands import *


class IntroWindow(Screen):
    pass

class MenuWindow(Screen):
    pass
'''        once = False
        def on_enter(self, *args):
            while MenuWindow.once == False:
                Command.start()
                Command.introMenu()
                while MenuWindow.once == False:
                    if Command.sel == "shapes":
                        self.parent.current = "shapes"
                        MenuWindow.once = True
                    elif Command.sel == "colours":
                        self.parent.current = "colours"
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
'''

                
        

class ShapeGame(Screen):
    rand_shape = StringProperty()
    count = 0
    def on_pre_enter(self, *args):        
        random_shape = {"τετράγωνο":'shapes/square.png', "τρίγωνο":'shapes/triangle.jpg', "κύκλος":'shapes/circle.jpg'}
        random_shape_key, random_shape_value = random.choice(list(random_shape.items()))
        print(random_shape_key)
        self.rand_shape_key = random_shape_key
        self.rand_shape = random_shape_value
        
    def on_enter(self, *args):
#        while self.count < 3:
            input = Command.audioIn().lower().split(' ')
            if any(word in input for word in [self.rand_shape_key]):
                Command.say("Σωστά!")
#                self.count += 1
#                ShapeGame.on_pre_enter(self, *args)
            else:
                Command.say("Λάθος!")
#                self.count += 1
#                ShapeGame.on_pre_enter(self, *args)

    
class ColourGame(Screen):
    pass

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