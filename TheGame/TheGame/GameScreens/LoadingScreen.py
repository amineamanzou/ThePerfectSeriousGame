#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder

from GameScreen import GameScreen

Builder.load_file("GameScreens/LoadingScreen.kv")

class LoadingScreen(GameScreen):
    pass