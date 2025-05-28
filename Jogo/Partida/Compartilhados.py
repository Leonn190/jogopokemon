import pygame
import random
from queue import Queue
from Visual.Imagens import Carregar_Imagens_Partida, Carrega_Gif_pokemon
from Visual.Mensagens import mensagens_passageiras
from Visual.Efeitos import gerar_gif, atualizar_efeitos
from Visual.Sonoridade import tocar
from Abas import Status_Pokemon,Inventario,Atacar, Loja
from Infos import TreinadorInfo
from Config import Configuraçoes, aplicar_claridade
import Mapa as M
import Geradores.GeradorPlayer as GPA
import Geradores.GeradorPokemon as GPO
import Geradores.GeradorOutros as GO
import Geradores.GeradorPartida as GP
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte23, Fonte25, Fonte28, Fonte30, Fonte35, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA,CINZA_ESCURO, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO,VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA,LARANJA_CLARO, ROXO,ROXO_CLARO, ROSA, DOURADO, PRATA, cores_raridade)

Partida = None

peca_em_uso = None
Tela = None

Gifs_ativos = []
PeçasArrastaveis = []

PokemonS = None
PokemonSV = None
PokemonV = None
PokemonVV = None
PokemonA = None
PokemonAV = None
alvo = None
PokebolaSelecionada = None
FrutaSelecionada = None
provocar = False

PokeGifs = {}
TiposEnergiaIMG = {}
ImagensPokemonIcons = {}
ImagensPokemonCentro = {}
IconesDeckIMG= {}
ImagensItens = {}
ImagensFichas = {}
OutrosIMG = []
FundosIMG = []
EfeitosIMG = {}

player = None
inimigo = None

Pausa = False
Config = False
Musica_Estadio_atual = None

def TrocaConfig():
    global Config
    if Config == False:
        tocar("Config")
        Config = True
    else:
        Config = False

def cronometro(tela, espaço, duracao_segundos, fonte, cor_fundo, cor_borda, cor_tempo, ao_terminar, turno_atual):

    x,y,largura,altura = espaço

    # Inicializa atributos na primeira execução
    if not hasattr(cronometro, "inicio") or not hasattr(cronometro, "turno_anterior"):
        cronometro.inicio = pygame.time.get_ticks()
        cronometro.tempo_encerrado = False
        cronometro.turno_anterior = turno_atual

    # Reinicia se o turno mudou
    if turno_atual != cronometro.turno_anterior:
        cronometro.inicio = pygame.time.get_ticks()
        cronometro.tempo_encerrado = False
        cronometro.turno_anterior = turno_atual

    # Pausa: não atualiza o tempo enquanto estiver pausado
    if hasattr(cronometro, "pausado") and cronometro.pausado:
        tempo_decorrido = (cronometro.momento_pausa - cronometro.inicio) // 1000
    else:
        tempo_atual = pygame.time.get_ticks()
        tempo_decorrido = (tempo_atual - cronometro.inicio) // 1000

    Partida.tempo_restante = max(0, duracao_segundos - tempo_decorrido)

    # Visual: fundo, barra preenchida, borda
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
    largura_barra = int((Partida.tempo_restante / duracao_segundos) * largura)
    pygame.draw.rect(tela, cor_tempo, (x, y, largura_barra, altura))  # cor do tempo separada
    pygame.draw.rect(tela, cor_borda, (x, y, largura, altura), 2)

    # Texto do tempo
    texto = fonte.render(str(Partida.tempo_restante), True, (0, 0, 0))
    texto_rect = texto.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto, texto_rect)

    # Chama função se o tempo zerar
    if Partida.tempo_restante <= 0 and not cronometro.tempo_encerrado:
        cronometro.tempo_encerrado = True
        ao_terminar()

def Resetar_Cronometro():
    for atributo in ["inicio", "tempo_encerrado", "turno_anterior", "pausado", "momento_pausa"]:
        if hasattr(cronometro, atributo):
            delattr(cronometro, atributo)

def pausaEdespausaCronometro():
    if not hasattr(cronometro, "pausado"):
        cronometro.pausado = False
        cronometro.tempo_pausado = 0

    if not cronometro.pausado:
        # Pausar: salva o momento da pausa
        cronometro.pausado = True
        cronometro.momento_pausa = pygame.time.get_ticks()
    else:
        # Despausar: ajusta o início somando o tempo pausado
        tempo_em_pausa = pygame.time.get_ticks() - cronometro.momento_pausa
        cronometro.inicio += tempo_em_pausa
        cronometro.pausado = False

def passar_turno(estados):
    global player,inimigo,provocar,Partida

    player.ouro += 2 + (Partida.tempo_restante // 25)
    GV.limpa_terminal()
    M.inverter_tabuleiro(player,inimigo)

    Partida.Mapa.Peças = []

    for pokemon in player.pokemons:
        pokemon.atacou = False
        pokemon.moveu = False
        pokemon.PodeEvoluir = True
        if pokemon.guardado != 0:
            pokemon.guardado -= 1
    
    provocar = False
    VerificaVitória(estados, Partida.Jogador1, Partida.Jogador2)

    player, inimigo = inimigo, player

    player.ContaPassiva += 1
    inimigo.ContaPassiva += 1

    if player.ContaPassiva >= player.AtivaPassiva:
        player.Passiva(player, inimigo, Partida.Mapa, Partida.Baralho, Partida.Turno)
        GV.adicionar_mensagem("Passiva Ativada")
        player.ContaPassiva = 0

    for pokemon in player.pokemons:
        if pokemon.local is not None:
            pokemon.Ganhar_XP(2,player)

    Passar_contadores()

    Partida.Centro = GO.spawn_do_centro(Partida.Centro, Partida.Baralho, Partida.Turno)

    Partida.Turno += 1
    fechar_tudo()
    GV.adicionar_mensagem(f"Novo Turno de {player.nome}!")

S1 = 1920
S2 = 1920
V1 = 1920
V2 = 1920
T1 = 800
T2 = 800
TI1 = 0
TI2 = 0
OP1 = 1080
OP2 = 1080

A1 = -385
A2 = -385
A3 = -385
A4 = -385
A5 = -385
A6 = -385
A7 = 0
A8 = 0

def seleciona(Pokemon):
    global PokemonS, S1, S2, animaS, OP1, OP2, animaOP
    if not isinstance(Pokemon,str):
        if Pokemon.Vida > 0 and Pokemon.efeitosNega["Congelado"] <= 0 and Pokemon not in inimigo.pokemons:
            PokemonS = Pokemon 
            S1 = 1920
            S2 = 1540
            OP1 = 1080
            OP2 = 920
            animaS = pygame.time.get_ticks()
            animaOP = pygame.time.get_ticks()
        else:
            PokemonS = None
            GV.adicionar_mensagem("Esse Pokémon não pode ser selecionado.")
    else:
        PokemonS = None
        GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")

def selecionaAlvo(Pokemon):
    global PokemonA, alvo
    if not isinstance(Pokemon,str):
        if PokemonA is not None:
            desselecionaAlvo()
            if Pokemon is None:
                return
        if Pokemon.efeitosPosi["Furtivo"] > 0:
            GV.adicionar_mensagem("Esse pokemon está em modo furtivo")
            return
        if provocar is True:
            if Pokemon.efeitosPosi["Provocando"] == 0:
                GV.adicionar_mensagem("Algum outro pokemon está provocando")
                return
        PokemonA = Pokemon
        tocar("Alvo")
        alvo = gerar_gif(OutrosIMG[14],((1400 - PokemonA.pos * 190),95),35)

def desselecionaAlvo():
    global PokemonA,alvo, estadoAlvo
    alvo = None
    PokemonA = None
    estadoAlvo = {"selecionado_esquerdo": None}

def desseleciona():
    global S1, S2, animaS, PokemonS
    global OP1, OP2, animaOP
    if PokemonS is not None:
        S1 = 1540
        S2 = 1920
        OP1 = 930
        OP2 = 1080
        animaS = pygame.time.get_ticks()
        animaOP = pygame.time.get_ticks()
        PokemonS = None
    estadoPokemon["selecionado_esquerdo"] = False

def visualiza(Pokemon):
    global V1, V2, animaV, PokemonV
    if not isinstance(Pokemon,str):
        PokemonV = Pokemon
        V1 = 1920
        V2 = 1540
        animaV = pygame.time.get_ticks()
        if TI2 != 0:
            Troca_Terminal_Inimigo()
    else:
        PokemonV = None
        GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")     

def oculta():
    global V1, V2, animaV, PokemonV
    if PokemonV is not None:
        V1 = 1540
        V2 = 1920
        animaV = pygame.time.get_ticks()
        PokemonV = None
    estadoVisualiza["selecionado_direito"] = False

def Abre(ID,player,inimigo):
    global A7, A8, animaAL
    if ID == "Inventario":
        global A1, A2, animaAI
        A1 = -385
        A2 = 1
        animaAI = pygame.time.get_ticks()
        if A8 != 1:
            A7 = -480
            A8 = 1
            animaAL = pygame.time.get_ticks()
    elif ID == "Centro":
        global A5, A6, animaAC
        A5 = -385
        A6 = 1
        animaAC = pygame.time.get_ticks()
        if A8 != 1:
            A7 = -480
            A8 = 1
            animaAL = pygame.time.get_ticks()
    elif ID == "Treinador":
        global A3, A4, animaAT
        A3 = -385
        A4 = 1
        animaAT = pygame.time.get_ticks()
    
def Fecha():
    global A1, A2, animaAI
    global A3, A4, animaAT
    global A5, A6, animaAC
    global A7, A8, animaAL
    global estadoOutros
    if A2 == 1:
        A1 = 1
        A2 = -385
        animaAI = pygame.time.get_ticks()
    elif A6 == 1:
        A5 = 1
        A6 = -385
        animaAC = pygame.time.get_ticks()
    elif A4 == 1:
        A3 = 1
        A4 = -385
        animaAT = pygame.time.get_ticks()

    estadoOutros["selecionado_esquerdo"] = None

def seleciona_pokebola(pokebola):
    global PokebolaSelecionada
    PokebolaSelecionada = pokebola

def desseleciona_pokebola():
    global PokebolaSelecionada,estadoPokebola
    PokebolaSelecionada = None
    estadoPokebola = {"selecionado_esquerdo": None,}

def seleciona_fruta(fruta):
    global FrutaSelecionada
    FrutaSelecionada = fruta

def desseleciona_fruta():
    global FrutaSelecionada,estadoFruta
    FrutaSelecionada = None
    estadoFruta = {"selecionado_esquerdo": None,}

def fechar_tudo():
    global estadoPokemon,estadoOutros,estadoPokebola,estadoItens,estadoFruta,estadoAlvo,estadoVisualiza
    global S1, S2, V1, V2, T1, T2, OP1, OP2, A1, A2, A3, A4, A5, A6, A7, A8, alvo

    estadoPokemon = {"selecionado_esquerdo": None}
    estadoAlvo = {"selecionado_esquerdo": None}
    estadoVisualiza ={"selecionado_direito": None}
    estadoPokebola = {"selecionado_esquerdo": None,}
    estadoItens = {"selecionado_direito": None}
    estadoFruta = {"selecionado_esquerdo": None,}
    estadoOutros = {"selecionado_esquerdo": None,}

    S1 = 1920
    S2 = 1920
    V1 = 1920
    V2 = 1920
    T1 = 800
    T2 = 800
    OP1 = 1080
    OP2 = 1080
    A1 = -382
    A2 = -382
    A3 = -382
    A4 = -382
    A5 = -400
    A6 = -400
    A7 = -480
    A8 = -480
    alvo = None

def PokemonCentro(pokemon,player):
    global estadoOutros

    AIV = 1
    
    if PokebolaSelecionada is not None:
        if not PokebolaSelecionada.get("extra"):
            Partida.Baralho.devolve_item(PokebolaSelecionada)
        player.inventario.remove(PokebolaSelecionada)
        Pokebola_usada = PokebolaSelecionada
        desseleciona_pokebola()
        maestria = random.randint(0,Pokebola_usada["poder"] * 2)
        if FrutaSelecionada is not None:
            if not FrutaSelecionada.get("extra"):
                Partida.Baralho.devolve_item(FrutaSelecionada)
            player.inventario.remove(FrutaSelecionada)
            if FrutaSelecionada["nome"] in ["Fruta Frambo","Fruta Frambo Dourada"]:
                pokemon["dificuldade"] -= FrutaSelecionada["poder"]
                AIV = 1
            elif FrutaSelecionada["nome"] in ["Fruta Caxi","Fruta Caxi Prateada"]:
                AIV = FrutaSelecionada["poder"]
            desseleciona_fruta()
        maestria += player.PoderCaptura
        if maestria >= pokemon["dificuldade"]:
            player.PokemonsCapturados += 1
            if len(player.pokemons) < 6:
                novo_pokemon = GPO.Gerador_final(pokemon["code"],AIV * player.MultiplicaIV,player)
                M.PosicionarGuardar(novo_pokemon,0)
                GV.adicionar_mensagem(f"Parabens! Capturou um {novo_pokemon.nome} usando uma {Pokebola_usada['nome']}")
                VerificaGIF(player,inimigo)
                tocar("Bom")
                indice = Partida.Centro.index(pokemon)
                Partida.Centro[indice] = None
                return
            else:
                tocar("Bloq")
                GV.adicionar_mensagem("Capturou, mas sua lista de pokemon está cheia")
        else:
            tocar("Falhou")
            GV.adicionar_mensagem("Voce falhou em capturar o pokemon, que pena")
        estadoPokebola["selecionado_esquerdo"] =  False
    else:
        tocar("Bloq")
        GV.adicionar_mensagem("Selecione uma pokebola para capturar um pokemon")

def barra_vida(tela, x, y, largura, altura, vida_atual, vida_maxima, cor_fundo, id_pokemon, barreira=0):
    if not hasattr(barra_vida, "vidas_animadas"):
        barra_vida.vidas_animadas = {}
    if not hasattr(barra_vida, "barreiras_animadas"):
        barra_vida.barreiras_animadas = {}

    # Inicializa animações se necessário
    vida_animada = barra_vida.vidas_animadas.get(id_pokemon, vida_atual)
    barreira_animada = barra_vida.barreiras_animadas.get(id_pokemon, barreira)

    velocidade = 1.5
    # Anima vida
    if abs(vida_animada - vida_atual) < velocidade:
        vida_animada = vida_atual
    else:
        if vida_animada < vida_atual:
            vida_animada = min(vida_animada + velocidade, vida_atual)
        else:
            vida_animada = max(vida_animada - velocidade, vida_atual)

    # Anima barreira
    if abs(barreira_animada - barreira) < velocidade:
        barreira_animada = barreira
    else:
        if barreira_animada < barreira:
            barreira_animada = min(barreira_animada + velocidade, barreira)
        else:
            barreira_animada = max(barreira_animada - velocidade, barreira)

    # Proporções corretas baseadas em vida_maxima
    proporcao_vida = max(vida_animada, 0) / vida_maxima
    proporcao_barreira = max(barreira_animada, 0) / vida_maxima

    largura_vida = int(largura * proporcao_vida)
    largura_barreira = int(largura * proporcao_barreira)

    # Garante que a soma não ultrapasse o total da barra
    if largura_vida + largura_barreira > largura:
        excesso = (largura_vida + largura_barreira) - largura
        largura_vida = max(largura_vida - excesso, 0)

    # Cor da vida conforme proporção da vida em relação à vida máxima
    proporcao_vida_real = vida_animada / vida_maxima if vida_maxima > 0 else 0
    if proporcao_vida_real > 0.6:
        cor_vida = (0, 200, 0)
    elif proporcao_vida_real > 0.3:
        cor_vida = (255, 200, 0)
    else:
        cor_vida = (200, 0, 0)

    # Fundo da barra
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    # Vida
    pygame.draw.rect(tela, cor_vida, (x, y, largura_vida, altura))

    # Barreira (por cima da vida, à direita)
    if largura_barreira > 0:
        pygame.draw.rect(tela, (0, 150, 255), (x + largura_vida, y, largura_barreira, altura))

    # Borda
    pygame.draw.rect(tela, (0, 0, 0), (x, y, largura, altura), 2)

    # Morto
    if vida_animada <= 0:
        img = OutrosIMG[8]
        img_rect = img.get_rect()
        img_x = x + (largura - img_rect.width) // 2
        img_y = y - img_rect.height + 12
        tela.blit(img, (img_x, img_y))

    # Salva valores animados
    barra_vida.vidas_animadas[id_pokemon] = vida_animada
    barra_vida.barreiras_animadas[id_pokemon] = barreira_animada

def pausarEdespausar():
    global Pausa
    if Pausa == True:
        pausaEdespausaCronometro()
        Pausa = False
    else:
        Pausa = True
        pausaEdespausaCronometro()

def Muter(config):

    if config["Volume"] == 0:
        config["Volume"] = 0.4
    else:
        config["Volume"] = 0

def tocar_musica_do_estadio():
    global Musica_Estadio_atual

    if Partida.Mapa.Musica != Musica_Estadio_atual:
        Z = Partida.Mapa.Musica 
        # Trocar a música
        pygame.mixer.music.stop()
        
        if Partida.Mapa.Musica == 0:
            pygame.mixer.music.load("Audio/Musicas/Partida.ogg")
        elif Partida.Mapa.Musica == 1:
            pygame.mixer.music.load("Audio/Musicas/Mer.ogg")
        elif Partida.Mapa.Musica == 2:
            pygame.mixer.music.load("Audio/Musicas/Shivre.ogg")
        elif Partida.Mapa.Musica == 3:
            pygame.mixer.music.load("Audio/Musicas/Auroma.ogg")
        elif Partida.Mapa.Musica == 4:
            pygame.mixer.music.load("Audio/Musicas/Kalos.ogg")
        elif Partida.Mapa.Musica == 5:
            pygame.mixer.music.load("Audio/Musicas/Skyloft.ogg")
        elif Partida.Mapa.Musica == 6:
            pygame.mixer.music.load("Audio/Musicas/Molgera.ogg")

        pygame.mixer.music.play(-1)  # -1 = loop infinito
        Musica_Estadio_atual = Z

def Centroo(tela, x_inicial, y_inicial, Centro, player, Fonte50, Fonte28, B6, estadoPokebola, estadoFruta, eventos):
    largura_total = 380
    altura_total = 420

    espacamento = 5
    x_inicial_animado = x_inicial

    # Calculando tamanhos
    tamanho_pokemon = (largura_total - (5 * espacamento)) // 4
    tamanho_botao_pokebola = 50
    tamanho_fruta = 50

    # Retângulo de fundo
    ret = pygame.Rect(x_inicial_animado, y_inicial, largura_total, altura_total)
    pygame.draw.rect(tela, (30, 30, 30), ret)
    pygame.draw.rect(tela, (255, 255, 255), ret, 3)

    # Seção superior com título
    altura_titulo = 30  # altura visual da seção de título
    texto = Fonte28.render("Centro Pokémon", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(x_inicial_animado + largura_total // 2, y_inicial + altura_titulo // 2))
    tela.blit(texto, texto_rect)

    # Linha branca separadora
    pygame.draw.line(tela, (255, 255, 255), (x_inicial_animado, y_inicial + altura_titulo), (x_inicial_animado + largura_total, y_inicial + altura_titulo), 2)

    # Ajuste Y inicial dos botões de pokébolas (começam logo após a linha)
    offset_y_pokebola = y_inicial + altura_titulo + espacamento

    espacamento = 5  # exemplo fixo, pode ajustar
    tamanho_botao_pokebola = (380 - 7 * espacamento) // 6  # vai dar 57

    for i, item in enumerate([i for i in player.inventario if i.get("classe") == "pokebola"][:6]):
        x = x_inicial_animado + espacamento + i * (tamanho_botao_pokebola + espacamento)
        y = offset_y_pokebola

        GV.Botao_Selecao(
            tela, (x, y, tamanho_botao_pokebola, tamanho_botao_pokebola),
            "", Fonte28,
            cor_fundo=AZUL_SUPER_CLARO, cor_borda_normal=PRETO,
            cor_borda_esquerda=VERMELHO,
            cor_borda_direita=None,
            cor_passagem=AMARELO, id_botao=i,
            estado_global=estadoPokebola, eventos=eventos,
            funcao_esquerdo=lambda item=item: seleciona_pokebola(item),
            funcao_direito=None,
            desfazer_esquerdo=lambda: desseleciona_pokebola(),
            desfazer_direito=None,
            tecla_esquerda=None, tecla_direita=None, grossura=3
        )
        tela.blit(ImagensItens[item["nome"]], (x + 2, y + 2))

    # Grade Pokémon (centro, 4x2)
    offset_y_pokemon = offset_y_pokebola + tamanho_botao_pokebola + espacamento
    for i, pokemon in enumerate(Centro):
        coluna = i % 4
        linha = i // 4
        x = x_inicial_animado + espacamento + coluna * (tamanho_pokemon + espacamento)
        y = offset_y_pokemon + linha * (tamanho_pokemon + espacamento) + 30

        if pokemon and pokemon["nome"] in ImagensPokemonCentro:
            # Define a cor pela raridade do Pokémon
            cor_fundo = cores_raridade.get(pokemon["raridade"])
            
            # Desenha botão com cor de fundo conforme raridade
            GV.Botao(
                tela, "", (x, y, tamanho_pokemon, tamanho_pokemon), cor_fundo, PRETO, AZUL,
                lambda p=pokemon: PokemonCentro(p, player),
                Fonte50, B6, 2, None, True, eventos
            )
            tela.blit(ImagensPokemonCentro[pokemon["nome"]], (x, y))
        else:
            # Desenha apenas a lacuna vazia
            vazio = pygame.Surface((tamanho_pokemon, tamanho_pokemon))
            vazio.fill((50, 50, 50))
            tela.blit(vazio, (x, y))

    espacamento = 5  # mesmo usado nas pokébolas
    tamanho_fruta = (380 - 7 * espacamento) // 6  # será 57

    offset_y_fruta = y_inicial + altura_total - tamanho_fruta - espacamento
    for i, item in enumerate([i for i in player.inventario if i.get("classe") == "Fruta"][:6]):
        x = x_inicial_animado + espacamento + i * (tamanho_fruta + espacamento)
        y = offset_y_fruta

        GV.Botao_Selecao(
            tela, (x, y, tamanho_fruta, tamanho_fruta),
            "", Fonte28,
            cor_fundo=(150, 100, 100), cor_borda_normal=PRETO,
            cor_borda_esquerda=VERDE,
            cor_borda_direita=None,
            cor_passagem=AMARELO, id_botao=i,
            estado_global=estadoFruta, eventos=eventos,
            funcao_esquerdo=lambda item=item: seleciona_fruta(item),
            funcao_direito=None,
            desfazer_esquerdo=lambda: desseleciona_fruta(),
            desfazer_direito=None,
            tecla_esquerda=None, tecla_direita=None, grossura=3
        )

        if item["nome"] in ImagensItens:
            tela.blit(ImagensItens[item["nome"]], (x + 2, y + 2))

def Troca_Terminal():
    global animaT, T1, T2
    if T2 == 800:
        T1 = 800
        T2 = 1030
        animaT = pygame.time.get_ticks()
    else:
        GV.limpa_terminal()
        T1 = 1030
        T2 = 800
        animaT = pygame.time.get_ticks()

def Troca_Terminal_Inimigo():
    global animaTI, TI1, TI2
    if TI2 == 0:
        TI1 = 0
        TI2 = 423
        animaTI = pygame.time.get_ticks()
        if PokemonV is not None:
            oculta()
    else:
        TI1 = 423
        TI2 = 0
        animaTI = pygame.time.get_ticks()

def Passar_contadores():
    for pokemon in player.pokemons:
        if pokemon.Vida > 0:
            dano_dos_efeitos = 0
            if pokemon.efeitosNega["Envenenado"] > 0:
                dano_dos_efeitos += 10
            if pokemon.efeitosNega["Tóxico"] > 0:
                dano_dos_efeitos += 20
                pokemon.vel -= 1
            if pokemon.efeitosNega["Queimado"] > 0:
                dano_dos_efeitos += 15
            if pokemon.efeitosPosi["Regeneração"]:
                pokemon.curar(15,player,Tela)
            if dano_dos_efeitos > 0:
                pokemon.atacado(dano_dos_efeitos,player,inimigo,Tela,Partida.Mapa)

        for efeito, contador in pokemon.efeitosNega.items():
            if contador > 0:
                pokemon.efeitosNega[efeito] -= 1
        for efeito, contador in pokemon.efeitosPosi.items():
            if contador > 0:
                pokemon.efeitosPosi[efeito] -= 1    

def VerificaGIF(player,inimigo=None):
    global Gifs_ativos

        # Ao capturar um novo Pokémon (exemplo)
    for i in range(len(player.pokemons)):
        nome = player.pokemons[i].nome

        # Verifica se o Pokémon ainda não foi adicionado
        if nome not in [gif["nome"] for gif in Gifs_ativos]:
            Gifs_ativos.append({
                "nome": nome,
                "frames": Carrega_Gif_pokemon(nome),
                "frame_atual": 0,
                "tempo_anterior": pygame.time.get_ticks(),
                "intervalo": 25  # Pode ser ajustado para cada Pokémon se necessário
            })
    if inimigo is not None:
        for i in range(len(inimigo.pokemons)):
            nome = inimigo.pokemons[i].nome

            # Verifica se o Pokémon ainda não foi adicionado
            if nome not in [gif["nome"] for gif in Gifs_ativos]:
                Gifs_ativos.append({
                    "nome": nome,
                    "frames": Carrega_Gif_pokemon(nome),
                    "frame_atual": 0,
                    "tempo_anterior": pygame.time.get_ticks(),
                    "intervalo": 25  # Pode ser ajustado para cada Pokémon se necessário
                })

estadoPokemon = {"selecionado_esquerdo": None}
estadoAlvo = {"selecionado_esquerdo": None}
estadoVisualiza ={"selecionado_direito": None}
estadoPokebola = {"selecionado_esquerdo": None,}
estadoItens = {"selecionado_direito": None}
estadoEnergias = {"selecionado_esquerdo": None}
estadoFruta = {"selecionado_esquerdo": None,}
estadoOutros = {"selecionado_esquerdo": None,}
EstadoOutrosAtual = None

animaS = 0
animaAI = 0
animaAT = 0
animaAC = 0
animaAL = 0
animaV = 0
animaT = 0
animaTI = 0
animaOP = 0


B1 = {"estado": False}
B6 = {"estado": False}
B7 = {"estado": False}
B21 = {"estado": False}
B22 = {"estado": False}
B23 = {"estado": False}
B24 = {"estado": False}

#botoes de clique unico = B6

def IniciaLocal(tela, config):
    global ImagensPokemonCentro,ImagensPokemonIcons,ImagensFichas,PokeGifs,ImagensItens,OutrosIMG,FundosIMG,TiposEnergiaIMG,EfeitosIMG
    global player, inimigo, Tela, Musica_Estadio_atual, Partida, Pausa

    Carregar = GV.Carregar_Imagem("imagens/fundos/carregando.jpg",(1920,1080))
    tela.blit(Carregar,(0,0))
    texto = Fonte70.render("Carregando ...", True, PRETO)
    tela.blit(texto, (tela.get_width() // 2 - 200, tela.get_height() // 2))
    pygame.display.update()
    pygame.mixer.music.load('Audio/Musicas/Carregamento.ogg')  
    pygame.mixer.music.play(-1)

    Tela = tela
    Mapa = GO.Gera_Mapa(0)

    fechar_tudo()
    GV.limpa_terminal()

    Musica_Estadio_atual = 0

    ImagensPokemonIcons,PokeGifs,OutrosIMG,FundosIMG,EfeitosIMG,ImagensPokemonCentro,ImagensItens,TiposEnergiaIMG, ImagensFichas = Carregar_Imagens_Partida(
    ImagensPokemonIcons,PokeGifs,OutrosIMG,FundosIMG,EfeitosIMG,ImagensPokemonCentro,ImagensItens,TiposEnergiaIMG, ImagensFichas)

    from PygameAções import informaçoesp1, informaçoesp2
    Jogador1 = GPA.Gerador_player(informaçoesp1)
    Jogador2 = GPA.Gerador_player(informaçoesp2)

    Jogador1.pokemons[0].pos = 0
    Jogador2.pokemons[0].pos = 0

    for i in range(15):
        GO.coletor(Jogador1)
        GO.coletor(Jogador2)

    largura, altura = M.Tabuleiros[Mapa.terreno].get_size()

    Jogador2.pokemons[0].local = [960, 570 - altura // 2]
    Jogador1.pokemons[0].local = [960, 510 + altura // 2]

    Baralho = GO.Gera_Baralho(Jogador1.deck,Jogador2.deck)

    player = Jogador1
    inimigo = Jogador2
    VerificaGIF(player,inimigo)

    pygame.mixer.music.load('Audio/Musicas/Partida.ogg')  
    pygame.mixer.music.set_volume(config["Volume"])
    pygame.mixer.music.play(-1)

    Pausa = False
    Partida = GP.GeraPartida(Jogador1,Jogador2,Baralho,Mapa)

    Resetar_Cronometro()
    cronometro.inicio = pygame.time.get_ticks()
    cronometro.tempo_encerrado = False

    player.Habilidade(player, inimigo, Partida.Mapa, Partida.Baralho, Partida.Turno)
    inimigo.Habilidade(inimigo, player, Partida.Mapa, Partida.Baralho, Partida.Turno)

    GPO.VerificaSituaçãoPokemon(player,inimigo,Partida.Mapa)
    Partida.Mapa.Verifica(player,inimigo)


# Exclusivos do modo Online

SuaVez = True
PassouVez = False
comunicaçao = False
atualizacoes_online = Queue()
DeveIniciarTurno = False
ComputouPassagemVez = True

def PassarTurnoOnline(estados):
    global player,inimigo,provocar,Partida, SuaVez, PassouVez, ComputouPassagemVez

    player.ouro += 2 + (Partida.tempo_restante // 25)
    GV.limpa_terminal()

    Partida.Mapa.Peças = []

    for pokemon in player.pokemons:
        pokemon.atacou = False
        pokemon.moveu = False
        pokemon.PodeEvoluir = True
        if pokemon.guardado != 0:
            pokemon.guardado -= 1
    
    provocar = False
    VerificaVitória(estados, Partida.Jogador1, Partida.Jogador2)
    GV.adicionar_mensagem("Seu turno acabou")
    PassouVez = True
    ComputouPassagemVez = False

def IniciarTurno():
    global SuaVez, comunicaçao
    player.ContaPassiva += 1
    inimigo.ContaPassiva += 1

    if player.ContaPassiva >= player.AtivaPassiva:
        player.Passiva(player, inimigo, Partida.Mapa, Partida.Baralho, Partida.Turno)
        GV.adicionar_mensagem("Passiva Ativada")
        player.ContaPassiva = 0

    for pokemon in player.pokemons:
        if pokemon.local is not None:
            pokemon.Ganhar_XP(2,player)

    Passar_contadores()

    Partida.Centro = GO.spawn_do_centro(Partida.Centro, Partida.Baralho, Partida.Turno)

    Partida.Turno += 1
    GV.adicionar_mensagem("Sua vez de jogar")
    SuaVez = True
    comunicaçao = False

def barra_vida_simples(tela, x, y, largura, altura, vida_atual, vida_maxima, cor_fundo, barreira=0):
    # Cálculo das proporções
    proporcao_vida = max(vida_atual, 0) / vida_maxima
    proporcao_barreira = max(barreira, 0) / vida_maxima

    largura_vida = int(largura * proporcao_vida)
    largura_barreira = int(largura * proporcao_barreira)

    # Garante que a soma não ultrapasse o total da barra
    if largura_vida + largura_barreira > largura:
        excesso = (largura_vida + largura_barreira) - largura
        largura_vida = max(largura_vida - excesso, 0)

    # Cor da vida conforme proporção
    proporcao_vida_real = vida_atual / vida_maxima if vida_maxima > 0 else 0
    if proporcao_vida_real > 0.6:
        cor_vida = (0, 200, 0)
    elif proporcao_vida_real > 0.3:
        cor_vida = (255, 200, 0)
    else:
        cor_vida = (200, 0, 0)

    # Fundo da barra
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    # Vida
    pygame.draw.rect(tela, cor_vida, (x, y, largura_vida, altura))

    # Barreira
    if largura_barreira > 0:
        pygame.draw.rect(tela, (0, 150, 255), (x + largura_vida, y, largura_barreira, altura))

    # Borda
    pygame.draw.rect(tela, (0, 0, 0), (x, y, largura, altura), 2)

    # Ícone de morto
    if vida_atual <= 0:
        img = OutrosIMG[8]
        img_rect = img.get_rect()
        img_x = x + (largura - img_rect.width) // 2
        img_y = y - img_rect.height + 12
        tela.blit(img, (img_x, img_y))

def PausarOnline():
    pass

def cronometro_falso(tela, espaço, tempo_restante, duracao_maxima, fonte, cor_fundo, cor_borda, cor_tempo):
    x, y, largura, altura = espaço

    # Visual: fundo da barra
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    # Barra de tempo restante proporcional ao tempo recebido
    tempo_restante = max(0, min(tempo_restante, duracao_maxima))  # Garante valores válidos
    largura_barra = int((tempo_restante / duracao_maxima) * largura)
    pygame.draw.rect(tela, cor_tempo, (x, y, largura_barra, altura))

    # Borda
    pygame.draw.rect(tela, cor_borda, (x, y, largura, altura), 2)

    # Texto do tempo restante
    texto = fonte.render(str(int(tempo_restante)), True, (0, 0, 0))
    texto_rect = texto.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto, texto_rect)

def IniciaOnline(tela, config):
    global ImagensPokemonCentro,ImagensPokemonIcons,ImagensFichas,PokeGifs,ImagensItens,OutrosIMG,FundosIMG,TiposEnergiaIMG,EfeitosIMG
    global player, inimigo, Tela, Musica_Estadio_atual, Partida, Pausa, SuaVez

    Carregar = GV.Carregar_Imagem("imagens/fundos/carregando.jpg",(1920,1080))
    tela.blit(Carregar,(0,0))
    texto = Fonte70.render("Carregando ...", True, PRETO)
    tela.blit(texto, (tela.get_width() // 2 - 200, tela.get_height() // 2))
    pygame.display.update()
    pygame.mixer.music.load('Audio/Musicas/Carregamento.ogg')  
    pygame.mixer.music.play(-1)

    Tela = tela

    fechar_tudo()
    GV.limpa_terminal()

    Musica_Estadio_atual = 0

    ImagensPokemonIcons,PokeGifs,OutrosIMG,FundosIMG,EfeitosIMG,ImagensPokemonCentro,ImagensItens,TiposEnergiaIMG, ImagensFichas = Carregar_Imagens_Partida(
    ImagensPokemonIcons,PokeGifs,OutrosIMG,FundosIMG,EfeitosIMG,ImagensPokemonCentro,ImagensItens,TiposEnergiaIMG, ImagensFichas)

    from Fila import DadosGerais
    Partida = DadosGerais[0]

    Partida.Jogador1.pokemons[0].pos = 0
    Partida.Jogador2.pokemons[0].pos = 0

    if DadosGerais[1] == 1:
        player = Partida.Jogador1
        inimigo = Partida.Jogador2
        player.ID_online = 1
        SuaVez = True
    else:
        player = Partida.Jogador2
        inimigo = Partida.Jogador1
        player.ID_online = 2
        SuaVez = False

    VerificaGIF(player,inimigo)

    pygame.mixer.music.load('Audio/Musicas/Partida.ogg')  
    pygame.mixer.music.set_volume(config["Volume"])
    pygame.mixer.music.play(-1)

    Pausa = False

    Resetar_Cronometro()
    cronometro.inicio = pygame.time.get_ticks()
    cronometro.tempo_encerrado = False

    # player.Habilidade(player, inimigo, Partida.Mapa, Partida.Baralho, Partida.Turno)
    # inimigo.Habilidade(inimigo, player, Partida.Mapa, Partida.Baralho, Partida.Turno)

    GPO.VerificaSituaçãoPokemon(player,inimigo,Partida.Mapa)
    Partida.Mapa.Verifica(player,inimigo)

def VerificaVitória(estados, Jogador1, Jogador2):

    VidaTotal1 = sum(p.Vida for p in Jogador1.pokemons)
    if VidaTotal1 <= 0:
        Partida.Vencedor = Jogador2
        Partida.Perdedor = Jogador1
        A.Fim_da_partida(estados)

    VidaTotal2 = sum(p.Vida for p in Jogador2.pokemons)
    if VidaTotal2 <= 0:
        Partida.Vencedor = Jogador1
        Partida.Perdedor = Jogador2
        A.Fim_da_partida(estados)

    Jogador1.Vitoria(Jogador1, Jogador2, Partida.Mapa, Partida.Baralho, Partida.Turno)
    Jogador1.Derrota(Jogador1, Jogador2, Partida.Mapa, Partida.Baralho, Partida.Turno)
    Jogador2.Vitoria(Jogador2, Jogador1, Partida.Mapa, Partida.Baralho, Partida.Turno)
    Jogador2.Derrota(Jogador2, Jogador1, Partida.Mapa, Partida.Baralho, Partida.Turno)

    if Jogador1.Pontos >= Jogador1.PontosVitoria:
        Partida.Vencedor = Jogador1
        Partida.Perdedor = Jogador2
        A.Fim_da_partida(estados)
    if Jogador1.PontosSofridos >= Jogador1.PontosDerrota:
        Partida.Vencedor = Jogador2
        Partida.Perdedor = Jogador1
        A.Fim_da_partida(estados)
    if Jogador2.Pontos >= Jogador2.PontosVitoria:
        Partida.Vencedor = Jogador2
        Partida.Perdedor = Jogador1
        A.Fim_da_partida(estados)
    if Jogador2.PontosSofridos >= Jogador2.PontosDerrota:
        Partida.Vencedor = Jogador1
        Partida.Perdedor = Jogador2
        A.Fim_da_partida(estados)
