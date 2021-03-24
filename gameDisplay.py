import pygame
#Standard lib
import os
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
import font

pygame.init()
height = 300
width = 300
window = pygame.display.set_mode((height,width),pygame.RESIZABLE)
pygame.display.set_caption('AMazeInGame!')
screen = pygame.display.get_surface()
screen.convert_alpha()
#clock = pygame.time.Clock()

class GameDisplay():
    def __init__(self):
        self.pd = map.MapData()
        self.md = player.PlayerData()
        #self.mgd = minigame.MinigameData()
        self.textfont = pygame.image.load('resources%s%s' % (os.sep, 'font-12x16.png'))

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
        pygame.display.flip()


    def drawMap(self):
        #print("drawmap")

        screen.fill((0,0,0))
        for i in range(self.md.height):
            for j in range(self.md.width):
                if (self.md.tiles[i][j] == '0'):
                    pygame.draw.rect(screen,(255,255,255) ,(30*i,30*j,30, 30))
                else:
                    pygame.draw.rect(screen,(0,0,0) ,(30*i,30*j,30, 30))

    def drawPlayer(self):
        pygame.draw.rect(screen,(0,255,0),(self.pd.x*30 + 10,self.pd.y*30 + 10,10,10))

    def drawMinigame(self):
        #print("drawminigame")
        screen.fill((255,255,255))
        for i in range(self.mgd.height):
            for j in range(self.mgd.width):
                if (self.mgd.tiles[i][j] == '0'):
                    pygame.draw.rect(screen,(255,255,255) ,(30*j,30*i,30, 30))
                elif (self.mgd.tiles[i][j] == 'w'):
                    pygame.draw.rect(screen,(0,0,255) ,(30*j,30*i,30, 30))
                    self.drawText("w", 30*j,30*i)

                else:
                    pygame.draw.rect(screen,(0,0,0) ,(30*j,30*i,30, 30))

        for i in self.mgd.bots:
            pygame.draw.rect(screen,(255,0,0),(i.x*30 + i.offset,i.y*30 + i.offset,i.width,i.height))

    def drawText(self, s, x, y):
        fontsize = font.size(s)
        result = pygame.Surface((fontsize[0], fontsize[1]), pygame.SRCALPHA)
        result.blit(font.render(self.textfont,s,(255,255,255,255)), (3,3))
        screen.blit(result,(x,y))
