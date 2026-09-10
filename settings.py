class Settings():
    def __init__(self):

        """A class for all the settings in alien invasion"""
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_colour = (169,169,169)
        self.ship_speed = 4

        #Bullets
        self.bullet_height = 13
        self.bullet_width = 5
        self.bullet_speed = 18
        self.bullet_color = (179,60,60)
        
        self.bullet_maxheat = 400
        self.bullet_coolingrate = 2.3
        self.bullet_heatrate_singlemode = 10
        self.bullet_heatrate_cannonmode = 25
        self.bullet_heatrate_trimode = 40
        self.trimode_delay = 500
        self.singlemode_delay = 280
        self.cannonmode_ddelay = 350