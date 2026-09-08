import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #creats a rect at (0,0)
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        #places midbottom of the rect to midtop of the ship

        self.rect.midbottom = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        #updates the bullets position
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        #Draws bullet on the surface
        pygame.draw.rect(self.screen, self.color, self.rect)