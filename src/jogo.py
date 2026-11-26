import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    FUNDO,
    COR_JOGADOR,
    COR_COMPUTADOR,
    COR_TEXTO,
    LARGURA_JOGADOR,
    ALTURA_JOGADOR,
    VELOCIDADE_JOGADOR,
    LARGURA_COMPUTADOR,
    ALTURA_COMPUTADOR,
    VIDAS_INICIAIS,
    PONTOS_RESPOSTA_CORRETA,
)

from src.funcoes import (
    desenhar_jogador,
    desenhar_cenario,
    desenhar_computador,
    desenhar_tela_investigacao,
)

from src.dados import (
    obter_noticia,
    verificar_resposta,
    obter_total_noticias,
)

from src.sprites import Animacao


# ==================================================
# SPRITES DO PERSONAGEM
# ==================================================

def criar_sprite_provisorio(direcao, quadro):
    """Cria um personagem em pixel art com animação."""

    largura = 48
    altura = 64

    sprite = pygame.Surface((largura, altura), pygame.SRCALPHA)

    contorno = (40, 27, 48)
    cabelo = (55, 35, 39)
    cabelo_claro = (90, 55, 48)
    pele = (235, 184, 143)

    roxo_escuro = (75, 42, 111)
    roxo = (116, 74, 164)
    roxo_claro = (157, 111, 202)

    verde = (112, 225, 161)
    calca = (49, 46, 76)

    tenis = (235, 235, 245)
    tenis_sola = (174, 174, 190)

    andando = quadro % 2 == 1
    deslocamento = 2 if andando else 0

    pygame.draw.ellipse(
        sprite,
        (20, 15, 30, 90),
        (9, 56, 30, 7)
    )

    direcao = direcao.lower()

    if direcao in ("baixo", "down", "frente", "front"):
        direcao = "baixo"
    elif direcao in ("cima", "up", "costas", "back"):
        direcao = "cima"
    elif direcao in ("esquerda", "left"):
        direcao = "esquerda"
    elif direcao in ("direita", "right"):
        direcao = "direita"
    else:
        direcao = "baixo"

    # Pernas
    pygame.draw.rect(
        sprite, contorno,
        (16, 43, 7, 14 + deslocamento)
    )

    pygame.draw.rect(
        sprite, contorno,
        (25, 43, 7, 14 - deslocamento)
    )

    pygame.draw.rect(
        sprite, calca,
        (17, 44, 5, 12 + deslocamento)
    )

    pygame.draw.rect(
        sprite, calca,
        (26, 44, 5, 12 - deslocamento)
    )

    # Tênis
    pygame.draw.rect(
        sprite, tenis_sola,
        (14, 55 + deslocamento, 10, 5)
    )

    pygame.draw.rect(
        sprite, tenis,
        (15, 54 + deslocamento, 8, 4)
    )

    pygame.draw.rect(
        sprite, tenis_sola,
        (24, 55 - deslocamento, 10, 5)
    )

    pygame.draw.rect(
        sprite, tenis,
        (25, 54 - deslocamento, 8, 4)
    )

    # Corpo
    pygame.draw.rect(
        sprite, contorno,
        (14, 25, 20, 22)
    )

    pygame.draw.rect(
        sprite, roxo,
        (15, 26, 18, 20)
    )

    pygame.draw.rect(
        sprite, roxo_claro,
        (15, 27, 3, 17)
    )

    pygame.draw.rect(
        sprite, roxo_escuro,
        (30, 27, 3, 17)
    )

    pygame.draw.rect(
        sprite, verde,
        (21, 29, 6, 12)
    )

    # Braços
    pygame.draw.rect(
        sprite, contorno,
        (10, 29, 7, 16 + deslocamento)
    )

    pygame.draw.rect(
        sprite, contorno,
        (31, 29, 7, 16 - deslocamento)
    )

    pygame.draw.rect(
        sprite, roxo,
        (11, 30, 5, 13 + deslocamento)
    )

    pygame.draw.rect(
        sprite, roxo,
        (32, 30, 5, 13 - deslocamento)
    )

    pygame.draw.rect(
        sprite, pele,
        (11, 42 + deslocamento, 5, 4)
    )

    pygame.draw.rect(
        sprite, pele,
        (32, 42 - deslocamento, 5, 4)
    )

    # Mochila
    if direcao == "cima":

        pygame.draw.rect(
            sprite, roxo_escuro,
            (17, 27, 14, 17)
        )

        pygame.draw.rect(
            sprite, roxo_claro,
            (18, 29, 3, 12)
        )

        pygame.draw.rect(
            sprite, roxo,
            (21, 30, 7, 10)
        )

    elif direcao == "esquerda":

        pygame.draw.rect(
            sprite, roxo_escuro,
            (28, 27, 8, 17)
        )

        pygame.draw.rect(
            sprite, roxo_claro,
            (30, 29, 3, 12)
        )

    elif direcao == "direita":

        pygame.draw.rect(
            sprite, roxo_escuro,
            (12, 27, 8, 17)
        )

        pygame.draw.rect(
            sprite, roxo_claro,
            (14, 29, 3, 12)
        )

    else:

        pygame.draw.rect(
            sprite, roxo_escuro,
            (12, 25, 24, 21)
        )

        pygame.draw.rect(
            sprite, roxo_claro,
            (13, 27, 4, 15)
        )

    # Pescoço
    pygame.draw.rect(
        sprite, pele,
        (20, 22, 8, 5)
    )

    # Cabeça
    pygame.draw.rect(
        sprite, contorno,
        (13, 7, 22, 19)
    )

    pygame.draw.rect(
        sprite, pele,
        (14, 9, 20, 16)
    )

    # Cabelo
    pygame.draw.rect(
        sprite, cabelo,
        (13, 6, 22, 8)
    )

    pygame.draw.rect(
        sprite, cabelo,
        (13, 7, 4, 15)
    )

    pygame.draw.rect(
        sprite, cabelo,
        (31, 7, 4, 15)
    )

    pygame.draw.rect(
        sprite, cabelo_claro,
        (17, 7, 8, 3)
    )

    # Cabelo visto por trás
    if direcao == "cima":

        pygame.draw.rect(
            sprite, cabelo,
            (14, 8, 20, 17)
        )

        pygame.draw.rect(
            sprite, cabelo_claro,
            (17, 10, 4, 4)
        )

        pygame.draw.rect(
            sprite, cabelo,
            (16, 15, 16, 7)
        )

    # Olhos e boca
    if direcao == "baixo":

        pygame.draw.rect(
            sprite, contorno,
            (18, 16, 3, 3)
        )

        pygame.draw.rect(
            sprite, contorno,
            (27, 16, 3, 3)
        )

        pygame.draw.rect(
            sprite, (255, 255, 255),
            (19, 16, 1, 1)
        )

        pygame.draw.rect(
            sprite, (255, 255, 255),
            (28, 16, 1, 1)
        )

        pygame.draw.rect(
            sprite, (165, 91, 90),
            (22, 21, 4, 1)
        )

    elif direcao == "esquerda":

        pygame.draw.rect(
            sprite, contorno,
            (17, 16, 3, 3)
        )

        pygame.draw.rect(
            sprite, (165, 91, 90),
            (17, 21, 3, 1)
        )

    elif direcao == "direita":

        pygame.draw.rect(
            sprite, contorno,
            (29, 16, 3, 3)
        )

        pygame.draw.rect(
            sprite, (165, 91, 90),
            (30, 21, 3, 1)
        )

    return sprite


def criar_animacoes_provisorias():
    """Cria animações nas quatro direções."""

    direcoes = ["baixo", "cima", "esquerda", "direita"]

    animacoes = {}

    for direcao in direcoes:

        quadros = [
            criar_sprite_provisorio(direcao, 0),
            criar_sprite_provisorio(direcao, 1)
        ]

        animacoes[direcao] = Animacao(
            quadros,
            duracao_quadro=0.15
        )

    return animacoes


# ==================================================
# FUNÇÕES DE INTERFACE
# ==================================================

def desenhar_texto_centralizado(
    tela,
    texto,
    fonte,
    cor,
    y
):
    """Desenha texto centralizado horizontalmente."""

    imagem = fonte.render(texto, True, cor)

    retangulo = imagem.get_rect(
        center=(LARGURA_TELA // 2, y)
    )

    tela.blit(imagem, retangulo)


def desenhar_botao(
    tela,
    texto,
    retangulo,
    fonte,
    mouse
):
    """Desenha botão com destaque ao passar o mouse."""

    cor_normal = (70, 57, 100)
    cor_destaque = (100, 82, 140)
    cor_texto = (255, 255, 255)

    if retangulo.collidepoint(mouse):
        cor = cor_destaque
    else:
        cor = cor_normal

    pygame.draw.rect(
        tela,
        cor,
        retangulo,
        border_radius=12
    )

    pygame.draw.rect(
        tela,
        (150, 130, 190),
        retangulo,
        width=2,
        border_radius=12
    )

    imagem = fonte.render(texto, True, cor_texto)

    imagem_rect = imagem.get_rect(
        center=retangulo.center
    )

    tela.blit(imagem, imagem_rect)

    return retangulo


# ==================================================
# COLISÃO E MOVIMENTAÇÃO
# ==================================================

def movimentar_com_colisao(
    x,
    y,
    largura,
    altura,
    velocidade,
    dt,
    obstaculos
):
    """Movimenta o personagem sem atravessar computadores."""

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

    # Evita velocidade diagonal maior
    if movimento_x != 0 or movimento_y != 0:

        tamanho = (
            movimento_x ** 2 + movimento_y ** 2
        ) ** 0.5

        movimento_x /= tamanho
        movimento_y /= tamanho

    jogador = pygame.Rect(
        int(x),
        int(y),
        largura,
        altura
    )

    # Colisão horizontal
    jogador.x += int(movimento_x * velocidade * dt)

    for obstaculo in obstaculos:

        if jogador.colliderect(obstaculo):

            if movimento_x > 0:
                jogador.right = obstaculo.left

            elif movimento_x < 0:
                jogador.left = obstaculo.right

    # Colisão vertical
    jogador.y += int(movimento_y * velocidade * dt)

    for obstaculo in obstaculos:

        if jogador.colliderect(obstaculo):

            if movimento_y > 0:
                jogador.bottom = obstaculo.top

            elif movimento_y < 0:
                jogador.top = obstaculo.bottom

    # Limites da tela
    jogador.x = max(
        0,
        min(
            jogador.x,
            LARGURA_TELA - largura
        )
    )

    jogador.y = max(
        0,
        min(
            jogador.y,
            ALTURA_TELA - altura
        )
    )

    return jogador.x, jogador.y


def computador_ao_alcance(
    jogador_x,
    jogador_y,
    largura_jogador,
    altura_jogador,
    computador_x,
    computador_y,
    largura_computador,
    altura_computador
):
    """Verifica se o jogador está próximo para investigar."""

    jogador = pygame.Rect(
        jogador_x,
        jogador_y,
        largura_jogador,
        altura_jogador
    )

    computador = pygame.Rect(
        computador_x,
        computador_y,
        largura_computador,
        altura_computador
    )

    area_interacao = computador.inflate(50, 50)

    return jogador.colliderect(area_interacao)


# ==================================================
# DESTAQUE VISUAL DO COMPUTADOR
# ==================================================

def desenhar_destaque_computador(tela, computador):
    """Desenha uma borda visual no computador interativo."""

    retangulo = pygame.Rect(
        computador["x"],
        computador["y"],
        LARGURA_COMPUTADOR,
        ALTURA_COMPUTADOR
    )

    # Borda externa roxa
    borda_externa = retangulo.inflate(16, 16)

    pygame.draw.rect(
        tela,
        (157, 111, 202),
        borda_externa,
        width=5,
        border_radius=12
    )

    # Borda interna dourada
    borda_interna = retangulo.inflate(9, 9)

    pygame.draw.rect(
        tela,
        (242, 215, 126),
        borda_interna,
        width=2,
        border_radius=9
    )


# ==================================================
# EXECUÇÃO DO JOGO
# ==================================================

def executar_jogo():
    """Inicializa e executa o Detetive Digital."""

    pygame.init()

    tela = pygame.display.set_mode(
        (LARGURA_TELA, ALTURA_TELA)
    )

    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    fonte = pygame.font.Font(None, 30)
    fonte_titulo = pygame.font.Font(None, 56)
    fonte_subtitulo = pygame.font.Font(None, 34)
    fonte_botao = pygame.font.Font(None, 32)
    fonte_pequena = pygame.font.Font(None, 24)

    rodando = True
    estado = "menu"

    total_noticias = obter_total_noticias()

    cor_painel = (48, 39, 71)
    cor_destaque = (242, 215, 126)
    cor_branca = (255, 255, 255)
    cor_computador_concluido = (100, 100, 110)

    # ==================================================
    # COMPUTADORES DO CENÁRIO
    # ==================================================

    computadores = [
        {
            "x": 120,
            "y": 250,
            "noticia": 0,
            "nome": "Caso 1",
        },
        {
            "x": 550,
            "y": 180,
            "noticia": 1,
            "nome": "Caso 2",
        },
        {
            "x": 350,
            "y": 420,
            "noticia": 2,
            "nome": "Caso 3",
        },
    ]

    # Cria as áreas de colisão dos computadores
    obstaculos = []

    for computador in computadores:

        obstaculo = pygame.Rect(
            computador["x"],
            computador["y"],
            LARGURA_COMPUTADOR,
            ALTURA_COMPUTADOR
        )

        obstaculos.append(obstaculo)

    # ==================================================
    # REINICIAR PARTIDA
    # ==================================================

    def iniciar_partida():

        jogador_x = 350
        jogador_y = 100

        vidas = VIDAS_INICIAIS
        pontos = 0

        investigando = False
        resultado = None

        noticia_atual = None
        numero_noticia_atual = None

        noticias_concluidas = []

        animacoes = criar_animacoes_provisorias()

        direcao_jogador = "baixo"
        estava_movendo = False

        return (
            jogador_x,
            jogador_y,
            vidas,
            pontos,
            investigando,
            resultado,
            noticia_atual,
            numero_noticia_atual,
            noticias_concluidas,
            animacoes,
            direcao_jogador,
            estava_movendo,
        )

    (
        jogador_x,
        jogador_y,
        vidas,
        pontos,
        investigando,
        resultado,
        noticia_atual,
        numero_noticia_atual,
        noticias_concluidas,
        animacoes,
        direcao_jogador,
        estava_movendo,
    ) = iniciar_partida()

    # ==================================================
    # BOTÕES
    # ==================================================

    botao_iniciar = pygame.Rect(250, 260, 300, 60)
    botao_instrucoes = pygame.Rect(250, 340, 300, 60)
    botao_sair = pygame.Rect(250, 420, 300, 60)
    botao_voltar = pygame.Rect(250, 470, 300, 60)

    botao_novamente = pygame.Rect(250, 300, 300, 60)
    botao_menu = pygame.Rect(250, 380, 300, 60)
    botao_sair_final = pygame.Rect(250, 460, 300, 60)

    # ==================================================
    # LOOP PRINCIPAL
    # ==================================================

    while rodando:

        dt = relogio.tick(FPS) / 1000

        mouse = pygame.mouse.get_pos()

        # ==================================================
        # EVENTOS
        # ==================================================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            # ----------------------------------------------
            # MENU
            # ----------------------------------------------

            if estado == "menu":

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_RETURN:

                        estado = "jogando"

                        (
                            jogador_x,
                            jogador_y,
                            vidas,
                            pontos,
                            investigando,
                            resultado,
                            noticia_atual,
                            numero_noticia_atual,
                            noticias_concluidas,
                            animacoes,
                            direcao_jogador,
                            estava_movendo,
                        ) = iniciar_partida()

                    elif evento.key == pygame.K_i:
                        estado = "instrucoes"

                    elif evento.key == pygame.K_ESCAPE:
                        rodando = False

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    if evento.button == 1:

                        if botao_iniciar.collidepoint(mouse):

                            estado = "jogando"

                            (
                                jogador_x,
                                jogador_y,
                                vidas,
                                pontos,
                                investigando,
                                resultado,
                                noticia_atual,
                                numero_noticia_atual,
                                noticias_concluidas,
                                animacoes,
                                direcao_jogador,
                                estava_movendo,
                            ) = iniciar_partida()

                        elif botao_instrucoes.collidepoint(mouse):
                            estado = "instrucoes"

                        elif botao_sair.collidepoint(mouse):
                            rodando = False

            # ----------------------------------------------
            # INSTRUÇÕES
            # ----------------------------------------------

            elif estado == "instrucoes":

                if evento.type == pygame.KEYDOWN:

                    if evento.key in (
                        pygame.K_ESCAPE,
                        pygame.K_RETURN,
                    ):
                        estado = "menu"

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    if evento.button == 1:

                        if botao_voltar.collidepoint(mouse):
                            estado = "menu"

            # ----------------------------------------------
            # PARTIDA
            # ----------------------------------------------

            elif estado == "jogando":

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_ESCAPE:
                        estado = "menu"

                    elif investigando:

                        if resultado is None:

                            if evento.key == pygame.K_1:
                                resposta = "Real"

                            elif evento.key == pygame.K_2:
                                resposta = "Manipulada"

                            elif evento.key == pygame.K_3:
                                resposta = "Criada por IA"

                            else:
                                resposta = None

                            if resposta is not None:

                                resultado = verificar_resposta(
                                    numero_noticia_atual,
                                    resposta
                                )

                                if resultado:
                                    pontos += PONTOS_RESPOSTA_CORRETA
                                else:
                                    vidas -= 1

                                if (
                                    numero_noticia_atual
                                    not in noticias_concluidas
                                ):

                                    noticias_concluidas.append(
                                        numero_noticia_atual
                                    )

                                if vidas <= 0:

                                    investigando = False
                                    estado = "derrota"

                        elif evento.key == pygame.K_e:

                            investigando = False

                            noticia_atual = None
                            numero_noticia_atual = None
                            resultado = None

                            if (
                                len(noticias_concluidas)
                                == total_noticias
                            ):
                                estado = "vitoria"

                    elif evento.key == pygame.K_e:

                        for computador in computadores:

                            perto = computador_ao_alcance(
                                jogador_x,
                                jogador_y,
                                LARGURA_JOGADOR,
                                ALTURA_JOGADOR,
                                computador["x"],
                                computador["y"],
                                LARGURA_COMPUTADOR,
                                ALTURA_COMPUTADOR,
                            )

                            numero = computador["noticia"]

                            if (
                                perto
                                and numero not in noticias_concluidas
                            ):

                                numero_noticia_atual = numero

                                noticia_atual = obter_noticia(
                                    numero_noticia_atual
                                )

                                investigando = True
                                resultado = None

                                break

            # ----------------------------------------------
            # VITÓRIA E DERROTA
            # ----------------------------------------------

            elif estado in ("vitoria", "derrota"):

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_r:

                        (
                            jogador_x,
                            jogador_y,
                            vidas,
                            pontos,
                            investigando,
                            resultado,
                            noticia_atual,
                            numero_noticia_atual,
                            noticias_concluidas,
                            animacoes,
                            direcao_jogador,
                            estava_movendo,
                        ) = iniciar_partida()

                        estado = "jogando"

                    elif evento.key == pygame.K_m:
                        estado = "menu"

                    elif evento.key == pygame.K_ESCAPE:
                        rodando = False

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    if evento.button == 1:

                        if botao_novamente.collidepoint(mouse):

                            (
                                jogador_x,
                                jogador_y,
                                vidas,
                                pontos,
                                investigando,
                                resultado,
                                noticia_atual,
                                numero_noticia_atual,
                                noticias_concluidas,
                                animacoes,
                                direcao_jogador,
                                estava_movendo,
                            ) = iniciar_partida()

                            estado = "jogando"

                        elif botao_menu.collidepoint(mouse):
                            estado = "menu"

                        elif botao_sair_final.collidepoint(mouse):
                            rodando = False

        # ==================================================
        # DESENHO
        # ==================================================

        if estado == "menu":

            tela.fill(FUNDO)

            desenhar_texto_centralizado(
                tela,
                "DETETIVE DIGITAL",
                fonte_titulo,
                cor_destaque,
                130,
            )

            desenhar_texto_centralizado(
                tela,
                "Escape da Desinformação",
                fonte_subtitulo,
                cor_branca,
                195,
            )

            desenhar_botao(
                tela,
                "INICIAR JOGO",
                botao_iniciar,
                fonte_botao,
                mouse,
            )

            desenhar_botao(
                tela,
                "INSTRUÇÕES",
                botao_instrucoes,
                fonte_botao,
                mouse,
            )

            desenhar_botao(
                tela,
                "SAIR",
                botao_sair,
                fonte_botao,
                mouse,
            )

            desenhar_texto_centralizado(
                tela,
                "Pressione ENTER para iniciar",
                fonte_pequena,
                cor_branca,
                550,
            )

        # ----------------------------------------------
        # INSTRUÇÕES
        # ----------------------------------------------

        elif estado == "instrucoes":

            tela.fill(FUNDO)

            desenhar_texto_centralizado(
                tela,
                "COMO JOGAR",
                fonte_titulo,
                cor_destaque,
                90,
            )

            instrucoes = [
                "Use WASD para movimentar o personagem.",
                "Encontre os 3 computadores no cenário.",
                "Pressione E perto de um computador.",
                "Use 1, 2 ou 3 para classificar a notícia.",
                "Respostas corretas valem 10 pontos.",
                "Respostas incorretas fazem perder uma vida.",
                "Pressione E após responder para continuar.",
                "Conclua todas as investigações para vencer.",
            ]

            y = 155

            for texto in instrucoes:

                imagem = fonte.render(
                    texto,
                    True,
                    cor_branca
                )

                retangulo = imagem.get_rect(
                    center=(LARGURA_TELA // 2, y)
                )

                tela.blit(imagem, retangulo)

                y += 34

            desenhar_botao(
                tela,
                "VOLTAR",
                botao_voltar,
                fonte_botao,
                mouse,
            )

        # ----------------------------------------------
        # JOGO
        # ----------------------------------------------

        elif estado == "jogando":

            desenhar_cenario(tela, FUNDO)

            # ==================================================
            # MOVIMENTAÇÃO E ANIMAÇÃO
            # ==================================================

            teclas = pygame.key.get_pressed()

            movendo = (
                teclas[pygame.K_w]
                or teclas[pygame.K_a]
                or teclas[pygame.K_s]
                or teclas[pygame.K_d]
            )

            if not investigando:

                if movendo:

                    if teclas[pygame.K_w]:
                        nova_direcao = "cima"

                    elif teclas[pygame.K_s]:
                        nova_direcao = "baixo"

                    elif teclas[pygame.K_a]:
                        nova_direcao = "esquerda"

                    elif teclas[pygame.K_d]:
                        nova_direcao = "direita"

                    else:
                        nova_direcao = direcao_jogador

                    if nova_direcao != direcao_jogador:
                        animacoes[nova_direcao].reiniciar()

                    direcao_jogador = nova_direcao

                    animacoes[direcao_jogador].atualizar(dt)

                    estava_movendo = True

                else:
                    estava_movendo = False

                # Movimenta respeitando os computadores
                jogador_x, jogador_y = movimentar_com_colisao(
                    jogador_x,
                    jogador_y,
                    LARGURA_JOGADOR,
                    ALTURA_JOGADOR,
                    VELOCIDADE_JOGADOR,
                    dt,
                    obstaculos,
                )

            # ==================================================
            # SPRITE ATUAL
            # ==================================================

            if movendo and not investigando:

                sprite_atual = animacoes[
                    direcao_jogador
                ].obter_quadro()

            else:

                sprite_atual = animacoes[
                    direcao_jogador
                ].quadros[0]

            sprite_atual = pygame.transform.scale(
                sprite_atual,
                (LARGURA_JOGADOR, ALTURA_JOGADOR)
            )

            # ==================================================
            # IDENTIFICAR COMPUTADOR PRÓXIMO
            # ==================================================

            computador_perto = None

            if not investigando:

                for computador in computadores:

                    numero = computador["noticia"]

                    perto = computador_ao_alcance(
                        jogador_x,
                        jogador_y,
                        LARGURA_JOGADOR,
                        ALTURA_JOGADOR,
                        computador["x"],
                        computador["y"],
                        LARGURA_COMPUTADOR,
                        ALTURA_COMPUTADOR,
                    )

                    if (
                        perto
                        and numero not in noticias_concluidas
                    ):

                        computador_perto = computador
                        break

            # ==================================================
            # CAMADAS / PROFUNDIDADE
            # ==================================================

            elementos = []

            # Adiciona computadores como elementos do cenário
            for computador in computadores:

                elementos.append({
                    "tipo": "computador",
                    "objeto": computador,
                    "profundidade": (
                        computador["y"] + ALTURA_COMPUTADOR
                    ),
                })

            # Adiciona personagem
            elementos.append({
                "tipo": "jogador",
                "objeto": None,
                "profundidade": (
                    jogador_y + ALTURA_JOGADOR
                ),
            })

            # Ordena pela posição vertical
            elementos.sort(
                key=lambda elemento: elemento["profundidade"]
            )

            # Desenha elementos na ordem correta
            for elemento in elementos:

                if elemento["tipo"] == "jogador":

                    desenhar_jogador(
                        tela,
                        COR_JOGADOR,
                        round(jogador_x),
                        round(jogador_y),
                        LARGURA_JOGADOR,
                        ALTURA_JOGADOR,
                        sprite=sprite_atual,
                    )

                elif elemento["tipo"] == "computador":

                    computador = elemento["objeto"]

                    numero = computador["noticia"]

                    # Cor normal ou de computador concluído
                    if numero in noticias_concluidas:

                        cor_computador = (
                            cor_computador_concluido
                        )

                    else:

                        cor_computador = COR_COMPUTADOR

                    # Desenha o computador
                    desenhar_computador(
                        tela,
                        computador["x"],
                        computador["y"],
                        LARGURA_COMPUTADOR,
                        ALTURA_COMPUTADOR,
                        cor_computador,
                    )

                    # Destaca computador disponível próximo
                    if computador == computador_perto:

                        desenhar_destaque_computador(
                            tela,
                            computador
                        )

                    # Nome do caso
                    texto_caso = fonte_pequena.render(
                        computador["nome"],
                        True,
                        cor_branca,
                    )

                    tela.blit(
                        texto_caso,
                        (
                            computador["x"] + 15,
                            computador["y"] - 25,
                        )
                    )

                    # Indicação de caso concluído
                    if numero in noticias_concluidas:

                        texto_concluido = fonte_pequena.render(
                            "Concluído",
                            True,
                            cor_branca,
                        )

                        tela.blit(
                            texto_concluido,
                            (
                                computador["x"] + 10,
                                computador["y"]
                                + ALTURA_COMPUTADOR + 5,
                            )
                        )

            # ==================================================
            # HUD
            # ==================================================

            texto_pontos = fonte.render(
                f"Pontos: {pontos}",
                True,
                COR_TEXTO,
            )

            texto_vidas = fonte.render(
                f"Vidas: {vidas}",
                True,
                COR_TEXTO,
            )

            texto_investigacoes = fonte.render(
                f"Concluídas: {len(noticias_concluidas)}/{total_noticias}",
                True,
                COR_TEXTO,
            )

            tela.blit(texto_pontos, (20, 20))
            tela.blit(texto_vidas, (20, 55))
            tela.blit(texto_investigacoes, (20, 90))

            # ==================================================
            # AVISO DE INTERAÇÃO
            # ==================================================

            if computador_perto is not None:

                texto = fonte.render(
                    f"Pressione E para investigar {computador_perto['nome']}",
                    True,
                    COR_TEXTO,
                )

                tela.blit(texto, (170, 520))

            # ==================================================
            # INVESTIGAÇÃO
            # ==================================================

            if investigando and noticia_atual is not None:

                desenhar_tela_investigacao(
                    tela,
                    noticia_atual,
                    resultado,
                )

                if resultado is not None:

                    texto = fonte.render(
                        "Pressione E para continuar",
                        True,
                        COR_TEXTO,
                    )

                    tela.blit(texto, (250, 550))

        # ----------------------------------------------
        # VITÓRIA
        # ----------------------------------------------

        elif estado == "vitoria":

            tela.fill(FUNDO)

            pygame.draw.rect(
                tela,
                cor_painel,
                (100, 120, 600, 430),
                border_radius=20,
            )

            desenhar_texto_centralizado(
                tela,
                "INVESTIGAÇÕES CONCLUÍDAS!",
                fonte_titulo,
                cor_destaque,
                190,
            )

            desenhar_texto_centralizado(
                tela,
                "Parabéns, Detetive Digital!",
                fonte_subtitulo,
                cor_branca,
                250,
            )

            desenhar_texto_centralizado(
                tela,
                f"Pontuação final: {pontos}",
                fonte,
                cor_branca,
                285,
            )

            desenhar_botao(
                tela,
                "JOGAR NOVAMENTE",
                botao_novamente,
                fonte_botao,
                mouse,
            )

            desenhar_botao(
                tela,
                "VOLTAR AO MENU",
                botao_menu,
                fonte_botao,
                mouse,
            )

            desenhar_botao(
                tela,
                "SAIR",
                botao_sair_final,
                fonte_botao,
                mouse,
            )

        # ----------------------------------------------
        # DERROTA
        # ----------------------------------------------

        elif estado == "derrota":

            tela.fill(FUNDO)

            pygame.draw.rect(
                tela,
                cor_painel,
                (100, 120, 600, 430),
                border_radius=20,
            )

            desenhar_texto_centralizado(
                tela,
                "FIM DE JOGO!",
                fonte_titulo,
                cor_destaque,
                190,
            )

            desenhar_texto_centralizado(
                tela,
                "Você ficou sem vidas.",
                fonte_subtitulo,
                cor_branca,
                250,
            )

            desenhar_texto_centralizado(
                tela,
                f"Pontuação final: {pontos}",
                fonte,
                cor_branca,
                285,
            )

            desenhar_botao(
                tela,
                "JOGAR NOVAMENTE",
                botao_novamente,
                fonte_botao,
                mouse,
            )

            desenhar_botao(
                tela,
                "VOLTAR AO MENU",
                botao_menu,
                fonte_botao,
                mouse,
            )

            desenhar_botao(
                tela,
                "SAIR",
                botao_sair_final,
                fonte_botao,
                mouse,
            )

        pygame.display.flip()

    pygame.quit()