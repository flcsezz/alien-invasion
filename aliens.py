import pygame
from pygame.sprite import Sprite

class Aliens(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)