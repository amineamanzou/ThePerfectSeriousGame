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
    displayed = True

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.ids.dialog.gameManager = self.app.gameManager

        roomIntro = Room()
        roomIntro.id = 99
        roomIntro.imageChar = "Images/Characters/profil-test.png"

        self.ids.dialog.startDialog(roomIntro)


    def click(self):

        if self.displayed:
            self.ids.dialog.hide()
        else:
            self.ids.dialog.show()
        self.displayed = not self.displayed
        #self.ids.dialog.changeElement(DialogTextElement(text="Attention, ceci est un test", isEnd=True))