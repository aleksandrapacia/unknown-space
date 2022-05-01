from tkinter import Grid
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, VariableListProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.uix.image import Image

class NavContent(BoxLayout):
    management = ObjectProperty(None)
    nav_drawer = ObjectProperty(None)


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
        Builder.load_file('mymanager.kv')
        return MyManager()
UnknownApp().run()

