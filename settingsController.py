import settings
import pygame

class SettingsController():
    def __init__(self):
        self.settings = settings.Settings()
        self.mc = None
        self.volume = 0

    def update(self):
        self.checkInput()
        self.displaySettings()

    def checkInput(self):
        #while (True):
        #gc.pc.timeUpPlayer()
        pygame.event.pump()
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            #key = pygame.key.get_pressed()
            key = event.key
            #pygame.event.pump()
            #print(key)

            if key == pygame.K_UP: 
                self.volume = (self.volume + 1) % 11
                self.volumeUpdate()
            elif key == pygame.K_DOWN: 
                self.volume = (self.volume - 1) % 11   
                self.volumeUpdate()             
            elif key == pygame.K_ESCAPE: 
                self.mc.returnToMenu()

    def volumeUpdate(self):
        self.settings.updateVolume(self.volume)
        try:
            pygame.mixer.music.set_volume(self.volume/10)
        except:
            pass

    def displaySettings(self):
        self.settings.displayContent()

    def setMC(self, menuController):
        self.mc = menuController