import pygame.font

class Scoreboard():
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_colour = (160,160,160)
        self.font = pygame.font.SysFont(None, 35)

        self.prep_score()

    def prep_score(self):

        self.score_str = str(self.stats.score)

        self.score_img = self.font.render(self.score_str, True, self.text_colour, self.settings.bg_colour)

        self.img_rect = self.score_img.get_rect()

        self.img_rect.right = self.screen_rect.right - 20
        self.img_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_img, self.img_rect)

    def show_stage(self, stage):
        self.text_colours = (200, 200, 200)
        self.stage_str = str(stage)

        self.stage_img = self.font.render(self.stage_str, True, self.text_colours, self.settings.bg_colour)

        self.stage_img_rect = self.stage_img.get_rect()
        self.stage_img_rect.right = self.screen_rect.right - 20
        self.stage_img_rect.top = 60

        self.screen.blit(self.stage_img, self.stage_img_rect)

    def show_banner(self, banner_text):
        """Displays a bold banner in the center of the screen when entering a new stage"""
        banner_font = pygame.font.SysFont(None, 56)
        banner_img = banner_font.render(banner_text, True, (255, 215, 0))
        banner_rect = banner_img.get_rect()
        banner_rect.center = self.screen_rect.center
        self.screen.blit(banner_img, banner_rect)

    def show_highscore(self):

        self.hscore_str = "Highscore " + str(self.stats.highscore)
        self.hscore_img = self.font.render(self.hscore_str, True, self.text_colour)
        self.hscore_img_rect = self.hscore_img.get_rect()

        self.hscore_img_rect.left = self.screen_rect.left + 30
        self.hscore_img_rect.top = 35

        self.screen.blit(self.hscore_img, self.hscore_img_rect)


        