#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

import os

from GameScreens.MapScreen import MapScreen
from GameScreens.DeskScreen import DeskScreen
from Managers.RoomsManager import RoomsManager

from Data.ChapterReader import ChapterReader
from Data.StoryReader import StoryReader

class GameApp(App):
    def build(self):
        from kivy.base import EventLoop
        EventLoop.ensure_window()
        self.window = EventLoop.window

        self.configure()
        self.root = GameWidget(app=self)

    def configure(self):
        self.window.size = (1200, 800)
        self.APPLICATION_PATH = os.path.dirname(os.path.abspath(__file__))
        self.APPLICATION_ENV = "DEBUG"


class GameWidget(Widget):
    app = ObjectProperty(None)
    gameScreen = ObjectProperty(None)
    roomsManager = object

    def __init__(self, **kwargs):
        super(GameWidget, self).__init__(**kwargs)
        self.roomsManager = RoomsManager(self.app.APPLICATION_PATH + os.path.normpath('/Ressources/rooms.xml'))
        
        """
        rooms = self.roomsManager.getRooms()
        print "Y A UN BUG LA A CAUSE DE ROOM READER"
        for r in rooms:
            print r.fuckDialogs

        ##### TEST CHAPTER READER
        testChapterReader = ChapterReader(self.app.APPLICATION_PATH + os.path.normpath('/Ressources/Chapters/chapter1.xml'))
        dialogs = testChapterReader.parse()
        print "Y A UN BUG LA A CAUSE DE CHAPTER READER"
        for d in dialogs:
            if(d.type == "E"):
                print d.choices

        ##### TEST STORY READER
        testStoryReader = StoryReader(self.app.APPLICATION_PATH + os.path.normpath('/Ressources/story.xml'))
        chapters = testStoryReader.parse()
        print "Y A UN BUG LA A CAUSE DE STORY READER"
        for c in chapters:
            print c.listIdMustBeRead
        """

        self.changeScreen("MapScreen")

    def changeScreen(self, screen):
        if self.gameScreen is not None:
            self.gameScreen.hide()

            while self.gameScreen.visible:
                continue

        self.clear_widgets()
        if screen == "MapScreen":
            self.gameScreen = MapScreen(app=self, opacity=0)
        elif screen == "DeskScreen":
            self.gameScreen = DeskScreen(app=self, opacity=0)
        else:
            self.gameScreen = MapScreen(app=self, opacity=0)
        self.add_widget(self.gameScreen)

        self.gameScreen.show()

GameApp().run()