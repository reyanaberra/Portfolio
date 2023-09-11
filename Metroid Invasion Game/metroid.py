import pygame
from pygame.sprite import Sprite

class Metroid(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, mi_game):
        """Initialize the metroid and set its starting position."""
        super().__init__()
        self.screen = mi_game.screen
        self.settings = mi_game.settings

        # Load the metroid animation and set its rect attribute.
        self.sprites = []
        self.sprites.append(pygame.image.load("frames\\frame0.png"))
        self.sprites.append(pygame.image.load("frames\\frame1.png"))
        self.sprites.append(pygame.image.load("frames\\frame2.png"))
        self.sprites.append(pygame.image.load("frames\\frame3.png"))
        self.current_sprite = 0
        self.current_integer = int(self.current_sprite)
        
        self.image = self.sprites[self.current_integer]
        self.rect = self.image.get_rect()

        # Start each new metroid near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the metroid's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if metroid is at edge of screen."""
        screen_bound_right = self.settings.screen_width - (self.rect.width / 3)
        screen_bound_left = self.rect.width / 3
        if self.rect.right >= screen_bound_right or self.rect.left <= screen_bound_left:
            return True

    def update(self):
        """Move the metroid right or left."""
        self.current_sprite += .0125

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.current_integer = int(self.current_sprite)
        self.image = self.sprites[self.current_integer]
        self.x += (self.settings.metroid_speed * self.settings.fleet_direction)
        self.rect.x = self.x