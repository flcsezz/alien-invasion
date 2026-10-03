import json
from pathlib import Path 

class GameStats():
    def __init__(self, ai_game):

        self.settings = ai_game.settings

        self.stat_reset()

        self.path = Path("highscore.json")

        self.highscore = self._load_highscore()

    def stat_reset(self):
        self.ship_left = self.settings.max_ships
        self.score = 0
        self.current_stage_idx = 0

    def _load_highscore(self):
        if self.path.exists():
            try:
                contents = self.path.read_text()
                return json.loads(contents)
            except (json.JSONDecodeError, ValueError):
                return 0 

        return 0

    def save_highscore(self):
            contents = json.dumps(self.score)
            self.path.write_text(contents)
            self.highscore = self.score

    def live_hscore(self):
        if self.score > self.highscore:
            self.highscore = self.score


        
