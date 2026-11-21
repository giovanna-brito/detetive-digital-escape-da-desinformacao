import math
import pygame


def desenhar_jogador(tela, cor, x, y, largura, altura):
    """Desenha o personagem na tela."""

    pygame.draw.rect(tela, cor, (x, y, largura, altura))


def movimentar_jogador(x, y, largura_jogador, altura_jogador, velocidade, dt):
    """Movimenta o jogador com WASD, normaliza a diagonal e limita à tela."""

    teclas = pygame.key.get_pressed()

    movimento_x = 0
    movimento_y = 0

    if teclas[pygame.K_a]:
        movimento_x -= 1
    if teclas[pygame.K_d]:
        movimento_x += 1
    if teclas[pygame.K_w]:
        movimento_y -= 1
    if teclas[pygame.K_s]:
        movimento_y += 1

    # Evita que o jogador ande mais rápido na diagonal
    if movimento_x != 0 or movimento_y != 0:
        tamanho = math.sqrt(movimento_x ** 2 + movimento_y ** 2)
        movimento_x /= tamanho
        movimento_y /= tamanho

    x += movimento_x * velocidade * dt
    y += movimento_y * velocidade * dt

    # Impede que o jogador saia da janela
    x = max(0, min(x, 800 - largura_jogador))
    y = max(0, min(y, 600 - altura_jogador))

    return x, y


def desenhar_cenario(tela, cor_fundo):
    """Desenha o fundo do cenário."""

    tela.fill(cor_fundo)


def desenhar_computador(tela, x, y, largura, altura, cor):
    """Desenha o computador no cenário."""

    pygame.draw.rect(tela, cor, (x, y, largura, altura))


def jogador_perto_computador(jogador_x, jogador_y, jogador_largura,
                             jogador_altura, computador_x, computador_y,
                             computador_largura, computador_altura):
    """Verifica se o jogador está encostando no computador."""

    jogador = pygame.Rect(
        jogador_x, jogador_y, jogador_largura, jogador_altura
    )

    computador = pygame.Rect(
        computador_x, computador_y, computador_largura, computador_altura
    )

    return jogador.colliderect(computador)


def desenhar_tela_investigacao(tela, resultado):
    """Desenha o painel de investigação e as opções de classificação."""

    fonte = pygame.font.Font(None, 28)
    fonte_titulo = pygame.font.Font(None, 36)

    pygame.draw.rect(tela, (48, 39, 71), (100, 100, 600, 400))

    titulo = fonte_titulo.render(
        "Investigação", True, (255, 255, 255)
    )
    tela.blit(titulo, (130, 125))

    opcoes = [
        "1 - Real",
        "2 - Manipulada",
        "3 - Criada por IA"
    ]

    for i, opcao in enumerate(opcoes):
        texto = fonte.render(opcao, True, (255, 255, 255))
        tela.blit(texto, (150, 250 + i * 45))

    if resultado is not None:
        mensagem = "Resposta correta!" if resultado else "Resposta incorreta!"
        texto_resultado = fonte.render(
            mensagem, True, (255, 255, 255)
        )
        tela.blit(texto_resultado, (150, 420))


def verificar_resposta(resposta_escolhida, resposta_correta):
    """Verifica se a classificação escolhida está correta."""

    return resposta_escolhida == resposta_correta
