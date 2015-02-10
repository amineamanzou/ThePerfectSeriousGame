#!/usr/bin/python

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.button import Button
from kivy.animation import Animation

from GameScreen import GameScreen
from CustomWidget.DynImage import DynImage
from Dialog.DialogWidget import DialogWidget
from Dialog.DialogTextElement import DialogTextElement

Builder.load_file("GameScreens/DeskScreen.kv")

class DeskScreen(GameScreen):
    displayed = True
    notes = []

    noteSize = ("50dp", "100dp")

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

    def click(self):
        self.hideNote()
        self.ids.dialog.hide()

        """
        if self.displayed:
            self.ids.dialog.hide()
        else:
            self.ids.dialog.show()
        self.displayed = not self.displayed
        self.ids.dialog.changeElement(DialogTextElement(text="Attention, ceci est un test", isEnd=True))"""

    def addNote(self, note):
        self.notes.append(note)

        image = DynImage(source=note.filename, pos=(note.posX, note.posY), size=self.noteSize)
        image.bind(on_press=lambda x: self.showNoteContent(note.content))
        self.add_widget(image)

    def showNoteContent(self, content):
        self.ids.note.text = content
        slide = Animation(pos=(self.ids.note.pos[0], self.size[1] * 0.1))
        slide.start(self.ids.note)
        self.ids.shadow.size = self.size

    def hideNote(self):
        slide = Animation(pos=(self.ids.note.pos[0], self.size[1]))
        slide.start(self.ids.note)
        self.ids.shadow.size = (0, 0)

    def test(self):
        self.addNote(Note())

class Note:
    filename = "Images/profil-test.png"
    posX = 500
    posY = 500
    content = "[b]Toto[/b] Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta."