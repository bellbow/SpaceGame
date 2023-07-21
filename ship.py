import pygame

class Ship():

    def __init__(self,screen):
        #initialize ship
        self.screen = screen

        #load ship image
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #starting ship placement
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        "draw ship at its location"
        self.screen.blit(self.image,self.rect)
        