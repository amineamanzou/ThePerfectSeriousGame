#!/usr/bin/python
# -*- coding: utf-8 -*-

from XmlReader import XmlReader
from Models.AbstractDialog import AbstractDialog
from Models.ClassicDialog import ClassicDialog
from Models.FicheDialog import FicheDialog
from Models.EvaluationDialog import EvaluationDialog
from Models.EvalChoice import EvalChoice

from kivy.properties import ListProperty

class ChapterReader(XmlReader):
    # heritage de XML reader
    def __init__(self, filename, *args):
        XmlReader.__init__(self, filename, *args)

    # parse le fichier passe en parametre et retourne la liste de dialogue
    def parse(self):
        listDialog = [] # la future liste de dialogue qui sera retournee
        # pour chaque element dialog lu
        for dialog in self.xml.getroot():
            # on regarde son type
            if(dialog.attrib["type"] == "C"): #classique
                d = ClassicDialog()
                d.text = dialog[0].text.encode('utf-8') # le texte
            if(dialog.attrib["type"] == "F"): #fiche
                d = FicheDialog()
                d.content = dialog[0].text.encode('utf-8') # le content
                d.x = float(dialog[1].text) # x pos
                d.y = float(dialog[2].text) # y pos
                d.image = dialog[3].text # l'image
            if(dialog.attrib["type"] == "E"): #evaluation
                d = EvaluationDialog()
                d.title = dialog[0].text.encode('utf-8') # le titre
                listOption = []
                #on enregistre les choix
                d.choices = []  # il FAUT vider le tableau, sinon les valeurs sont conservess...
                for choice in dialog[1]:
                    option = EvalChoice()
                    option.id = int(choice.attrib["id"])
                    option.text = choice[0].text.encode('utf-8')
                    option.score = int(choice[1].text)
                    listOption.append(option)
                d.choices = listOption

            #on lui attribut ses elements communs a un dialog
            self.parseDialog(d, dialog)

            # on ajoute le dialog a la liste
            listDialog.append(d)
  
        return listDialog

    # attribut les elements communs a un dialog a partir d'un element xml dialog
    def parseDialog(self, dialog, xml):
        dialog.id = int(xml.attrib["id"])
        dialog.idParent = int(xml.attrib["idParent"])
        dialog.idBat = int(xml.attrib["idBat"])
        dialog.type = xml.attrib["type"]
        dialog.end = self.str_to_bool(xml.attrib["end"])
        dialog.done = self.str_to_bool("false")
        return dialog

    # string to boolean
    def str_to_bool(self, s):
        if s.lower() == 'true':
             return True
        elif s.lower() == 'false':
             return False
        else:
             raise ValueError # evil ValueError that doesn't tell you what the wrong value was

            