"""This is a practice file of a exercise in the book this dosent affect the main programm in any way"""

import pygame
import sys

class Rocket:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        pygame.display.set_caption("Rocket at the center")

        self.moveup = False
        self.movedown = False
        self.mover = False
        self.movel = False

        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            self.check_events()
            self.update_ship()
            self.screen.fill((169, 169, 169))
            self.render_rocket()
            pygame.display.flip()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.moveup = True
                if event.key == pygame.K_DOWN:
                    self.movedown = True
                if event.key == pygame.K_LEFT:
                    self.movel = True
                if event.key == pygame.K_RIGHT:
                    self.mover = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.moveup = False
                if event.key == pygame.K_DOWN:
                    self.movedown = False
                if event.key == pygame.K_LEFT:
                     self.movel = False
                if event.key == pygame.K_RIGHT:
                    self.mover = False


    def update_ship(self):
        if self.movel and self.rect.left > 0:
            self.rect.x -= 5
        if self.mover and self.rect.right < self.screen_rect.right:
            self.rect.x += 5
        if self.moveup and self.rect.top > 0:
            self.rect.y -= 5
        if self.movedown and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y +=5

    def render_rocket(self):
        self.screen.blit(self.image, self.rect)

if __name__ == "__main__":
    game = Rocket()
    game.run_game()


    


                
