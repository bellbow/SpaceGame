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

        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update position
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        "draw ship at its location"
        self.screen.blit(self.image,self.rect)
        