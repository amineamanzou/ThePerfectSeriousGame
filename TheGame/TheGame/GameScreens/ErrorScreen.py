#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty

Builder.load_file("GameScreens/ErrorScreen.kv")

class ErrorScreen(GridLayout):
    app = ObjectProperty()
    debug = StringProperty()

    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)

    def setDebugMessage(self, message):
        if self.app.app.APPLICATION_ENV == "DEBUG":
            self.debug = message