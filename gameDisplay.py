import pygame
#Standard lib
# import os
# import sys
# import time
# import random
# import math
#Own Files
import map
#import minigame
import player
# import mapController
# import minigameController
# import playerController
# import gamedisplay
#import dataTypes

pygame.init()
height = 300
width = 300
window = pygame.display.set_mode((height,width),pygame.RESIZABLE)
pygame.display.set_caption('AMazeInGame!')
screen = pygame.display.get_surface()
screen.convert_alpha()
screen.fill((0,0,0))
#clock = pygame.time.Clock()

class GameDisplay():
    def __init__(self):
        self.pd = map.MapData()
        self.md = player.PlayerData()
        #self.mgd = minigame.MinigameData()

    def displayMap(self, playerData, mapData):
        self.pd = playerData
        self.md = mapData
        self.drawMap()
        self.drawPlayer()
        pygame.display.flip()

    def displayMinigame(self, playerData, minigameData):
        self.pd = playerData
        self.mgd = minigameData
        self.drawMinigame()
        self.drawPlayer()

    def drawMap(self):
        for i in range(self.md.height):
            for j in range(self.md.width):
                if (self.md.tiles[i][j] == '0'):
                    pygame.draw.rect(screen,(255,255,255) ,(30*i,30*j,30, 30))
                else:
                    pygame.draw.rect(screen,(0,0,0) ,(30*i,30*j,30, 30))

    def drawPlayer(self):
        pygame.draw.rect(screen,(0,255,0),(self.pd.x*30 + 10,self.pd.y*30 + 10,10,10))
