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
        dialog = DialogTextElement()
        dialog.type = "C"
        dialog.text = "Bien, je pense qu'il est temps de faire un point à propos de l'étude préalable à la création de notre serious game."
        self.dialogs.append(dialog)

        rooms = self.app.gameManager.roomsManager.getRooms()
        globalscore = 0
        for room in rooms:
            globalscore += room.score
            dialog = DialogTextElement()
            dialog.type = "C"
            if room.score >= 50:
                dialog.text = "J'ai eu des retours positifs en passant devant le département " + room.name + " ils sont très entousiaste à l'idée de jouer à un Serious Game, vous avez su les motiver et les impliquer dans le projet."
            elif room.score >= 0:
                dialog.text = "Comme vous l'avez constaté le département " + room.name + " est favorable à la poursuite du projet"
            elif room.score >= -50:
                dialog.text = "J'ai entendu dire que le département " + room.name + " n'est pas très enthousiaste à l'idée "
            else:
                dialog.text = "Le département " + room.name + " est fortement hostile au projet, vous n'avez pas du tout cerné leurs attentes et avez négligé leur point de vue."
            self.dialogs.append(dialog)

        dialog = DialogTextElement()
        dialog.type = "C"
        if globalscore >= 300:
            dialog.text = "Tu as du talent, je pense qu'on est sur la bonne voie. J'autorise le lancement de ce projet."
        elif globalscore >= 200:
            dialog.text = "Beau boulôt, je pense qu'on peut mener le projet ensemble avec les départements."
        elif globalscore >= 100:
            dialog.text = "Mmmh... Go ou No go ? J'ai pas beaucoup de retours positifs mais on va quand même tenter le projet."
        elif globalscore >= 0:
            dialog.text = "Mmmh... Go ou No go ? J'ai pas beaucoup de retours positifs malheursement il faut refaire une autre étude préalable."
        elif globalscore >= -100:
            dialog.text = "J'ai vraiment pas beaucoup de retours positifs, je pense qu'on devrait mettre en place une formation e-learning."
        elif globalscore >= -200:
            dialog.text = "Qu'est ce qui se passe ? J'ai que des mauvais retours. J'ai bien peur que les départements pensent à faire grève à cause de ce projet. No go."
        else:
            dialog.text = ""
        self.dialogs.append(dialog)

    def end(self, obj, val):
        self.app.changeScreen("CreditsScreen")