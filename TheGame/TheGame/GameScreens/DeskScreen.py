#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder

from GameScreen import GameScreen
from CustomWidget.DynImage import DynImage

Builder.load_file("GameScreens/DeskScreen.kv")

class DeskScreen(GameScreen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

    def click(self):
        pass