import pygame

class Ship:

    def __init__(self, ai_game):

        self.screen =ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #starts each new ship at the bottom center of the window
        self.rect.midbottom = self.screen_rect.midbottom

        #ships movements control
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.settings = ai_game.settings
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right:
            self.x += self.settings.ship_speed
        if self.move_left:
            self.x -= self.settings.ship_speed
        if self.move_up:
            self.y -= self.settings.ship_speed
        if self.move_down:
            self.y += self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y