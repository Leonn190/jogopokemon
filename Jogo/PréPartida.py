import pygame
import os
import importlib

# Importa utilitários visuais e ações customizadas
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Config import aplicar_claridade
from Visual.Sonoridade import tocar
from Visual.Imagens import Carregar_Imagens_Pré_Partida

# Importa constantes de fonte, cores e texturas
from Visual.GeradoresVisuais import (
    Fonte15, Fonte23, Fonte30, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO, AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO, VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA, TexturasDic
)

pygame.mixer.init()  # Inicializa sistema de áudio

# Variáveis globais de interface e controle de decks
ImagensPokemonInicial = {}
IconesDeckIMG = {}
ListaDecks = []

DeckSelecionadoP1 = None
DeckSelecionadoP2 = None

# Variáveis para textos e estado de seleção nos campos de nome
texto1, selecionado1 = "", False
texto2, selecionado2 = "", False

# Pokémons selecionados pelos jogadores
Poke1_p1 = Poke2_p1 = Poke3_p1 = None
Poke1_p2 = Poke2_p2 = Poke3_p2 = None

# Carrega todos os decks válidos a partir de arquivos .py na pasta informada
def carregar_decks(pasta, ListaDecks):
    ListaDecks.clear()
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith(".py"):
            caminho = os.path.join(pasta, nome_arquivo)
            nome_modulo = nome_arquivo[:-3]
            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)

            for atributo in dir(modulo):
                valor = getattr(modulo, atributo)
                if isinstance(valor, dict):
                    ListaDecks.append(valor)
                    break
    return ListaDecks

# Valida se o deck respeita as regras de raridade e composição
def VerificaDeck(Deck):
    if None in Deck["pokemons"] or None in Deck["itens"] or Deck["treinador"] is None:
        return 1  # Deck incompleto

    # Contagem de raridades entre pokémons
    contagem_raridades = {r: 0 for r in ["Comum", "Incomum", "Raro", "Epico", "Mitico", "Lendario"]}
    for pokemon in Deck["pokemons"]:
        raridade = pokemon.get("raridade", "")
        if raridade in contagem_raridades:
            contagem_raridades[raridade] += 1

    if contagem_raridades["Lendario"] > 2 or contagem_raridades["Mitico"] > 2:
        return 0

    # Os três primeiros pokémons devem ser de baixa raridade
    for pokemon in Deck["pokemons"][:3]:
        if pokemon["raridade"] not in ["Comum", "Incomum"]:
            return 0

    # Verifica duplicatas
    nomes = [poke["nome"] for poke in Deck["pokemons"]]
    if len(nomes) != len(set(nomes)):
        return 0

    # Validação dos itens
    contagem_raridades = {r: 0 for r in contagem_raridades}
    for item in Deck["itens"]:
        raridade = item.get("raridade", "")
        if raridade in contagem_raridades:
            contagem_raridades[raridade] += 1

    if contagem_raridades["Lendario"] > 3 or contagem_raridades["Mitico"] > 3:
        return 0

    return 2  # Deck válido

# Seleciona o deck de um jogador
def selecionaDeck(Deck, p):
    global DeckSelecionadoP1, DeckSelecionadoP2
    if p == 1:
        DeckSelecionadoP1 = Deck
    else:
        DeckSelecionadoP2 = Deck
    A.EnviaDeck(Deck, p)

# Remove a seleção de deck
def desselecionaDeck(p):
    global DeckSelecionadoP1, DeckSelecionadoP2
    if p == 1:
        DeckSelecionadoP1 = None
    else:
        DeckSelecionadoP2 = None

# Estados dos botões e seleções
estado1 = {"selecionado_esquerdo": None}
estado2 = {"selecionado_esquerdo": None}
estadoDecksP1 = {"selecionado_direito": None}
estadoDecksP2 = {"selecionado_direito": None}
B2 = {"estado": False}
B3 = {"estado": False}
B8 = {"estado": False}

# Tela de pré-partida usada no modo online (apenas Player 1 interage)
def TelaPréPartida_Solo(tela, eventos, estados):
    global texto1, selecionado1

    # Texto de instrução para o nome do jogador
    GV.Texto(tela, "Escreva seu Nome:", (635, 430), Fonte40, PRETO)

    # Botão de sair do jogo
    GV.Botao(tela, "Sair do jogo", (800, 400, 320, 80), CINZA, PRETO, AZUL,
             lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

    # Botão de voltar à tela anterior
    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), TexturasDic["FundoCinza"], PRETO, AZUL,
             lambda: A.Voltar(estados), Fonte40, B8, 3, None, True, eventos)

    # Parâmetros de layout para exibição dos pokémons iniciais
    largura_botao = 255
    altura_botao = 255
    espaçamento = 85
    altura_inicial = 110
    largura_tela = 1920
    largura_ocupada = (largura_botao * 3) + (espaçamento * 2)

    # Renderiza os 3 primeiros pokémons do deck selecionado pelo Player 1
    for i in range(3):
        pos_x = (i * (largura_botao + espaçamento)) + (largura_tela - largura_ocupada) // 2
        pos_y = altura_inicial

        if DeckSelecionadoP1 is not None:
            pokemon = DeckSelecionadoP1["pokemons"][i]
            # Botão de seleção do pokémon inicial
            GV.Botao_Selecao(
                tela, (pos_x, pos_y, largura_botao, altura_botao),
                "", Fonte30,
                cor_fundo=VERDE_CLARO, cor_borda_normal=PRETO,
                cor_borda_esquerda=AMARELO,
                cor_borda_direita=None,
                cor_passagem=AMARELO,
                id_botao=pokemon["nome"] + "P1",
                estado_global=estado1, eventos=eventos,
                funcao_esquerdo=lambda poke=pokemon: A.Pokemon_inicial(poke, DeckSelecionadoP1, 1),
                funcao_direito=None,
                desfazer_esquerdo=lambda poke=pokemon: A.Remover_inicial(3),
                desfazer_direito=None,
                tecla_esquerda=[pygame.K_1, pygame.K_2, pygame.K_3][i],
                tecla_direita=None,
                som="Seleciona"
            )
            # Mostra imagem do pokémon centralizada no botão
            imagem = ImagensPokemonInicial[pokemon["nome"]]
            imagem_rect = imagem.get_rect(center=(pos_x + largura_botao // 2, pos_y + altura_botao // 2))
            tela.blit(imagem, imagem_rect)
        else:
            # Slot vazio
            pygame.draw.rect(tela, CINZA, (pos_x, pos_y, largura_botao, altura_botao))
            pygame.draw.rect(tela, PRETO, (pos_x, pos_y, largura_botao, altura_botao), 5)

    # Parâmetros para exibição dos decks
    largura_botao = 150
    altura_botao = 150
    espaçamento = 75
    altura_inicial = 500
    espaçamento_linhas = 20

    # Função interna que desenha os decks disponíveis para o Player 1
    def desenhar_decks_central(lista_decks, estado, player):
        largura_ocupada = (largura_botao * 5) + (espaçamento * 4)

        # Filtra apenas decks válidos
        DecksPermitidos = [deck for deck in lista_decks if VerificaDeck(deck) == 2]

        for i, deck in enumerate(DecksPermitidos):
            if len(lista_decks) == 16 and i == 15:
                linha = 3
                coluna = 2
            else:
                linha = i // 5
                coluna = i % 5

            pos_x = (coluna * (largura_botao + espaçamento)) + (1920 - largura_ocupada) // 2
            pos_y = altura_inicial + (linha * (altura_botao + espaçamento_linhas))

            # Botão de seleção do deck
            GV.Botao_Selecao(
                tela,
                (pos_x, pos_y, largura_botao, altura_botao),
                "",
                Fonte30,
                cor_fundo=AZUL_CLARO,
                cor_borda_normal=PRETO,
                cor_borda_esquerda=VERDE,
                cor_borda_direita=None,
                cor_passagem=AMARELO,
                id_botao=deck,
                estado_global=estado,
                eventos=eventos,
                funcao_esquerdo=lambda deck=deck: selecionaDeck(deck, player),
                funcao_direito=None,
                desfazer_esquerdo=lambda: desselecionaDeck(player),
                desfazer_direito=None,
                tecla_esquerda=pygame.K_1,
                tecla_direita=None
            )

            # Mostra o nome do deck
            texto_surface = Fonte23.render(deck["nome"], True, PRETO)
            texto_rect = texto_surface.get_rect(center=(pos_x + largura_botao // 2, pos_y + texto_surface.get_height() // 2 + 5))
            tela.blit(texto_surface, texto_rect)

            # Mostra ícone do deck, se existir
            if deck["icone"] in IconesDeckIMG:
                icone_original = IconesDeckIMG[deck["icone"]]
                icone_rect = icone_original.get_rect(center=(pos_x + largura_botao // 2, pos_y + altura_botao // 2 + 10))
                tela.blit(icone_original, icone_rect)

    # Desenha os decks permitidos para Player 1
    desenhar_decks_central(ListaDecks, estadoDecksP1, 1)

    # Caixa de texto para digitar o nome do jogador
    texto1, selecionado1 = GV.Barra_De_Texto(
        tela, (970, 425, 300, 40), Fonte30,
        CINZA, PRETO, PRETO, eventos, texto1,
        A.Nome_p1, AZUL, selecionado1)

    # Botão de entrar na fila (habilitado apenas se houver um deck selecionado)
    if DeckSelecionadoP1 is None:
        GV.Botao(tela, "Entrar Na Fila", (770, 960, 380, 110), CINZA, PRETO, DOURADO,
                 lambda: tocar("Bloq"), Fonte70, B3, 4, None, True, eventos)
    else:
        GV.Botao(tela, "Entrar Na Fila", (770, 960, 380, 110), TexturasDic["FundoAmarelo"], PRETO, DOURADO,
                 lambda: A.Entrar_Fila(estados), Fonte70, B3, 4, None, True, eventos, "clique")

# Tela de preparação da partida local entre dois jogadores (modo 1v1)
def TelaPréPartida(tela, eventos, estados):
    global texto1, texto2, selecionado1, selecionado2

    # Títulos e instruções iniciais
    GV.Texto(tela, "Jogador 1", (360, 50), Fonte70, PRETO)
    GV.Texto(tela, "Jogador 2", (1320, 50), Fonte70, PRETO)
    GV.Texto(tela, "Escreva seu Nome:", (190, 455), Fonte40, PRETO)
    GV.Texto(tela, "Escreva seu Nome:", (1170, 455), Fonte40, PRETO)
    GV.Reta_Central(tela, 1920, 1080, PRETO, 4)  # Linha divisória no meio da tela

    # Botões de navegação
    GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
             lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)
    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), TexturasDic["FundoCinza"], PRETO, AZUL,
             lambda: A.Voltar(estados), Fonte40, B8, 3, None, True, eventos)

    # --- Exibição dos 3 pokémons iniciais de cada jogador ---
    largura_botao = 240
    altura_botao = 240
    espaçamento = 30
    altura_inicial = 150

    # ----- Jogador 1 -----
    largura_tela_p1 = 960  # metade esquerda da tela
    largura_ocupada_p1 = (largura_botao * 3) + (espaçamento * 2)

    for i in range(3):
        pos_x = (i * (largura_botao + espaçamento)) + (largura_tela_p1 - largura_ocupada_p1) // 2
        pos_y = altura_inicial

        if DeckSelecionadoP1 is not None:
            pokemon = DeckSelecionadoP1["pokemons"][i]
            # Botão de seleção de pokémon inicial
            GV.Botao_Selecao(
                tela, (pos_x, pos_y, largura_botao, altura_botao),
                "", Fonte30,
                cor_fundo=VERDE_CLARO, cor_borda_normal=PRETO,
                cor_borda_esquerda=AMARELO,
                cor_passagem=AMARELO,
                id_botao=pokemon["nome"] + "P1",
                estado_global=estado1, eventos=eventos,
                funcao_esquerdo=lambda poke=pokemon: A.Pokemon_inicial(poke, DeckSelecionadoP1, 1),
                desfazer_esquerdo=lambda poke=pokemon: A.Remover_inicial(3),
                tecla_esquerda=[pygame.K_1, pygame.K_2, pygame.K_3][i],
                som="Seleciona"
            )
            # Imagem do pokémon no centro do botão
            imagem = ImagensPokemonInicial[pokemon["nome"]]
            imagem_rect = imagem.get_rect(center=(pos_x + largura_botao // 2, pos_y + altura_botao // 2))
            tela.blit(imagem, imagem_rect)
        else:
            # Slot vazio
            pygame.draw.rect(tela, CINZA, (pos_x, pos_y, largura_botao, altura_botao))
            pygame.draw.rect(tela, PRETO, (pos_x, pos_y, largura_botao, altura_botao), 5)

    # ----- Jogador 2 -----
    largura_tela_p2 = 960  # metade direita da tela
    largura_ocupada_p2 = (largura_botao * 3) + (espaçamento * 2)

    for i in range(3):
        pos_x = (i * (largura_botao + espaçamento)) + (largura_tela_p2 - largura_ocupada_p2) // 2 + 960
        pos_y = altura_inicial

        if DeckSelecionadoP2 is not None:
            pokemon = DeckSelecionadoP2["pokemons"][i]
            # Botão de seleção de pokémon inicial
            GV.Botao_Selecao(
                tela, (pos_x, pos_y, largura_botao, altura_botao),
                "", Fonte30,
                cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
                cor_borda_esquerda=AMARELO,
                cor_passagem=AMARELO,
                id_botao=pokemon["nome"] + "P2",
                estado_global=estado2, eventos=eventos,
                funcao_esquerdo=lambda poke=pokemon: A.Pokemon_inicial(poke, DeckSelecionadoP2, 2),
                desfazer_esquerdo=lambda poke=pokemon: A.Remover_inicial(3),
                tecla_esquerda=[pygame.K_7, pygame.K_8, pygame.K_9][i],
                som="Seleciona"
            )
            # Imagem do pokémon no centro do botão
            imagem = ImagensPokemonInicial[pokemon["nome"]]
            imagem_rect = imagem.get_rect(center=(pos_x + largura_botao // 2, pos_y + altura_botao // 2))
            tela.blit(imagem, imagem_rect)
        else:
            pygame.draw.rect(tela, CINZA, (pos_x, pos_y, largura_botao, altura_botao))
            pygame.draw.rect(tela, PRETO, (pos_x, pos_y, largura_botao, altura_botao), 5)

    # --- Exibição dos decks disponíveis para ambos os jogadores ---
    largura_botao = 120
    altura_botao = 120
    espaçamento = 40
    largura_meia_tela = 960
    altura_inicial = 520
    espaçamento_linhas = 20

    # Função interna para desenhar os decks
    def desenhar_decks_lado(lista_decks, offset_x, estado, player):
        largura_ocupada = (largura_botao * 5) + (espaçamento * 4)
        DecksPermitidos = [deck for deck in lista_decks if VerificaDeck(deck) == 2]

        for i, deck in enumerate(DecksPermitidos):
            if len(lista_decks) == 16 and i == 15:
                linha = 3
                coluna = 2
            else:
                linha = i // 5
                coluna = i % 5

            pos_x = (coluna * (largura_botao + espaçamento)) + (largura_meia_tela - largura_ocupada) // 2 + offset_x
            pos_y = altura_inicial + (linha * (altura_botao + espaçamento_linhas))

            # Criação do botão do deck
            GV.Botao_Selecao(
                tela,
                (pos_x, pos_y, largura_botao, altura_botao),
                "", Fonte30,
                cor_fundo=AZUL_CLARO,
                cor_borda_normal=PRETO,
                cor_borda_esquerda=VERDE,
                cor_passagem=AMARELO,
                id_botao=deck,
                estado_global=estado,
                eventos=eventos,
                funcao_esquerdo=lambda deck=deck: selecionaDeck(deck, player),
                desfazer_esquerdo=lambda: desselecionaDeck(player),
                tecla_esquerda=pygame.K_1
            )

            # Nome do deck
            texto_surface = Fonte23.render(deck["nome"], True, PRETO)
            texto_rect = texto_surface.get_rect(center=(pos_x + largura_botao // 2, pos_y + texto_surface.get_height() // 2 + 5))
            tela.blit(texto_surface, texto_rect)

            # Ícone do deck
            if deck["icone"] in IconesDeckIMG:
                icone_original = IconesDeckIMG[deck["icone"]]
                icone_rect = icone_original.get_rect(center=(pos_x + largura_botao // 2, pos_y + altura_botao // 2 + 10))
                tela.blit(icone_original, icone_rect)

    # Decks do jogador 1 (lado esquerdo)
    desenhar_decks_lado(ListaDecks, 0, estadoDecksP1, 1)
    # Decks do jogador 2 (lado direito)
    desenhar_decks_lado(ListaDecks, largura_meia_tela, estadoDecksP2, 2)

    # Caixas de texto para nomes dos jogadores
    texto1, selecionado1 = GV.Barra_De_Texto(tela, (500, 450, 300, 40), Fonte30,
                                             CINZA, PRETO, PRETO, eventos, texto1,
                                             A.Nome_p1, AZUL, selecionado1)
    texto2, selecionado2 = GV.Barra_De_Texto(tela, (1470, 450, 300, 40), Fonte30,
                                             CINZA, PRETO, PRETO, eventos, texto2,
                                             A.Nome_p2, AZUL, selecionado2)

    # Botão para iniciar partida, só aparece se ambos os decks forem válidos
    if DeckSelecionadoP1 is None or DeckSelecionadoP2 is None:
        GV.Botao(tela, "Iniciar Partida", (770, 960, 380, 110), CINZA, PRETO, DOURADO,
                 lambda: tocar("Bloq"), Fonte70, B3, 4, None, True, eventos)
    else:
        GV.Botao(tela, "Iniciar Partida", (770, 960, 380, 110), TexturasDic["FundoAmarelo"], PRETO, DOURADO,
                 lambda: A.Iniciar_partida(estados), Fonte70, B3, 4, None, True, eventos, "clique")
        
# Tela de pré-partida: onde os jogadores escolhem seus nomes, decks e pokémons iniciais.
def PréPartida(tela, estados, relogio, Config):
    # --- Variáveis globais usadas entre diferentes telas do jogo ---
    global ListaDecks, ImagensPokemonInicial, IconesDeckIMG
    global estado1, estado2, estadoDecksP1, estadoDecksP2
    global texto1, texto2, selecionado1, selecionado2
    global DeckSelecionadoP1, DeckSelecionadoP2
    global Poke1_p1, Poke2_p1, Poke3_p1, Poke1_p2, Poke2_p2, Poke3_p2

    # Estados que controlam a seleção visual dos botões (pokémons iniciais)
    estado1 = {"selecionado_esquerdo": None}
    estado2 = {"selecionado_esquerdo": None}

    # Estados que controlam a seleção de decks
    estadoDecksP1 = {"selecionado_direito": None}
    estadoDecksP2 = {"selecionado_direito": None}

    # Variáveis que armazenam o deck escolhido por cada jogador
    DeckSelecionadoP1 = None
    DeckSelecionadoP2 = None

    # Nome digitado e foco das caixas de texto dos dois jogadores
    texto1 = ""
    selecionado1 = False
    texto2 = ""
    selecionado2 = False

    # Pokémons iniciais escolhidos pelos jogadores
    Poke1_p1 = None
    Poke2_p1 = None
    Poke3_p1 = None
    Poke1_p2 = None
    Poke2_p2 = None
    Poke3_p2 = None

    # --- Música de fundo da tela de pré-partida ---
    pygame.mixer.music.load('Audio/Musicas/PréPartida.ogg')
    pygame.mixer.music.set_volume(Config["Volume"] * 1.2)
    pygame.mixer.music.play(-1)  # Reproduz em loop

    # --- Carregamento do fundo visual da tela ---
    Fundo_pré = GV.Carregar_Imagem("imagens/fundos/Fundo1.jpg", (1920, 1080))

    # --- Carregamento dos decks disponíveis na pasta "Decks" ---
    ListaDecks = carregar_decks("Decks", ListaDecks)

    # --- Carregamento de imagens dos pokémons iniciais e ícones dos decks ---
    ImagensPokemonInicial, IconesDeckIMG = Carregar_Imagens_Pré_Partida(ImagensPokemonInicial, IconesDeckIMG)

    # --- Loop principal da tela de pré-partida ---
    while estados["Rodando_PréPartida"]:
        # Desenha o fundo
        tela.blit(Fundo_pré, (0, 0))

        # Captura eventos do pygame (cliques, teclas, etc)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_PréPartida"] = False
                estados["Rodando_Jogo"] = False  # Fecha o jogo inteiro

        # Exibe a interface correta conforme o modo de jogo selecionado
        if Config["Modo"] == "Modo Padrão":
            TelaPréPartida(tela, eventos, estados)         # Modo 1v1 local
        elif Config["Modo"] == "Modo Online":
            TelaPréPartida_Solo(tela, eventos, estados)    # Modo online

        # Aplica um filtro de claridade sobre a tela (efeito visual configurável)
        aplicar_claridade(tela, Config["Claridade"])

        # Atualiza o conteúdo da tela
        pygame.display.update()

        # Controla a taxa de atualização do jogo (FPS)
        relogio.tick(Config["FPS"])
