#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.properties import NumericProperty, StringProperty, ListProperty, BooleanProperty
from Models.AbstractDialog import AbstractDialog

class EvaluationDialog(AbstractDialog):
    # les attributs du dialogue evaluation reprennent ceux d'un dialogue plus d'autres attributs
    title = StringProperty() # le titre
    choices = [] # la liste d'objets Choice

    # redefinition du toString
    def __str__( self ):
        return "DIALOGUE EVALUATION -- ID : " + str(self.id) + " PARENT : " +  str(self.idParent) + " TITLE : " +  str(self.title)