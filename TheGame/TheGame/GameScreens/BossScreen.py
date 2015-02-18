#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.button import Button
from kivy.animation import Animation

from GameScreen import GameScreen
from CustomWidget.DynImage import DynImage
from CustomWidget.RoomTitle import RoomTitle
from Dialog.DialogWidget import DialogWidget
from Dialog.DialogTextElement import DialogTextElement

Builder.load_file("GameScreens/BossScreen.kv")

class BossScreen(GameScreen):
    rooms = []
    dialogs = []

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.bossDecision()
        self.ids.dialog.dialogsCustom = self.dialogs
        self.ids.dialog.startDialogCustom()
        self.ids.dialog.bind(visible=self.end)

    def bossDecision(self):
        rooms = self.app.gameManager.roomsManager.getRooms()
        globalscore = 0
        for room in rooms:
            globalscore += room.score
            dialog = DialogTextElement()
            dialog.type = "C"
            if room.score >= 50:
                dialog.text = "Le département " + room.name + " est très entousiaste à l'idée du Serious Game de notre entreprise, vous avez sus les motiver et les impliquer dans le projet."
            elif room.score >= 0:
                dialog.text = "Le département " + room.name + " est favorable à la poursuite du projet"
            elif room.score >= -50:
                dialog.text = "Le département " + room.name + " n'est pas très "
            else:
                dialog.text = "Le département " + room.name + " est fortement hostile au projet, vous n'avez pas du tout cerné leurs attentes et avez négligé leur point de vue."
            self.dialogs.append(dialog)

        dialog = DialogTextElement()
        dialog.type = "C"
        if globalscore >= 400:
            dialog.text = ""
        elif globalscore >= 300:
            dialog.text = ""
        elif globalscore >= 200:
            dialog.text = ""
        elif globalscore >= 100:
            dialog.text = ""
        elif globalscore >= 0:
            dialog.text = ""
        elif globalscore >= -100:
            dialog.text = ""
        elif globalscore >= -200:
            dialog.text = ""
        elif globalscore >= -300:
            dialog.text = ""
        else:
            dialog.text = ""
        self.dialogs.append(dialog)

    def end(self, obj, val):
        self.app.changeScreen("CreditsScreen    ")