#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

from DialogElement import DialogElement

Builder.load_file("Dialog/DialogEvalElement.kv")

class DialogEvalElement(DialogElement):
    text = StringProperty('')
    isEnd = BooleanProperty(False)
    close = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(DialogTextElement, self).__init__(**kwargs)
        self.ids.textViewer.text = self.text

    def click(self):
        self.close = True