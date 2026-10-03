import sys
from time import sleep
from ship import Ship
import pygame
from settings import Settings
from bullets import BulletR , BulletL, BulletM
from aliens import Aliens
from backgroun_assets import Background
from game_stats import GameStats
from button import Buttons
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage games assets and behaviour"""

    def __init__(self):
        """initialize game and , and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien invasion UwU")
      
      #Stats
        self.stats = GameStats(self)
        self.game_active = False
     
        self.clock = pygame.time.Clock()
        self.bg_color = self.settings.bg_colour
        self.ship = Ship(self)
       

        self.bulletsR = pygame.sprite.Group()
        self.bulletsL = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        

        self.last_fired = 0
        self.not_heated = True
        self.bullet_heat= float(0)    
        self.cannon_mode = False  
        self.trimode = False
        self.single_mode = False
        self.bullet_delay= 0
        self.firing = False
        

        #Aliens
        self.aliens = pygame.sprite.Group()
        self.last_spawned = 0

        #bg objects
        self.last_rendered = 0
        self.bg_objects = pygame.sprite.Group()
        self.destructive_obj = pygame.sprite.Group()

        #buttons
        self.play_button = Buttons(self, "Play")

        #scoreboard
        self.scoreboard = Scoreboard(self)
        self.settings.apply_stage(0)
        self.stage = self.settings.stages[0]["name"]
        self.stage_banner = self.stage
        self.stage_banner_timer = 0



        
    def run_game(self):
        "Runs the game"
        while True:
            self._check_events()
            if self.game_active:
                    self.ship.update()           
                    self._bullet_heat()
                    self._fire_bullet()
                    self.bg_objects.update()
                    self._spawn_alien()
                    self.bullets.update()
                    self.aliens.update()
                    self._update_alien()
                    self._remove_bullets()
                    self._check_bullet_alien_asteroid_collision()
                    self._check_alien_ship_collision()
                    self._check_alien_bottom()
                    self._game_progression()
                    self._render_bg_objects()
                    self._remove_obj()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
                """respond to keypresses and mouse events"""
                for events in pygame.event.get():
                    if events.type == pygame.QUIT or events.type == pygame.KEYDOWN and events.key == pygame.K_q:
                        self.stats.save_highscore()
                        sys.exit()
                    elif events.type == pygame.KEYDOWN:
                        self._check_keydown_events(events)
                    elif events.type ==  pygame.KEYUP:
                         self._check_keyup_events(events)
                    elif events.type == pygame.MOUSEBUTTONDOWN:
                         mouse_pos = pygame.mouse.get_pos()
                         self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
         if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
              self.stats.stat_reset()
              self.settings.apply_stage(0)
              self.stage = self.settings.stages[0]["name"]
              self.stage_banner = self.stage
              self.stage_banner_timer = pygame.time.get_ticks() + 2000
              self.bg_objects.empty()
              self.destructive_obj.empty()
              self.bullets.empty()
              self.ship.center_ship()
              self.aliens.empty()
              self.game_active = True
              pygame.mouse.set_visible(False)
              self.scoreboard.prep_score()
         

                                              

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
             self.firing = False
        elif events.key == pygame.K_LSHIFT:
             self.ship.swifty = False
        
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
        elif events.key == pygame.K_1:
             self.single_mode = True
             self.trimode = False
             self.cannon_mode = False
        elif events.key == pygame.K_2:
             self.cannon_mode = True
             self.single_mode = False
             self.trimode = False
        elif events.key == pygame.K_3:
             self.trimode = True
             self.cannon_mode = False
             self.single_mode = False
        elif events.key == pygame.K_SPACE:
             self.firing = True
        elif events.key == pygame.K_LSHIFT:
             self.ship.swifty = True
        

    def _update_screen(self):

        "Redraws a screen fill from this colour on each passthrogh"
        self.screen.fill(self.bg_color)
        self.bg_objects.draw(self.screen)
        self.ship.blitme()   
        self.aliens.draw(self.screen)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        if not self.game_active:
             self.play_button.draw()

        self.scoreboard.show_score()
        self.scoreboard.show_stage(self.stage)
        self.scoreboard.show_highscore()
        if self.game_active and pygame.time.get_ticks() < self.stage_banner_timer:
            self.scoreboard.show_banner(self.stage_banner)

        #Makes the most recently drawn screen visible
        pygame.display.flip()


    def _fire_bullet(self):
        self.current_time = pygame.time.get_ticks()
        if self.firing and (self.current_time - self.last_fired >= self.bullet_delay) and self.not_heated:
            if self.cannon_mode:
                new_bulletR = BulletR(self)
                new_bulletL = BulletL(self)
                self.bullets.add(new_bulletR)
                self.bullets.add(new_bulletL)
                self.last_fired = self.current_time
                self.bullet_heat += self.settings.bullet_heatrate_cannonmode
                self.bullet_delay = self.settings.cannonmode_ddelay

            elif self.trimode:
                 new_bulletR = BulletR(self)
                 new_bulletL = BulletL(self)
                 new_bulletM = BulletM(self)
                 self.bullets.add(new_bulletR)
                 self.bullets.add(new_bulletL)
                 self.bullets.add(new_bulletM)
                 self.last_fired = self.current_time
                 self.bullet_heat += self.settings.bullet_heatrate_trimode
                 self.bullet_delay = self.settings.trimode_delay

            elif self.single_mode or self.firing:
                 new_bulletM = BulletM(self)
                 self.bullets.add(new_bulletM)
                 self.last_fired = self.current_time
                 self.bullet_heat += self.settings.bullet_heatrate_singlemode
                 self.bullet_delay = self.settings.singlemode_delay

    def _bullet_heat(self):
         
         if self.bullet_heat <= 0:
              self.not_heated = True
         elif self.bullet_heat >= self.settings.bullet_maxheat:
               self.not_heated = False
         if (not self.not_heated or not self.firing) and self.bullet_heat > 0:
              self.bullet_heat -= self.settings.bullet_coolingrate

    def _remove_bullets(self):
         for bullets in self.bullets.copy():
            if bullets.rect.bottom <=0:
                 self.bullets.remove(bullets)
            

    def _check_bullet_alien_asteroid_collision(self):
         collision = pygame.sprite.groupcollide(self.bullets , self.aliens, True, True)
         collisiona = pygame.sprite.groupcollide(self.bullets, self.destructive_obj, True, True)
         
         if collision:
              for alien_hit in collision.values():
                   self.stats.score += self.settings.alien_points * len(alien_hit)
                   self.scoreboard.prep_score()
                   self.stats.live_hscore()
                   


    def _check_alien_ship_collision(self):
         collision = pygame.sprite.spritecollideany(self.ship, self.aliens)
         collisiona = pygame.sprite.spritecollideany(self.ship, self.destructive_obj)
         if collision or collisiona:
              self._ship_hit()
         

    def _render_bg_objects(self):
         self.current_time = pygame.time.get_ticks()
         if self.current_time - self.last_rendered >= self.settings.spawn_delay_bgobject:
              self.asteroids = Background(self, self.settings.asteroid_img, self.settings.obj_speed)
              self.bg_objects.add(self.asteroids)
              self.destructive_obj.add(self.asteroids)
              self.last_rendered = self.current_time

    def _remove_obj(self):
         for asteroids in self.bg_objects.copy():
              if asteroids.rect.top > self.settings.screen_height:
                   self.bg_objects.remove(asteroids)
                   self.destructive_obj.remove(asteroids)


    def _spawn_alien(self):
         if self.current_time - self.last_spawned > self.settings.spawn_delay_alien:
              self.alien = Aliens(self, self.settings.alien1, 3, self.settings.alien_speed)
              self.aliens.add(self.alien)
              self.last_spawned = self.current_time

    def _ship_hit(self):

         if self.settings.max_ships > 0:
               self.settings.max_ships -=1
               self.bullets.empty()
               self.aliens.empty()
               self.destructive_obj.empty()
               self.bg_objects.empty()

               self.ship.center_ship()

               sleep(0.5)
         else:
              self.game_active = False
              self.stats.save_highscore()
              pygame.mouse.set_visible(True)
              
              

    def _check_alien_bottom(self):
         for alien in self.aliens.copy():
              if alien.rect.bottom > self.settings.screen_height:
                   self._ship_hit()
                   break


     
    def _update_alien(self):
         """updates the aliens positoin"""
         self.aliens.update()

    def _game_progression(self):
         """Check if score reached target to advance to the next stage"""
         current_idx = self.stats.current_stage_idx
         if current_idx < len(self.settings.stages) - 1:
              stage_data = self.settings.stages[current_idx]
              target = stage_data.get("score_target")
              if target is not None and self.stats.score >= target:
                   self.stats.current_stage_idx += 1
                   self.settings.apply_stage(self.stats.current_stage_idx)
                   new_stage = self.settings.stages[self.stats.current_stage_idx]
                   self.stage = new_stage["name"]
                   self.stage_banner = new_stage["name"]
                   self.stage_banner_timer = pygame.time.get_ticks() + 2000
              
              
            


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()