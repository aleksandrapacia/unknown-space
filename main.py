from doctest import testmod
from itertools import count
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
from kivy_garden.mapview import MapView,MapMarkerPopup
from kivy.core.text import LabelBase
from kivy.uix.label import Label
import json
import turtle
import urllib.request
import time
# # # #
from datetime import datetime, timedelta
import os
import json

from kivy_garden.mapview import MapView, MapMarker, MarkerMapLayer
from kivy.clock import Clock
import requests
import ephem

Window.size=360,640

LabelBase.register(name='WorkSans', 
                fn_regular='WorkSans-VariableFont_wght.ttf')


class FirstScreen(Screen):
    first_manager = ObjectProperty(None)
    
class NavContent(RelativeLayout):
    management = ObjectProperty(None)
    nav_drawer = ObjectProperty(None)

class Layout_(Screen):
    Builder.load_file('mymanager.kv')


class AboutScreen(Screen):
    Builder.load_file('screens//aboutapp_screen.kv')

class ProfileScreen(Screen):
    Builder.load_file('screens//profile_screen.kv')

class MineScreen(Screen):
    pass

class MoonScreen(Screen):
    pass


class TrackScreen(Screen):
    Builder.load_file('screens//trackscreen.kv')
    def __init__(self, **kwargs):
        super(TrackScreen, self).__init__(**kwargs)
        self.marker = None
        self.map = None

    def on_enter(self):
        self.map = self.ids.map
        Clock.schedule_interval(self.update_map, 2)

        
    def update_map(self, data):
        r = requests.get('http://api.open-notify.org/iss-now.json')
        data = r.json()
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']

        if self.marker:
            self.map.remove_widget(self.marker)

        self.map.remove_widget(self.marker)
        self.marker = MapMarker(source = 'images//iss.gif', lat=lat, lon=lon)
        self.map.add_widget(self.marker)
        
        #text_ = f"Latitude:{lat}\nLongitude:{lon}"
        #data_ = Label(text = text_, pos_hint= {'center_x': .8, 'center_y': .8}, font_name='WorkSans')
        #text_color=(232/255.0,176/255.0,243/255.0,1))
        #self.map.add_widget(data_)

        return self.map
        

class UnknownScreen(Screen):

    pass

class MoonPhaseScreen(Screen):
    pass

class UnknownApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"

        return Layout_()
        
    

        



UnknownApp().run()
