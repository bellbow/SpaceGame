import sys
import pygame
from bullet import Bullet
from alien import Alien

#start move
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

#stop move
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    #respond to events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)        
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    #update and flip to screen
    screen.fill(ai_settings.bg_color)
    #draw bullets under ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #updates screen
    pygame.display.flip()

#update bullet positions and remove offscreen
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens(ai_settings, alien_width):
    #aliens in a row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    #create alien
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    #horizontal spacing
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)

    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)