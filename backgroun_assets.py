import pygame
from pygame.sprite import Sprite
from random import randint

class Background(Sprite):
    def __init__(self, ai_game, image, speed):
        super().__init__()
        self.settings = ai_game.settings

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = randint(0 , self.settings.screen_width)
        self.rect.y = randint(-50, 0 )
        self.speed = speed
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
    
    