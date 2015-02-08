#!/usr/bin/python

import xml.etree.ElementTree

class XmlReader():
    xml = object

    def __init__(self, filename, *args):
        try:
            self.xml = ElementTree.parse(filename)
        except Exception:
            raise Exception("Erreur lors de la récupèration du xml") 

        return super().__init__(*args)