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
        self.name = str(data[0]["Phase"])
        print(self.name)
        percentage_text = Label( text=f'{self.illumination}%', 
                                halign='center',
                                font_name= 'WorkSans',
                                font_size= 23,
                                color=(0/255.0,0/255.0,0/255.0),
                                pos_hint={'center_x':.5, 'center_y':.3})
        name_text = Label( text=f'Phase: {self.name}', 
                                halign='center',
                                font_name= 'WorkSans',
                                font_size= 23,
                                color=(0/255.0,0/255.0,0/255.0),
                                pos_hint={'center_x':.5, 'center_y':.2})
        self.age = int(data[0]["Age"]) # 22.1 = full moon in 2022

        age_text = Label( text=f'Age: {self.age}', 
                                halign='center',
                                font_name= 'WorkSans',
                                font_size= 23,
                                color=(0/255.0,0/255.0,0/255.0),
                                pos_hint={'center_x':.5, 'center_y':.1})
    # PRE FULL MOON PHASES
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

    # POST FULL MOON PHASES
        self.fourteen = Image(
            source= 'images/phases/to_full/14.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.fifteen = Image(
            source= 'images/phases/to_full/15.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})
        
        self.sixteen = Image(
            source= 'images/phases/to_full/16.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.seventeen = Image(
            source= 'images/phases/to_full/17.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.eighteen = Image(
            source= 'images/phases/to_full/18.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.nineteen =  Image(
            source= 'images/phases/to_full/19.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.twenty =  Image(
            source= 'images/phases/to_full/20.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.twentyone =  Image(
            source= 'images/phases/to_full/21.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.twentytwo =  Image(
            source= 'images/phases/to_full/22.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.twentythree =  Image(
            source= 'images/phases/to_full/23.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.twentyfour =  Image(
            source= 'images/phases/to_full/24.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})

        self.twentyfive=  Image(
            source= 'images/phases/to_full/25.png',
            allow_stretch= False,
            keep_ratio= False,
            opacity= 0.8,
            size_hint= (1,1),
            pos_hint= {'center_x': 0.5, 'center_y': 0.5})


        #TODO: finish -> when does the specific image have to appear
        # TO THE FULL MOON
        # 1
        print(self.age)
        if self.age <=22.1:
            if self.illumination >= 0 and self.illumination < 4:
                self.add_widget(self.one)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)
            # 2
            if self.illumination >=4 and self.illumination < 16:
                self.remove_widget(self.one)
                self.add_widget(self.two)
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                # new data
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)

            # 3
            if self.illumination >=9 and self.illumination <=16:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.two)
                # new data
                self.add_widget(self.three)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 4
            if self.illumination > 16 and self.illumination < 24:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.three) 
                # new data
                self.add_widget(self.four)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 5 
            if self.illumination >= 24 and self.illumination <= 34:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.four)
                # new data
                self.add_widget(self.five)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 6
            if self.illumination > 34 and self.illumination <= 45:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.five)
                # new data
                self.add_widget(self.six)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 7
            if self.illumination > 45 and self.illumination <= 56:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.six)
                # new data
                self.add_widget(self.seven)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 8 
            if self.illumination > 56 and self.illumination <=68:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.seven)
                # new data
                self.add_widget(self.eight)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 9
            if self.illumination > 68 and self.illumination <= 78:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.eight)
                # new data
                self.add_widget(self.nine)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 10
            if self.illumination > 78 and self.illumination <=87:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.nine)
                # new data
                self.add_widget(self.ten)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 11
            if self.illumination > 87 and self.illumination <= 93:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.ten)
                # new data
                self.add_widget(self.eleven)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 12
            if self.illumination > 93 and self.illumination <= 98:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.eleven)
                # new data
                self.add_widget(self.twelve)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)


            # 13 
            if self.illumination > 98 and self.illumination <= 100:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.twelve)
                # new data
                self.add_widget(self.thirteen)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)
        # POST FULL MOON PHASES
        if self.age <=22.1:
            # 14    
            if self.illumination < 100 and self.illumination >= 98:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.thirteen)
                # new data
                self.add_widget(self.fourteen)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)

            # 15
            if self.illumination < 98 and self.illumination >= 95:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.fourteen)
                # new data
                self.add_widget(self.fifteen)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)
            # 16
            if self.illumination < 95 and self.illumination >= 89:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.fifteen)
                # new data
                self.add_widget(self.sixteen)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)
            # 17
            if self.illumination < 89 and self.illumination >= 81:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.sixteen)
                # new data
                self.add_widget(self.seventeen)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)
            # 18
            if self.illumination < 81 and self.illumination >= 72:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.seventeen)
                # new data
                self.add_widget(self.eighteen)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)
            
            if self.illumination < 72 and self.illumination >= 53:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.eighteen)
                # new data
                self.add_widget(self.nineteen)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)

            if self.illumination < 53 and self.illumination >= 43:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.nineteen)
                # new data
                self.add_widget(self.twenty)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)

            if self.illumination < 43 and self.illumination >= 33:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.twenty)
                # new data
                self.add_widget(self.twentyone)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)

            if self.illumination < 33 and self.illumination >= 25:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.twentyone)
                # new data
                self.add_widget(self.twentytwo)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)

            if self.illumination < 25 and self.illumination >= 17:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.twentytwo)
                # new data
                self.add_widget(self.twentythree)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)

            if self.illumination < 17 and self.illumination >= 11:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.twentythree)
                # new data
                self.add_widget(self.twentyfour)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)

            if self.illumination < 11 and self.illumination >= 5:
                # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.twentyfour)
                # new data
                self.add_widget(self.twentyfive)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)

            if self.illumination < 5:
                 # delete old data
                self.remove_widget(percentage_text)
                self.remove_widget(name_text)
                self.remove_widget(age_text)
                self.remove_widget(self.twentyfive)
                # new data
                self.add_widget(self.one)
                self.add_widget(percentage_text)
                self.add_widget(name_text)
                self.add_widget(age_text)




            







   



            


                
                




        
            

    def run_away_phase(self):
        self.manager.current = 'mine' 

class UnknownApp(MDApp):
    def build(self):

        self.theme_cls.primary_palette = "Purple"


        return Layout_()

UnknownApp().run()
