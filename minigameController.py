# import pygame
#Standard lib
# import os
# import sys
# import time
# import random
# import math
#Own Files
#import GameController
import minigame
import minigameContainer

class MinigameController():
    def __init__(self):
        self.mgd = minigameContainer.MinigameData()
        self.mg = minigame.Minigame()
        self.gc = 0
        self.minigameNum = -1

        self.pause = False

    def set(self, gameController):
        self.gc = gameController

    def startMinigame(self, minigameNum):
        self.mgd = self.mg.g[minigameNum]
        self.minigameNum = minigameNum

    def exitMinigame(self):
        self.mg.reset(self.minigameNum)

    def pauseMinigame(self):
        self.pause = not(self.pause)

    def fetchMinigameData(self, minigameNum):
        self.mgd = self.mg.readMinigame(minigameNum)

        return self.mgd

    def updateMinigameData(self, minigameNum, minigameData):
        self.mgd = minigameData
        self.mg.writeMinigame(minigameNum, self.mgd)

    def timeUpMinigame(self):
        self.mgd = self.mg.readMinigame()
        self.minigameChange()

    def minigameChange(self):
        #CHANGE

        self.mg.writeMinigame(self.minigameNum, self.mgd)
        self.gc.sendMinigameData(self.mgd)