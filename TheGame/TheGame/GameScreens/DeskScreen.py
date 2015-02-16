#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
import os
import kivy.metrics as Metrics
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.button import Button
from kivy.animation import Animation

from GameScreen import GameScreen
from CustomWidget.DynImage import DynImage
from Dialog.DialogWidget import DialogWidget
from Dialog.DialogTextElement import DialogTextElement

from Models.FicheDialog import FicheDialog

Builder.load_file("GameScreens/DeskScreen.kv")

class DeskScreen(GameScreen):
    noteSize = (0.05, 0.09)

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.ids.dialog.gameManager = self.app.gameManager
        self.ids.dialog.bind(visible=self.reloadNotes)
        self.ids.dialog.startDialog(self.app.gameManager.roomsManager.getRoomById(4))
        self.reloadNotes()

    def addNote(self, fiche):
        image = DynImage(source=fiche.image, pos=(self.size[0] * (fiche.x / 100.0), self.size[1] * (fiche.y/100.0)), size_hint=self.noteSize)
        image.bind(on_press=lambda x: self.showNoteContent(fiche))
        self.ids.ficheContainer.add_widget(image)

    def showNoteContent(self, fiche):
        if not self.ids.dialog.visible:
            self.ids.note.source = self.app.app.APPLICATION_PATH + os.path.normpath(fiche.content)
            slide = Animation(pos=(self.ids.note.pos[0], self.size[1] * 0.1))
            slide.start(self.ids.note)
            self.ids.shadow.size = self.size
            self.app.gameManager.setDialogDone(fiche.id)

    def hideNote(self):
        slide = Animation(pos=(self.ids.note.pos[0], self.size[1]))
        slide.start(self.ids.note)
        self.ids.shadow.size = (0, 0)

    def backToMap(self):
        if not self.ids.dialog.visible:
            self.app.changeScreen("MapScreen")

    def reloadNotes(self, opt1=None, opt2=None):
        self.ids.ficheContainer.clear_widgets()
        for fiche in self.app.gameManager.fiches:
            self.addNote(fiche)