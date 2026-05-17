from abc import ABC, abstractmethod
import pygame
from typing import Any


class IUpdatable(ABC):
    """Interface pequena: apenas objetos que podem ser atualizados."""
    @abstractmethod
    def update(self) -> None:
        pass


class IDrawable(ABC):
    """Interface pequena: apenas objetos que podem ser desenhados."""
    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass


class ICollidable(ABC):
    """Interface para objetos que participam de colisões."""
    @abstractmethod
    def get_rect(self):
        pass