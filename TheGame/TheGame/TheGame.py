#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy import platform

import os
if platform == 'win':
    from win32api import GetSystemMetrics

from GameScreens.StartScreen import StartScreen
from GameScreens.MapScreen import MapScreen
from GameScreens.DeskScreen import DeskScreen
from GameScreens.BossScreen import BossScreen
from GameScreens.CreditsScreen import CreditsScreen

from Managers.GameManager import GameManager

from CustomWidget.MenuDialog import MenuDialog

class GameApp(App):
    menu = ObjectProperty()

    def build(self):
        from kivy.base import EventLoop
        EventLoop.ensure_window()
        self.window = EventLoop.window
        self.menu = MenuDialog(app=self)

        self.configure()
        self.root = GameWidget(app=self)
        self.root.keyboard = Window.request_keyboard(self.keyboard_closed, self.root)
        self.root.keyboard.bind(on_key_down=self.on_keyboard_down)

    def configure(self):
        self.APPLICATION_ENV = "PROD"

        if self.APPLICATION_ENV == "DEV":
            self.window.size = (1200, 800)
        else:
            if platform == 'win':
                self.window.size = (min(GetSystemMetrics(0), 1920), min(GetSystemMetrics(1), 1080))
            elif platform == 'macosx':
                self.window.size = (1920, 1080)
            self.window.borderless = True
            self.window.fullscreen = "fake"
        
        self.APPLICATION_PATH = os.path.dirname(os.path.abspath(__file__))

    def keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self.on_keyboard_down)
        self.keyboard = None

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'escape':
            self.menu.open()
        return True

    def quitter(self):
        App.get_running_app().stop()
        
class GameWidget(Widget):
    app = ObjectProperty(None)
    gameScreen = ObjectProperty(None)
    gameManager = object

    def __init__(self, **kwargs):
        super(GameWidget, self).__init__(**kwargs)
        
        try:
            self.changeScreen("LoadingScreen")
            self.gameManager = GameManager(self.app.APPLICATION_PATH, self.app.APPLICATION_ENV)
            self.changeScreen("StartScreen")
        except Exception as ex:
            self.gameScreen.showError(ex.message)

    def changeScreen(self, screen):
        if self.gameScreen is not None:
            self.gameScreen.hide()

            while self.gameScreen.visible:
                continue

        self.clear_widgets()
        if screen == "StartScreen":
            self.gameScreen = StartScreen(app=self, opacity=0)
        elif screen == "MapScreen":
            self.gameScreen = MapScreen(app=self, opacity=0)
        elif screen == "DeskScreen":
            self.gameScreen = DeskScreen(app=self, opacity=0)
        elif screen == "BossScreen":
            self.gameScreen = BossScreen(app=self, opacity=0)
        elif screen == "CreditsScreen":
            self.gameScreen = CreditsScreen(app=self, opacity=0)
        else:
            self.gameScreen = MapScreen(app=self, opacity=0)
        self.add_widget(self.gameScreen)

        self.gameScreen.show()

GameApp().run()