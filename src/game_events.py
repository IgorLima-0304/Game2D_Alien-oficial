import sys
import pygame
from typing import Any


class GameEventHandler:
    """Responsável apenas por tratar eventos de teclado e mouse (SRP)."""

    def __init__(self, ship: Any, bullet_manager: Any) -> None:
        self.ship = ship
        self.bullet_manager = bullet_manager

    def check_events(self) -> None:
        """Responde a eventos de pressionamento de teclas e mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)

            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event: pygame.event.Event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.bullet_manager.fire_bullet()

    def _handle_keyup(self, event: pygame.event.Event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False