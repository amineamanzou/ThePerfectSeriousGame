#!/usr/bin/python

from kivy.properties import NumericProperty, StringProperty, ListProperty, BooleanProperty
from Models.AbstractDialog import AbstractDialog

class FicheDialog(AbstractDialog):
    # les attributs du dialogue fiche reprennent ceux d'un dialogue plus d'autres attributs
    content = image = StringProperty() # lecontenu et l'image
    x = y = NumericProperty() # la position de l'image

    # redefinition du toString
    def __str__( self ):
        return "DIALOGUE FICHE -- ID : " + str(self.id) + " PARENT : " +  str(self.idParent) + " CONTENT : " +  str(self.content)