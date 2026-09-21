import pygame
from pygame.sprite import Sprite
from random import randint

class Aliens(Sprite):

    def __init__(self, ai_game, image, health, speed = None):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = image
        self.rect = self.image.get_rect()
        self.health = health
        self.speed = speed if speed is not None else self.settings.alien_speed

        self.rect.x = randint(0, self.settings.screen_width)
        self.rect.y = randint(-60,0)

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y