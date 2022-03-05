from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

class IntroWindow(Screen):
    pass

class MenuWindow(Screen):
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