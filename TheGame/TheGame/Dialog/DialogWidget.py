#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.animation import Animation

from DialogTextElement import DialogTextElement
from DialogElement import DialogElement

Builder.load_file("Dialog/DialogWidget.kv")

class DialogWidget(Widget):
    icon = StringProperty('')
    visible = BooleanProperty(True)
    gameManager = ObjectProperty()

    def __init__(self, **kwargs):
        super(DialogWidget, self).__init__(**kwargs)

    def hide(self):
        anim = Animation(pos=(self.pos[0], self.pos[1] - self.size[1]))
        anim.start(self)
        self.visible = False

    def show(self):
        anim = Animation(pos=(self.pos[0], self.pos[1] + self.size[1]))
        anim.start(self)
        self.visible = True

    def changeElement(self, element):
        self.ids.elementContainer = element
        self.ids.elementContainer.size = (self.ids.layout.size[0] - self.height, self.ids.layout.size[1])
        self.ids.elementContainer.displayDialog("Ceci est un test plus long pour voir si c'est justifie")