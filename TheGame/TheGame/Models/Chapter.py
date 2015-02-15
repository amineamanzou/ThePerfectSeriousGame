#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.properties import NumericProperty, StringProperty, ListProperty

class Chapter():
    # les attributs du chapitre 
    id = nextChapter = NumericProperty() # id et chapitre suivant
    file = StringProperty() # fichier associe a lire
    listIdMustBeRead = [] # les id qui doivent etre lus pour finir le chapitre

    # redefinition du toString
    def __str__( self ):
        return "CHAPTER -- ID : " + str(self.id) + " FILE : " +  str(self.file)