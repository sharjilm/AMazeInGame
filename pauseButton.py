import pygame

class PauseButton:
    def __init__(self):
        self.mc = None

    def setMC(self, mc):
        self.mc = mc

    def read(self):
        #pygame.event.pump()
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_p: 
                self.mc.pause()
            elif not(self.mc.paused):
                pygame.event.post(event)

    def display(self):
        self.mc.displayExitButton()