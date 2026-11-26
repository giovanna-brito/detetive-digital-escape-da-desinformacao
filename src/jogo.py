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
    movimentar_jogador,
    desenhar_cenario,
    desenhar_computador,
    jogador_perto_computador,
    desenhar_tela_investigacao,
)

from src.dados import (
    obter_noticia,
    verificar_resposta,
    obter_total_noticias,
)


def desenhar_texto_centralizado(tela, texto, fonte, cor, y):
    """Desenha um texto centralizado horizontalmente."""

    imagem = fonte.render(texto, True, cor)

    retangulo = imagem.get_rect(
        center=(LARGURA_TELA // 2, y)
    )

    tela.blit(imagem, retangulo)


def desenhar_botao(tela, texto, retangulo, fonte, mouse):
    """Desenha um botão com destaque quando o mouse está sobre ele."""

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


def executar_jogo():
    """Inicializa e executa o jogo Detetive Digital."""

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

    # Estados das telas
    estado = "menu"

    # Quantidade de notícias cadastradas
    total_noticias = obter_total_noticias()

    # Cores adicionais
    cor_painel = (48, 39, 71)
    cor_destaque = (242, 215, 126)
    cor_branca = (255, 255, 255)
    cor_computador_concluido = (100, 100, 110)

    # --------------------------------------------------
    # COMPUTADORES DO CENÁRIO
    # --------------------------------------------------

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

    # --------------------------------------------------
    # FUNÇÃO PARA REINICIAR UMA PARTIDA
    # --------------------------------------------------

    def iniciar_partida():

        jogador_x = 350
        jogador_y = 100

        vidas = VIDAS_INICIAIS
        pontos = 0

        investigando = False
        resultado = None

        noticia_atual = None
        numero_noticia_atual = None

        # Armazena os índices das notícias concluídas
        noticias_concluidas = []

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
        )

    # Inicializa os valores da partida
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
    ) = iniciar_partida()

    # --------------------------------------------------
    # BOTÕES DO MENU
    # --------------------------------------------------

    botao_iniciar = pygame.Rect(
        250, 260, 300, 60
    )

    botao_instrucoes = pygame.Rect(
        250, 340, 300, 60
    )

    botao_sair = pygame.Rect(
        250, 420, 300, 60
    )

    # Botão da tela de instruções
    botao_voltar = pygame.Rect(
        250, 470, 300, 60
    )

    # Botões das telas finais
    botao_novamente = pygame.Rect(
        250, 300, 300, 60
    )

    botao_menu = pygame.Rect(
        250, 380, 300, 60
    )

    botao_sair_final = pygame.Rect(
        250, 460, 300, 60
    )

    # --------------------------------------------------
    # LOOP PRINCIPAL
    # --------------------------------------------------

    while rodando:

        dt = relogio.tick(FPS) / 1000

        mouse = pygame.mouse.get_pos()

        # --------------------------------------------------
        # PROCESSAMENTO DOS EVENTOS
        # --------------------------------------------------

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            # ----------------------------------------------
            # MENU INICIAL
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
                            ) = iniciar_partida()

                        elif botao_instrucoes.collidepoint(mouse):
                            estado = "instrucoes"

                        elif botao_sair.collidepoint(mouse):
                            rodando = False

            # ----------------------------------------------
            # TELA DE INSTRUÇÕES
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
            # DURANTE A PARTIDA
            # ----------------------------------------------

            elif estado == "jogando":

                if evento.type == pygame.KEYDOWN:

                    # ESC retorna ao menu
                    if evento.key == pygame.K_ESCAPE:
                        estado = "menu"

                    # Quando o jogador está investigando
                    elif investigando:

                        # Se ainda não respondeu
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

                                # Resposta correta
                                if resultado:

                                    pontos += (
                                        PONTOS_RESPOSTA_CORRETA
                                    )

                                # Resposta incorreta
                                else:

                                    vidas -= 1

                                # Marca o caso como concluído
                                if (
                                    numero_noticia_atual
                                    not in noticias_concluidas
                                ):

                                    noticias_concluidas.append(
                                        numero_noticia_atual
                                    )

                                # Verifica derrota
                                if vidas <= 0:

                                    investigando = False
                                    estado = "derrota"

                        # Depois de responder
                        elif evento.key == pygame.K_e:

                            investigando = False

                            noticia_atual = None
                            numero_noticia_atual = None
                            resultado = None

                            # Verifica se todas as notícias foram concluídas
                            if (
                                len(noticias_concluidas)
                                == total_noticias
                            ):

                                estado = "vitoria"

                    # Jogador fora da investigação
                    elif evento.key == pygame.K_e:

                        # Verifica qual computador está próximo
                        for computador in computadores:

                            perto = jogador_perto_computador(
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

                            # Verifica se está perto e se o caso não foi concluído
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
            # TELAS DE VITÓRIA E DERROTA
            # ----------------------------------------------

            elif estado in ("vitoria", "derrota"):

                if evento.type == pygame.KEYDOWN:

                    # Jogar novamente
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
                        ) = iniciar_partida()

                        estado = "jogando"

                    # Voltar ao menu
                    elif evento.key == pygame.K_m:
                        estado = "menu"

                    # Sair
                    elif evento.key == pygame.K_ESCAPE:
                        rodando = False

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    if evento.button == 1:

                        # Jogar novamente
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
                            ) = iniciar_partida()

                            estado = "jogando"

                        # Voltar ao menu
                        elif botao_menu.collidepoint(mouse):
                            estado = "menu"

                        # Sair
                        elif botao_sair_final.collidepoint(mouse):
                            rodando = False

        # --------------------------------------------------
        # DESENHO DAS TELAS
        # --------------------------------------------------

        # ----------------------------------------------
        # MENU INICIAL
        # ----------------------------------------------

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
        # PARTIDA
        # ----------------------------------------------

        elif estado == "jogando":

            desenhar_cenario(tela, FUNDO)

            # Desenha os computadores
            for computador in computadores:

                numero = computador["noticia"]

                # Muda a cor dos computadores concluídos
                if numero in noticias_concluidas:
                    cor_computador = cor_computador_concluido
                else:
                    cor_computador = COR_COMPUTADOR

                desenhar_computador(
                    tela,
                    computador["x"],
                    computador["y"],
                    LARGURA_COMPUTADOR,
                    ALTURA_COMPUTADOR,
                    cor_computador,
                )

                # Identificação dos computadores
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

                # Indica computador concluído
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
                            computador["y"] + ALTURA_COMPUTADOR + 5,
                        )
                    )

            # Desenho do jogador
            desenhar_jogador(
                tela,
                COR_JOGADOR,
                round(jogador_x),
                round(jogador_y),
                LARGURA_JOGADOR,
                ALTURA_JOGADOR,
            )

            # HUD
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

            # Movimentação
            if not investigando:

                jogador_x, jogador_y = movimentar_jogador(
                    jogador_x,
                    jogador_y,
                    LARGURA_JOGADOR,
                    ALTURA_JOGADOR,
                    VELOCIDADE_JOGADOR,
                    dt,
                )

            # Verifica se está perto de algum computador disponível
            computador_perto = None

            if not investigando:

                for computador in computadores:

                    numero = computador["noticia"]

                    perto = jogador_perto_computador(
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

            # Instrução para investigar
            if computador_perto is not None:

                texto = fonte.render(
                    f"Pressione E para investigar {computador_perto['nome']}",
                    True,
                    COR_TEXTO,
                )

                tela.blit(texto, (170, 520))

            # Painel de investigação
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