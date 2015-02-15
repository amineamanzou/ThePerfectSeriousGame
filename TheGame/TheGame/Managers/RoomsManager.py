#!/usr/bin/python
# -*- coding: utf-8 -*-

from Data.RoomReader import RoomReader

class RoomsManager(object):
    rooms = []
    xmlFilePath = ""

    def __init__(self, xmlFilePath, *args):
        self.xmlFilePath = xmlFilePath

        try:
            reader = RoomReader(self.xmlFilePath)
            self.rooms = reader.parse()
        except Exception as ex:
            raise ex

    def getRooms(self):
        return self.rooms

    def getRoomById(self, roomId):
        for room in self.rooms:
            if room.id == roomId:
                return room