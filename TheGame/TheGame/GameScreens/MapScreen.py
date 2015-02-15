#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.layout import Layout
from kivy.animation import Animation

from GameScreen import GameScreen
from Dialog.DialogWidget import DialogWidget
from CustomWidget.DynImage import DynImage
from CustomWidget.ScoreSlider import ScoreSlider

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

        for room in self.rooms:
            if room.name != "bureau" and room.name != "boss":
                slider = ScoreSlider(size=("100dp", "30dp"))
                slider.pos = (room.xMax * self.size[0] - slider.size[0], room.yMin * self.size[1])
                self.ids.map.add_widget(slider)
       
    def click(self):
        if not self.ids.dialog.visible:
            mouse = self.app.app.window.mouse_pos
            width = self.size[0]
            height = self.size[1]

            for room in self.rooms:
                if(mouse[0] > room.xMin * width and mouse[0] < room.xMax * width and mouse[1] > room.yMin * height and mouse[1] < room.yMax * height):
                    if(room.name == "bureau"):
                        self.app.changeScreen("DeskScreen")
                    elif(room.name == "boss"):
                        self.app.changeScreen("BossScreen")
                    else:
                        try:
                            self.ids.room.source = room.imageBackground
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
        anim.start(self.ids.room)
