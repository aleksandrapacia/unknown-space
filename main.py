from re import L
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
from kivy.uix.label import Label
import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

Window.size=360,640

LabelBase.register(name='WorkSans', 
                fn_regular='WorkSans-VariableFont_wght.ttf')

class FirstScreen(Screen):
    first_manager = ObjectProperty(None)
    
class NavContent(RelativeLayout):
    management = ObjectProperty(None)
    nav_drawer = ObjectProperty(None)

class Layout_(Screen):
    pass
    

class AboutScreen(Screen):
    Builder.load_file('screens//aboutapp_screen.kv')

class ProfileScreen(Screen):
    Builder.load_file('screens//profile_screen.kv')

class MineScreen(Screen):
    pass

class MoonScreen(Screen):
    pass

class TrackScreen(Screen):
    #g = geocoder.ip('me')
    #text = Label(text="Your current lat / long is: " + str(g.latlng), font_size='20sp', pos_hint={'center_x':.5,'center_y':.5})
    Builder.load_file('screens//trackscreen.kv')
        
class UnknownScreen(Screen):
    pass

class MoonPhaseScreen(Screen):
    pass
class UnknownApp(MDApp):
    def build(self):
        Builder.load_file('mymanager.kv')
        LabelBase.register(name='WorkSans', 
                fn_regular='WorkSans-VariableFont_wght.ttf')
        self.theme_cls.primary_palette = "Purple"
        return Layout_()


UnknownApp().run()
