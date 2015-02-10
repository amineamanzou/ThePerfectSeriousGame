#!/usr/bin/python

from kivy.properties import NumericProperty, StringProperty

class EvalChoice():
    # les attributs du choix 
    id = score = NumericProperty() # id et score du choix 
    text = StringProperty() # texte du choix

    # redefinition du toString
    def __str__( self ):
        return "CHOICE -- ID : " + str(self.id) + " TEXTE : " +  str(self.text) + " SCORE : " +  str(self.score)