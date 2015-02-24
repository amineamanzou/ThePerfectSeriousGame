#!/usr/bin/python

import kivy
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
from Models.Room import Room

Builder.load_file("GameScreens/StartScreen.kv")


class StartScreen(GameScreen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.ids.dialog.gameManager = self.app.gameManager
        self.ids.dialog.bind(visible=self.nextScreen)

        roomIntro = Room()
        roomIntro.id = 99
        roomIntro.imageChar = "Images/Characters/char_rh.png"

        self.ids.dialog.startDialog(roomIntro)

    def nextScreen(self, bindValue, bindedObject):
        if not self.ids.dialog.visible:
            self.app.changeScreen('MapScreen')