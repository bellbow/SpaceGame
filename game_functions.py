import sys
import pygame

def check_events(ship):
    #respond to events
    for event in pygame.event.get():
            #close game
            if event.type == pygame.QUIT:
                sys.exit()

            #right movement
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RIGHT:
                      ship.self.moving_right = True
                    
            elif event.type == pygame.KEYUP:
                 if event.key == pygame.K_RIGHT:
                      ship.self.moving_right = False


def update_screen(ai_settings, screen, ship):
    #update and flip to screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #updates screen
    pygame.display.flip()

     