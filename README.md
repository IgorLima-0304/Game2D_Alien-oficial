# Game2D Alien

Um jogo 2D simples desenvolvido em aula para a disciplina AQS. Este repositório contém a implementação do jogo, recursos (imagens/sons) e código-fonte em Python, utilizando a biblioteca Pygame.

## Sumário

- [Sobre](#sobre)
- [Recursos](#recursos)
- [Tecnologias](#tecnologias)
- [Requisitos](#requisitos)
- [Instalação](#instalacao)
- [Como executar](#como-executar)
- [Controles](#controles)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Contribuição](#contribuicao)
- [Licença](#licenca)
- [Contato](#contato)

## Sobre

Game2D Alien é um projeto didático que demonstra conceitos básicos de desenvolvimento de jogos 2D: loop principal, detecção de colisões, renderização de sprites, entrada do jogador e gerenciamento de estados (menu, jogo, game over). O objetivo principal é reforçar conteúdos vistos em sala e servir como base para extensões e melhorias.

## Recursos

- Jogabilidade 2D com inimigos e tiros
- Animação de sprites e efeitos sonoros (se incluídos)
- Sistema simples de pontuação e vidas
- Menus básicos (iniciar, pausar, game over)

## Tecnologias

- Python 3.8+ (recomendado)
- Pygame

## Requisitos

- Python 3.8 ou superior
- pip
- Pygame (instalável via pip)

## Instalação

1. Clone o repositório:

   git clone https://github.com/IgorLima-0304/Game2D_Alien-oficial.git
   cd Game2D_Alien-oficial

2. (Opcional) Crie e ative um ambiente virtual:

   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate

3. Instale dependências:

   pip install pygame

Se houver um arquivo requirements.txt no repositório, instale com:

   pip install -r requirements.txt

## Como executar

Execute o arquivo principal do jogo. Dependendo da organização do repositório, o nome do arquivo principal pode ser `main.py`, `game.py` ou estar dentro de um diretório (por exemplo `src/`). Exemplos:

   python main.py
   # ou
   python game.py

Se receber erros sobre arquivos faltando (assets), verifique se a pasta de recursos foi baixada corretamente.

> Observação: ajuste o comando acima conforme o nome do arquivo principal presente no repositório.

## Controles

Os controles abaixo são exemplos comuns; verifique a implementação real no código e atualize conforme necessário:

- Teclas de seta: mover o jogador
- Espaço: atirar
- P: pausar
- Esc: sair

## Estrutura do projeto (exemplo)

- assets/        → Imagens, sons e outros recursos
- src/           → Código-fonte do jogo
- main.py        → Ponto de entrada (exemplo)
- README.md      → Documentação

Atualize esta seção para refletir a estrutura real do seu repositório.

## Contribuição

Contribuições são bem-vindas! Algumas sugestões:

1. Abra uma issue descrevendo a proposta ou o bug.
2. Crie uma branch com um nome descritivo: `feature/nova-funcionalidade` ou `fix/descricao-do-bug`.
3. Faça commits claros e concisos.
4. Abra um pull request explicando as mudanças.

Por favor, adicione testes quando possível e mantenha o padrão de código.

## Licença

Adicione aqui a licença do projeto (por exemplo MIT) ou remova esta seção se não aplicável.

## Contato

Igor Lima — https://github.com/IgorLima-0304

