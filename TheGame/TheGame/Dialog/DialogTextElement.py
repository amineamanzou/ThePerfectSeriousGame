#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

from DialogElement import DialogElement

Builder.load_file("Dialog/DialogTextElement.kv")

class DialogTextElement(DialogElement):
    text = StringProperty('')
    isEnd = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(DialogTextElement, self).__init__(**kwargs)
        self.ids.textViewer.text = self.text

        if self.isEnd:
            self.ids.nextButton.text = "Partir"
        else:
            self.ids.nextButton.text = "Suite"