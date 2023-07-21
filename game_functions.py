import sys
import pygame

def check_events():
    #respond to events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def update_screen(ai_settings, screen, ship):
    #update and flip to screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #updates screen
    pygame.display.flip()

     