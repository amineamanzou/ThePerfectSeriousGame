#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import StringProperty

Builder.load_file("CustomWidget/RoomTitle.kv")

class RoomTitle(Widget):
    libelle = StringProperty()

    def __init__(self, **kwargs):
        return super(RoomTitle, self).__init__(**kwargs)