#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.layout import Layout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.graphics.transformation import Matrix
from kivy.clock import Clock

from functools import partial

from GameScreen import GameScreen
from Dialog.DialogWidget import DialogWidget

Builder.load_file("GameScreens/MapScreen.kv")

class MapScreen(GameScreen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

    def click(self):
        mouse = self.app.app.window.mouse_pos
        width = self.size[0]
        height = self.size[1]

        if(mouse[0] > 0.20 * width and mouse[0] < 0.75 * width and mouse[1] < 0.95 * height and mouse[1] > 0.138 * height):
            if(mouse[0] < 0.44375 * width and mouse[1] > 0.566 * height):
                """ Case MOE """
            elif(mouse[0] > 0.44375 * width and mouse[1] > 0.75 * height):
                """ Case RH """
                print " Case RH "
            elif(mouse[0] < 0.34375 * width and mouse[1] < 0.394 * height):
                """ Case bureau """
                print " Case bureau "
            elif(mouse[0] > 0.34375 * width and mouse[0] < 0.56875 * width and mouse[1] < 0.394 * height):
                """ Case marketing """
                print " Case marketing "
            elif(mouse[0] > 0.56875 * width and mouse[1] < 0.577 * height):
                """ Case patron """
                print " Case patron "
            else:
                """ Couloir """
                print " Couloir "
        else:
            """ En dehors de la map """
            print " En dehors de la map "


class IconButton(ButtonBehavior, Image):
    pass