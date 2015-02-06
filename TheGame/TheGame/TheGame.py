#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image

from GameScreens.MapScreen import MapScreen
from GameScreens.DeskScreen import DeskScreen

class GameApp(App):
    def build(self):
        from kivy.base import EventLoop
        EventLoop.ensure_window()
        self.window = EventLoop.window

        self.configure()
        self.root = GameWidget(app=self)

    def configure(self):
        self.window.size = (1600, 900)

class GameWidget(Widget):
    app = ObjectProperty(None)

    def __init__(self, **kwargs):
		super(GameWidget, self).__init__(**kwargs)		
		self.changeScreen("MapScreen")

    def changeScreen(self, screen):
        self.clear_widgets()
        if screen == "MapScreen":
            self.add_widget(MapScreen(app=self))
        elif screen == "DeskScreen":
            self.add_widget(DeskScreen(app=self))
        else:
            self.changeScreen("MapScreen")

GameApp().run()