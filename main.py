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
    rand_shape = StringProperty()
    count1 = 0
    count2 = 0

    def on_pre_enter(self, *args):        
        def callback_pre_image(dt):
            if ShapeGame.count1 < 5:
                if ShapeGame.count1 < 5:
                    Command.say("Τι είναι?")
                    random_shape = {"ορθογώνιο":'shapes/rectangle.jpg', "οβάλ":'shapes/oval.jpg', "αστέρι":'shapes/star.png', "τετράγωνο":'shapes/square.png', "τρίγωνο":'shapes/triangle.jpg', "κύκλος":'shapes/circle.jpg'}
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
                    if any(word in input for word in [self.rand_shape_key]):
                        Command.say("Σωστά!")
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
                    else:
                        Command.say("Λάθος!")
                        ShapeGame.count2 += 1
                        return ShapeGame.count2
            elif ShapeGame.count2 >=5:
                Clock.unschedule(callback_on_image)
                ShapeGame.count2 = 0
                Command.say("Μπράβο!")
                return ShapeGame.count2

        Clock.schedule_once(callback_on_image)
        Clock.schedule_interval(callback_on_image, 10)

    
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