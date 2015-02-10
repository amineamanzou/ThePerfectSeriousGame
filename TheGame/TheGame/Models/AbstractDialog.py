#!/usr/bin/python

from kivy.properties import NumericProperty, StringProperty, ListProperty, BooleanProperty

class AbstractDialog():
    # les attributs du dialogue 
    id = idParent = idBat = NumericProperty() # id, id du dialogue parent, id du batiment
    end = BooleanProperty() # end = boolean a true si c'est un dialogue de fin
    done = BooleanProperty() # done = boolean a true si le dialog est termine par l'utilisateur
    type = StringProperty() # le type de dialogue (C = classique, E = Evaluation, F = Fiche)

    # redefinition du toString
    def __str__( self ):
        return "DIALOGUE -- ID : " + str(self.id) + " PARENT : " +  str(self.idParent) + " TYPE : " +  str(self.type)