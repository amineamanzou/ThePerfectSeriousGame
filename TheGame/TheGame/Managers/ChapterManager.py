#!/usr/bin/python

from Data.ChapterReader import ChapterReader

class ChapterManager(object):
    dialogs = []
    availables = []
    xmlFilePath = ""

    def __init__(self, xmlFilePath, *args):
        self.xmlFilePath = xmlFilePath

        try:
            reader = ChapterReader(self.xmlFilePath)
            self.dialogs = reader.parse()
        except Exception as ex:
            raise ex

        sorted(self.dialogs, key=lambda dialog: dialog.idParent)
        self.availables.append(self.dialogs[0])

    def setDone(self, dialogId):
        for dialog in self.availables:
            if(dialog.id == dialogId):     
                dialog.done = True
                self.availables.remove(dialog)
                for nextDialog in self.dialogs:
                    if(nextDialog.idParent == dialogId):
                        self.availables.append(nextDialog)

    def getNextDialog(self, roomId):
        for dialog in self.availables:
            if(dialog.idBat == roomId):
                return dialog

    def haveNext(self, dialogId):
        for nextDialog in self.dialogs:
            if(nextDialog.idParent == dialogId):
                if(nextDialog.type != "F"):
                    return True
        return False