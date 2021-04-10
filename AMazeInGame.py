import gameController
import menuController
import mainMenu
import pygame
import time

def main():

    mc = menuController.MenuController()

    # m = mainMenu.MainMenu()
    # m.displayButtons()

    gc = gameController.GameController()
    mc.setGC(gc)

    clock = pygame.time.Clock()

    # Does not work on virtual display (X-ming) -- use Windows instead
    # pygame.mixer.init()
    # pygame.mixer.music.load("sound/menu.ogg")
    # pygame.mixer.music.play(loops=-1)

    while(True):
        if mc.gameStarted:
            gc.pc.timeUpPlayer()
            #mc.checkButtons()
            # mc.checkExit()
            # mc.checkPause()
        else:
            mc.update()
            #print("who")
        clock.tick(30) # 30fps

main()
        
