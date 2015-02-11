#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.layout import Layout

from GameScreen import GameScreen
from Dialog.DialogWidget import DialogWidget
from CustomWidget.DynImage import DynImage

from Data.RoomReader import RoomReader
from Data.StoryReader import StoryReader

from Models.AbstractDialog import AbstractDialog
from Models.ClassicDialog import ClassicDialog
from Models.FicheDialog import FicheDialog
from Models.EvaluationDialog import EvaluationDialog
from Models.EvalChoice import EvalChoice

Builder.load_file("GameScreens/MapScreen.kv")

class MapScreen(GameScreen):
    rooms = []

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

        try:
            self.rooms = self.app.roomsManager.getRooms()
        except Exception as ex:
            self.showError(ex.message)
       

    def click(self):
        mouse = self.app.app.window.mouse_pos
        width = self.size[0]
        height = self.size[1]

        for room in self.rooms:
            if(mouse[0] > room.xMin * width and mouse[0] < room.xMax * width and mouse[1] > room.yMin * height and mouse[1] < room.yMax * height):
                print room
                if(room.name == "bureau"):
                    self.app.changeScreen("DeskScreen")
                else:
                    pass
                break