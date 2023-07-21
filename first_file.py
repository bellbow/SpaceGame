import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #initialize 
    pygame.init()
    
    #make the background
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion!")

    #make the ship
    ship = Ship(screen)
    
    #game main loop
    while True:
        
        #watch for action
        for event in pygame.event.get():
            #close game
            if event.type == pygame.QUIT:
                sys.exit()

        #redrawing the screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #updates screen
        pygame.display.flip()

run_game()