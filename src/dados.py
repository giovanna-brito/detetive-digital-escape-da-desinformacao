
# Notícias disponíveis para as investigações do jogo

NOTICIAS = [
    {
        "id": 1,
        "titulo": "Biblioteca municipal amplia horário",
        "conteudo": "Uma publicação afirma que a biblioteca municipal "
                    "passará a funcionar também aos domingos. "
                    "O comunicado oficial confirma a mudança.",
        "alternativas": [
            "Real",
            "Manipulada",
            "Criada por IA"
        ],
        "resposta_correta": "Real",
        "explicacao": "A informação corresponde ao comunicado oficial "
                      "disponibilizado como evidência no caso."
    },

    {
        "id": 2,
        "titulo": "Escolas serão fechadas por tempo indeterminado",
        "conteudo": "Uma publicação afirma que todas as escolas da cidade "
                    "serão fechadas por tempo indeterminado. "
                    "O comunicado original informa apenas que duas escolas "
                    "terão aulas suspensas durante um dia.",
        "alternativas": [
            "Real",
            "Manipulada",
            "Criada por IA"
        ],
        "resposta_correta": "Manipulada",
        "explicacao": "O conteúdo distorce o comunicado original. "
                      "A suspensão era limitada a duas escolas e a um dia, "
                      "não abrangia toda a rede por tempo indeterminado."
    },

    {
        "id": 3,
        "titulo": "Descoberta de animal fantástico",
        "conteudo": "Uma notícia apresenta a descoberta de um animal "
                    "fantástico capaz de brilhar no escuro e fala sobre "
                    "uma pesquisa científica inexistente. "
                    "O material foi produzido por uma ferramenta de IA "
                    "e identificado em seus registros de criação.",
        "alternativas": [
            "Real",
            "Manipulada",
            "Criada por IA"
        ],
        "resposta_correta": "Criada por IA",
        "explicacao": "Os registros de produção do material confirmam "
                      "que o conteúdo foi gerado por Inteligência Artificial. "
                      "A classificação não é baseada apenas na aparência."
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
