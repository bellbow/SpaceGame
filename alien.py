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

    def blitme(self):
        "draw alien at its location"
        self.screen.blit(self.image,self.rect)