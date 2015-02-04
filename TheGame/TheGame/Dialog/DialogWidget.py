#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder

Builder.load_file("Dialog/DialogWidget.kv")

class DialogWidget(Widget):
    icon = ""
    def __init__(self, **kwargs):
        super(DialogWidget, self).__init__(**kwargs)