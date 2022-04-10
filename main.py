from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, VariableListProperty
from kivy.uix.floatlayout import FloatLayout


class NavContent(BoxLayout):
    management = ObjectProperty()
    nav_drawer = ObjectProperty()

class FirstScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class CalendarScreen(Screen):
    pass

class ArticlesScreen(Screen):
    pass

class SkyviewScreen(Screen):
    pass


class MyManager(ScreenManager):
    pass

    def build(self):
        mm = MyManager()


    

class UnknownApp(MDApp):
    def build(self):
        Builder.load_file('demo.kv')
        return MyManager()

UnknownApp().run()

#TODO: issue
