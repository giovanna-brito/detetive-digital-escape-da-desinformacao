import math
import pygame


# ==================================================
# PERSONAGEM
# ==================================================

def _criar_sprite_personagem(direcao, quadro):
    """Cria um quadro do personagem em pixel art."""

    sprite = pygame.Surface((32, 48), pygame.SRCALPHA)

    pele = (238, 190, 151)
    cabelo = (48, 34, 55)
    roupa = (105, 65, 155)
    roupa_clara = (145, 105, 190)
    sombra = (65, 40, 105)
    mochila = (65, 45, 90)
    mochila_clara = (105, 75, 130)
    calca = (45, 48, 75)
    sapato = (35, 30, 45)
    olho = (35, 30, 40)

    movimento = quadro % 2

    pygame.draw.ellipse(sprite, (30, 20, 45, 100), (5, 38, 22, 8))

    # CABEÇA
    if direcao == "baixo":

        pygame.draw.rect(sprite, pele, (11, 7, 10, 10))
        pygame.draw.rect(sprite, cabelo, (10, 5, 12, 5))
        pygame.draw.rect(sprite, cabelo, (9, 8, 3, 8))
        pygame.draw.rect(sprite, cabelo, (21, 8, 3, 7))
        pygame.draw.rect(sprite, cabelo, (12, 4, 8, 2))

        pygame.draw.rect(sprite, olho, (13, 11, 2, 2))
        pygame.draw.rect(sprite, olho, (18, 11, 2, 2))

    elif direcao == "cima":

        pygame.draw.rect(sprite, cabelo, (10, 5, 12, 12))
        pygame.draw.rect(sprite, cabelo, (9, 8, 3, 8))
        pygame.draw.rect(sprite, cabelo, (21, 8, 3, 8))
        pygame.draw.rect(sprite, (75, 55, 85), (12, 7, 8, 3))

    elif direcao == "esquerda":

        pygame.draw.rect(sprite, pele, (10, 7, 11, 10))
        pygame.draw.rect(sprite, cabelo, (10, 5, 12, 5))
        pygame.draw.rect(sprite, cabelo, (9, 7, 4, 10))
        pygame.draw.rect(sprite, cabelo, (18, 8, 4, 6))
        pygame.draw.rect(sprite, olho, (11, 11, 2, 2))

    elif direcao == "direita":

        pygame.draw.rect(sprite, pele, (11, 7, 11, 10))
        pygame.draw.rect(sprite, cabelo, (10, 5, 12, 5))
        pygame.draw.rect(sprite, cabelo, (20, 7, 4, 10))
        pygame.draw.rect(sprite, cabelo, (10, 8, 4, 6))
        pygame.draw.rect(sprite, olho, (20, 11, 2, 2))

    # PESCOÇO
    pygame.draw.rect(sprite, pele, (14, 16, 4, 3))

    # MOCHILA
    if direcao == "cima":
        pygame.draw.rect(sprite, mochila, (10, 19, 12, 11))
        pygame.draw.rect(sprite, mochila_clara, (12, 21, 8, 2))
        pygame.draw.rect(sprite, mochila_clara, (14, 24, 4, 4))
    elif direcao == "esquerda":
        pygame.draw.rect(sprite, mochila, (19, 19, 5, 11))
        pygame.draw.rect(sprite, mochila_clara, (20, 21, 3, 6))
    else:
        pygame.draw.rect(sprite, mochila, (7, 19, 5, 11))
        pygame.draw.rect(sprite, mochila_clara, (8, 21, 3, 6))

    # CORPO
    pygame.draw.rect(sprite, roupa, (10, 18, 12, 12))
    pygame.draw.rect(sprite, roupa_clara, (14, 19, 4, 9))
    pygame.draw.rect(sprite, sombra, (10, 28, 12, 2))

    # BRAÇOS ANIMADOS
    if movimento == 0:
        pygame.draw.rect(sprite, roupa, (8, 20, 4, 9))
        pygame.draw.rect(sprite, roupa, (20, 20, 4, 9))
        pygame.draw.rect(sprite, pele, (8, 28, 3, 3))
        pygame.draw.rect(sprite, pele, (21, 28, 3, 3))
    else:
        pygame.draw.rect(sprite, roupa, (7, 21, 4, 7))
        pygame.draw.rect(sprite, roupa, (21, 19, 4, 8))
        pygame.draw.rect(sprite, pele, (7, 27, 3, 3))
        pygame.draw.rect(sprite, pele, (22, 26, 3, 3))

    # PERNAS ANIMADAS
    if movimento == 0:
        pygame.draw.rect(sprite, calca, (11, 30, 4, 9))
        pygame.draw.rect(sprite, calca, (17, 30, 4, 9))
        pygame.draw.rect(sprite, sapato, (10, 38, 5, 4))
        pygame.draw.rect(sprite, sapato, (17, 38, 5, 4))
    else:
        pygame.draw.rect(sprite, calca, (10, 30, 5, 8))
        pygame.draw.rect(sprite, calca, (18, 30, 4, 9))
        pygame.draw.rect(sprite, calca, (9, 36, 4, 3))
        pygame.draw.rect(sprite, sapato, (8, 38, 5, 4))
        pygame.draw.rect(sprite, sapato, (18, 38, 5, 4))

    return sprite


def desenhar_jogador(tela, cor, x, y, largura, altura, sprite=None):
    """Desenha o personagem com animação de caminhada."""

    if sprite is not None:
        tela.blit(sprite, (x, y))
        return

    if not hasattr(desenhar_jogador, "sprites"):

        desenhar_jogador.sprites = {}

        direcoes = ["baixo", "cima", "esquerda", "direita"]

        for direcao in direcoes:
            desenhar_jogador.sprites[direcao] = [
                _criar_sprite_personagem(direcao, 0),
                _criar_sprite_personagem(direcao, 1)
            ]

    teclas = pygame.key.get_pressed()

    andando = (
        teclas[pygame.K_w]
        or teclas[pygame.K_a]
        or teclas[pygame.K_s]
        or teclas[pygame.K_d]
    )

    if teclas[pygame.K_w]:
        direcao = "cima"
    elif teclas[pygame.K_s]:
        direcao = "baixo"
    elif teclas[pygame.K_a]:
        direcao = "esquerda"
    elif teclas[pygame.K_d]:
        direcao = "direita"
    else:
        direcao = getattr(desenhar_jogador, "direcao", "baixo")

    desenhar_jogador.direcao = direcao

    if andando:
        quadro = (pygame.time.get_ticks() // 180) % 2
    else:
        quadro = 0

    imagem = desenhar_jogador.sprites[direcao][quadro]

    imagem = pygame.transform.scale(imagem, (largura, altura))

    tela.blit(imagem, (x, y))


# ==================================================
# MOVIMENTAÇÃO
# ==================================================

def movimentar_jogador(
    x,
    y,
    largura_jogador,
    altura_jogador,
    velocidade,
    dt,
    obstaculos=None
):
    """Movimenta o jogador e impede que atravesse obstáculos."""

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

    if movimento_x != 0 or movimento_y != 0:
        tamanho = math.sqrt(movimento_x ** 2 + movimento_y ** 2)
        movimento_x /= tamanho
        movimento_y /= tamanho

    if obstaculos is None:
        obstaculos = []

    jogador = pygame.Rect(
        int(x), int(y),
        largura_jogador, altura_jogador
    )

    # MOVIMENTO HORIZONTAL
    deslocamento_x = movimento_x * velocidade * dt
    jogador.x = int(x + deslocamento_x)

    for obstaculo in obstaculos:
        if jogador.colliderect(obstaculo):
            if deslocamento_x > 0:
                jogador.right = obstaculo.left
            elif deslocamento_x < 0:
                jogador.left = obstaculo.right

    x = jogador.x

    # MOVIMENTO VERTICAL
    jogador.x = int(x)
    jogador.y = int(y)

    deslocamento_y = movimento_y * velocidade * dt
    jogador.y = int(y + deslocamento_y)

    for obstaculo in obstaculos:
        if jogador.colliderect(obstaculo):
            if deslocamento_y > 0:
                jogador.bottom = obstaculo.top
            elif deslocamento_y < 0:
                jogador.top = obstaculo.bottom

    y = jogador.y

    # LIMITES DA TELA
    largura_tela, altura_tela = pygame.display.get_surface().get_size()

    x = max(0, min(x, largura_tela - largura_jogador))
    y = max(0, min(y, altura_tela - altura_jogador))

    return x, y


# ==================================================
# CENÁRIO
# ==================================================

def desenhar_cenario(tela, cor_fundo):
    """Desenha um laboratório de investigação digital."""

    largura, altura = tela.get_size()

    # PALETA
    parede = (34, 27, 53)
    parede_clara = (47, 37, 69)
    piso = (34, 29, 50)
    piso_claro = (43, 36, 62)

    roxo = (117, 78, 165)
    roxo_claro = (164, 120, 210)
    roxo_escuro = (65, 45, 100)

    verde = (112, 225, 161)
    amarelo = (242, 215, 126)
    azul = (104, 165, 230)

    branco = (225, 220, 240)
    sombra = (20, 15, 30)

    # FUNDO
    tela.fill(parede)

    pygame.draw.rect(tela, parede_clara, (0, 0, largura, 103))

    # Painéis verticais na parede
    for x in range(0, largura, 100):
        pygame.draw.line(
            tela,
            (53, 43, 77),
            (x, 0),
            (x, 95),
            2
        )

    # Rodapé
    pygame.draw.rect(tela, roxo_escuro, (0, 95, largura, 8))
    pygame.draw.rect(tela, roxo, (0, 100, largura, 3))

    # PISO
    pygame.draw.rect(
        tela,
        piso,
        (0, 103, largura, altura - 103)
    )

    tamanho = 50

    for x in range(0, largura, tamanho):
        for y in range(103, altura, tamanho):

            if (x // tamanho + y // tamanho) % 2 == 0:
                pygame.draw.rect(
                    tela,
                    piso_claro,
                    (x, y, tamanho, tamanho)
                )

            pygame.draw.rect(
                tela,
                (53, 45, 75),
                (x, y, tamanho, tamanho),
                1
            )

    # LUZES DA PAREDE
    for x in range(190, largura - 50, 150):
        pygame.draw.rect(
            tela,
            (63, 52, 92),
            (x, 20, 70, 8),
            border_radius=4
        )

        pygame.draw.rect(
            tela,
            (183, 145, 220),
            (x + 5, 22, 60, 4),
            border_radius=3
        )

    # QUADRO CENTRAL
    quadro_x = largura // 2 - 90

    pygame.draw.rect(
        tela,
        sombra,
        (quadro_x + 4, 15, 180, 72),
        border_radius=5
    )

    pygame.draw.rect(
        tela,
        (73, 52, 91),
        (quadro_x, 12, 180, 72),
        border_radius=5
    )

    pygame.draw.rect(
        tela,
        roxo_claro,
        (quadro_x, 12, 180, 72),
        2,
        border_radius=5
    )

    fonte = pygame.font.Font(None, 24)

    titulo = fonte.render(
        "CENTRAL DE INVESTIGACAO",
        True,
        branco
    )

    tela.blit(titulo, (quadro_x + 14, 19))

    # Lupa
    pygame.draw.circle(
        tela,
        amarelo,
        (quadro_x + 75, 55),
        12,
        3
    )

    pygame.draw.line(
        tela,
        amarelo,
        (quadro_x + 84, 64),
        (quadro_x + 96, 74),
        4
    )

    # Computador no quadro
    pygame.draw.rect(
        tela,
        verde,
        (quadro_x + 108, 43, 35, 24),
        2,
        border_radius=3
    )

    pygame.draw.line(
        tela,
        verde,
        (quadro_x + 125, 67),
        (quadro_x + 125, 73),
        2
    )

    pygame.draw.line(
        tela,
        verde,
        (quadro_x + 117, 73),
        (quadro_x + 133, 73),
        2
    )

    # ESTANTE
    estante_x = 20
    estante_y = 20

    pygame.draw.rect(
        tela,
        sombra,
        (estante_x + 4, estante_y + 4, 160, 65),
        border_radius=4
    )

    pygame.draw.rect(
        tela,
        (76, 52, 68),
        (estante_x, estante_y, 160, 65),
        border_radius=4
    )

    pygame.draw.rect(
        tela,
        (131, 91, 112),
        (estante_x, estante_y, 160, 65),
        3,
        border_radius=4
    )

    pygame.draw.rect(
        tela,
        (131, 91, 112),
        (estante_x + 5, estante_y + 43, 150, 5)
    )

    cores_livros = [
        (130, 80, 150),
        (85, 110, 160),
        (185, 120, 95),
        (80, 145, 115),
        (165, 85, 110),
        (100, 85, 160),
        (200, 170, 100),
        (115, 130, 175),
    ]

    x_livro = estante_x + 10

    for i, cor_livro in enumerate(cores_livros):

        altura_livro = 25 + (i % 3) * 6

        pygame.draw.rect(
            tela,
            cor_livro,
            (x_livro, estante_y + 43 - altura_livro, 14, altura_livro)
        )

        pygame.draw.line(
            tela,
            (225, 215, 225),
            (x_livro + 4, estante_y + 20),
            (x_livro + 4, estante_y + 43),
            1
        )

        x_livro += 17

    # JANELA
    janela_x = largura - 180

    pygame.draw.rect(
        tela,
        sombra,
        (janela_x + 4, 17, 155, 66),
        border_radius=5
    )

    pygame.draw.rect(
        tela,
        (64, 70, 115),
        (janela_x, 12, 155, 66),
        border_radius=5
    )

    pygame.draw.rect(
        tela,
        (160, 155, 210),
        (janela_x, 12, 155, 66),
        3,
        border_radius=5
    )

    pygame.draw.rect(
        tela,
        (93, 110, 161),
        (janela_x + 7, 20, 65, 50)
    )

    pygame.draw.rect(
        tela,
        (102, 125, 177),
        (janela_x + 83, 20, 65, 50)
    )

    pygame.draw.line(
        tela,
        (153, 170, 220),
        (janela_x + 15, 25),
        (janela_x + 40, 45),
        3
    )

    pygame.draw.line(
        tela,
        (153, 170, 220),
        (janela_x + 92, 25),
        (janela_x + 120, 45),
        3
    )

    pygame.draw.rect(
        tela,
        (180, 170, 220),
        (janela_x + 75, 17, 5, 58)
    )

    pygame.draw.rect(
        tela,
        (180, 170, 220),
        (janela_x + 7, 43, 141, 4)
    )

    # TAPETE
    tapete_x = largura // 2 - 125
    tapete_y = altura // 2 - 25

    pygame.draw.rect(
        tela,
        sombra,
        (tapete_x + 5, tapete_y + 5, 250, 150),
        border_radius=10
    )

    pygame.draw.rect(
        tela,
        (48, 37, 72),
        (tapete_x, tapete_y, 250, 150),
        border_radius=10
    )

    pygame.draw.rect(
        tela,
        (95, 72, 130),
        (tapete_x + 10, tapete_y + 10, 230, 130),
        2,
        border_radius=8
    )

    pygame.draw.line(
        tela,
        (95, 72, 130),
        (tapete_x + 125, tapete_y + 10),
        (tapete_x + 125, tapete_y + 140),
        2
    )

    pygame.draw.line(
        tela,
        (95, 72, 130),
        (tapete_x + 10, tapete_y + 75),
        (tapete_x + 240, tapete_y + 75),
        2
    )

    # PLANTAS
    def desenhar_planta(x, y):

        pygame.draw.rect(
            tela,
            (120, 78, 63),
            (x, y, 35, 30),
            border_radius=4
        )

        pygame.draw.rect(
            tela,
            (155, 105, 85),
            (x - 3, y, 41, 7),
            border_radius=3
        )

        pygame.draw.ellipse(
            tela,
            (56, 120, 83),
            (x - 10, y - 35, 22, 40)
        )

        pygame.draw.ellipse(
            tela,
            (75, 160, 105),
            (x + 10, y - 45, 22, 42)
        )

        pygame.draw.ellipse(
            tela,
            (47, 105, 75),
            (x + 20, y - 30, 22, 37)
        )

        pygame.draw.ellipse(
            tela,
            (87, 175, 120),
            (x - 5, y - 50, 22, 35)
        )

        pygame.draw.ellipse(
            tela,
            (65, 140, 95),
            (x + 5, y - 25, 20, 30)
        )

    desenhar_planta(20, altura - 45)
    desenhar_planta(largura - 55, altura - 45)

    # ARMÁRIO
    armario_x = largura // 2 - 55
    armario_y = altura - 45

    pygame.draw.rect(
        tela,
        sombra,
        (armario_x + 4, armario_y + 4, 110, 30),
        border_radius=4
    )

    pygame.draw.rect(
        tela,
        (75, 55, 75),
        (armario_x, armario_y, 110, 30),
        border_radius=4
    )

    pygame.draw.rect(
        tela,
        (130, 95, 115),
        (armario_x, armario_y, 110, 30),
        2,
        border_radius=4
    )

    pygame.draw.line(
        tela,
        (130, 95, 115),
        (armario_x + 55, armario_y + 4),
        (armario_x + 55, armario_y + 26),
        2
    )

    pygame.draw.circle(
        tela,
        amarelo,
        (armario_x + 48, armario_y + 15),
        2
    )

    pygame.draw.circle(
        tela,
        amarelo,
        (armario_x + 62, armario_y + 15),
        2
    )

    # DETALHES TECNOLÓGICOS
    pygame.draw.line(tela, (75, 62, 105), (0, 115), (25, 115), 3)
    pygame.draw.line(tela, (75, 62, 105), (25, 115), (25, 145), 3)

    pygame.draw.line(
        tela,
        (75, 62, 105),
        (largura - 1, 120),
        (largura - 25, 120),
        3
    )

    pygame.draw.line(
        tela,
        (75, 62, 105),
        (largura - 25, 120),
        (largura - 25, 145),
        3
    )

    for i in range(4):

        pygame.draw.circle(
            tela,
            verde if i % 2 == 0 else azul,
            (35 + i * 12, 125),
            3
        )

        pygame.draw.circle(
            tela,
            roxo_claro,
            (largura - 35 - i * 12, 125),
            3
        )


    # PEQUENAS LUZES DECORATIVAS
    for i in range(5):

        pygame.draw.circle(
            tela,
            (90, 75, 125),
            (largura // 2 - 40 + i * 20, 90),
            2
        )


# ==================================================
# COMPUTADORES
# ==================================================

def desenhar_computador(tela, x, y, largura, altura, cor):
    """Desenha uma estação de investigação digital."""

    mesa = (76, 54, 73)
    mesa_clara = (123, 88, 112)
    mesa_escura = (48, 35, 53)

    monitor = (25, 22, 38)
    monitor_borda = (100, 88, 130)

    teclado = (35, 30, 48)
    teclas = (95, 83, 117)

    verde = (112, 225, 161)
    amarelo = (242, 215, 126)

    # SOMBRA
    pygame.draw.rect(
        tela,
        (20, 15, 30),
        (x + 4, y + 38, largura, altura - 30),
        border_radius=5
    )

    # TAMPO
    pygame.draw.rect(
        tela,
        mesa,
        (x, y + 35, largura, altura - 35),
        border_radius=5
    )

    pygame.draw.rect(
        tela,
        mesa_clara,
        (x, y + 35, largura, 7),
        border_radius=3
    )

    pygame.draw.line(
        tela,
        mesa_escura,
        (x + 5, y + 43),
        (x + largura - 5, y + 43),
        2
    )

    # PÉS
    pygame.draw.rect(
        tela,
        mesa_escura,
        (x + 8, y + altura - 5, 7, 5)
    )

    pygame.draw.rect(
        tela,
        mesa_escura,
        (x + largura - 15, y + altura - 5, 7, 5)
    )

    # MONITOR
    monitor_largura = min(64, largura - 12)
    monitor_x = x + (largura - monitor_largura) // 2
    monitor_altura = 42

    pygame.draw.rect(
        tela,
        monitor,
        (monitor_x, y, monitor_largura, monitor_altura),
        border_radius=5
    )

    pygame.draw.rect(
        tela,
        monitor_borda,
        (monitor_x, y, monitor_largura, monitor_altura),
        2,
        border_radius=5
    )

    # TELA
    margem = 5

    pygame.draw.rect(
        tela,
        cor,
        (
            monitor_x + margem,
            y + margem,
            monitor_largura - margem * 2,
            monitor_altura - margem * 2 - 3
        ),
        border_radius=2
    )

    # INTERFACE
    tela_x = monitor_x + margem + 3
    tela_y = y + margem + 3

    pygame.draw.rect(
        tela,
        (35, 37, 60),
        (tela_x, tela_y, monitor_largura - 16, 4)
    )

    pygame.draw.circle(
        tela,
        verde,
        (tela_x + 4, tela_y + 2),
        1
    )

    pygame.draw.circle(
        tela,
        amarelo,
        (tela_x + 8, tela_y + 2),
        1
    )

    # LINHAS
    for i in range(3):
        pygame.draw.rect(
            tela,
            (35, 37, 60),
            (
                tela_x + 4,
                tela_y + 9 + i * 5,
                monitor_largura - 23 - i * 5,
                2
            )
        )

    # GRÁFICO
    grafico_x = monitor_x + monitor_largura - 17
    grafico_y = y + 23

    pygame.draw.line(
        tela,
        verde,
        (grafico_x, grafico_y + 10),
        (grafico_x + 4, grafico_y + 5),
        2
    )

    pygame.draw.line(
        tela,
        verde,
        (grafico_x + 4, grafico_y + 5),
        (grafico_x + 8, grafico_y + 8),
        2
    )

    pygame.draw.line(
        tela,
        verde,
        (grafico_x + 8, grafico_y + 8),
        (grafico_x + 12, grafico_y),
        2
    )

    # SUPORTE
    pygame.draw.rect(
        tela,
        monitor_borda,
        (x + largura // 2 - 5, y + 42, 10, 7)
    )

    pygame.draw.rect(
        tela,
        monitor_borda,
        (x + largura // 2 - 15, y + 49, 30, 4),
        border_radius=2
    )

    # TECLADO
    teclado_x = x + 8
    teclado_y = y + 55
    teclado_largura = largura - 16

    pygame.draw.rect(
        tela,
        teclado,
        (teclado_x, teclado_y, teclado_largura, 9),
        border_radius=3
    )

    for i in range(7):

        tecla_x = teclado_x + 4 + i * (
            max(1, (teclado_largura - 8) // 7)
        )

        pygame.draw.rect(
            tela,
            teclas,
            (tecla_x, teclado_y + 2, 3, 2)
        )

        pygame.draw.rect(
            tela,
            teclas,
            (tecla_x, teclado_y + 5, 3, 2)
        )

    # MOUSE
    mouse_x = x + largura - 14
    mouse_y = y + 54

    pygame.draw.ellipse(
        tela,
        teclado,
        (mouse_x, mouse_y, 9, 12)
    )

    pygame.draw.line(
        tela,
        monitor_borda,
        (mouse_x + 4, mouse_y + 2),
        (mouse_x + 4, mouse_y + 5),
        1
    )

    # LUZ DE STATUS
    pygame.draw.circle(
        tela,
        verde,
        (x + largura - 8, y + 40),
        2
    )


# ==================================================
# COLISÃO / PROXIMIDADE
# ==================================================

def jogador_perto_computador(
    jogador_x,
    jogador_y,
    jogador_largura,
    jogador_altura,
    computador_x,
    computador_y,
    computador_largura,
    computador_altura
):
    """Verifica se o jogador está encostando no computador."""

    jogador = pygame.Rect(
        jogador_x,
        jogador_y,
        jogador_largura,
        jogador_altura
    )

    computador = pygame.Rect(
        computador_x,
        computador_y,
        computador_largura,
        computador_altura
    )

    return jogador.colliderect(computador)


# ==================================================
# TELA DE INVESTIGAÇÃO
# ==================================================

def desenhar_tela_investigacao(tela, noticia, resultado):
    """Desenha o painel de investigação com visual atualizado."""

    largura, altura = tela.get_size()

    fonte = pygame.font.Font(None, 27)
    fonte_titulo = pygame.font.Font(None, 38)
    fonte_noticia = pygame.font.Font(None, 30)
    fonte_explicacao = pygame.font.Font(None, 24)
    fonte_opcao = pygame.font.Font(None, 27)
    fonte_pequena = pygame.font.Font(None, 22)

    branco = (245, 242, 255)
    amarelo = (242, 215, 126)
    verde = (112, 225, 161)
    vermelho = (255, 120, 120)

    roxo = (48, 39, 71)
    roxo_claro = (110, 90, 145)
    roxo_escuro = (31, 25, 49)

    azul = (104, 165, 230)

    # FUNDO ESCURECIDO
    camada = pygame.Surface(tela.get_size(), pygame.SRCALPHA)
    camada.fill((10, 5, 20, 190))
    tela.blit(camada, (0, 0))

    # PAINEL PRINCIPAL
    painel = pygame.Rect(50, 35, largura - 100, altura - 90)

    pygame.draw.rect(
        tela,
        roxo_escuro,
        (painel.x + 5, painel.y + 6, painel.width, painel.height),
        border_radius=18
    )

    pygame.draw.rect(
        tela,
        roxo,
        painel,
        border_radius=18
    )

    pygame.draw.rect(
        tela,
        roxo_claro,
        painel,
        2,
        border_radius=18
    )

    # BARRA DO CABEÇALHO
    pygame.draw.rect(
        tela,
        (64, 51, 95),
        (painel.x + 2, painel.y + 2, painel.width - 4, 58),
        border_radius=15
    )

    # INDICADOR
    pygame.draw.circle(
        tela,
        verde,
        (painel.x + 30, painel.y + 30),
        7
    )

    titulo = fonte_titulo.render(
        "CENTRAL DE INVESTIGACAO",
        True,
        branco
    )

    tela.blit(
        titulo,
        (painel.x + 50, painel.y + 17)
    )

    # SEPARADOR
    pygame.draw.line(
        tela,
        roxo_claro,
        (painel.x + 25, painel.y + 65),
        (painel.right - 25, painel.y + 65),
        2
    )

    # FUNÇÃO DE QUEBRA DE TEXTO
    def quebrar_texto(texto, fonte, largura_maxima):

        palavras = str(texto).split()
        linhas = []
        linha_atual = ""

        for palavra in palavras:

            teste = linha_atual + palavra + " "

            if fonte.size(teste)[0] <= largura_maxima:
                linha_atual = teste

            else:

                if linha_atual:
                    linhas.append(linha_atual.strip())

                linha_atual = palavra + " "

        if linha_atual:
            linhas.append(linha_atual.strip())

        return linhas

    # CARTÃO DA NOTÍCIA
    cartao = pygame.Rect(
        painel.x + 25,
        painel.y + 80,
        painel.width - 50,
        175
    )

    pygame.draw.rect(
        tela,
        (38, 31, 58),
        cartao,
        border_radius=12
    )

    pygame.draw.rect(
        tela,
        (95, 78, 130),
        cartao,
        1,
        border_radius=12
    )

    # ÍCONE DE NOTÍCIA
    pygame.draw.rect(
        tela,
        azul,
        (cartao.x + 18, cartao.y + 18, 30, 30),
        border_radius=6
    )

    pygame.draw.line(
        tela,
        branco,
        (cartao.x + 24, cartao.y + 25),
        (cartao.x + 42, cartao.y + 25),
        2
    )

    pygame.draw.line(
        tela,
        branco,
        (cartao.x + 24, cartao.y + 31),
        (cartao.x + 42, cartao.y + 31),
        2
    )

    pygame.draw.line(
        tela,
        branco,
        (cartao.x + 24, cartao.y + 37),
        (cartao.x + 36, cartao.y + 37),
        2
    )

    # TÍTULO DA NOTÍCIA
    titulo_noticia = noticia.get("titulo", "Notícia sem título")

    linhas_titulo = quebrar_texto(
        titulo_noticia,
        fonte_noticia,
        cartao.width - 80
    )

    y = cartao.y + 18

    for linha in linhas_titulo[:3]:

        texto = fonte_noticia.render(
            linha,
            True,
            amarelo
        )

        tela.blit(
            texto,
            (cartao.x + 60, y)
        )

        y += 30

    # CONTEÚDO
    conteudo = noticia.get("conteudo", "")

    y = cartao.y + 75

    linhas_conteudo = quebrar_texto(
        conteudo,
        fonte,
        cartao.width - 40
    )

    # Limita linhas para não ultrapassar o cartão
    espaco_conteudo = cartao.bottom - 15 - y
    max_linhas = max(1, espaco_conteudo // 25)

    for linha in linhas_conteudo[:max_linhas]:

        texto = fonte.render(
            linha,
            True,
            branco
        )

        tela.blit(
            texto,
            (cartao.x + 20, y)
        )

        y += 25

    # PERGUNTA
    pergunta = fonte.render(
        "Como voce classificaria esta noticia?",
        True,
        branco
    )

    tela.blit(
        pergunta,
        (painel.x + 30, painel.y + 270)
    )

    # ALTERNATIVAS
    opcoes = [
        ("1", "REAL", verde),
        ("2", "MANIPULADA", amarelo),
        ("3", "CRIADA POR IA", azul)
    ]

    largura_opcao = (painel.width - 70) // 3
    altura_opcao = 58
    opcao_y = painel.y + 305

    for i, (numero, texto, cor) in enumerate(opcoes):

        opcao_x = painel.x + 25 + i * (largura_opcao + 10)

        caixa = pygame.Rect(
            opcao_x,
            opcao_y,
            largura_opcao,
            altura_opcao
        )

        pygame.draw.rect(
            tela,
            (39, 32, 59),
            caixa,
            border_radius=10
        )

        pygame.draw.rect(
            tela,
            cor,
            caixa,
            2,
            border_radius=10
        )

        # Número
        pygame.draw.circle(
            tela,
            cor,
            (caixa.x + 25, caixa.centery),
            15
        )

        texto_numero = fonte_opcao.render(
            numero,
            True,
            roxo_escuro
        )

        tela.blit(
            texto_numero,
            texto_numero.get_rect(
                center=(caixa.x + 25, caixa.centery)
            )
        )

        # Texto
        texto_opcao = fonte_opcao.render(
            texto,
            True,
            cor
        )

        texto_rect = texto_opcao.get_rect(
            center=(caixa.x + caixa.width // 2 + 12, caixa.centery)
        )

        tela.blit(
            texto_opcao,
            texto_rect
        )

    # RESULTADO
    if resultado is not None:

        resultado_y = painel.y + 380

        if resultado:
            cor_resultado = verde
            mensagem = "RESPOSTA CORRETA!"
        else:
            cor_resultado = vermelho
            mensagem = "RESPOSTA INCORRETA!"

        # Caixa do resultado
        caixa_resultado = pygame.Rect(
            painel.x + 25,
            resultado_y,
            painel.width - 50,
            65
        )

        pygame.draw.rect(
            tela,
            (39, 32, 59),
            caixa_resultado,
            border_radius=10
        )

        pygame.draw.rect(
            tela,
            cor_resultado,
            caixa_resultado,
            2,
            border_radius=10
        )

        texto_resultado = fonte.render(
            mensagem,
            True,
            cor_resultado
        )

        tela.blit(
            texto_resultado,
            (caixa_resultado.x + 15, caixa_resultado.y + 10)
        )

        # EXPLICAÇÃO
        explicacao = noticia.get("explicacao", "")

        linhas_explicacao = quebrar_texto(
            explicacao,
            fonte_explicacao,
            caixa_resultado.width - 30
        )

        y_explicacao = caixa_resultado.y + 38

        for linha in linhas_explicacao[:1]:

            texto = fonte_explicacao.render(
                linha,
                True,
                branco
            )

            tela.blit(
                texto,
                (caixa_resultado.x + 15, y_explicacao)
            )

    # RODAPÉ
    pygame.draw.line(
        tela,
        (85, 70, 115),
        (painel.x + 25, painel.bottom - 20),
        (painel.right - 25, painel.bottom - 20),
        1
    )

    rodape = fonte_pequena.render(
        "UTILIZE AS TECLAS 1, 2 OU 3 PARA RESPONDER",
        True,
        (175, 165, 205)
    )

    tela.blit(
        rodape,
        rodape.get_rect(
            center=(painel.centerx, painel.bottom - 10)
        )
    )