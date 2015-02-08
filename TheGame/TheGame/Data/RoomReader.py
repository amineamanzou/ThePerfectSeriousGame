#!/usr/bin/python

from XmlReader import XmlReader
from Models.Room import Room

class RoomReader(XmlReader):
    def __init__(self, filename, *args):
        XmlReader.__init__(self, filename, *args)

    def parse(self):
        listRoom = []
        for room in self.xml.getroot():
            aRoom = Room()
            aRoom.id = room.attrib.id
            aRoom.name = root[0].text
            aRoom.imageBackground = root[1].text
            aRoom.imageChar = root[2].text
            aRoom.xMin = root[3].attrib.min
            aRoom.xMax = root[3].attrib.max
            aRoom.yMin = root[4].attrib.min
            aRoom.yMax = root[4].attrib.min
            score= 0
            for fuck in root.findall('text'):
                aRoom.fuckDialogs.append(fuck.find('text').text)
            listRoom.append(aRoom)
        return listRoom