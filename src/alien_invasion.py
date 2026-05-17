import sys
import pygame
from typing import NoReturn

from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self) -> None:
        """Construtor da classe que inicializa o jogo e cria os recursos básicos."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Cria uma instância da nave
        self.ship = Ship(self.screen, self.settings)

        # Muda a cor de fundo
        self.bg_color = self.settings.bg_color

        # Cria grupos para armazenar projéteis e aliens
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def _check_events(self) -> None:
        """Responde a eventos de pressionamento de teclas e mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)

            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)


    def _handle_keydown(self, event: pygame.event.Event) -> None:
        """Responde a eventos de pressionamento de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _handle_keyup(self, event: pygame.event.Event) -> None:
        """Responde a eventos de soltura de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self) -> None:
        """Dispara um projétil se o limite ainda não tiver sido alcançado."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)


    def _update_bullets(self) -> None:
        """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
        self.bullets.update()
        self._remove_offscreen_bullets()


    def _remove_offscreen_bullets(self) -> None:
        """Remove os projéteis que desapareceram da tela."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _check_bullet_alien_collisions(self) -> None:
        """Verifica colisões entre projéteis e alienígenas."""
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)


    def _update_aliens(self) -> None:
        """Verifica se a frota de alienígenas está em uma borda, então atualiza as posições."""
        self._check_fleet_edges()
        self.aliens.update()


    def _check_fleet_edges(self) -> None:
        """Responde apropriadamente se algum alienígena tiver alcançado uma borda."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self) -> None:
        """Desce toda a frota e muda a direção."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _create_fleet(self) -> None:
        """Cria uma frota de alienígenas."""
        alien = Alien(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        available_space_y = self.settings.screen_height - (3 * alien_height) - self.ship.rect.height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                alien = Alien(self.screen, self.settings)
                alien.x = alien_width + (2 * alien_width * alien_number)
                alien.rect.x = alien.x
                alien.rect.y = alien_height + (2 * alien_height * row_number)
                self.aliens.add(alien)


    def _update_screen(self) -> None:
        """Atualiza as imagens na tela e alterna para a nova tela."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


    def run_game(self) -> NoReturn:
        """Cria um laço de repetição para a tela sempre ficar visível."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._check_bullet_alien_collisions()
            self._update_aliens()
            self._update_screen()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()