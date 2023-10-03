import json

class Stats:
    """Track statistics for Metroid Invasion."""

    def __init__(self, mi_game):
        """Initialize statistics."""
        self.settings = mi_game.settings
        self.reset_stats()

        # Start Metroid Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        high_score_file = "score.json"
        with open(high_score_file) as hsf:
            self.high_score = json.load(hsf)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.samus_health = self.settings.samus_health
        self.score = 0
        self.level = 1
