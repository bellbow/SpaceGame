class GameStats():
    #track stats for game

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        #initialize stats
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.game_active = False
