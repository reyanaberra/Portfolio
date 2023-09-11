import pygame
from pygame.sprite import Sprite

class Samus(Sprite):
    """A class to manage Samus."""

    def __init__(self, mi_game):
        """Initialize Samus and set her starting position."""
        super().__init__()
        self.screen = mi_game.screen
        self.settings = mi_game.settings
        self.screen_rect = mi_game.screen.get_rect()

        # Load the Samus image and gets its rect.
        self.image = pygame.image.load("C:\\Users\\reyan\\Desktop\\Python Projects\\Metroid Invasion\\images\\SamusCenter.png")
        self.rect = self.image.get_rect()

        # Start each Samus at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for Samus's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Look flag
        self.look_right = False
        self.look_left = False

    def update(self):
        """Update Samus's position based on the movement flags."""
        # Update Samus's x value, not the rect.
        if self.moving_right and not self.moving_left and self.rect.right < self.settings.screen_width:
            self.image = pygame.image.load("C:\\Users\\reyan\\Desktop\\Python Projects\\Metroid Invasion\\images\\SamusRight.png")
            self.x += self.settings.samus_speed
        if self.moving_left and not self.moving_right and self.rect.left > 0:
            self.image = pygame.image.load("C:\\Users\\reyan\\Desktop\\Python Projects\\Metroid Invasion\\images\\SamusLeft.png")
            self.x -= self.settings.samus_speed

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.x = self.x

    def blitme(self):
        """Draw Samus at her current location."""
        self.screen.blit(self.image, self.rect)

    def center_samus(self):
        """Center Samus on the screen."""
        self.image = pygame.image.load("C:\\Users\\reyan\\Desktop\\Python Projects\\Metroid Invasion\\images\\SamusCenter.png")
        self.look_right = False
        self.look_left = False
        self.moving_right = False
        self.moving_left = False
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)