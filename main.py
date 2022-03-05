from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from commands import *


class IntroWindow(Screen):
    pass

class MenuWindow(Screen):
        counter = False
        def on_enter(self):
            while MenuWindow.counter == False:
                Command.start()
                Command.introMenu()
                MenuWindow.counter = True
                return MenuWindow.counter
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