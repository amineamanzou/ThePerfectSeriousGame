#!/usr/bin/python

from xml.etree.ElementTree import ElementTree

class XmlReader():
    xml = object

    def __init__(self, filename, *args):
        try:
            self.xml = ElementTree()
            self.xml.parse(filename)
        except IOError as ex:
            raise Exception("I/O error({0}): {1}".format(ex.errno, ex.strerror))