import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

    play_button = Button(ai_settings, screen, "Play")
    #make the ship, bullets, aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #game main loop - always happening
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        #game active loop - only while active
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
  

run_game()