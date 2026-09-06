import sys
from ship import Ship
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
        self.bg_color = self.settings.bg_colour
        self.ship = Ship(self)
        
    def run_game(self):
        "Runs the game"
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
                """respond to keypresses and mouse events"""
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        sys.exit()
                    elif events.type == pygame.KEYDOWN:
    
                        if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
                            self.ship.move_right =True
                            #moves ship to right
                        if events.key == pygame.K_a or events.key == pygame.K_LEFT:
                             #moves ship to left 
                            self.ship.move_left = True
                        if events.key == pygame.K_w or events.key == pygame.K_UP:
                             #moves ship up
                             self.ship.move_up = True
                        if events.key == pygame.K_s or events.key == pygame.K_DOWN:
                            self.ship.move_down = True

                    elif events.type ==  pygame.KEYUP:

                        if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
                            self.ship.move_right =False
                            #moves ship to right
                        if events.key == pygame.K_a or events.key == pygame.K_LEFT:
                             #moves ship to left 
                            self.ship.move_left = False
                        if events.key == pygame.K_w or events.key == pygame.K_UP:
                             #moves ship up
                             self.ship.move_up = False
                        if events.key == pygame.K_s or events.key == pygame.K_DOWN:
                            self.ship.move_down = False
                         

                        
                    
                    

    def _update_screen(self):

        "Redraws a screen fill from this colour on each passthrogh"
        self.screen.fill(self.bg_color)    
        self.ship.blitme()    
        
        
        #Makes the most recently drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()