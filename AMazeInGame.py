import gameController
import menuController
import settingsController
import mainMenu
import pygame
import time

def main():

    mc = menuController.MenuController()
    gc = gameController.GameController()
    sc = settingsController.SettingsController()

    mc.setGC(gc)
    mc.setSC(sc)
    sc.setMC(mc)

    clock = pygame.time.Clock()

    # Does not work on virtual display (X-ming) -- use Windows instead
    # pygame.mixer.init()
    # pygame.mixer.music.load("sound/menu.ogg")
    # pygame.mixer.music.play(loops=-1)
    # mc.initVolume()

    while(True):
        if mc.gameStarted:
            mc.checkButtons()
            if not mc.paused:
                gc.pc.timeUpPlayer()
            # mc.checkExit()
            # mc.checkPause()
        else:
            mc.update()
            #print("who")
        clock.tick(30) # 30fps

main()
        
