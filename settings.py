import pygame

class Settings():
    def __init__(self):

        """A class for all the settings in alien invasion"""
        self.screen_height = 900
        self.screen_width = 1400
        self.bg_colour = (15, 15, 26)
        self.swift_speed = 9
        self.normal_speed = 4
        self.max_ships = 3

        #Bullets
        self.bullet_height = 13
        self.bullet_width = 5
        self.bullet_speed = 18
        self.bullet_color = (255, 170, 0)
        
        self.bullet_maxheat = 400
        self.bullet_coolingrate = 2.3
        self.bullet_heatrate_singlemode = 10
        self.bullet_heatrate_cannonmode = 25
        self.bullet_heatrate_trimode = 40
        self.trimode_delay = 500
        self.singlemode_delay = 280
        self.cannonmode_ddelay = 350

        self.obj_speed = 10

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
        