#!/usr/bin/python

from Managers.RoomsManager import RoomsManager
from Managers.StoryManager import StoryManager
from Managers.ChapterManager import ChapterManager

import os

class GameManager(object):
    roomsManager = storyManager = chapterManager = object
    basePath = ""
    end = False

    def __init__(self, basePath, *args):
        self.basePath = basePath

        try:
            self.roomsManager = RoomsManager(self.basePath + os.path.normpath('/Ressources/rooms.xml'))
            self.storyManager = StoryManager(self.basePath + os.path.normpath('/Ressources/story.xml'))
            self.chapterManager = ChapterManager(self.basePath + os.path.normpath(self.storyManager.getNextChapter().file))
        except Exception as ex:
            raise ex

    def getNextDialog(self, roomId):
        if not self.end:
            try:
               return self.chapterManager.getNextDialog(roomId)
            except Exception as ex:
                raise ex

    def setDialogDone(self, dialogId):
        if not self.end:
            try:
                self.chapterManager.setDone(dialogId)
                if(len(self.chapterManager.availables) == 0):
                    nextChapter = self.storyManager.getNextChapter()
                    if(nextChapter == None):
                        self.end = True
                    else:
                        self.chapterManager = ChapterManager(self.basePath + os.path.normpath(nextChapter.file))
            except Exception as ex:
                raise ex