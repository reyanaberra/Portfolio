import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
    """A class to manage missiles fired from the ship."""
    
    def __init__(self, mi_game):
        super().__init__()
        self.screen = mi_game.screen
        self.settings = mi_game.settings
        self.stats = mi_game.stats
        self.samus = mi_game.samus

        # Create a missile rect at (0, 0) and then set correct position.
        self.image = pygame.image.load("images\\SamusMissile.png")
        self.rect = self.image.get_rect()
        if self.samus.look_right:
            self.rect.midbottom = (mi_game.samus.rect.x + 25, mi_game.samus.rect.y + 5)
        if self.samus.look_left:
            self.rect.midbottom = (mi_game.samus.rect.x + 13, mi_game.samus.rect.y + 5)

        # Store the missile's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the missile up the screen."""
        # Update the decimal position of the missile.
        self.y -= self.settings.missile_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_missile(self):
        """Draw the missile to the screen."""
        if self.stats.game_active:
            self.screen.blit(self.image, self.rect)
