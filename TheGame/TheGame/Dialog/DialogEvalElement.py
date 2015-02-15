#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.button import Button
from kivy.properties import ListProperty, BooleanProperty

from DialogElement import DialogElement

Builder.load_file("Dialog/DialogEvalElement.kv")

class DialogEvalElement(DialogElement):
    options = ListProperty([])
    close = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(DialogTextElement, self).__init__(**kwargs)
        for option in self.options:
            self.ids.layoutButtons.add_widget(Button(text=option.text))

    def click(self):
        self.close = True