import gameController
import pygame
import time

def main():
    gc = gameController.GameController()
    print("what")
    gc.startGame()
    print("hmm")
    clock = pygame.time.Clock()


    while(True):
        gc.pc.timeUpPlayer()
        #print("who")
        clock.tick(30) # 30fps
        pass

main()
        
