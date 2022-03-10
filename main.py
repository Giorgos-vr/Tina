from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            pass

    
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