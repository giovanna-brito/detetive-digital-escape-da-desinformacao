# Notícias disponíveis para as investigações do jogo

NOTICIAS = [
    {
        "id": 1,
        "titulo": "Alerta sobre enchentes na cidade",
        "conteudo": "Uma publicação afirma que a prefeitura anunciou "
                    "o fechamento de todas as escolas devido às enchentes.",
        "alternativas": [
            "Real",
            "Manipulada",
            "Criada por IA"
        ],
        "resposta_correta": "Manipulada",
        "explicacao": "A publicação utiliza uma informação verdadeira "
                      "sobre as enchentes, mas altera o comunicado oficial. "
                      "O aviso original não determinou o fechamento de "
                      "todas as escolas."
    }
]


def obter_noticia(numero):
    """Retorna os dados de uma notícia pelo seu índice."""

    if 0 <= numero < len(NOTICIAS):
        return NOTICIAS[numero]

    return None


def obter_alternativas(numero):
    """Retorna as alternativas de classificação de uma notícia."""

    noticia = obter_noticia(numero)

    if noticia is not None:
        return noticia["alternativas"]

    return []


def verificar_resposta(numero, resposta):
    """Verifica se a resposta escolhida corresponde à correta."""

    noticia = obter_noticia(numero)

    if noticia is not None:
        return resposta == noticia["resposta_correta"]

    return False


def obter_explicacao(numero):
    """Retorna a explicação da classificação correta."""

    noticia = obter_noticia(numero)

    if noticia is not None:
        return noticia["explicacao"]

    return "Notícia não encontrada."
