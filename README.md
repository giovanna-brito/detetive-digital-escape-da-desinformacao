# 🕵️ Detetive Digital: Escape da Desinformação

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

O jogo tem como proposta estimular o pensamento crítico e a análise de informações por meio de investigações sobre notícias reais, manipuladas e conteúdos criados por Inteligência Artificial.

## Integrantes do grupo

- Giovanna Brito Silva Ribeiro

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo, incluindo configurações, funções, gerenciamento de dados, sprites e execução da partida.
- `assets/`: imagens, fontes e sons utilizados no jogo.
- `data/`: diretório destinado ao armazenamento de dados do jogo.
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo a proposta inicial.

## Descrição do jogo

Detetive Digital: Escape da Desinformação é um jogo educativo em 2D no qual o jogador assume o papel de um investigador digital. Por meio da exploração de um cenário e da interação com computadores, o jogador recebe notícias e precisa analisar as informações apresentadas.

Cada conteúdo deve ser classificado em uma das seguintes categorias:

- **Real:** informação autêntica, respaldada por evidências.
- **Manipulada:** conteúdo que apresenta alterações ou distorções de informações.
- **Criada por IA:** conteúdo produzido por ferramentas de Inteligência Artificial.

Após cada investigação, o jogador recebe o resultado da classificação e uma explicação sobre o conteúdo analisado.

## Objetivo do jogador

O objetivo é investigar os conteúdos apresentados, identificar corretamente sua classificação e avançar pelas etapas do jogo.

O jogador deve utilizar as informações disponíveis e desenvolver uma postura crítica diante de conteúdos que circulam no ambiente digital.

## Regras do jogo

- O jogador controla um personagem que pode se movimentar pelo cenário.
- Para iniciar uma investigação, é necessário se aproximar de um computador e pressionar a tecla E.
- Cada notícia apresenta três possibilidades de classificação.
- Uma resposta correta aumenta a pontuação.
- Uma resposta incorreta reduz uma vida.
- O jogo possui inicialmente três vidas.
- Após responder, o jogador recebe uma explicação sobre a classificação.

## Controles

- W: mover para cima.
- S: mover para baixo.
- A: mover para a esquerda.
- D: mover para a direita.
- E: interagir com o computador e abrir ou fechar a investigação.
- 1: classificar como Real.
- 2: classificar como Manipulada.
- 3: classificar como Criada por IA.
- Fechar a janela: sair do jogo.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/giovanna-brito/detetive-digital-escape-da-desinformacao.git
cd detetive-digital-escape-da-desinformacao
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o jogo

```bash
python main.py
```

## Como executar os testes

Para executar os testes automatizados, utilize:

```bash
python -m pytest
```

## Checklist mínimo para entrega

- [x] Preencher o README com a descrição e as regras atuais do jogo.
- [ ] Atualizar `docs/proposta.MD` com a proposta do grupo.
- [x] Garantir que o jogo executa com `python main.py`.
- [ ] Criar e executar os testes com `pytest`.

## Observações

- O projeto está sendo desenvolvido de forma modular, com separação entre configurações, regras, dados e execução do jogo.
- As notícias e suas respectivas respostas são previamente cadastradas.
- O desenvolvimento está em andamento. Funcionalidades como progressão entre investigações e organização das três fases ainda serão implementadas.
