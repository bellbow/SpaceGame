import sys
import pygame

#start move
def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

#stop move
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    #respond to events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ship)        
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship):
    #update and flip to screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #updates screen
    pygame.display.flip()

     