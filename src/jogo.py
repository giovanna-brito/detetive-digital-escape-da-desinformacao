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
)


def executar_jogo():
    """Inicializa e executa o jogo Detetive Digital."""

    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 30)

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

    # Carregando a primeira notícia
    noticia_atual = obter_noticia(0)

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
                                0, resposta
                            )

                            if resultado:
                                pontos += PONTOS_RESPOSTA_CORRETA
                            else:
                                vidas -= 1

                            noticia_concluida = True

                    elif evento.key == pygame.K_e:
                        investigando = False

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

                    if perto and not noticia_concluida:
                        investigando = True

        # Movimentação do jogador
        if not investigando and vidas > 0 and not noticia_concluida:

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

        tela.blit(texto_pontos, (20, 20))
        tela.blit(texto_vidas, (20, 55))

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

        if perto and not investigando and not noticia_concluida:
            texto = fonte.render(
                "Pressione E para investigar",
                True,
                COR_TEXTO,
            )
            tela.blit(texto, (250, 520))

        # Exibe a tela de investigação
        if investigando and noticia_atual is not None:

            desenhar_tela_investigacao(
                tela,
                noticia_atual,
                resultado,
            )

            if resultado is not None:
                texto = fonte.render(
                    "Pressione E para fechar",
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

        # Verifica se o jogador perdeu todas as vidas
        if vidas <= 0:
            texto = fonte.render(
                "Fim de jogo! Você ficou sem vidas.",
                True,
                COR_TEXTO,
            )
            tela.blit(texto, (200, 520))

        pygame.display.flip()

    pygame.quit()
