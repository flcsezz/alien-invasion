import pygame.font

class Buttons():

    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50

        self.button_colour = (0, 135, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0,0 , self.width, self.height )  

        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)      

    def _prep_msg(self, msg):

        self.msg_img = self.font.render(msg, True, self.text_colour, self.button_colour)

        self.msg_img_rect = self.msg_img.get_rect()

        self.msg_img_rect.center = self.rect.center

    def draw(self):

        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)