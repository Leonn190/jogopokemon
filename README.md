# Pokémon Teams

**Pokémon Teams** é um jogo estratégico por turnos feito 100% em Python, utilizando principalmente a biblioteca Pygame. O jogo traz uma experiência local 1v1, com suporte parcial ao modo online, e oferece uma grande variedade de pokémons, ataques, itens e mecânicas para explorar.

---

## 🎮 Sobre o Jogo

Neste jogo, cada jogador monta um deck e utiliza pokémons que podem se **mover, atacar e até ser capturados** durante a batalha. A vitória depende de você entender e cumprir sua **condição de vitória**, ou forçar a **condição de derrota do oponente**. 

É um jogo com foco em **estratégia**, embora o balanceamento ainda esteja em construção por falta de testes recorrentes. 

---

## 📦 Conteúdo Atual

- +55 Pokémons jogáveis
- +120 ataques únicos
- +30 itens
- Sistema de decks personalizados
- Múltiplas configurações para personalização
- Suporte parcial ao modo multiplayer (beta)
- Interface com texturas e muitos botões reutilizando funções utilitárias
- API integrada para modo online (em construção) (muitos erros mas de certa forma "jogavel")
- Mais de 15.000 linhas de código
- Arquivos já incluem +120 novos Pokémons ainda não lançados
- Mais de 600.000.000 combinações para criar um deck

---

## ⚠️ Estado Atual: Beta 1.2.4

Embora o jogo funcione bem em geral, ele **ainda está em fase Beta** e possui alguns bugs conhecidos:

### 🐞 Problemas Atuais

- **Modo online**:
  - A partida não termina automaticamente (condição de vitória não implementada)
  - Requer controle manual do servidor
  - Não possui limpeza automática das salas
- **Estádios**:
  - Apenas visuais, sem efeito no gameplay — não recomendado usá-los em decks
- **Movimentação no tabuleiro**:
  - Bugs ocasionais devido à nova mecânica de peças arrastáveis
  - Ataques que dependem disso (como *Mão Espectral* ou *Controle do Oceano*) estão **nerfados**, mas não travam o jogo
  - *Teleporte* é o único ataque de movimento totalmente funcional
- **Dano em área**:
  - Mecânica não funcional no momento
  - Pokémons com esse foco estão temporariamente nerfados
- **Treinadores recentes** (Red, James, Giovanni):
  - Pouco testados — podem apresentar comportamentos imprevistos

---
## 🧠 Como Jogar

No modo principal de **Pokémon Teams**, a partida acontece em turnos entre dois jogadores locais (1v1), controlando seus times através do **mouse**. O teclado não é utilizado.

### 🪙 Preparação
- Antes de jogar, você precisa **escolher um deck válido** (montado previamente).
- O jogo já vem com **3 decks prontos** para facilitar.
- Você também pode montar seus próprios decks usando os pokémons e itens disponíveis.

### 🎯 Objetivo
- Seu objetivo é **alcançar sua condição de vitória** ou forçar a **condição de derrota do oponente**.
- As condições variam de acordo com os pokémons, treinadores e estratégias escolhidas.

### ⚔️ Durante o jogo, você pode:
- **Capturar** pokémons (quando possível)
- **Atacar** com os pokémons usando seus ataques únicos
- **Mover** os pokémons no tabuleiro (via sistema de arraste com o mouse)
- **Usar itens**, tanto nos pokémons quanto em elementos gerais do jogo
- **Comprar itens** na loja compartilhada (mistura de itens dos dois decks)
- **Evoluir** pokémons com o sistema de **XP**

### 💡 Dicas:
- O jogo conta com **tooltips** (caixas de ajuda) para explicar partes da interface e das mecânicas. Você pode **ativar ou desativar isso nas configurações**.
- Evite usar **pokémons, ataques, treinadores e itens que dependem de mecânicas instáveis ou bugs confirmados**, pois eles podem funcionar de forma limitada ou incorreta (ver seção "Problemas Atuais").

---

## 🧩 Módulos do Projeto

Abaixo estão os principais diretórios e arquivos do projeto, com suas respectivas funções:

- **Audio/**  
  Contém músicas, sons e efeitos sonoros utilizados no jogo.

- **Imagem/**  
  Armazena imagens, animações, texturas e fundos usados nas interfaces e batalhas.

- **Geradores/**  
  Funções responsáveis pela geração de elementos do jogo, como pokémons, partidas, mapas, baralhos e itens.

- **Decks/**  
  Guarda os decks dos jogadores, incluindo os três modelos prontos e outros personalizados.

- **Jogo/**  
  Contém os módulos principais de funcionamento do jogo, incluindo os loops das partidas locais e online.

- **Visual/**  
  Agrupa diversas funções de suporte, geralmente ligadas a elementos visuais ou sonoros. Apesar do nome, algumas dessas funções afetam também o comportamento lógico do jogo.

- **Dados/**  
  Funciona como um banco de informações do jogo. Contém a maioria dos dicionários fixos que definem os pokémons, itens e outras estruturas essenciais.

- **Z/**  
  Pasta auxiliar usada durante o desenvolvimento. Contém arquivos que **podem ser removidos**, mas foram úteis como apoio em certos momentos.

- **ConfigFixa.py**  
  Arquivo de configuração básica do jogo, onde podem ser definidas opções fixas como volume, FPS e outras preferências.

- **ControleAPI.py**  
  Script que gerencia o funcionamento da API do modo online. Não faz parte de um módulo maior, mas é importante para testes com o servidor.


## 🛠 Tecnologias Usadas

- Python 3.11 (variou)
- [Pygame](https://www.pygame.org/)
- Bibliotecas adicionais: `time`, `threading`, `json`, `re`, `os`, `copy`, entre outras.
- API feita com Flask e rodada pelo Render em um servidor da Virginia (EUA)
- GPT foi utilizado na maioria das funções Visuais, alem dele ter me ensinado o pygame, flask e as bibliotecas extras
- GPT foi utiizado em processos repetitivos e na passagem da planilha do google para os dicionarios pokemon
- Também foi criado um GPT para analisar dados do jogo e ajudar no balanceamento
- Gemini, Uma gema do gemini foi criada para ajudar na criaçao de ataques automatica atraves do leitor de ataques em Abas.py


---

## 🚀 Como Rodar o Jogo

> ⚠️ Um vídeo explicativo será publicado em breve para facilitar o entendimento do jogo.  
> Algumas correções já podem ter sido feitas em versões mais recentes.

1. Instale o Python 3: https://www.python.org  

2. Instale o Pygame com o comando:  
   `pip install pygame`

3. Instale as demais bibliotecas utilizadas (como Flask, se necessário):  
   `pip install flask`

4. Rode o arquivo `game.py`, que está dentro da pasta `Jogo`:  
   `python Jogo/game.py`