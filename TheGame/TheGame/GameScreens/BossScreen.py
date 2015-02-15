#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.button import Button
from kivy.animation import Animation

from GameScreen import GameScreen
from CustomWidget.DynImage import DynImage
from Dialog.DialogWidget import DialogWidget
from Dialog.DialogTextElement import DialogTextElement

Builder.load_file("GameScreens/BossScreen.kv")

class BossScreen(GameScreen):
    displayed = True
    rooms = []

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

    def click(self):
        if self.displayed:
            self.ids.dialog.hide()
        else:
            self.ids.dialog.show()
        self.displayed = not self.displayed

    def bossDecision(self):
        rooms = self.app.gameManager.roomsManager.getRooms()
        globalscore = 0
        for room in rooms:
            globalscore += room.score
        if (globalscore > 0):
            print "Boss : Go pour le projet les differents departements ont l'air satisfait de votre travail."
        else:
            print "Boss : No go, desole ton projet ne reponds pas au besoin de l'entreprise. On a besoin de dynamiser les differents departements."