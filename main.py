from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from commands import *


class IntroWindow(Screen):
    pass

class MenuWindow(Screen):
        once = False
        def on_enter(self):
            while MenuWindow.once == False:
                Command.start()
                Command.introMenu()
                MenuWindow.once = True
                return MenuWindow.once

            if Command.sel is ["shapes"]:
                ScreenManager().switch_to = "shapes"
            elif Command.sel is ["colours"]:
                ScreenManager().switch_to = "colours"
            elif Command.sel is ["letters"]:
                ScreenManager().switch_to = "letters"
            elif Command.sel is ["numbers"]:
                ScreenManager().switch_to = "numbers"
            else:
                pass


                
        

class ShapeGame(Screen):
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