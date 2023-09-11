import pygame
from pygame.sprite import Sprite

class Health(Sprite):
    """A class to manage health points."""

    def __init__(self, mi_game):
        """Initialize health."""
        super().__init__()

        # Initialize health points and get its rect.
        self.image = pygame.image.load("images\\EnergyTank.png")
        self.rect = self.image.get_rect()