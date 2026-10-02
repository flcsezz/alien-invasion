import pygame

class Settings():
    def __init__(self):

        """A class for all the settings in alien invasion"""
        self.screen_height = 900
        self.screen_width = 1400
        self.bg_colour = (15, 15, 26)
        self.swift_speed = 15
        self.normal_speed = 4
        self.max_ships = 3

        self.alien_points = 20

        #Bullets
        self.bullet_height = 13
        self.bullet_width = 5
        self.bullet_speed = 0
        self.bullet_color = (255, 170, 0)
        
        self.bullet_maxheat = 400
        self.bullet_coolingrate = 2.3
        self.bullet_heatrate_singlemode = 10
        self.bullet_heatrate_cannonmode = 25
        self.bullet_heatrate_trimode = 40
        self.trimode_delay = 500
        self.singlemode_delay = 280
        self.cannonmode_ddelay = 350

        self.obj_speed = 0

        #Images
        self.asteroid_img = pygame.image.load("images/asteroid.bmp")
        self.nebula_img = pygame.image.load("images/nebula.bmp")
        self.planet_gas = pygame.image.load("images/planet_gas_giant.bmp")
        self.planet_ice = pygame.image.load("images/planet_ice_toxic.bmp")
        self.planet_terrestrial = pygame.image.load('images/planet_terrestrial.bmp')
        self.starL = pygame.image.load('images/star_large.bmp')
        self.starM = pygame.image.load("images/star_medium.bmp")
        self.starS = pygame.image.load('images/star_small.bmp')

        self.alien1 = pygame.image.load('images/alien.bmp')

        #Alien settings
        self.alien_speed = 3.0
        self.spawn_delay_alien = 1000
        self.spawn_delay_bgobject = 1000

        # Stage progression data (5 Handcrafted Stages)
        self.stages = [
            {
                "name": "STAGE 1: SCOUT PATROL",
                "score_target": 120,
                "alien_speed": 2,
                "bullet_speed": 6.0,
                "spawn_delay_alien": 2000,
                "spawn_delay_bgobject": 2000,
                "obj_speed": 3.0,
                "alien_points": 20,
            },
            {
                "name": "STAGE 2: ASTEROID SECTOR",
                "score_target": 500,
                "alien_speed": 3,
                "bullet_speed": 6.5,
                "spawn_delay_alien": 1500,
                "spawn_delay_bgobject": 2000,
                "obj_speed": 4.5,
                "alien_points": 30,
            },
            {
                "name": "STAGE 3: VANGUARD ASSAULT",
                "score_target": 1800,
                "alien_speed": 3.5,
                "bullet_speed": 8.0,
                "spawn_delay_alien": 1300,
                "spawn_delay_bgobject": 1400,
                "obj_speed": 5.0,
                "alien_points": 45,
            },
            {
                "name": "STAGE 4: DEEP SPACE SWARM",
                "score_target": 3000,
                "alien_speed": 5.0,
                "bullet_speed": 8.0,
                "spawn_delay_alien": 500,
                "spawn_delay_bgobject": 1000,
                "obj_speed": 6.0,
                "alien_points": 75,
            },
            {
                "name": "STAGE 5: FINAL INVASION",
                "score_target": None,
                "alien_speed": 6.2,
                "bullet_speed": 9.0,
                "spawn_delay_alien": 380,
                "spawn_delay_bgobject": 800,
                "obj_speed": 7.0,
                "alien_points": 100,
            },
        ]

    def apply_stage(self, stage_idx):
        if 0 <= stage_idx < len(self.stages):
            stage = self.stages[stage_idx]
            self.alien_speed = stage["alien_speed"]
            self.bullet_speed = stage["bullet_speed"]
            self.spawn_delay_alien = stage["spawn_delay_alien"]
            self.spawn_delay_bgobject = stage["spawn_delay_bgobject"]
            self.obj_speed = stage["obj_speed"]
            self.alien_points = stage["alien_points"]