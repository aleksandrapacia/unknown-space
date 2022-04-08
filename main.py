from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty, VariableListProperty
from kivy.uix.floatlayout import FloatLayout


class NavContent(BoxLayout):
    management = ObjectProperty()
    nav_drawer = ObjectProperty()


class Demo(ScreenManager):
    pass

class UnknownApp(MDApp):
    def build(self):
        Builder.load_file('demo.kv')
        return Demo()

UnknownApp().run()

#TODO: issue
