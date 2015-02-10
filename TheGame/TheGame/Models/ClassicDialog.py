#!/usr/bin/python

from kivy.properties import NumericProperty, StringProperty, ListProperty, BooleanProperty
from Models.AbstractDialog import AbstractDialog

class ClassicDialog(AbstractDialog):
    # les attributs du dialogue classique reprennent ceux d'un dialogue plus un texte
    text = StringProperty() # le text

    # redefinition du toString
    def __str__( self ):
        return "DIALOGUE CLASSIQUE -- ID : " + str(self.id) + " PARENT : " +  str(self.idParent) + " TEXT : " +  str(self.text)