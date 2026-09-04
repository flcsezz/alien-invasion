import sys

import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage games assets and behaviour"""

    def __init__(self):
        """initialize game and , and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien invasion UwU")
        self.clock = pygame.time.Clock()
        self.bg_color = (169, 169, 169)

    def run_game(self):
        "Runs the game"
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    sys.exit()
            
            "Redraws a screen fill from this colour on each passthrogh"
            self.screen.fill(self.bg_color)    

            #Makes the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()