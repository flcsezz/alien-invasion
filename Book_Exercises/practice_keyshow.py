import sys
import pygame

class keyshow:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.clock = pygame.time.Clock()
   
    def showkeys(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            elif events.type == pygame.KEYDOWN:
                print(events.key)


    def run(self):
        while True:
            self.screen.fill((169,169,169))
            self.showkeys()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = keyshow()
    game.run()
            
    