from alien import Alien


class FastAlien(Alien):
    """Exemplo de LSP: subclasse pode substituir a classe pai sem quebrar o jogo."""

    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.speed_multiplier = 2.5  # Alien mais rápido

    def update(self) -> None:
        """Sobrescreve o comportamento mantendo o contrato da classe pai."""
        self.x += (self.settings.alien_speed * self.speed_multiplier * 
                  self.settings.fleet_direction)
        self.rect.x = self.x