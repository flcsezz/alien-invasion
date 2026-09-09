import sys
from ship import Ship
import pygame
from settings import Settings
from bullets import BulletR , BulletL, BulletM

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
        self.bulletsR = pygame.sprite.Group()
        self.bulletsL = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bullet_firing = False
        self.last_fired = 0
        self.not_heated = True
        self.bullet_heat= float(0)    
        self.cannon_mode = False  
        self.trimode = False
        self.single_mode = False
          
        
    def run_game(self):
        "Runs the game"
        while True:
            self._check_events()
            self.ship.update()
            self._bullet_heat()
            self._fire_bullet()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
                """respond to keypresses and mouse events"""
                for events in pygame.event.get():
                    if events.type == pygame.QUIT or events.type == pygame.KEYDOWN and events.key == pygame.K_q:
                        sys.exit()
                    elif events.type == pygame.KEYDOWN:
                        self._check_keydown_events(events)
                    elif events.type ==  pygame.KEYUP:
                         self._check_keyup_events(events)



    def _check_keyup_events(self,events):

        if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
            self.ship.move_right =False
            #moves ship to right
        elif events.key == pygame.K_a or events.key == pygame.K_LEFT:
             #moves ship to left 
            self.ship.move_left = False
        elif events.key == pygame.K_w or events.key == pygame.K_UP:
             #moves ship up
             self.ship.move_up = False
        elif events.key == pygame.K_s or events.key == pygame.K_DOWN:
                self.ship.move_down = False 
        elif events.key == pygame.K_SPACE:
                self.bullet_firing = False 
                self.single_mode = False
        elif events.key == pygame.K_f:
             self.bullet_firing = False
             self.cannon_mode = False
        elif events.key == pygame.K_t:
             self.bullet_firing = False
             self.trimode = False
        
    def _check_keydown_events(self, events):
        if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
            self.ship.move_right =True
            #moves ship to right
        elif events.key == pygame.K_a or events.key == pygame.K_LEFT:
             #moves ship to left 
             self.ship.move_left = True
        elif events.key == pygame.K_w or events.key == pygame.K_UP:
             #moves ship up
            self.ship.move_up = True
        elif events.key == pygame.K_s or events.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif events.key == pygame.K_SPACE:
             self.bullet_firing = True
             self.single_mode = True
        elif events.key == pygame.K_f:
             self.bullet_firing = True
             self.cannon_mode = True
        elif events.key == pygame.K_t:
             self.bullet_firing = True
             self.trimode = True
        

    def _update_screen(self):

        "Redraws a screen fill from this colour on each passthrogh"
        self.screen.fill(self.bg_color)    
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()    
        
        
        #Makes the most recently drawn screen visible
        pygame.display.flip()

    def _fire_bullet(self):
        self.current_time = pygame.time.get_ticks()
        if self.bullet_firing and (self.current_time - self.last_fired >= self.settings.bullet_delay) and self.not_heated:
            if self.cannon_mode:
                new_bulletR = BulletR(self)
                new_bulletL = BulletL(self)
                self.bullets.add(new_bulletR)
                self.bullets.add(new_bulletL)
                self.last_fired = self.current_time
                self.bullet_heat += self.settings.bullet_heatrate_cannonmode
            elif self.trimode:
                 new_bulletR = BulletR(self)
                 new_bulletL = BulletL(self)
                 new_bulletM = BulletM(self)
                 self.bullets.add(new_bulletR)
                 self.bullets.add(new_bulletL)
                 self.bullets.add(new_bulletM)
                 self.last_fired = self.current_time
                 self.bullet_heat += self.settings.bullet_heatrate_Trimode
            elif self.single_mode:
                 new_bulletM = BulletM(self)
                 self.bullets.add(new_bulletM)
                 self.last_fired = self.current_time
                 self.bullet_heat += self.settings.bullet_heatrate_singlemode

    def _bullet_heat(self):
         
         if self.bullet_heat <= 0:
              self.not_heated = True
         elif self.bullet_heat >= self.settings.bullet_maxheat:
               self.not_heated = False
         if (self.not_heated == False or self.bullet_firing == False) and self.bullet_heat > 0:
              self.bullet_heat -= self.settings.bullet_coolingrate
            
         
         

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()