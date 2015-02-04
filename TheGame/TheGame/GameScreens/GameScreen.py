#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import ObjectProperty

Builder.load_file("GameScreens/GameScreen.kv")

class GameScreen(Widget):
    app = ObjectProperty(None)

    def __init__(self, **kwargs):
		super(GameWidget, self).__init__(**kwargs);self.size = self.app.app.window.size