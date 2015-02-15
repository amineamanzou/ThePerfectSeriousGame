#!/usr/bin/python
# -*- coding: utf-8 -*-

from XmlReader import XmlReader
from Models.Chapter import Chapter

class StoryReader(XmlReader):
    # heritage de XML reader
    def __init__(self, filename, *args):
        XmlReader.__init__(self, filename, *args)

    # parse le fichier passe en parametre
    def parse(self):
        listChapter = [] # la future liste qui sera retournee
        # pour chaque element chapitre lu
        for chapter in self.xml.getroot():
            aChapter = Chapter()   # on creer un chapitre
            aChapter.id = int(chapter.attrib['id']) # on recupere son attribut id dans le XML
            aChapter.file = chapter[0].text # on recupere son element file
            aChapter.nextChapter = int(chapter[1].text) # son chapitre suivant...
            # et pour tous les id a lire, on les enregistres
            aChapter.listIdMustBeRead = []  # il FAUT vider le tableau, sinon les valeurs sont conservess...
            for idMustBeRead in chapter[2]:
                aChapter.listIdMustBeRead.append(int(idMustBeRead.text))

            #on ajoute le chapitre cree a notre liste
            listChapter.append(aChapter)

        # quand il n'y a plus de chapitre a lire, on retourne la liste
        return listChapter