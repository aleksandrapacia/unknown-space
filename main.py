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
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.core.text import LabelBase
Window.size=360,640

LabelBase.register(name='WorkSans', 
                fn_regular='WorkSans-VariableFont_wght.ttf')

class NavContent(RelativeLayout):
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

class AboutAppScreen(FirstScreen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        

class Layout_(Screen):
    pass

class UnknownApp(MDApp):
    def build(self):
        Builder.load_file('mymanager.kv')
        LabelBase.register(name='WorkSans', 
                fn_regular='WorkSans-VariableFont_wght.ttf')
        self.theme_cls.primary_palette = "Purple"
        return Layout_()


UnknownApp().run()

