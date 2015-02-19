#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.uix.widget import Widget, Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.animation import Animation

from GameScreen import GameScreen

import os

Builder.load_file("GameScreens/CreditsScreen.kv")

class CreditsScreen(GameScreen):
    credits = []

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.credits.append({"Title": "Développement", "Lines": ["Amanzou Amine", "Bouchez Django", "Taverne Émile"]})
        self.credits.append({"Title": "Scénario", "Lines": ["Hennequin-Parrey Thomas", "Pierres Julie"]})
        self.credits.append({"Title": "Graphismes", "Lines": ["Taverne Émile"]})

        for element in self.credits:
            bloc = GridLayout(cols=1, size_hint= (1, None), spacing=(0, "10dp") )
            bloc.add_widget(Label(text=element["Title"], font_size="30sp"))
            for line in element["Lines"]:
                bloc.add_widget(Label(text=line, font_size="20sp"))
            self.ids.creditContainer.add_widget(bloc)
            
        self.ids.creditContainer.add_widget(Image(source=os.path.normpath("Images/logo-univ-paris1.png")))
     
        anim = Animation(pos=(0, self.size[1] - 200 - self.ids.creditContainer.size[1]), duration=700, t='linear')
        anim.start(self.ids.creditContainer)