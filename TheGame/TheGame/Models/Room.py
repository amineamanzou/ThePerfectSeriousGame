#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.properties import NumericProperty, StringProperty, BoundedNumericProperty, ListProperty

class Room():

        # id, positions, et score
    id = xMin = xMax = yMin = yMax = NumericProperty()
    score = BoundedNumericProperty(0, min=-100, max=100, errorhandler=lambda x: 100 if x > 100 else -100)
    name = libelle = imageBackground = imageChar = StringProperty("") # nom de la piece et images
    fuckDialogs = [] # les dialogues en cas de "je n'ai rien a te dire"

    # redefinition du to string
    def __str__( self ):
        return "ROOM -- ID : " + str(self.id) + "\n" \
                + "NAME : " + str(self.name) + "\n" \
                + "SCORE : " + str(self.score)