#!/usr/bin/python

from kivy.properties import NumericProperty, StringProperty, ListProperty

class Room():
    id = xMin = xMax = yMin = yMax = score = NumericProperty()
    name = imageBackground = imageChar = StringProperty()
    dialogs = ListProperty()