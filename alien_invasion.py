import sys

import pygame

class AlienInvasion:
    """Overall class to manage games assets and behaviour"""

    def __init__(self):
        """initialize game and , and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien invasion UwU")

    def run_game(self):
        "Runs the game"
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    sys.exit()

            #Makes the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()