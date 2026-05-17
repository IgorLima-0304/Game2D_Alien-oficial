import pygame
from typing import Any, Type

from alien import Alien


class FleetManager:
    """Responsável por criar e gerenciar a frota de alienígenas (SRP)."""

    def __init__(self, screen: pygame.Surface, settings: Any, ship: Any, alien_class: Type[Alien]) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.alien_class = alien_class
        self.aliens = pygame.sprite.Group()

    def create_fleet(self) -> None:
        """Cria a frota completa de alienígenas."""
        alien = self.alien_class(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - self.ship.rect.height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number, alien_width, alien_height)

    def _create_alien(self, alien_number: int, row_number: int, alien_width: int, alien_height: int) -> None:
        alien = self.alien_class(self.screen, self.settings)
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (2 * alien_height * row_number)
        self.aliens.add(alien)

    def update_aliens(self) -> None:
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self) -> None:
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1