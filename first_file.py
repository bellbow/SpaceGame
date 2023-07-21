import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

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
        gf.check_events()

        #updating the screen
        gf.update_screen(ai_settings, screen, ship)
        
run_game()