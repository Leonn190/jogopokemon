import pygame
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.Imagens import Carregar_Imagens_Pré_Partida
from Visual.GeradoresVisuais import (
    Fonte15, Fonte23, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

pygame.mixer.init()

clique = pygame.mixer.Sound("Audio/Sons/Som1.wav")
Compra = pygame.mixer.Sound("Audio/Sons/Compra.wav")
Escolha = pygame.mixer.Sound("Audio/Sons/EscolhaPoke.wav")

ImagensPokemonInicial = {}
IconesDeckIMG = {}

ListaDecks = []
DeckSelecionadoP1 = None
DeckSelecionadoP2 = None

Poke1_p1 = None
Poke2_p1 = None
Poke3_p1 = None
Poke1_p2 = None
Poke2_p2 = None
Poke3_p2 = None

def VerificaDeck(Deck):
    contagem_raridades = {
    "Comum": 0,
    "Incomum": 0,
    "Raro": 0,
    "Epico": 0,
    "Mitico": 0,
    "Lendario": 0}
    for pokemon in Deck["pokemons"]:
        raridade = pokemon.get("raridade", "")
        if raridade in contagem_raridades:
            contagem_raridades[raridade] += 1
    
    if contagem_raridades["Lendario"] > 2:
        return False
    if contagem_raridades["Mitico"] > 2:
        return False
    
    for pokemon in Deck["pokemons"][:3]:
        if pokemon["raridade"] not in ["Comum","Incomum"]:
            return False
    
    if len(Deck["pokemons"]) != len(set(Deck["pokemons"])):
        return False
    
    return True

def selecionaDeck(Deck,p):
    global DeckSelecionadoP1,DeckSelecionadoP2
    if p == 1:
        DeckSelecionadoP1 = Deck
    else:
        DeckSelecionadoP2 = Deck

def desselecionaDeck(p):
    global DeckSelecionadoP1,DeckSelecionadoP2
    if p == 1:
        DeckSelecionadoP1 = None
    else:
        DeckSelecionadoP2 = None

estado1 = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

estado2 = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

estadoDecksP1 = {"selecionado_direito": None}
estadoDecksP2 = {"selecionado_direito": None}

B2 = {"estado": False}
B3 = {"estado": False}
B8 = {"estado": False}

def TelaPréPartida(tela,eventos,estados):

    GV.Texto(tela, "Jogador 1", (360, 50), Fonte70, PRETO)
    GV.Texto(tela, "Jogador 2", (1320, 50), Fonte70, PRETO)
    GV.Texto(tela, "Escreva seu Nome:", (190, 455), Fonte40, PRETO)
    GV.Texto(tela, "Escreva seu Nome:", (1170, 455), Fonte40, PRETO)
    GV.Reta_Central(tela, 1920, 1080, PRETO, 4)

    GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)  
    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), CINZA, PRETO, AZUL,
                 lambda: A.Voltar(estados), Fonte40, B8, 3, None, True, eventos)

    largura_botao = 240
    altura_botao = 240
    espaçamento = 30
    altura_inicial = 150

    # --- Player 1 ---
    largura_tela_p1 = 960
    largura_ocupada_p1 = (largura_botao * 3) + (espaçamento * 2)

    for i in range(3):
        pos_x = (i * (largura_botao + espaçamento)) + (largura_tela_p1 - largura_ocupada_p1) // 2
        pos_y = altura_inicial

        if DeckSelecionadoP1 is not None:
            pokemon = DeckSelecionadoP1["pokemons"][i]
            GV.Botao_Selecao(
                tela, (pos_x, pos_y, largura_botao, altura_botao),
                "", Fonte30,
                cor_fundo=VERDE_CLARO, cor_borda_normal=PRETO,
                cor_borda_esquerda=AMARELO, cor_borda_direita=None,
                cor_passagem=AMARELO, id_botao=pokemon["nome"] + "P1",   
                estado_global=estado1, eventos=eventos,
                funcao_esquerdo=lambda poke=pokemon: A.Pokemon_inicial(poke + "P1"), funcao_direito=None,
                desfazer_esquerdo=lambda poke=pokemon: A.Remover_inicial(poke + "P1"), desfazer_direito=None,
                tecla_esquerda=[pygame.K_1, pygame.K_2, pygame.K_3][i],
                tecla_direita=None, som=Escolha
            )
            # Desenha a imagem do Pokémon centralizada no botão
            imagem = ImagensPokemonInicial[pokemon["nome"]]
            imagem_rect = imagem.get_rect(center=(pos_x + largura_botao // 2, pos_y + altura_botao // 2))
            tela.blit(imagem, imagem_rect)
        else:
            pygame.draw.rect(tela, CINZA, (pos_x, pos_y, largura_botao, altura_botao))
            pygame.draw.rect(tela, PRETO, (pos_x, pos_y, largura_botao, altura_botao), 5)

    # --- Player 2 ---
    largura_tela_p2 = 960
    largura_ocupada_p2 = (largura_botao * 3) + (espaçamento * 2)

    for i in range(3):
        pos_x = (i * (largura_botao + espaçamento)) + (largura_tela_p2 - largura_ocupada_p2) // 2 + 960
        pos_y = altura_inicial

        if DeckSelecionadoP2 is not None:
            pokemon = DeckSelecionadoP2["pokemons"][i]
            GV.Botao_Selecao(
                tela, (pos_x, pos_y, largura_botao, altura_botao),
                "", Fonte30,
                cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
                cor_borda_esquerda=AMARELO, cor_borda_direita=None,
                cor_passagem=AMARELO, id_botao=pokemon["nome"] + "P2",   
                estado_global=estado2, eventos=eventos,
                funcao_esquerdo=lambda poke=pokemon: A.Pokemon_inicial(poke + "P2"), funcao_direito=None,
                desfazer_esquerdo=lambda poke=pokemon: A.Remover_inicial(poke + "P2"), desfazer_direito=None,
                tecla_esquerda=[pygame.K_7, pygame.K_8, pygame.K_9][i],
                tecla_direita=None, som=Escolha
            )
            # Desenha a imagem do Pokémon centralizada no botão
            imagem = ImagensPokemonInicial[pokemon["nome"]]
            imagem_rect = imagem.get_rect(center=(pos_x + largura_botao // 2, pos_y + altura_botao // 2))
            tela.blit(imagem, imagem_rect)
        else:
            pygame.draw.rect(tela, CINZA, (pos_x, pos_y, largura_botao, altura_botao))
            pygame.draw.rect(tela, PRETO, (pos_x, pos_y, largura_botao, altura_botao), 5)

    largura_botao = 120 
    altura_botao = 120 
    espaçamento = 40
    largura_meia_tela = 960
    altura_inicial = 520
    espaçamento_linhas = 20

    def desenhar_decks_lado(lista_decks, offset_x, estado, player):
        largura_ocupada = (largura_botao * 5) + (espaçamento * 4)
        for i, deck in enumerate(lista_decks):
            
            # Caso especial: deck 16 (índice 15), queremos centralizar na linha 4, posição 3 (coluna 2)
            if len(lista_decks) == 16 and i == 15:
                linha = 3
                coluna = 2  # terceira coluna (0, 1, **2**, 3, 4)
            else:
                linha = i // 5
                coluna = i % 5

            pos_x = (coluna * (largura_botao + espaçamento)) + (largura_meia_tela - largura_ocupada) // 2 + offset_x
            pos_y = altura_inicial + (linha * (altura_botao + espaçamento_linhas))

            # Criação do botão
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
                funcao_esquerdo=lambda deck=deck: selecionaDeck(deck,player), 
                funcao_direito=None,
                desfazer_esquerdo=lambda: desselecionaDeck(player), 
                desfazer_direito=None,
                tecla_esquerda=pygame.K_1, 
                tecla_direita=None
            )

            # --- Texto no topo do botão ---
            texto_surface = Fonte23.render(deck["nome"], True, PRETO)
            texto_rect = texto_surface.get_rect(center=(pos_x + largura_botao // 2, pos_y + texto_surface.get_height() // 2 + 5))
            tela.blit(texto_surface, texto_rect)

            # --- Imagem do ícone no centro, sem redimensionar ---
            if deck["icone"] in IconesDeckIMG:
                icone_original = IconesDeckIMG[deck["icone"]]
                icone_rect = icone_original.get_rect(center=(pos_x + largura_botao // 2, pos_y + altura_botao // 2 + 10))
                tela.blit(icone_original, icone_rect)

    # --- Desenha decks do lado esquerdo (Player 1)
    desenhar_decks_lado(ListaDecks, 0, estadoDecksP1, 1)

    # --- Desenha decks do lado direito (Player 2)
    desenhar_decks_lado(ListaDecks, largura_meia_tela, estadoDecksP2, 2)


    GV.Botao(tela, "Iniciar Partida", (770, 960, 380, 110), AMARELO_CLARO, PRETO, DOURADO,
                 lambda: A.Iniciar_partida(estados), Fonte70, B3, 4, None, True, eventos, clique)

def PréPartida(tela,estados,relogio):
    global ListaDecks, ImagensPokemonInicial, IconesDeckIMG

    # itens para deixar as barras de texto funcionais
    texto1 = ""
    selecionado1 = False

    texto2 = ""
    selecionado2 = False

    pygame.mixer.music.load('Audio/Musicas/PréPartida.ogg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    Fundo_pré = GV.Carregar_Imagem("imagens/fundos/Fundo1.jpg", (1920,1080))

    ListaDecks = A.carregar_decks("Decks",ListaDecks)

    ImagensPokemonInicial,IconesDeckIMG = Carregar_Imagens_Pré_Partida(ImagensPokemonInicial,IconesDeckIMG)

    while estados["Rodando_PréPartida"]:
        tela.blit(Fundo_pré, (0, 0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_PréPartida"] = False
                estados["Rodando_Jogo"] = False

        TelaPréPartida(tela,eventos,estados)


        texto1, selecionado1 = GV.Barra_De_Texto(
    tela, (500, 450, 300, 40), Fonte30, 
    CINZA, PRETO, PRETO, eventos, texto1,
    A.Nome_p1, AZUL,selecionado1)

        texto2, selecionado2 = GV.Barra_De_Texto(
    tela, (1470, 450, 300, 40), Fonte30, 
    CINZA, PRETO, PRETO, eventos, texto2,
    A.Nome_p2, AZUL, selecionado2)

        pygame.display.update()
        relogio.tick(60)

