from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
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


                
        

class ShapeGame(Screen):
    def on_enter(self, *args):
        for x in range(3):

            random_shape = {"τετράγωνο": 'square.png', "τρίγωνο": 'striangle.png', "κύκλος": 'circle.png'}
            random_shape_key, random_shape_value = random.choice(list(random_shape.items()))
            #print(random_shape_value)
            Command.say(random_shape_key)
            return Image(source=random_shape_value)

    
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