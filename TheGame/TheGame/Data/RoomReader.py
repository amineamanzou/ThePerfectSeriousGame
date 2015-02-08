#!/usr/bin/python

from XmlReader import XmlReader
from Models.Room import Room

class RoomReader(XmlReader):
    def __init__(self, filename, *args):
        return super().__init__(filename, *args)

    def parse(self):
        for room in self.xml.getroot():
            pass     