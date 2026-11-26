# Notícias disponíveis para as investigações do jogo

NOTICIAS = [
    {
        "id": 1,
        "titulo": "Biblioteca municipal amplia horário",
        "conteudo": (
            "A biblioteca municipal passará a funcionar aos domingos. "
            "O comunicado oficial confirma a mudança."
        ),
        "alternativas": [
            "Real",
            "Manipulada",
            "Criada por IA"
        ],
        "resposta_correta": "Real",
        "explicacao": (
            "A informação foi confirmada pelo comunicado oficial."
        )
    },

    {
        "id": 2,
        "titulo": "Escolas serão fechadas por tempo indeterminado",
        "conteudo": (
            "Uma publicação anuncia o fechamento de todas as escolas. "
            "O comunicado original cita apenas duas escolas por um dia."
        ),
        "alternativas": [
            "Real",
            "Manipulada",
            "Criada por IA"
        ],
        "resposta_correta": "Manipulada",
        "explicacao": (
            "A publicação exagera e distorce o comunicado original."
        )
    },

    {
        "id": 3,
        "titulo": "Aeroporto é inaugurado com tecnologia de IA",
        "conteudo": (
            "Uma notícia anuncia um aeroporto controlado por IA. "
            "As imagens e fontes citadas foram identificadas como falsas."
        ),
        "alternativas": [
            "Real",
            "Manipulada",
            "Criada por IA"
        ],
        "resposta_correta": "Criada por IA",
        "explicacao": (
            "O material foi produzido por inteligência artificial."
        )
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


def obter_total_noticias():
    """Retorna a quantidade total de notícias cadastradas."""

    return len(NOTICIAS)