import pygame
from typing import Any

from bullet import Bullet


class BulletManager:
    """Responsável apenas por gerenciar projéteis (SRP)."""

    def __init__(self, screen: pygame.Surface, settings: Any, ship: Any) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets = pygame.sprite.Group()

    def fire_bullet(self) -> None:
        """Dispara um projétil se o limite não foi atingido."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)

    def update_bullets(self, aliens: pygame.sprite.Group) -> None:
        """Atualiza projéteis e verifica colisões."""
        self.bullets.update()
        self._remove_offscreen_bullets()
        self._check_bullet_alien_collisions(aliens)

    def _remove_offscreen_bullets(self) -> None:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self, aliens: pygame.sprite.Group) -> None:
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)