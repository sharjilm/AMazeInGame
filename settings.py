import pygame
import font
import os

from gameDisplay import Colour, GameDisplay

#pygame inititializations, duped from gameDisplay
pygame.init()
height = 330
width = 300
window = pygame.display.set_mode((width,height),pygame.RESIZABLE)
pygame.display.set_caption('AMazeInGame!')
screen = pygame.display.get_surface()
screen.convert_alpha()

def drawText(s, col, x, y):
    textfont = pygame.image.load('resources%s%s' % (os.sep, 'font-12x16.png'))
    offset = 30
    fontsize = font.size(s)
    result = pygame.Surface((fontsize[0], fontsize[1]), pygame.SRCALPHA)
    col = (col[0], col[1], col[2], 255)
    result.blit(font.render(textfont,s,col), (0,0))
    screen.blit(result,(x,y + offset))

class Settings:
    def __init__(self):
        self.textfont = pygame.image.load('resources%s%s' % (os.sep, 'font-12x16.png'))
        self.volume = 5

    def displayContent(self):
        screen.fill(Colour.black)
        drawText("Esc", Colour.red, 10, 0)
        drawText("Volume:", Colour.blue, width/2 - 30, height/2 - 75)
        drawText(str(self.volume), Colour.blue, width/2, height/2 - 35)
        pygame.display.flip()
        #print("drawn")

    def updateVolume(self, newVolume):
        self.volume = newVolume