class GameStats():
    def __init__(self, ai_game):

        self.settings = ai_game.settings

        self.stat_reset()

    def stat_reset(self):
        self.ship_left = self.settings.max_ships

        
