#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.clock import Clock

from kivy.uix.label import Label

import itertools

from GameScreens.ErrorScreen import ErrorScreen

Builder.load_file("GameScreens/GameScreen.kv")

class GameScreen(Widget):
    app = ObjectProperty(None)
    visible = False

    def __init__(self, **kwargs):
        super(GameWidget, self).__init__(**kwargs)
        self.size = self.app.app.window.size

    def show(self):
        anim = Animation(opacity=1, duration=2)
        anim.bind(on_complete=self.setVisible(True))
        anim.start(self)

    def hide(self):
        anim = Animation(opacity=0, duration=2)
        anim.bind(on_complete=self.setVisible(False))
        anim.start(self)

    def setVisible(self, bool, **kwargs):
        self.visible = bool

    def showError(self, ex):
        x = itertools.count(0)
        message = "Une erreur est survenue lors de l'execution de l'ecran : " + type(self).__name__
        message += "\n" + ex

        error = ErrorScreen(size=self.size, app=self.app)
        error.setDebugMessage(message)

        self.clear_widgets()
        self.add_widget(error)
