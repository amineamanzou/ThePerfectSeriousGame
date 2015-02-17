#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Builder
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

Builder.load_file("CustomWidget/MenuDialog.kv")

class MenuDialog(Popup):
    app = ObjectProperty(None)
    title = "Menu"
    auto_dismiss = False

    def __init__(self, **kwargs):
        super(Popup, self).__init__(**kwargs)