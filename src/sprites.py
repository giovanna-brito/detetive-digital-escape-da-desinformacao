
import pygame


def pegar_sprite(local_arquivo, x, y, width, height, scale=1):
    """Recorta um sprite de uma spritesheet BMP."""

    sheet = pygame.image.load(local_arquivo).convert()

    sprite = pygame.Surface((width, height))
    sprite.set_colorkey((0, 0, 0))

    sprite.blit(sheet, (0, 0), (x, y, width, height))

    if scale != 1:
        sprite = pygame.transform.scale(
            sprite,
            (int(width * scale), int(height * scale))
        )

    return sprite


class Animacao:
    """Controla a animação de um conjunto de sprites."""

    def __init__(self, quadros, duracao_quadro=0.15):
        self.quadros = quadros
        self.duracao_quadro = duracao_quadro
        self.tempo = 0
        self.indice = 0

    def atualizar(self, dt):
        """Avança a animação de acordo com o tempo."""

        if len(self.quadros) <= 1:
            self.indice = 0
            return

        self.tempo += dt

        if self.tempo >= self.duracao_quadro:
            self.tempo = 0
            self.indice += 1

            if self.indice >= len(self.quadros):
                self.indice = 0

    def obter_quadro(self):
        """Retorna o sprite atual."""

        return self.quadros[self.indice]

    def reiniciar(self):
        """Reinicia a animação."""

        self.tempo = 0
        self.indice = 0
