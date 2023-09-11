import pygame.font
from pygame.sprite import Group

from health import Health
import json

class Scores:
    """A Class to report scoring information."""

    def __init__(self, mi_game):
        """Initialize scorekeeping attributes."""
        self.mi_game = mi_game
        self.screen = mi_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = mi_game.settings
        self.stats = mi_game.stats

        # Fonts ettings for scoring ifnromation.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_health()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_health(self):
        """Show how much health Samus has."""
        self.health = Group()
        for hp in range(self.stats.samus_health):
            health = Health(self.mi_game)
            health.rect.x = 20 + hp * health.rect.width
            health.rect.y = 20
            self.health.add(health)

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            high_score_file = "C:\\Users\\reyan\\Desktop\\Python Projects\\Metroid Invasion\\score.json"
            with open(high_score_file, "w") as hsf:
                json.dump(self.stats.score, hsf)
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw scores, level, and health to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.health.draw(self.screen)