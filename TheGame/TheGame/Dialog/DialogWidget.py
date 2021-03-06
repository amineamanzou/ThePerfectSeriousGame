#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.animation import Animation

from DialogTextElement import DialogTextElement
from DialogEvalElement import DialogEvalElement
from DialogElement import DialogElement

import random

Builder.load_file("Dialog/DialogWidget.kv")

class DialogWidget(Widget):
    icon = StringProperty('')
    visible = BooleanProperty(True)
    gameManager = ObjectProperty()
    currentRoom = ObjectProperty()
    dialog = object
    dialogsCustom = ListProperty()

    def __init__(self, **kwargs):
        super(DialogWidget, self).__init__(**kwargs)

    def hide(self):
        anim = Animation(pos=(self.pos[0], self.pos[1] - self.size[1]))
        anim.start(self)
        self.visible = False

    def show(self):
        anim = Animation(pos=(self.pos[0], self.pos[1] + self.size[1]))
        anim.start(self)
        self.visible = True

    def startDialog(self, room):
        self.currentRoom = room   
        self.icon = self.currentRoom.imageChar
        
        self.dialog = self.gameManager.getNextDialog(self.currentRoom.id)

        if self.dialog == None: # S'il s'agit d'une fiche ou pas de dialogue
            if len(self.currentRoom.fuckDialogs) != 0:
                dialog = self.currentRoom.fuckDialogs[random.randint(0, len(self.currentRoom.fuckDialogs) - 1)]
                element = DialogTextElement(text=dialog, isEnd=True)
            else:
                if self.visible:
                    self.hide()
                return None
        elif self.dialog.type == "C":
            element = DialogTextElement(text=self.dialog.text, isEnd=not self.gameManager.chapterManager.haveNext(self.dialog.id))
        elif self.dialog.type == "E":
            element = DialogEvalElement(options=self.dialog.choices, title=self.dialog.title)
        else:
            raise Exception("Type de dialogue inconnu")

        element.bind(close=self.closeElement)
        
        self.changeElement(element)

        return True

    def startDialogCustom(self):
        if len(self.dialogsCustom) > 0:
            self.dialog = self.dialogsCustom[0]
            self.dialogsCustom.remove(self.dialog)

            if self.dialog.type == "C":
                element = DialogTextElement(text=self.dialog.text, isEnd=len(self.dialogsCustom) == 0)
            elif self.dialog.type == "E":
                element = DialogEvalElement(options=self.dialog.choices, title=self.dialog.title)
            else:
                raise Exception("Type de dialogue inconnu")

            element.bind(close=self.closeCustomElement)
            self.changeElement(element)

    def changeElement(self, element):
        self.ids.elementContainer.clear_widgets()
        element.pos = self.ids.elementContainer.pos
        self.ids.elementContainer.add_widget(element)

    def closeElement(self, obj, val):
        if self.dialog != None:
            try:
                self.gameManager.setDialogDone(self.dialog.id)
            except Exception as ex:
                pass
            if self.dialog.type == "E":
                self.currentRoom.score += self.dialog.choices[obj.result].score

        if self.gameManager.getNextDialog(self.currentRoom.id) != None:
            self.startDialog(self.currentRoom)
        else:
            self.ids.elementContainer.clear_widgets()
            self.hide()

    def closeCustomElement(self, obj, val):
        if len(self.dialogsCustom) > 0:
            self.startDialogCustom()
        else:
            self.ids.elementContainer.clear_widgets()
            self.hide()