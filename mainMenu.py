import pygame
import font
import os

from gameDisplay import Colour, GameDisplay

# pygame inititializations, duped from gameDisplay
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

class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.selected = True if self.text == "Start game!" else False

    def display(self):
        drawText(self.text, Colour.green if self.selected else Colour.blue, self.x, self.y)

class MainMenu:
    def __init__(self):
        self.textfont = pygame.image.load('resources%s%s' % (os.sep, 'font-12x16.png'))
        self.offset = 30
        self.buttons = []
        self.buttons.append(Button("Start game!", width/2 - 70, height/2 - 70))
        self.buttons.append(Button("Change settings", width/2 - 70, height/2))
        self.selected = 0

    def displayButtons(self):
        screen.fill(Colour.black)
        for button in self.buttons:
            button.display()
        pygame.display.flip()
        #print("drawn")