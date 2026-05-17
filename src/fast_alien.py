from alien import Alien


class FastAlien(Alien):
    """Alienígena mais rápido - demonstra Open/Closed Principle."""

    def update(self) -> None:
        """Sobrescreve o update para ser mais rápido."""
        self.x += (self.settings.alien_speed * 2.5 * self.settings.fleet_direction)
        self.rect.x = self.x