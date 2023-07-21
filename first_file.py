import sys
import pygame

def run_game():
    pygame.init()
    #make the background - size is 1560 x 800
    screen = pygame.display.set_mode((1560,800))
    pygame.display.set_caption("Alien Invasion!")

    #game main loop
    while True:
        
        #watch for action
        for event in pygame.event.get():

            #close game
            if event.type == pygame.QUIT:
                sys.exit()
            
        #updates screen
        pygame.display.flip()

run_game()