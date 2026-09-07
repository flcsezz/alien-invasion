"""This is a practice file of a exercise in the book this dosent affect the main programm in any way"""
import pygame

class Character_at_Center:

    def __init__(self, char):  

        self.screen = char.screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #main sauce

        self.rect.center = self.screen_rect.center

    def blitmechr(self):
        self.screen.blit(self.image, self.rect)
