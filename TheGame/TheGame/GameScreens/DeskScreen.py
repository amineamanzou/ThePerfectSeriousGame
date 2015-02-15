#!/usr/bin/python

import kivy
import kivy.metrics as Metrics
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.button import Button
from kivy.animation import Animation

from GameScreen import GameScreen
from CustomWidget.DynImage import DynImage
from Dialog.DialogWidget import DialogWidget
from Dialog.DialogTextElement import DialogTextElement

from Models.FicheDialog import FicheDialog

Builder.load_file("GameScreens/DeskScreen.kv")

class DeskScreen(GameScreen):
    displayed = True

    noteSize = (0.05, 0.09)

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        
        for fiche in self.app.gameManager.fiches:
            self.addNote(fiche)

        self.ids.dialog.gameManager = self.app.gameManager

    def click(self):
        self.hideNote()

        if self.displayed:
            self.ids.dialog.hide()
        else:
            self.ids.dialog.show()
        self.displayed = not self.displayed
        self.ids.dialog.changeElement(DialogTextElement(text="Attention, ceci est un test", isEnd=True))

    def addNote(self, fiche):
        image = DynImage(source=fiche.image, pos=(self.size[0] * (fiche.x / 100.0), self.size[1] * (fiche.y/100.0)), size_hint=self.noteSize)
        image.bind(on_press=lambda x: self.showNoteContent(fiche.content))
        self.ids.ficheContainer.add_widget(image)

    def showNoteContent(self, content):
        self.ids.note.source = content
        slide = Animation(pos=(self.ids.note.pos[0], self.size[1] * 0.1))
        slide.start(self.ids.note)
        self.ids.shadow.size = self.size

    def hideNote(self):
        slide = Animation(pos=(self.ids.note.pos[0], self.size[1]))
        slide.start(self.ids.note)
        self.ids.shadow.size = (0, 0)

        """
    def test(self):
        self.addNote(Note())

class Note:
    filename = "Images/profil-test.png"
    posX = 500
    posY = 500
    content = "[b]Toto[/b] Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta.Ut semper leo vel justo luctus vestibulum. Duis tincidunt odio diam, sit amet cursus ex dignissim ut. Cras in urna dui. Donec pulvinar luctus varius. Morbi ultricies condimentum ex, quis ullamcorper justo scelerisque consectetur. Nulla in massa finibus justo iaculis fringilla. Aliquam porttitor odio mi, id elementum turpis varius commodo. Mauris viverra massa vitae malesuada luctus. Maecenas dapibus luctus turpis. Ut egestas in nulla facilisis rutrum. Suspendisse iaculis malesuada bibendum. Etiam pellentesque lacinia neque, suscipit suscipit mauris feugiat vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus egestas auctor porta."
    """