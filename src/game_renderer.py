import pygame
from typing import Any


class GameRenderer:
    """Responsável apenas por renderizar (desenhar) tudo na tela (SRP)."""

    def __init__(self, screen: pygame.Surface, bg_color: tuple, ship: Any,
                 bullets: pygame.sprite.Group, aliens: pygame.sprite.Group) -> None:
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens

    def render_screen(self) -> None:
        """Redesenha a tela a cada frame."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()