from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.theming import ThemeManager


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="BlueGray"
        return Builder.load_file('Main.kv')

MainApp().run()