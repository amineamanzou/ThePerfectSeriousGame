#!/usr/bin/python

from XmlReader import XmlReader
from Models.Room import Room

class RoomReader(XmlReader):
    def __init__(self, filename, *args):
        XmlReader.__init__(self, filename, *args)

    def parse(self):
        # pour l'explication du code, voir l'exemple commente dans StoryReader.py
        listRoom = []
        print listRoom
        for room in self.xml.getroot():
            aRoom = Room()   
            aRoom.id = room.attrib['id']
            aRoom.name = room[0].text
            aRoom.imageBackground = room[1].text
            aRoom.imageChar = room[2].text
            aRoom.xMin = float(room[3].attrib['min'])
            aRoom.xMax = float(room[3].attrib['max'])
            aRoom.yMin = float(room[4].attrib['min'])
            aRoom.yMax = float(room[4].attrib['max'])
            score= 0
            for fuck in room.findall('text'):
                aRoom.fuckDialogs.append(fuck.find('text').text)
            listRoom.append(aRoom)
        return listRoom