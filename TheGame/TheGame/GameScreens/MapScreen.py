#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.layout import Layout
from kivy.animation import Animation
from kivy.uix.image import Image

from GameScreen import GameScreen
from Dialog.DialogWidget import DialogWidget
from CustomWidget.DynImage import DynImage
from CustomWidget.RoomTitle import RoomTitle
from CustomWidget.ScoreSlider import ScoreSlider

import os

Builder.load_file("GameScreens/MapScreen.kv")

class MapScreen(GameScreen):
    rooms = []

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        try:
            self.rooms = self.app.gameManager.roomsManager.getRooms()
        except Exception as ex:
            self.showError(ex.message)

        self.ids.dialog.gameManager = self.app.gameManager
        self.ids.dialog.bind(visible=self.setRoomVisible)
        self.reloadIcons()
       
    def click(self):
        if not self.ids.dialog.visible:
            mouse = self.app.app.window.mouse_pos
            border_x = self.ids.map.pos[0]
            border_y = self.ids.map.pos[1]
            image_width = self.ids.map.size[0]
            image_height = self.ids.map.size[1]

            for room in self.rooms:
                if(mouse[0] > room.xMin * image_width + border_x and mouse[0] < room.xMax * image_width + border_x and mouse[1] > room.yMin * image_height + border_y and mouse[1] < room.yMax * image_height + border_y):
                    if(room.name == "bureau"):
                        self.app.changeScreen("DeskScreen")
                    elif(room.name == "boss" and self.app.gameManager.end):
                        self.app.changeScreen("BossScreen")
                    else:
                        try:
                            self.ids.room.source = room.imageBackground
                            self.ids.roomLabel.libelle = room.libelle
                            self.ids.dialog.startDialog(room)
                            self.ids.dialog.show()
                        except Exception as ex:
                            self.showError(ex.message)
                    break

    def setRoomVisible(self, obj, visible):
        if visible:
            anim = Animation(opacity=1)
        else:
            anim = Animation(opacity=0)
            self.reloadIcons()
        anim.start(self.ids.room)
        anim.start(self.ids.roomLabel)

    def reloadIcons(self):
        self.ids.map.clear_widgets()
        for room in self.rooms:
            if room.name != "bureau" and room.name != "boss":
                slider = ScoreSlider(size=("30dp", "30dp"), pos=(room.xMin * self.ids.map.size[0] + self.ids.map.pos[0] + 10, room.yMin * self.ids.map.size[1] + self.ids.map.pos[1]), score=room.score)
                self.ids.map.add_widget(slider)
            if(self.app.gameManager.dialogAvailableInRoom(room.id)):
                warning = Image(source=(self.app.app.APPLICATION_PATH + os.path.normpath('/Images/warning.png')), size=("60dp", "80dp"), keep_ratio = False, allow_stretch = True)
                warning.pos = (room.xMax * self.ids.map.size[0] + self.ids.map.pos[0] - warning.size[0], room.yMin * self.ids.map.size[1] + self.ids.map.pos[1] + 10)
                self.ids.map.add_widget(warning)