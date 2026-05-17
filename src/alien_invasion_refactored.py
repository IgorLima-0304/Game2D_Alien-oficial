import sys
import pygame
from typing import NoReturn

from settings import Settings
from ship import Ship
from alien import Alien
from fast_alien import FastAlien

from game_events import GameEventHandler
from bullet_manager import BulletManager
from fleet_manager import FleetManager
from game_renderer import GameRenderer


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos (orquestrador)."""

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self.screen, self.settings)
        self.bg_color = self.settings.bg_color

        # Managers (SRP)
        self.bullet_manager = BulletManager(self.screen, self.settings, self.ship)
        self.fleet_manager = FleetManager(self.screen, self.settings, self.ship, Alien)
        self.event_handler = GameEventHandler(self.ship, self.bullet_manager)
        self.renderer = GameRenderer(
            self.screen, self.bg_color, self.ship,
            self.bullet_manager.bullets, self.fleet_manager.aliens
        )


    def run_game(self) -> NoReturn:
        """Loop principal do jogo."""
        self.fleet_manager.create_fleet()

        while True:
            self.event_handler.check_events()
            self._update_game_state()
            self.renderer.render_screen()


    def _update_game_state(self) -> None:
        """Atualiza todos os elementos do jogo."""
        self.ship.update()
        self.bullet_manager.update_bullets(self.fleet_manager.aliens)
        self.fleet_manager.update_aliens()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()