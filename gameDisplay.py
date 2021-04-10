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
from enum import Enum

pygame.init()
height = 330
width = 300
window = pygame.display.set_mode((width,height),pygame.RESIZABLE)
pygame.display.set_caption('AMazeInGame!')
screen = pygame.display.get_surface()
screen.convert_alpha()
#clock = pygame.time.Clock()

class Colour():
    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (169, 169, 169)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    brown = (165, 42, 42)
    bassel = (200, 0, 80)
    jm = (200,200,0)


class GameDisplay():
    def __init__(self):
        self.pd = map.MapData()
        self.md = player.PlayerData()
        #self.mgd = minigame.MinigameData()
        self.textfont = pygame.image.load('resources%s%s' % (os.sep, 'font-12x16.png'))
        self.offset = 30

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

        screen.fill(Colour.black)
        for i in range(self.md.height):
            for j in range(self.md.width):
                if (self.md.tiles[i][j] == '0'):
                    self.drawRect(screen,Colour.white ,(30*i,30*j,30, 30))
                else:
                    self.drawRect(screen,Colour.black ,(30*i,30*j,30, 30))


        for i in self.md.stars:
            self.drawStar((i[0][0]*30, i[0][1]*30, 30, 30))

        if self.pd.stars == 5:
            self.drawExit((self.md.exit[0]*30, self.md.exit[1]*30, 30, 30), 1)

        self.drawCamera()

        for i in range(self.pd.stars):
            self.drawStar((i*30, -self.offset + 5, 20, 20))

    def drawCamera(self):
        col = (255, 0, 0, 0)
        c = (self.pd.x*30 + 15, self.pd.y*30 + 15)
        r = self.pd.stars * 25 + 50
        s = 1000
        scr = pygame.Surface((s, s), pygame.SRCALPHA)
        scr.fill((0,0,0,255))
        center = (c[0] - s/2, c[1] - s/2 + self.offset)
        c = (s//2, s//2 - self.offset)
        self.drawCircle(scr, col, c, r)
        screen.blit(scr, center)

        # scr = pygame.Surface(r, r), pygame.SRCALPHA)
        # scr.fill((255,255,255,255))
        # scr.blit(font.render(self.textfont,ent.text,(140,140,180,255)),
        # (2,2))
        # w = 150-fontsize[0]/2
        # scr.blit(result,(w,250))
    
    def drawCircle(self, scr, col, c, r):
        c = (c[0], c[1] + self.offset)
        pygame.draw.circle(scr, col, c, r)


    def drawPlayer(self):
        self.drawRect(screen,Colour.green,(self.pd.x*30 + 10,self.pd.y*30 + 10,10,10))
        self.drawText(str(self.pd.time//30), Colour.red, width - 50, -self.offset)
        #self.drawText("hp: " + str(self.pd.hp), Colour.white, 0, -self.offset)
        #self.drawText("score: " + str(self.pd.score), Colour.white, 75, -self.offset)

    # def drawMinigame(self):
    #     #print("drawminigame")
    #     screen.fill(Colour.white)
    #     for i in range(self.mgd.height):
    #         for j in range(self.mgd.width):
    #             if (self.mgd.tiles[i][j] == '0'):
    #                 self.drawRect(screen,Colour.white ,(30*j,30*i,30, 30))
    #             elif (self.mgd.tiles[i][j] == 'w'):
    #                 self.drawWall((30*j,30*i,30, 30))


    #             else:
    #                 self.drawRect(screen,Colour.black ,(30*j,30*i,30, 30))

    #     for i in self.mgd.bots:
    #         self.drawRect(screen,Colour.red,(i.x*30 + i.offset,i.y*30 + i.offset,i.width,i.height))

    def drawMinigame(self):
        #print("drawminigame")
        screen.fill(Colour.black)
        for i in range(self.mgd.height):
            for j in range(self.mgd.width):
                if (self.mgd.tiles[i][j] == '0'):
                    self.drawRect(screen,Colour.white ,(30*j,30*i,30, 30))
                elif (self.mgd.tiles[i][j] == 'w'):
                    self.drawWall((30*j,30*i,30, 30))

                else:
                    self.drawRect(screen,Colour.black ,(30*j,30*i,30, 30))

        if self.pd.hp >= 0:
            self.drawText("hp:" + str(self.pd.hp), Colour.white, 0, -self.offset)

        if self.pd.score >= 0:
            self.drawText("score:" + str(self.pd.score), Colour.white, 0, -self.offset)

        if self.mgd.end != 0:
            self.drawExit((self.mgd.exit[0]*30, self.mgd.exit[1]*30, 30, 30), self.mgd.end)

        for i in self.mgd.items:
            self.drawItem(i.name, (i.x*30,i.y*30,30, 30))

        for i in self.mgd.bots:
            self.drawRect(screen,Colour.red,(i.x*30 + i.offset,i.y*30 + i.offset,i.width,i.height))
            if i.score >= 0:
                self.drawText("bot:" + str(i.score), Colour.white, 125, -self.offset)
        
        for i in self.mgd.projectiles:
            self.drawRect(screen,Colour.bassel,(i.x*30 + i.offset,i.y*30 + i.offset,i.width,i.height))

        for i in self.mgd.rockets:
            self.drawRect(screen,Colour.bassel,(i.x*30 + i.offset,i.y*30 + i.offset, i.width, i.height))
            
        if self.mgd.timer >= 0:
            self.drawText("time:" + str(int(self.mgd.timer/30)), Colour.white, 75, -self.offset)

    def drawText(self, s, col, x, y):
        fontsize = font.size(s)
        result = pygame.Surface((fontsize[0], fontsize[1]), pygame.SRCALPHA)
        col = (col[0], col[1], col[2], 255)
        result.blit(font.render(self.textfont,s,col), (0,0))
        screen.blit(result,(x,y + self.offset))

    def drawRect(self, scr, col, rect):
        rect = (rect[0], rect[1] + self.offset, rect[2], rect[3])
        pygame.draw.rect(scr, col, rect)

    def drawWall(self, rect):
        self.drawRect(screen,Colour.brown ,rect)
        for i in range(5):
            self.drawRect(screen,Colour.gray ,(rect[0], rect[1] + 4 + 6*i, 30, 2))

        for j in range(5):
            if (j + rect[1]/30) % 2 == 0:
                offsetx = 4
            else:
                offsetx = 8
            for i in range(3):
                self.drawRect(screen,Colour.gray ,(rect[0] + offsetx + i*10, rect[1] + j*6, 2, 4))

    def drawPoly(self, scr, col, pts):
        for i in range(len(pts)):
            pts[i] = (pts[i][0], pts[i][1] + self.offset)
        pygame.draw.polygon(scr, col, pts)

    def drawItem(self, name, rect):
        #self.drawRect(screen,Colour.white, rect)
        #self.drawText("i", Colour.red, rect[0], rect[1])
        if name == "d":
            pts = [(rect[0] + rect[2]/2, rect[1] + rect[3]/6), 
                    (rect[0] + rect[2]/2 + 10, rect[1] + rect[3]/2),
                    (rect[0] + rect[2]/2, rect[1] + rect[3]*5/6),
                    (rect[0] + rect[2]/2 - 10, rect[1] + rect[3]/2)]
            col = Colour.blue
        if name == "de":
            pts = [(rect[0] + rect[2]/2, rect[1] + rect[3]/6), 
                    (rect[0] + rect[2]/2 + 10, rect[1] + rect[3]/2),
                    (rect[0] + rect[2]/2, rect[1] + rect[3]*5/6),
                    (rect[0] + rect[2]/2 - 10, rect[1] + rect[3]/2)]
            col = Colour.green
        if name == "def":
            pts = [(rect[0] + rect[2]/2, rect[1] + rect[3]/6), 
                    (rect[0] + rect[2]/2 + 10, rect[1] + rect[3]/2),
                    (rect[0] + rect[2]/2, rect[1] + rect[3]*5/6),
                    (rect[0] + rect[2]/2 - 10, rect[1] + rect[3]/2)]
            col = Colour.black
        
        elif name == "r":
            pts = [(rect[0] + rect[2]/2, rect[1] + rect[3]/6), 
                    (rect[0] + rect[2]/2 + 10, rect[1] + rect[3]/2),
                    (rect[0] + rect[2]/2, rect[1] + rect[3]*5/6),
                    (rect[0] + rect[2]/2 - 10, rect[1] + rect[3]/2)]
            col = Colour.red  

        elif name == "colour":
            pts = [(rect[0] + rect[2]/2, rect[1] + rect[3]/6), 
                    (rect[0] + rect[2]/2 + 10, rect[1] + rect[3]/2),
                    (rect[0] + rect[2]/2, rect[1] + rect[3]*5/6),
                    (rect[0] + rect[2]/2 - 10, rect[1] + rect[3]/2)]
            col = Colour.jm
        
        self.drawPoly(screen, col, pts)


    def drawExit(self, rect, win):
        if win == 1:
            exit = pygame.image.load('resources%s%s' % (os.sep, 'exitWin.png'))
        else:
            exit = pygame.image.load('resources%s%s' % (os.sep, 'exitLose.png'))
        screen.blit(exit, (rect[0], rect[1] + self.offset))

    def drawStar(self, rect):
        star = pygame.image.load('resources%s%s' % (os.sep, 'star.png'))
        star = pygame.transform.scale(star, (rect[2],rect[3]))
        screen.blit(star, (rect[0], rect[1] + self.offset))



