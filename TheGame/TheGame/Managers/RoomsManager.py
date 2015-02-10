#!/usr/bin/python

from Data.RoomReader import RoomReader

class RoomsManager(object):
    rooms = []
    xmlFilePath = ""

    def __init__(self, xmlFilePath, *args):
        self.xmlFilePath = xmlFilePath

    def getRooms(self):
        if len(self.rooms) == 0:
            try:
                reader = RoomReader(self.xmlFilePath)
                self.rooms = reader.parse()
            except Exception as ex:
                raise ex
        return self.rooms