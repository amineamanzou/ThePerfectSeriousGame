#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import NumericProperty

Builder.load_file("CustomWidget/ScoreSlider.kv")

class ScoreSlider(Widget):
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super(ScoreSlider, self).__init__(**kwargs)

        self.changeIcon()
        self.bind(score=self.changeIcon)

    def changeIcon(self):
        if self.score >= 50:
            self.ids.icon.source = "Images/Emoticons/emo-2.png"
        elif self.score >= 0:
            self.ids.icon.source = "Images/Emoticons/emo-1.png"
        elif self.score >= -50:
            self.ids.icon.source = "Images/Emoticons/emo-3.png"
        else:
            self.ids.icon.source = "Images/Emoticons/emo-4.png"