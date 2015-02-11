#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty

Builder.load_file("CustomWidget/ScoreSlider.kv")

class ScoreSlider(Widget):
    score = NumericProperty(0)