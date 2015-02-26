#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.uix.rst import RstDocument
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file("CustomWidget/RstButton.kv")

class RstButton(Button):
    source = StringProperty()

    def __init__(self, **kwargs):
        super(RstButton, self).__init__(**kwargs)
        self.ids.document.text = "[color=ffffff]" + self.source + "[/color]"
        self.ids.fake.bind(on_press=self.press)

    def press(self, obj):
        self._do_press()
        self.dispatch('on_press')