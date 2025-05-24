import pygame
import random
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
            OP2 = 930
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
animaOP = 0

B1 = {"estado": False}
B6 = {"estado": False}
B7 = {"estado": False}
B21 = {"estado": False}
B22 = {"estado": False}
B23 = {"estado": False}
B24 = {"estado": False}

#botoes de clique unico = B6

def PartidaLoop(tela,estados,relogio,config):
    global peca_em_uso, Config

    Inicia(tela,config)

    while estados["Rodando_Partida"]:
        tela.fill(BRANCO)
        tela.blit(FundosIMG[Partida.Mapa.Fundo],(0,0))
        pygame.mixer.music.set_volume(config["Volume"])
        eventos = pygame.event.get()

        pos_mouse = pygame.mouse.get_pos()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Partida"] = False
                estados["Rodando_Jogo"] = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Clique esquerdo
                    for peca in Partida.Mapa.Peças:
                        if peca.pokemon.PodeMover:
                            if peca.iniciar_arraste(pos_mouse):
                                peca_em_uso = peca
                                break

            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1 and peca_em_uso is not None:
                    peca_em_uso.soltar(pos_mouse)
                    peca_em_uso = None
        
        tocar_musica_do_estadio()

        if not Pausa:
            # Atualiza as telas do jogo
            TelaTabuleiro(tela, eventos, estados, config)
            TelaOpções(tela, eventos, estados, config)
            TelaOutros(tela, eventos, estados, config)
            TelaPokemons(tela, eventos, estados, config)

            # Desenha as peças
            for peca in Partida.Mapa.Peças:
                if peca.pokemon.local is not None:
                    peca.desenhar(pos_mouse)

            # Desenha mensagens passageiras
            for mensagem in mensagens_passageiras[:]:
                mensagem.desenhar(tela)
                mensagem.atualizar()
                if not mensagem.ativa:
                    mensagens_passageiras.remove(mensagem)
        else:
            if Config == False:
                tela.blit(FundosIMG[0], (0, 0))
                Telapausa(tela, eventos, estados, config)
            else:
                Config = Configuraçoes(tela,eventos,config)

        # Se tiver uma peça sendo usada, desenha o raio de alcance dela
        if peca_em_uso is not None:
            peca_em_uso.atualizar_local_durante_arrasto(pos_mouse)
            peca_em_uso.desenhar_raio_velocidade()

        if config["Mostrar Fps"]:
            tela.blit(pygame.font.SysFont(None, 36).render(f"FPS: {relogio.get_fps():.2f}", True, (255, 255, 255)), (1780, 55))

        aplicar_claridade(tela,config["Claridade"])
        pygame.display.update()
        relogio.tick(config["FPS"])

def Inicia(tela, config):
    global ImagensPokemonCentro,ImagensPokemonIcons,ImagensFichas,PokeGifs,ImagensItens,OutrosIMG,FundosIMG,TiposEnergiaIMG,EfeitosIMG
    global player, inimigo, Tela, Musica_Estadio_atual, Partida

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

    largura, altura = Mapa.terreno.get_size()

    Jogador2.pokemons[0].local = 960, 570 - altura // 2
    Jogador1.pokemons[0].local = 960, 510 + altura // 2

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

def TelaPokemons(tela, eventos,estados, config):
    global PokemonS, PokemonV, PokemonSV, PokemonVV, provocar

    for pokemon in inimigo.pokemons:
        if pokemon.efeitosPosi["Provocando"] > 0:
            provocar = True

    VerificaGIF(player,inimigo)

    YO = GV.animar(OP1,OP2,animaOP,tempo=250)

    try:
        if PokemonS.PodeAtacar == True:
            GV.Botao(tela, "Atacar", (1570, YO, 340, 50), VERMELHO_CLARO, PRETO, AZUL,lambda: Atacar(PokemonS,PokemonV,PokemonA,player,inimigo,Partida.Mapa,tela,Partida.Baralho),Fonte40, B22, 3, None, True, eventos)
        else:
            GV.Botao(tela, "Atacar", (1570, YO, 340, 50), (123, 138, 148), PRETO, AZUL,lambda: tocar("Bloq"),Fonte40, B22, 3, None, True, eventos)
    
    except AttributeError:
        GV.Botao(tela, "Atacar", (1570, YO, 340, 50), (123, 138, 148), PRETO, AZUL,lambda: tocar("Bloq"),Fonte40, B22, 3, None, True, eventos)
        
    try:
        if PokemonS.PodeEvoluir == True:
            GV.Botao(tela, "Evoluir", (1570, YO + 50, 340, 50), VERDE_CLARO, PRETO, AZUL,lambda: PokemonS.evoluir(player),Fonte40, B22, 3, None, True, eventos)
        else:
            GV.Botao(tela, "Evoluir", (1570, YO + 50, 340, 50), (123, 138, 148), PRETO, AZUL,lambda: tocar("Bloq"),Fonte40, B22, 3, None, True, eventos)
    
    except AttributeError:
        GV.Botao(tela, "Evoluir", (1570, YO + 50, 340, 50), (123, 138, 148), PRETO, AZUL,lambda: tocar("Bloq"),Fonte40, B22, 3, None, True, eventos)

    try:
        if PokemonS.local is not None:
            
            GV.Botao(tela, "Guardar", (1570, YO + 100, 340, 50), AZUL_CLARO, PRETO, AZUL,lambda: M.PosicionarGuardar(PokemonS,2),Fonte40, B23, 3, None, True, eventos)

        else:
            if PokemonS.guardado > 0:
                GV.Botao(tela, f"Posicione em {PokemonS.guardado} turnos", (1570, YO + 100, 340, 50), (123, 138, 148), PRETO, AZUL,lambda: tocar("Bloq"),Fonte40, B23, 3, None, True, eventos)
            else:
                GV.Botao(tela, "Posicionar", (1570, YO + 100, 340, 50), AZUL_CLARO, PRETO, AZUL,lambda: M.PosicionarGuardar(PokemonS,0),Fonte40, B23, 3, None, True, eventos)

    except AttributeError:
        pass

    for i in range(6):
        x = 420 + i * 190
        if len(player.pokemons) > i:
            id_poke = player.pokemons[i]
        else:
            id_poke = f"A{i}"

        if not isinstance(id_poke,str):
            if id_poke.atacou == True:
                cor_do_fundo_pokemon = (123, 138, 148)
            else:
                cor_do_fundo_pokemon = AZUL_SUPER_CLARO
        else:
            cor_do_fundo_pokemon = AZUL_SUPER_CLARO

        GV.Botao_Selecao2(
            tela, (x, 890, 190, 190),
            "", Fonte30,
            cor_fundo=cor_do_fundo_pokemon, cor_borda_normal=PRETO,
            cor_borda_esquerda=VERDE, cor_borda_direita=AZUL,
            cor_passagem=AMARELO, id_botao=id_poke,
            estado_global_esquerdo=estadoPokemon, estado_global_direito=estadoVisualiza, eventos=eventos,
            funcao_esquerdo=lambda i=i: seleciona(id_poke),
            funcao_direito=lambda i=i: visualiza(id_poke),
            desfazer_esquerdo=lambda: desseleciona(), desfazer_direito=lambda: oculta(),
            tecla_esquerda=pygame.K_1, tecla_direita=None, som="clique")

    for i in range(6):
        x = 1310 - i * 190  # ajusta a posição horizontal
        if len(inimigo.pokemons) > i:
            id_poke = inimigo.pokemons[i]
        else:
            id_poke = f"I{i}"
        GV.Botao_Selecao2(
            tela, (x, 0, 190, 190),
            "", Fonte30,
            cor_fundo=VERMELHO_SUPER_CLARO, cor_borda_normal=PRETO,
            cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
            cor_passagem=AMARELO, id_botao=id_poke,
            estado_global_esquerdo=estadoAlvo ,estado_global_direito=estadoVisualiza, eventos=eventos,
            funcao_esquerdo=lambda i=i: selecionaAlvo(id_poke),
            funcao_direito=lambda i=i: visualiza(id_poke),
            desfazer_esquerdo=lambda: desselecionaAlvo(), desfazer_direito=lambda: oculta(),
            tecla_esquerda=pygame.K_1, tecla_direita=None, som="clique")
        
        if not isinstance(id_poke,str):
            j = 0
            for efeito,valor in id_poke.efeitosPosi.items():
                if valor > 0:
                    GV.Efeito(tela,(x + 150, 30 + j * 30),EfeitosIMG[efeito],VERDE,valor)
                    j +=1
            for efeito,valor in id_poke.efeitosNega.items():
                if valor > 0:
                    GV.Efeito(tela,(x + 150, 30 + j * 30),EfeitosIMG[efeito],VERMELHO,valor)
                    j +=1

    for i in range(len(player.pokemons)):
        barra_vida(tela, 425 + i * 190, 875, 180, 15, player.pokemons[i].Vida, player.pokemons[i].VidaMax,(100,100,100),player.pokemons[i].ID,player.pokemons[i].barreira)
    
    for i in range(len(inimigo.pokemons)):
        barra_vida(tela, 1315 - i * 190, 190, 180, 15, inimigo.pokemons[i].Vida, inimigo.pokemons[i].VidaMax,(100,100,100),inimigo.pokemons[i].ID,inimigo.pokemons[i].barreira)

    if PokemonS is not None:
        PokemonSV = PokemonS

    if PokemonV is not None:
        PokemonVV = PokemonV

    XstatusS = GV.animar(S1,S2,animaS)

    if XstatusS != 1920:
        Status_Pokemon((XstatusS,502), tela, PokemonSV,TiposEnergiaIMG, player, eventos,"S", Partida.Mapa, PokemonA)

    XstatusV = GV.animar(V1,V2,animaV)

    if XstatusV != 1920:
        Status_Pokemon((XstatusV,115), tela, PokemonVV,TiposEnergiaIMG, player, eventos,"V", Partida.Mapa, PokemonA)

    try:
        if alvo.ativo:
            alvo.atualizar(tela)
    except AttributeError:
        pass

    agora = pygame.time.get_ticks()

   # Para cada Pokémon no time, atualize e desenhe o GIF
    for i in range(len(player.pokemons)):
        nome = player.pokemons[i].nome
        gif = next(g for g in Gifs_ativos if g["nome"] == nome)

        if agora - gif["tempo_anterior"] > gif["intervalo"]:
            gif["frame_atual"] = (gif["frame_atual"] + 1) % len(gif["frames"])
            gif["tempo_anterior"] = agora

        frame = gif["frames"][gif["frame_atual"]]
        
        # Posição base do quadrado
        x = 420 + i * 190
        y = 890

        # Centraliza o frame dentro do quadrado 190x190
        pos_x = x + (190 - frame.get_width()) // 2
        pos_y = y + (190 - frame.get_height()) // 2

        tela.blit(frame, (pos_x, pos_y))

        if player.pokemons[i].local is None:
            tela.blit(OutrosIMG[11], ((x+10), (y+10)))
    

# Para os Pokémon inimigos, ajustando a posição X dinamicamente
    for i in range(len(inimigo.pokemons)):
        nome = inimigo.pokemons[i].nome
        gif = next(g for g in Gifs_ativos if g["nome"] == nome)

        if agora - gif["tempo_anterior"] > gif["intervalo"]:
            gif["frame_atual"] = (gif["frame_atual"] + 1) % len(gif["frames"])
            gif["tempo_anterior"] = agora

        frame = gif["frames"][gif["frame_atual"]]

        # Posição base do quadrado
        x = 1305 - i * 190
        y = 5

        # Centraliza o frame dentro do quadrado 190x190
        pos_x = x + (190 - frame.get_width()) // 2
        pos_y = y + (190 - frame.get_height()) // 2


        tela.blit(frame, (pos_x, pos_y))

        if inimigo.pokemons[i].local is None:
            tela.blit(OutrosIMG[11], ((x+15), (y+10)))


    for Pokemon in player.pokemons:
            j = 0
            x = 420 + Pokemon.pos * 190
            for efeito,valor in Pokemon.efeitosPosi.items():
                if valor > 0:
                    GV.Efeito(tela,(x + 160, 920 + j * 30),EfeitosIMG[efeito],VERDE,valor)
                    GV.tooltip((x + 146, 906 + j * 30,28,28),(x + 10, 810, 170, 60),
                               player.pokemons[0].descrição[efeito],efeito,Fonte20,Fonte28,tela)
                    j +=1
            for efeito,valor in Pokemon.efeitosNega.items():
                if valor > 0:
                    GV.Efeito(tela,(x + 160, 920 + j * 30),EfeitosIMG[efeito],VERMELHO,valor)
                    GV.tooltip((x + 146, 906 + j * 30,28,28),(x + 10, 810, 170, 60),
                               player.pokemons[0].descrição[efeito],efeito,Fonte20,Fonte28,tela)
                    j +=1

    for Pokemon in inimigo.pokemons:
            j = 0
            x = 1310 - Pokemon.pos * 190
            for efeito,valor in Pokemon.efeitosPosi.items():
                if valor > 0:
                    GV.Efeito(tela,(x + 150, 30 + j * 30),EfeitosIMG[efeito],VERDE,valor)
                    GV.tooltip((x + 136, 16 + j * 30,28,28),(x + 10, 210, 170, 60),
                               player.pokemons[0].descrição[efeito],efeito,Fonte20,Fonte28,tela)
                    j +=1
            for efeito,valor in Pokemon.efeitosNega.items():
                if valor > 0:
                    GV.Efeito(tela,(x + 150, 30 + j * 30),EfeitosIMG[efeito],VERMELHO,valor)
                    GV.tooltip((x + 136, 16 + j * 30,28,28),(x + 10, 210, 170, 60),
                               player.pokemons[0].descrição[efeito],efeito,Fonte20,Fonte28,tela)
                    j +=1

    atualizar_efeitos(tela)
    GPO.VerificaSituaçãoPokemon(player,inimigo,Partida.Mapa)

def TelaOpções(tela, eventos,estados,config):
    global EstadoOutrosAtual, A7, A8, animaAL

    YT = GV.animar(T1,T2,animaT,300)
    GV.Botao(tela, "", (0, YT, 420, 50), PRETO, PRETO, PRETO,lambda: Troca_Terminal(),Fonte40, B24, 3, None, True, eventos)
    GV.Texto_caixa(tela,f"{player.ouro}",(280, (YT - 60), 140, 60),Fonte40,LARANJA,PRETO)
    GV.Texto_caixa(tela,player.nome,(0, YT, 420, 50),Fonte50,AZUL,PRETO) 
    GV.Terminal(tela, (0, (YT + 50), 420, 230), Fonte23, AZUL_CLARO, PRETO)

    nomes_botoes_outros = ["Inventario", "Centro", "Treinador", "Estadio"]

        # Loop de criação dos botões
    for i, nome in enumerate(nomes_botoes_outros):
            GV.Botao_Selecao(
                tela, (i * 70, (YT - 60), 70, 60),
                "", Fonte30,
                cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
                cor_borda_esquerda=VERDE, cor_borda_direita=None,
                cor_passagem=AMARELO, id_botao=nome,   
                estado_global=estadoOutros, eventos=eventos,
                funcao_esquerdo=lambda nome=nome: Abre(nome, player, inimigo), 
                funcao_direito=None,
                desfazer_esquerdo=lambda: Fecha(), desfazer_direito=None,
                tecla_esquerda=pygame.K_1, tecla_direita=None)

        # Desenho seguro das imagens correspondentes sem desalinhamento
    tela.blit(OutrosIMG[0], (5, (YT - 60)))     # Inventario
    tela.blit(OutrosIMG[2], (69, (YT - 65)))    # Centro
    tela.blit(OutrosIMG[13], (150, (YT - 55)))  # Treinador
    tela.blit(OutrosIMG[3], (217, (YT - 58)))   # Estadio

    if EstadoOutrosAtual != estadoOutros["selecionado_esquerdo"]:
        EstadoOutrosAtual = estadoOutros["selecionado_esquerdo"]
        if estadoOutros["selecionado_esquerdo"] == None:
            if A8 == 1:
                A7 = 1
                A8 = -480
                animaAL = pygame.time.get_ticks()

    XInvetario = GV.animar(A1,A2,animaAI)

    if XInvetario != -385:
        Inventario((XInvetario,310),tela,player,ImagensItens,estadoItens,eventos,PokemonS, Partida.Mapa, Partida.Baralho, estadoEnergias)

    XCentro = GV.animar(A5,A6,animaAC)

    if XCentro != -385:
        Centroo(tela, XCentro, 310, Partida.Centro, player, Fonte50, Fonte28, B6, estadoPokebola,estadoFruta, eventos)
    
    XTreinador = GV.animar(A3,A4,animaAT)

    if XTreinador != -385:
        TreinadorInfo((XTreinador,310),tela,player.treinador,ImagensFichas,"P",player)

    if config["Dicas"]:
        GV.tooltip((280, (YT - 60), 140, 60),(30,(YT - 130),360,70), f"Quanto mais fizer sua jogada, mais ouro vai ganhar", f"Ganho Atual {2 + (Partida.tempo_restante // 25)}",Fonte25,Fonte35,tela)
        GV.tooltip((210, (YT - 60), 70, 60),(30,(YT - 130),360,70), f"Veja quais são as mudanças e as caracteristicas do estádio atual", f"Estádio",Fonte25,Fonte35,tela)
        GV.tooltip((140, (YT - 60), 70, 60),(30,(YT - 130),360,70), f"Veja quais são as caracteristicas do seu apoiador", f"Apoiador",Fonte25,Fonte35,tela)
        GV.tooltip((70, (YT - 60), 70, 60),(30,(YT - 130),360,70), f"Veja os pokemons que podem ser capturados", f"Centro",Fonte25,Fonte35,tela)
        GV.tooltip((0, (YT - 60), 70, 60),(30,(YT - 130),360,70), f"Veja suas energias e seus itens, podendo usa-los", f"Inventário",Fonte25,Fonte35,tela)

def TelaOutros(tela, eventos,estados, config):
    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,lambda: pausarEdespausar(), Fonte50, B1, 3, pygame.K_ESCAPE, False, eventos)
    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,lambda: Muter(), Fonte50, B1, 3, pygame.K_m, False, eventos)
    GV.Botao(tela, "Passar Turno", (10, 90, 340, 50), AMARELO_CLARO, PRETO, AZUL,lambda: passar_turno(estados),Fonte40, B7, 3, None, True, eventos)
    GV.Texto_caixa(tela,f"Turno: {Partida.Turno}",(0, 0, 360, 60),Fonte70,AMARELO,PRETO) 
    GV.Texto_caixa(tela,inimigo.nome,(1500, 0, 420, 50),Fonte50,VERMELHO_CLARO,PRETO)

    cronometro(tela, (0, 60, 360, 30), player.tempo, Fonte40, CINZA, PRETO, AMARELO, lambda:passar_turno(estados),Partida.Turno)

    XL = GV.animar(A7,A8,animaAL)

    Loja((XL,195),tela,Partida.Baralho,ImagensItens,Partida.Turno,eventos,player,2,Partida.Loja)

def Telapausa(tela, eventos,estados, config):
    GV.Botao(tela, "Despausar partida", (600, 160, 720, 130), CINZA, PRETO, AZUL,lambda: pausarEdespausar(),Fonte70, B6, 5, pygame.K_ESCAPE, True, eventos)
    GV.Botao(tela, "Configuraçoes", (600, 385, 720, 130), CINZA, PRETO, AZUL,lambda: TrocaConfig(),Fonte70, B6, 5, None, True, eventos)
    GV.Botao(tela, "Sair da partida", (600, 610, 720, 130), CINZA, PRETO, AZUL,lambda: A.Voltar(estados),Fonte70, B6, 5, None, True, eventos)
    GV.Botao(tela, "Sair do jogo", (600, 835, 720, 130), CINZA, PRETO, AZUL,lambda: A.fechar_jogo(estados),Fonte70, B6, 5, None, True, eventos)

def TelaTabuleiro(tela, eventos, estados, config):
    global Musica_Estadio_atual

    M.Desenhar_Casas_Disponiveis(tela,Partida.Mapa,player,inimigo,eventos,estadoAlvo,estadoVisualiza,selecionaAlvo,desselecionaAlvo,oculta,visualiza)
    if Partida.Mapa.mudança == True:
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
