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

def desenhar_tela_investigacao(tela, noticia, resultado):
    """Desenha o painel com a notícia e as opções de classificação."""

    fonte = pygame.font.Font(None, 25)
    fonte_titulo = pygame.font.Font(None, 34)
    fonte_noticia = pygame.font.Font(None, 28)
    fonte_explicacao = pygame.font.Font(None, 23)

    cor_branca = (255, 255, 255)
    cor_amarela = (242, 215, 126)
    cor_painel = (48, 39, 71)

    # Desenha o painel
    pygame.draw.rect(
        tela,
        cor_painel,
        (60, 55, 680, 490)
    )

    # Título do painel
    titulo = fonte_titulo.render(
        "Investigação",
        True,
        cor_branca
    )

    tela.blit(titulo, (100, 75))

    # Função para quebrar textos em linhas
    def quebrar_texto(texto, fonte, largura_maxima):

        palavras = texto.split()
        linhas = []
        linha_atual = ""

        for palavra in palavras:

            teste = linha_atual + palavra + " "

            if fonte.size(teste)[0] <= largura_maxima:
                linha_atual = teste

            else:
                if linha_atual:
                    linhas.append(linha_atual)

                linha_atual = palavra + " "

        if linha_atual:
            linhas.append(linha_atual)

        return linhas

    # Desenha o título da notícia
    linhas_titulo = quebrar_texto(
        noticia["titulo"],
        fonte_noticia,
        620
    )

    y = 125

    for linha in linhas_titulo:

        texto = fonte_noticia.render(
            linha,
            True,
            cor_amarela
        )

        tela.blit(texto, (100, y))
        y += 32

    # Desenha o conteúdo da notícia
    y += 10

    linhas_conteudo = quebrar_texto(
        noticia["conteudo"],
        fonte,
        620
    )

    for linha in linhas_conteudo:

        texto = fonte.render(
            linha,
            True,
            cor_branca
        )

        tela.blit(texto, (100, y))
        y += 29

    # Desenha as opções de classificação
    y += 15

    opcoes = [
        "1 - Real",
        "2 - Manipulada",
        "3 - Criada por IA"
    ]

    for opcao in opcoes:

        texto = fonte.render(
            opcao,
            True,
            cor_branca
        )

        tela.blit(texto, (120, y))
        y += 32

    # Se o jogador já respondeu, exibe o resultado
    if resultado is not None:

        y += 10

        if resultado:
            mensagem = "Resposta correta!"
        else:
            mensagem = "Resposta incorreta!"

        texto_resultado = fonte.render(
            mensagem,
            True,
            cor_branca
        )

        tela.blit(texto_resultado, (120, y))

        # Desenha a explicação com quebra automática
        y += 35

        linhas_explicacao = quebrar_texto(
            noticia["explicacao"],
            fonte_explicacao,
            600
        )

        for linha in linhas_explicacao:

            texto = fonte_explicacao.render(
                linha,
                True,
                cor_branca
            )

            tela.blit(texto, (120, y))
            y += 26

def verificar_resposta(resposta_escolhida, resposta_correta):
    """Verifica se a classificação escolhida está correta."""

    return resposta_escolhida == resposta_correta
