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


def executar_jogo():
    """Inicializa e executa o jogo Detetive Digital."""

    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 30)
    fonte_titulo = pygame.font.Font(None, 48)

    rodando = True

    # Criando o jogador
    jogador_x = 100
    jogador_y = 100

    # Criando o computador
    computador_x = 550
    computador_y = 350

    # Estado inicial do jogo
    vidas = VIDAS_INICIAIS
    pontos = 0

    investigando = False
    resultado = None
    noticia_concluida = False
    jogo_concluido = False

    # Controle das notícias
    numero_noticia = 0
    total_noticias = obter_total_noticias()

    # Carregando a primeira notícia
    noticia_atual = obter_noticia(numero_noticia)

    # Loop principal do jogo
    while rodando:

        dt = relogio.tick(FPS) / 1000

        # Processamento dos eventos
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:

                # Quando o jogador está investigando
                if investigando:

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

                        # Verifica a resposta escolhida
                        if resposta is not None:

                            resultado = verificar_resposta(
                                numero_noticia,
                                resposta
                            )

                            # Se acertou
                            if resultado:
                                pontos += PONTOS_RESPOSTA_CORRETA

                            # Se errou
                            else:
                                vidas -= 1

                            noticia_concluida = True

                    # Se já respondeu, E fecha a investigação
                    elif evento.key == pygame.K_e:

                        investigando = False

                        # Se ainda possui vidas
                        if vidas > 0:

                            # Avança para a próxima notícia
                            numero_noticia += 1

                            # Verifica se existem mais notícias
                            if numero_noticia < total_noticias:

                                noticia_atual = obter_noticia(
                                    numero_noticia
                                )

                                resultado = None
                                noticia_concluida = False

                            # Se todas as notícias foram investigadas
                            else:
                                jogo_concluido = True

                # Quando o jogador está no cenário
                elif evento.key == pygame.K_e:

                    perto = jogador_perto_computador(
                        jogador_x,
                        jogador_y,
                        LARGURA_JOGADOR,
                        ALTURA_JOGADOR,
                        computador_x,
                        computador_y,
                        LARGURA_COMPUTADOR,
                        ALTURA_COMPUTADOR,
                    )

                    # Inicia uma investigação
                    if (
                        perto
                        and not noticia_concluida
                        and not jogo_concluido
                        and vidas > 0
                    ):
                        investigando = True

        # Movimentação do jogador
        if (
            not investigando
            and vidas > 0
            and not jogo_concluido
        ):

            jogador_x, jogador_y = movimentar_jogador(
                jogador_x,
                jogador_y,
                LARGURA_JOGADOR,
                ALTURA_JOGADOR,
                VELOCIDADE_JOGADOR,
                dt,
            )

        # Desenho do cenário
        desenhar_cenario(tela, FUNDO)

        # Desenho do computador
        desenhar_computador(
            tela,
            computador_x,
            computador_y,
            LARGURA_COMPUTADOR,
            ALTURA_COMPUTADOR,
            COR_COMPUTADOR,
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

        # Informações da partida
        texto_pontos = fonte.render(
            f"Pontos: {pontos}", True, COR_TEXTO
        )

        texto_vidas = fonte.render(
            f"Vidas: {vidas}", True, COR_TEXTO
        )

        texto_investigacoes = fonte.render(
            f"Investigação: {min(numero_noticia + 1, total_noticias)}/{total_noticias}",
            True,
            COR_TEXTO,
        )

        tela.blit(texto_pontos, (20, 20))
        tela.blit(texto_vidas, (20, 55))
        tela.blit(texto_investigacoes, (20, 90))

        # Verifica se o jogador está perto do computador
        perto = jogador_perto_computador(
            jogador_x,
            jogador_y,
            LARGURA_JOGADOR,
            ALTURA_JOGADOR,
            computador_x,
            computador_y,
            LARGURA_COMPUTADOR,
            ALTURA_COMPUTADOR,
        )

        # Mensagem para iniciar investigação
        if (
            perto
            and not investigando
            and not noticia_concluida
            and not jogo_concluido
            and vidas > 0
        ):

            texto = fonte.render(
                "Pressione E para investigar",
                True,
                COR_TEXTO,
            )

            tela.blit(texto, (250, 520))

        # Exibe a tela de investigação
        # Exibe a tela de investigação somente se o jogador ainda tiver vidas
        if (
            investigando
            and noticia_atual is not None
            and vidas > 0
            and not jogo_concluido
        ):

            desenhar_tela_investigacao(
                tela,
                noticia_atual,
                resultado,
            )

            # Após responder, mostra a instrução para continuar
            if resultado is not None:

                texto = fonte.render(
                    "Pressione E para continuar",
                    True,
                    COR_TEXTO,
                )

                tela.blit(texto, (250, 550))

        # Mensagem de investigação concluída
        if noticia_concluida and not investigando and vidas > 0:

            texto = fonte.render(
                "Investigação concluída!",
                True,
                COR_TEXTO,
            )

            tela.blit(texto, (250, 520))

        # Tela de fim de jogo por falta de vidas
        if vidas <= 0:

            pygame.draw.rect(
                tela,
                (48, 39, 71),
                (100, 200, 600, 200),
            )

            texto_titulo = fonte_titulo.render(
                "Fim de jogo!",
                True,
                COR_TEXTO,
            )

            texto_mensagem = fonte.render(
                "Você ficou sem vidas.",
                True,
                COR_TEXTO,
            )

            texto_pontuacao = fonte.render(
                f"Pontuação final: {pontos}",
                True,
                COR_TEXTO,
            )

            tela.blit(texto_titulo, (280, 230))
            tela.blit(texto_mensagem, (260, 290))
            tela.blit(texto_pontuacao, (270, 340))

        # Tela de conclusão das investigações
        if jogo_concluido:

            pygame.draw.rect(
                tela,
                (48, 39, 71),
                (100, 180, 600, 240),
            )

            texto_titulo = fonte_titulo.render(
                "Investigações concluídas!",
                True,
                COR_TEXTO,
            )

            texto_pontuacao = fonte.render(
                f"Pontuação final: {pontos}",
                True,
                COR_TEXTO,
            )

            texto_mensagem = fonte.render(
                "Parabéns, Detetive Digital!",
                True,
                COR_TEXTO,
            )

            tela.blit(texto_titulo, (145, 230))
            tela.blit(texto_mensagem, (210, 300))
            tela.blit(texto_pontuacao, (250, 350))

        pygame.display.flip()

    pygame.quit()