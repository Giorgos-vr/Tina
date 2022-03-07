from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from commands import *


class IntroWindow(Screen):
    pass

class MenuWindow(Screen):
        once = False
        twice = False
        def on_enter(self, *args):
            while MenuWindow.once == False:
                Command.start()
                Command.introMenu()
                MenuWindow.once = True
                while MenuWindow.twice == False:
                    if Command.sel == "shapes":
                        self.parent.current = "shapes"
                        MenuWindow.twice = True
                        return MenuWindow.twice
                    elif Command.sel == "colours":
                        self.parent.current = "colours"
                        MenuWindow.twice = True
                        return MenuWindow.twice
                    elif Command.sel == "letters":
                        self.parent.current = "letters"
                        MenuWindow.twice = True
                        return MenuWindow.twice
                    elif Command.sel == "numbers":
                        self.parent.current = "numbers"
                        MenuWindow.twice = True
                        return MenuWindow.twice
                    else:
                        MenuWindow.twice = True
                        return MenuWindow.twice
                

            return MenuWindow.once


                
        

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