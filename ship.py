import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        #initialize ship
        self.screen = screen
        self.ai_settings = ai_settings

        #load ship image
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #starting ship placement
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #ship center point
        self.center = float(self.rect.centerx)

        #movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #update
        self.rect.centerx = self.center

    def blitme(self):
        "draw ship at its location"
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        self.center = self.screen_rect.centerx
        