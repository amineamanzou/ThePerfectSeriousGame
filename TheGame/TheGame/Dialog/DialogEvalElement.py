#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.button import Button
from kivy.properties import ListProperty, NumericProperty, StringProperty, BooleanProperty

from DialogElement import DialogElement

Builder.load_file("Dialog/DialogEvalElement.kv")

class DialogEvalElement(DialogElement):
    options = ListProperty([])
    result = NumericProperty(0)
    title = StringProperty()
    close = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(DialogEvalElement, self).__init__(**kwargs)
        i = 0
        for option in self.options:
            button = CustomButton(text=option.text, val=i, markup=True)
            button.bind(on_press=self.click)
            self.ids.layoutButtons.add_widget(button)
            i += 1

        self.ids.labelEval.text = self.title

    def click(self, o):
        self.result = o.val
        self.close = True

class CustomButton(Button):
    val = NumericProperty()