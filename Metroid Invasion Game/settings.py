import pygame

class Settings:
    """A class to store all settings for Metroid Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1368
        self.screen_height = 768
        # self.bg_color = (230, 230, 230)
        self.bg = pygame.image.load("images\\MetroidBackground1.png")
        self.full_screen = False

        # Samus settings
        self.samus_health = 3

        # Missile settings
        self.missiles_allowed = 3

        # Metroid settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the metroid point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.samus_speed = 1.5
        self.missile_speed = 3.0
        self.metroid_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.metroid_points = 50

    def increase_speed(self):
        """Increase speed settings and metorid point values."""
        self.samus_speed *= self.speedup_scale
        self.missile_speed *= self.speedup_scale
        self.metroid_speed *= self.speedup_scale

        self.metroid_points += int(self.metroid_points * self.score_scale)