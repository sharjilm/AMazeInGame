# import pygame
#Standard lib
# import os
# import sys
# import time
# import random
# import math
#Own Files
#import GameController
import map
#import dataTypes

# pygame.init()
# height = 320
# width = 320
# window = pygame.display.set_mode((height,width),pygame.RESIZABLE)
# pygame.display.set_caption('AMazeInGame!')
# screen = pygame.display.get_surface()
# screen.convert_alpha()
# clock = pygame.time.Clock()

class MapController():
    def __init__(self):
        self.md = map.MapData()
        self.m = map.Map()
        self.gc = 0

        self.pause = False

    def set(self, gameController):
        self.gc = gameController

    def startMap(self):
        pass

    def exitMap(self):
        pass

    def pauseMap(self):
        self.pause = not(self.pause)

    def fetchMapData(self):
        self.md = self.m.readMap()

        return self.md

    def updateMapData(self, mapData):
        self.md = mapData
        self.m.writeMap(self.md)

    def timeUpMap(self):
        self.md = self.m.readMap()
        self.mapChange()

    def mapChange(self):
        #CHANGE

        self.m.writeMap(self.md)
        self.gc.sendMapData(self.md)