from doctest import testmod
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
from kivy_garden.mapview import MapView
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
        Clock.schedule_interval(self.update_map, 1)  

    # Usando api do ISS para pegar a posição da estação espacial internacional e atualizar o mapa
    def update_map(self, data):
        r = requests.get('http://api.open-notify.org/iss-now.json')
        data = r.json()
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']
        self.map = self.ids.map
        mml = MarkerMapLayer()
        self.map.add_layer(mml)
        self.marker = MapMarker( lat=lat, lon=lon, source = 'images//iss.gif')
        self.map.add_widget(self.marker)
        return self.map
    def on_eneter(self):
        self.map.remove_widget(self.marker)
        self.map.add_widget(self.marker)



    

class UnknownScreen(Screen):
    pass

class MoonPhaseScreen(Screen):
    pass

class UnknownApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"

        return Layout_()
        
    

        



UnknownApp().run()
