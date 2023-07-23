from typing import Any
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        #create alien
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #add image
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #start at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #store position
        self.x = float(self.rect.x)

    def check_edges(self):
        #hit edge of screen = True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #move right or left
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def blitme(self):
        "draw alien at its location"
        self.screen.blit(self.image,self.rect)