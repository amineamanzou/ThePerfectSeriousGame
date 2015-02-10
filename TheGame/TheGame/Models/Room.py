#!/usr/bin/python

from kivy.properties import NumericProperty, StringProperty, ListProperty

class Room():
    # les attributs de la piece 
    id = xMin = xMax = yMin = yMax = score = NumericProperty() # id, positions, et score
    name = imageBackground = imageChar = StringProperty() # nom de la piece et images
    fuckDialogs = ListProperty() # les dialogues en cas de "je n'ai rien a te dire"

    # redefinition du to string
    def __str__( self ):
        return "ROOM -- ID : " + str(self.id) + " NAME : " +  str(self.name)