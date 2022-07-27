from calendar import day_abbr
from codecs import latin_1_decode
from doctest import testmod
from itertools import count
from kivy.uix.scatter import Scatter
from numbers import Number
from re import L
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
from kivymd.uix.button import MDIconButton
from kivy.uix.widget import Widget
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

from kivyauth.google_auth import initialize_google, login_google, logout_google

Window.size=360,640

LabelBase.register(name='WorkSans', 
                fn_regular='WorkSans-VariableFont_wght.ttf')


class ContentNavigationDrawer(BoxLayout):
    management = ObjectProperty(None)
    nav_drawer = ObjectProperty(None)
    check = ObjectProperty(None)

class Layout_(Screen):
    Builder.load_file('mymanager.kv')
    
class AboutScreen(Screen):
    Builder.load_file('screens//aboutapp_screen.kv')
    def come_back_m_n(self):
        self.manager.current = 'mine'

class SignInScreen(Screen):
    pass

class LikeScreen(Screen):
    pass

class MineScreen(Screen):
    def tracking(self):
        self.manager.current = 'iss_tracking'
    def telling_abt(self):
        self.manager.current = 'aboutapp'
    def moon_mapping(self):
        self.manager.current = 'moon'
    def moon_phase(self):
        self.manager.current = 'moon_phase'

class MoonScreen(Screen):
    def menu_get(self):
        self.manager.current = 'mine'

class SquareWidget(Widget):
    pass

class ScatterWidget(Scatter):
    pass

class Labela(Label):
    pass
class TrackScreen(Screen):
    
    Builder.load_file('screens//trackscreen.kv')
    def __init__(self, **kwargs):
        super(TrackScreen, self).__init__(**kwargs)
        self.marker = None
        self.map = None
        self.data_=None
        r = requests.get('http://api.open-notify.org/iss-now.json')
        data = r.json()
        self.lat = float(data['iss_position']['latitude'])
        self.lon =float(data['iss_position']['longitude'])
        print(data['message'])
        
        
        
    def come_back_m(self):
        self.manager.current = 'mine'
        
    def on_enter(self):
        self.map = self.ids.map
        Clock.schedule_interval(self.update_map, 2)
    
    def update_map(self, data):
        
        
        if self.marker:
            self.map.remove_widget(self.marker)

        self.map.remove_widget(self.marker)
        self.marker = MapMarker(source = 'images//iss.gif', lat=self.lat, lon=self.lon)
        self.map.center_on(self.lat,self.lon)
        self.map.add_widget(self.marker)
        if self.data_:
            self.map.remove_widget(self.data_)
        self.map.remove_widget(self.data_)
        #text_ = f"Latitude:{self.lat}\nLongitude:{self.lon}"
        #self.data_ = Labela(text = text_, font_name='WorkSans')
        #self.map.add_widget(self.data_)
        print(self.lat,self.lon)

        return self.map


class UnknownScreen(Screen):
    pass



class MoonPhaseScreen(Screen):
    Builder.load_file('screens//moon_phase.kv')
    def __init__(self, **kwargs):
        super(MoonPhaseScreen, self).__init__(**kwargs)
        
        # api
        req = requests.get('https://api.farmsense.net/v1/moonphases/?d=1350526582')
        data = req.json()
        
        # getting moon illumination in percent 
        self.illumination = float(data[0]["Illumination"])*10
        percentage_text = Label( text=f'{self.illumination}%', 
                                halign='center',
                                font_name= 'WorkSans',
                                font_size= 23,
                                color=(0/255.0,0/255.0,0/255.0),
                                pos_hint={'center_x':.5, 'center_y':.3})
        # images 
        self.one = Image(
            source= 'images/phases/to_full/1.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.two = Image(
            source= 'images/phases/to_full/2.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.three = Image(
            source= 'images/phases/to_full/3.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.four = Image(
            source= 'images/phases/to_full/4.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.five= Image(
            source= 'images/phases/to_full/5.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.six= Image(
            source= 'images/phases/to_full/6.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.seven= Image(
            source= 'images/phases/to_full/7.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.eight= Image(
            source= 'images/phases/to_full/8.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.nine= Image(
            source= 'images/phases/to_full/9.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.ten= Image(
            source= 'images/phases/to_full/10.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.eleven= Image(
            source= 'images/phases/to_full/11.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.twelve= Image(
            source= 'images/phases/to_full/12.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.thirteen= Image(
            source= 'images/phases/to_full/13.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})


        #TODO: finish -> when does the specific image have to appear
        if self.illumination >= 0 and self.illumination < 4:
            self.add_widget(self.one)
            self.add_widget(percentage_text)
        #if self.illumination >=4 and self.illumination < 16:
            

    def run_away_phase(self):
        self.manager.current = 'mine' 

class UnknownApp(MDApp):
    def build(self):

        self.theme_cls.primary_palette = "Purple"


        return Layout_()

UnknownApp().run()
