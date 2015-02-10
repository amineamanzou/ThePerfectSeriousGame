#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

import os

from GameScreens.MapScreen import MapScreen
from GameScreens.DeskScreen import DeskScreen
from GameScreens.ErrorScreen import ErrorScreen

class GameApp(App):
    def build(self):
        from kivy.base import EventLoop
        EventLoop.ensure_window()
        self.window = EventLoop.window

        self.configure()
        self.root = GameWidget(app=self)

    def configure(self):
        self.window.size = (1200, 800)
        self.APPLICATION_PATH = os.path.dirname(__file__)
        self.APPLICATION_ENV = "DEBUG"


class GameWidget(Widget):
    app = ObjectProperty(None)
    gameScreen = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(GameWidget, self).__init__(**kwargs)
        self.changeScreen("MapScreen")

    def changeScreen(self, screen):
        if self.gameScreen is not None:
            self.gameScreen.hide()

            while self.gameScreen.visible:
                continue

        self.clear_widgets()
        if screen == "MapScreen":
            self.gameScreen = MapScreen(app=self, opacity=0)
        elif screen == "DeskScreen":
            self.gameScreen = DeskScreen(app=self, opacity=0)
        elif screen == "ErrorScreen":
            self.gameScreen = ErrorScreen()
        else:
            self.gameScreen = MapScreen(app=self, opacity=0)
        self.add_widget(self.gameScreen)

        self.gameScreen.show()

GameApp().run()