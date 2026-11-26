# Testes das funções do arquivo dados.py

import unittest

from src.dados import (
    obter_noticia,
    obter_alternativas,
    verificar_resposta,
    obter_explicacao,
    obter_total_noticias
)


class TestDados(unittest.TestCase):

    # TESTE 1: Verifica a quantidade de notícias
    def test_total_noticias(self):
        self.assertEqual(obter_total_noticias(), 3)

    # TESTE 2: Verifica se uma notícia válida é retornada
    def test_obter_noticia_valida(self):
        noticia = obter_noticia(0)

        self.assertIsNotNone(noticia)
        self.assertEqual(
            noticia["titulo"],
            "Biblioteca municipal amplia horário"
        )

    # TESTE 3: Verifica índice inválido
    def test_obter_noticia_invalida(self):
        self.assertIsNone(obter_noticia(-1))
        self.assertIsNone(obter_noticia(3))

    # TESTE 4: Verifica as alternativas
    def test_obter_alternativas(self):
        alternativas = obter_alternativas(0)

        self.assertEqual(
            alternativas,
            ["Real", "Manipulada", "Criada por IA"]
        )

    # TESTE 5: Verifica resposta correta
    def test_resposta_correta(self):
        self.assertTrue(verificar_resposta(0, "Real"))
        self.assertTrue(verificar_resposta(1, "Manipulada"))
        self.assertTrue(verificar_resposta(2, "Criada por IA"))

    # TESTE 6: Verifica resposta incorreta
    def test_resposta_incorreta(self):
        self.assertFalse(verificar_resposta(0, "Manipulada"))
        self.assertFalse(verificar_resposta(1, "Real"))
        self.assertFalse(verificar_resposta(2, "Real"))

    # TESTE 7: Verifica resposta em índice inválido
    def test_resposta_indice_invalido(self):
        self.assertFalse(verificar_resposta(10, "Real"))

    # TESTE 8: Verifica se a explicação é retornada
    def test_obter_explicacao(self):
        explicacao = obter_explicacao(0)

        self.assertIsInstance(explicacao, str)
        self.assertGreater(len(explicacao), 0)

    # TESTE 9: Verifica explicação para notícia inexistente
    def test_explicacao_noticia_invalida(self):
        explicacao = obter_explicacao(10)

        self.assertEqual(
            explicacao,
            "Notícia não encontrada."
        )


if __name__ == "__main__":
    unittest.main()