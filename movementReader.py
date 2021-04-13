import pygame

class MovementReader():
    def __init__(self):
        self.pc = 0

    def set(self, playerController):
        self.pc = playerController

    def read(self):
        #while (True):
        #gc.pc.timeUpPlayer()
        pygame.event.pump()
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            #key = pygame.key.get_pressed()
            key = event.key
            #pygame.event.pump()
            #print(key)

            if key == pygame.K_LEFT: 
                self.pc.move('L')
            elif key == pygame.K_RIGHT: 
                self.pc.move('R')
            elif key == pygame.K_UP: 
                self.pc.move('U')
            elif key == pygame.K_DOWN: 
                self.pc.move('D')
            elif key == pygame.K_SPACE:
                self.pc.move('S')
            # elif key == pygame.K_ESCAPE: 
            #     exit()
