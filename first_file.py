import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
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

    #make the ship, bullets, aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    stats = GameStats(ai_settings)

    #game main loop - always happening
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        #game active loop - only while active
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()