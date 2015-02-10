#!/usr/bin/python

from kivy.properties import NumericProperty, StringProperty, ListProperty

class Room():
    id = xMin = xMax = yMin = yMax = score = NumericProperty()
    name = imageBackground = imageChar = StringProperty()
    fuckDialogs = ListProperty()

    def __str__( self ):
        return "ROOM -- ID : " + str(self.id) + " NAME : " +  str(self.name)