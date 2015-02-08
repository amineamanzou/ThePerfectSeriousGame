#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import ObjectProperty
from kivy.animation import Animation

Builder.load_file("GameScreens/GameScreen.kv")

class GameScreen(Widget):
    app = ObjectProperty(None)
    visible = False

    def __init__(self, **kwargs):
		super(GameWidget, self).__init__(**kwargs);self.size = self.app.app.window.size

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