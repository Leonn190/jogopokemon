import pygame
import random
from Visual.Imagens import Carregar_Imagens, Carrega_Gif_pokemon
from Visual.Mensagens import mensagens_passageiras
from Visual.Efeitos import gerar_gif, atualizar_efeitos
from Visual.Sonoridade import tocar
from Abas import Status_Pokemon,Inventario,Atacar, Loja
import Tabuleiro as M
import Geradores.GeradorPlayer as GPA
import Geradores.GeradorPokemon as GPO
import Geradores.GeradorOutros as GO
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte25, Fonte28, Fonte30, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA,CINZA_ESCURO, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO,VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA,LARANJA_CLARO, ROXO,ROXO_CLARO, ROSA, DOURADO, PRATA,)

pygame.mixer.init()
selecionaSOM = pygame.mixer.Sound("Audio/Sons/Som1.wav")

Tela = None
Mapa = None
Baralho = None

Gifs_ativos = []

Mute = False
PeçaS = None
PokemonS = None
PokemonSV = None
PokemonV = None
PokemonVV = None
PokemonA = None
PokemonAV = None
alvo = None
informacao = None
Visor = None
PokebolaSelecionada = None
FrutaSelecionada = None
provocar = False

PokeGifs = {}
TiposEnergiaIMG = {}
ImagensPokemonIcons = {}
ImagensPokemonCentro = {}
ImagensCaptura = {}
ImagensItens = {}
OutrosIMG = []
FundosIMG = []
EfeitosIMG = {}

Centro = [None,None,None,None,None,None,None,None]
ver_centro = "n"

Turno = 1
tempo_restante = 0

Jogador1 = None
Jogador2 = None

player = None
inimigo = None

Vencedor = None
Perdedor = None

Pausa = False

# variaveis do mapa

LojaItensP = None
LojaPokeP = None
LojaAmpliP = None
LojaEnerP = None
LojaEstTreP = None
Musica_Estadio_atual = None

def cronometro(tela, espaço, duracao_segundos, fonte, cor_fundo, cor_borda, cor_tempo, ao_terminar, turno_atual):
    global tempo_restante

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

    tempo_restante = max(0, duracao_segundos - tempo_decorrido)

    # Visual: fundo, barra preenchida, borda
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
    largura_barra = int((tempo_restante / duracao_segundos) * largura)
    pygame.draw.rect(tela, cor_tempo, (x, y, largura_barra, altura))  # cor do tempo separada
    pygame.draw.rect(tela, cor_borda, (x, y, largura, altura), 2)

    # Texto do tempo
    texto = fonte.render(str(tempo_restante), True, (0, 0, 0))
    texto_rect = texto.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto, texto_rect)

    # Chama função se o tempo zerar
    if tempo_restante <= 0 and not cronometro.tempo_encerrado:
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

def passar_turno():
    global Turno
    global Centro
    global player
    global inimigo

    player.ouro += 2 + (tempo_restante // 25)
    GV.limpa_terminal()
    Mapa.Zona = M.Inverter_Tabuleiro(player, inimigo, Mapa.Zona)

    for pokemon in player.pokemons:
        pokemon.atacou = False
        pokemon.PodeEvoluir = True
        if pokemon.guardado != 0:
            pokemon.guardado -= 1

    player, inimigo = inimigo, player

    for pokemon in player.pokemons:
        if pokemon.local is not None:
            pokemon.Ganhar_XP(2,player)
    Passar_contadores()

    Centro = GO.spawn_do_centro(Centro, Baralho, Turno)

    Turno += 1
    fechar_tudo()
    GV.adicionar_mensagem(f"Novo turno de {player.nome}!")

S1 = 1920
S2 = 1920
V1 = 1920
V2 = 1920
AT1 = -60
AT2 = -60
T1 = 800
T2 = 800
OP1 = 1080
OP2 = 1080

def seleciona_peça(p,dono,player):
    global PeçaS
    if dono == "player":
            if p.efeitosNega["Congelado"] == 0 or p.efeitosNega["Paralisado"] == 0:
                pagou = 0
                gastas = []
                Custo = p.custo
                if p.efeitosNega["Encharcado"]:
                    Custo += 2
                for i in range(Custo):
                    for cor in player.energiasDesc:
                        if player.energias[cor] >= 1:
                            player.energias[cor] -= 1
                            gastas.append(cor)
                            pagou += 1
                            break
                
                if pagou != Custo:
                    tocar("Bloq")
                    GV.adicionar_mensagem("Sem energias, não pode se mover")
                    for i in range(len(gastas)):
                        player.energias[gastas[i]] += 1
                    desseleciona_peça()
                    return 

                PeçaS = p
            else:
                GV.adicionar_mensagem("Esse pokemon está congelado ou paralisado")
    else:
        print (p)
        selecionaAlvo(p)

def desseleciona_peça():
    global PeçaS, estadoTabuleiro, PokemonA
    if PeçaS == None:
        print ("jujuba")
        desselecionaAlvo()
    PeçaS = None
    estadoTabuleiro["selecionado_esquerdo"] =  False

def seleciona(Pokemon):
    global PokemonS
    if not isinstance(Pokemon,str):
        if Pokemon.Vida > 0 and Pokemon.efeitosNega["Congelado"] <= 0 and Pokemon not in inimigo.pokemons:
            PokemonS = Pokemon
            global S1, S2, animaS
            global AT1, AT2, animaA
            global OP1, OP2, animaOP
            S1 = 1920
            S2 = 1540
            AT1 = -60
            AT2 = 210
            OP1 = 1080
            OP2 = 930
            animaS = pygame.time.get_ticks()
            animaA = pygame.time.get_ticks()
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
        if Pokemon.efeitosPosi["Furtivo"] > 0:
            GV.adicionar_mensagem("Esse pokemon está em modo furtivo")
            return
        if provocar is True:
            if Pokemon.efeitosPosi["Provocando"] == 0:
                GV.adicionar_mensagem("Algum outro pokemon está provocando")
                return
        PokemonA = Pokemon
        alvo = gerar_gif(OutrosIMG[14],((1400 - PokemonA.pos * 190),95),35)

def desselecionaAlvo():
    global PokemonA,alvo, estadoAlvo
    alvo = None
    PokemonA = None
    estadoAlvo = {"selecionado_esquerdo": None}

def desseleciona():
    global PokemonS
    global estadoPokemon
    global estadoInfo
    global S1, S2, animaS
    global AT1, AT2, animaA
    global OP1, OP2, animaOP
    if PokemonS is not None:
        S1 = 1540
        S2 = 1920
        AT1 = 210
        AT2 = -60
        OP1 = 930
        OP2 = 1080
        animaS = pygame.time.get_ticks()
        animaA = pygame.time.get_ticks()
        animaOP = pygame.time.get_ticks()
        PokemonS = None
    estadoPokemon["selecionado_esquerdo"] = False

def vizualiza(Pokemon):
    global PokemonV
    global V1, V2, animaV
    if not isinstance(Pokemon,str):
        PokemonV = Pokemon
        V1 = 1920
        V2 = 1540
        animaV = pygame.time.get_ticks()
    else:
        PokemonV = None
        GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")     

def oculta():
    global PokemonV
    global estadoInfo
    global V1, V2, animaV
    if PokemonV is not None:
        V1 = 1540
        V2 = 1920
        animaV = pygame.time.get_ticks()
        PokemonV = None
    estadoVizualiza["selecionado_direito"] = False

A1 = -382
A2 = -382
A3 = -382
A4 = -382
A5 = -400
A6 = -400
A7 = 0
A8 = 0

def informa(ID,Pokemon):
    pass

def desinforma():
    global estadoInfo
    estadoInfo["selecionado_esquerdo"] = None
    pass

def Abre(ID,player,inimigo):
    if ID == "Inventario":
        global A1, A2, animaAI
        A1 = -382
        A2 = 0
        animaAI = pygame.time.get_ticks()
    elif ID == "Energias":
        global A3, A4, animaAE
        A3 = -382
        A4 = 0
        animaAE = pygame.time.get_ticks()
    elif ID == "Centro":
        global A5, A6, animaAC
        A5 = -400
        A6 = 0
        animaAC = pygame.time.get_ticks()
    elif ID == "Lojas":
        global A7, A8, animaAL
        A7 = 0
        A8 = 0
        animaAL = pygame.time.get_ticks()
    
def Fecha():
    global A1, A2, animaAI
    global A3, A4, animaAE
    global A5, A6, animaAC
    global A7, A8, animaAL
    global estadoOutros
    if A2 == 0:
        A1 = 0
        A2 = -382
        animaAI = pygame.time.get_ticks()
    elif A4 == 0:
        A3 = 0
        A4 = -382
        animaAE = pygame.time.get_ticks()
    elif A6 == 0:
        A5 = 0
        A6 = -400
        animaAC = pygame.time.get_ticks()
    elif A8 == 0:
        A7 = 0
        A8 = 0
        animaAL = pygame.time.get_ticks()
    estadoOutros["selecionado_esquerdo"] =  False

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
    global estadoPokemon
    global estadoInfo
    global estadoOutros
    global estadoPokebola
    global estadoItens
    global estadoFruta
    global estadoAlvo
    global estadoVizualiza
    global S1, S2, V1, V2,AT1,AT2,T1,T2,OP1,OP2,A1, A2, A3, A4, A5, A6, A7, A8, alvo

    estadoPokemon = {"selecionado_esquerdo": None}

    estadoAlvo = {"selecionado_esquerdo": None}

    estadoVizualiza ={"selecionado_direito": None}

    estadoInfo = {
        "selecionado_esquerdo": None,
        "selecionado_direito": None}
    estadoOutros = {
        "selecionado_esquerdo": None,
        "selecionado_direito": None}
    estadoPokebola = {
        "selecionado_esquerdo": None,
        "selecionado_direito": None}
    estadoItens = {
        "selecionado_esquerdo": None,
        "selecionado_direito": None}
    estadoFruta = {
        "selecionado_esquerdo": None,
        "selecionado_direito": None}
    
    S1 = 1920
    S2 = 1920
    V1 = 1920
    V2 = 1920
    AT1 = -60
    AT2 = -60
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
    global Centro
    global estadoOutros

    AIV = 1
    
    if PokebolaSelecionada is not None:
        Baralho.devolve_item(PokebolaSelecionada)
        player.inventario.remove(PokebolaSelecionada)
        Pokebola_usada = PokebolaSelecionada
        desseleciona_pokebola()
        maestria = random.randint(0,Pokebola_usada["poder"] * 2)
        if FrutaSelecionada is not None:
            Baralho.devolve_item(FrutaSelecionada)
            player.inventario.remove(FrutaSelecionada)
            if FrutaSelecionada["nome"] in ["Fruta Frambo","Fruta Frambo Dourada"]:
                pokemon["dificuldade"] -= FrutaSelecionada["poder"]
                AIV = 1
            elif FrutaSelecionada["nome"] in ["Fruta Caxi","Fruta Caxi Prateada"]:
                AIV = FrutaSelecionada["poder"]
            desseleciona_fruta()
        if maestria >= pokemon["dificuldade"]:
            if len(player.pokemons) < 6:
                novo_pokemon = GPO.Gerador_final(pokemon["code"],AIV,player)
                M.GuardarPosicionar(novo_pokemon,player,0,Mapa.Zona)
                GV.adicionar_mensagem(f"Parabens! Capturou um {novo_pokemon.nome} usando uma {Pokebola_usada['nome']}")
                VerificaGIF(player,inimigo)
                tocar("Bom")
                indice = Centro.index(pokemon)
                Centro[indice] = None
                return
            else:
                tocar("Bloq")
                GV.adicionar_mensagem("sua lista de pokemon está cheia")
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
    print (Pausa)
    if Pausa == True:
        pausaEdespausaCronometro()
        Pausa = False
    else:
        Pausa = True
        pausaEdespausaCronometro()

def AddLocalPokemonINIC(pokemon,jogador):
    if jogador == Jogador1:
        M.Move(pokemon,11,12,Mapa.Zona)
    else:
        M.Move(pokemon,3,12,Mapa.Zona)

def Muter():
    global Mute

    if Mute is False:
        pygame.mixer.music.set_volume(0.0)
        Mute = True
    else:
        pygame.mixer.music.set_volume(0.3)
        Mute = False

def tocar_musica_do_estadio():
    global Musica_Estadio_atual

    if Mapa.Musica != Musica_Estadio_atual:
        Z = Mapa.Musica 
        # Trocar a música
        pygame.mixer.music.stop()
        
        if Mapa.Musica == 0:
            pygame.mixer.music.load("Audio/Musicas/Partida.ogg")
        elif Mapa.Musica == 1:
            pygame.mixer.music.load("Audio/Musicas/Mer.ogg")
        elif Mapa.Musica == 2:
            pygame.mixer.music.load("Audio/Musicas/Shivre.ogg")
        elif Mapa.Musica == 3:
            pygame.mixer.music.load("Audio/Musicas/Auroma.ogg")
        elif Mapa.Musica == 4:
            pygame.mixer.music.load("Audio/Musicas/Kalos.ogg")
        elif Mapa.Musica == 5:
            pygame.mixer.music.load("Audio/Musicas/Skyloft.ogg")
        elif Mapa.Musica == 6:
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

    # Pokébolas (topo, 6 espaços)
    for i, item in enumerate([i for i in player.inventario if i.get("classe") == "pokebola"][:6]):
        x = x_inicial_animado + i * (tamanho_botao_pokebola + espacamento)
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
        tela.blit(ImagensCaptura[item["nome"]], (x + 2, y + 2))

    # Grade Pokémon (centro, 4x2)
    offset_y_pokemon = offset_y_pokebola + tamanho_botao_pokebola + espacamento
    for i, pokemon in enumerate(Centro):
        coluna = i % 4
        linha = i // 4
        x = x_inicial_animado + espacamento + coluna * (tamanho_pokemon + espacamento)
        y = offset_y_pokemon + linha * (tamanho_pokemon + espacamento)

        if pokemon and pokemon["nome"] in ImagensPokemonCentro:
            # Desenha botão e imagem do Pokémon
            GV.Botao(
                tela, "", (x, y, tamanho_pokemon, tamanho_pokemon), CINZA, PRETO, AZUL,
                lambda p=pokemon: PokemonCentro(p, player),
                Fonte50, B6, 2, None, True, eventos
            )
            tela.blit(ImagensPokemonCentro[pokemon["nome"]], (x, y))
        else:
            # Desenha apenas a lacuna vazia
            vazio = pygame.Surface((tamanho_pokemon, tamanho_pokemon))
            vazio.fill((50, 50, 50))
            tela.blit(vazio, (x, y))

    # Frutas (parte inferior, 6 espaços)
    offset_y_fruta = y_inicial + altura_total - tamanho_fruta - espacamento
    for i, item in enumerate([i for i in player.inventario if i.get("classe") == "Fruta"][:6]):
        x = x_inicial_animado + i * (tamanho_fruta + espacamento)
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

        if item["nome"] in ImagensCaptura:
            tela.blit(ImagensCaptura[item["nome"]], (x + 2, y + 2))

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
                pokemon.atacado(dano_dos_efeitos,player,inimigo,Tela,Mapa)

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

estadoVizualiza ={"selecionado_direito": None}

estadoInfo = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}
estadoOutros = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

estadoPokebola = {"selecionado_esquerdo": None,}

estadoItens = {"selecionado_direito": None}

estadoEnergias = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

estadoFruta = {"selecionado_esquerdo": None,}

estadoTabuleiro = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

animaS = 0
animaAI = 0
animaAE = 0
animaAC = 0
animaV = 0
animaA = 0
animaT = 0
animaOP = 0
animaAL = 0

B1 = {"estado": False}
B2 = {"estado": False, "ID": "item"}
B3 = {"estado": False, "ID": "pokebola"}
B4 = {"estado": False, "ID": "amplificador"}
B5 = {"estado": False, "ID": "energia"}
B6 = {"estado": False}
B7 = {"estado": False}

B8 = {"estado": False, "ID": 0}
B9 = {"estado": False, "ID": 1}
B10 = {"estado": False, "ID": 2}
B11 = {"estado": False, "ID": 3}
B12 = {"estado": False, "ID": 4}
B13 = {"estado": False, "ID": 5}
B14 = {"estado": False, "ID": 0}
B15 = {"estado": False, "ID": 1}
B16 = {"estado": False, "ID": 2}
B17 = {"estado": False, "ID": 3}
B18 = {"estado": False, "ID": 4}
B19 = {"estado": False, "ID": 5}

B20 = {"estado": False, "ID": "estadio"}
B21 = {"estado": False}

B22 = {"estado": False}
B23 = {"estado": False}

BA = [B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19,]
#botoes de clique unico = B6

def Partida(tela,estados,relogio):
    global Vencedor
    global Perdedor

    Inicia(tela)

    while estados["Rodando_Partida"]:
        tela.fill(BRANCO)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Partida"] = False
                estados["Rodando_Jogo"] = False
        
        tocar_musica_do_estadio()

        if Pausa == False:
            TelaTabuleiro(tela,eventos,estados)
            TelaOpções(tela,eventos,estados)
            TelaOutros(tela,eventos,estados)
            TelaPokemons(tela,eventos,estados)

            VidaTotal1 = sum(p.Vida for p in Jogador1.pokemons)
            if VidaTotal1 <= 0:
                Vencedor = Jogador2
                Perdedor = Jogador1
                A.Fim_da_partida(estados)

            VidaTotal2 = sum(p.Vida for p in Jogador2.pokemons)
            if VidaTotal2 <= 0:
                Vencedor = Jogador1
                Perdedor = Jogador2
                A.Fim_da_partida(estados)

            for mensagem in mensagens_passageiras[:]:
                mensagem.desenhar(tela)
                mensagem.atualizar()
                if not mensagem.ativa:
                    mensagens_passageiras.remove(mensagem)
        else:
            tela.blit(FundosIMG[0],(0,0))
            Telapausa(tela,eventos,estados)

        tela.blit(pygame.font.SysFont(None, 36).render(f"FPS: {relogio.get_fps():.2f}", True, (255, 255, 255)), (1780, 55))

        pygame.display.update()
        relogio.tick(170)

def Inicia(tela):
    global Turno
    global ImagensPokemonCentro
    global ImagensPokemonIcons
    global PokeGifs
    global ImagensCaptura
    global ImagensItens
    global OutrosIMG
    global FundosIMG
    global TiposEnergiaIMG
    global EfeitosIMG
    global Jogador1
    global Jogador2
    global player
    global inimigo
    global Vencedor
    global Perdedor
    global Pausa
    global Centro
    global Mapa
    global Musica_Estadio_atual
    global LojaItensP
    global LojaPokeP
    global LojaEnerP
    global LojaAmpliP
    global LojaEstTreP
    global Tela
    global Baralho

    Carregar = GV.Carregar_Imagem("imagens/fundos/carregando.jpg",(1920,1080))

    tela.blit(Carregar,(0,0))
    fonte = pygame.font.SysFont(None, 70)
    texto = fonte.render("Carregando ...", True, PRETO)
    tela.blit(texto, (tela.get_width() // 2 - 200, tela.get_height() // 2))
    pygame.display.update()

    pygame.mixer.music.load('Audio/Musicas/Carregamento.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    Tela = tela
    Mapa = GO.Gera_Mapa(0)
    Baralho = GO.Gera_Baralho()

    fechar_tudo()

    GV.limpa_terminal()

    Musica_Estadio_atual = 0
    LojaItensP = Mapa.PlojaI
    LojaPokeP = Mapa.PlojaP
    LojaAmpliP = Mapa.PlojaA
    LojaEnerP = Mapa.PlojaE
    LojaEstTreP = Mapa.pLojaT

    ImagensPokemonIcons,ImagensPokemonCentro,PokeGifs,ImagensCaptura,ImagensItens,OutrosIMG,FundosIMG,TiposEnergiaIMG,EfeitosIMG = Carregar_Imagens(ImagensPokemonIcons,ImagensPokemonCentro,PokeGifs,ImagensCaptura,ImagensItens,OutrosIMG,FundosIMG,TiposEnergiaIMG,EfeitosIMG)
    Mapa.Zona = M.Gerar_Mapa()

    from PygameAções import informaçoesp1, informaçoesp2
    Jogador1 = GPA.Gerador_player(informaçoesp1)
    Jogador2 = GPA.Gerador_player(informaçoesp2)

    Jogador1.pokemons[0].pos = 0
    Jogador2.pokemons[0].pos = 0

    for i in range(15):
        Jogador1.energias[GO.coletor()] += 1
        Jogador2.energias[GO.coletor()] += 1

    AddLocalPokemonINIC(Jogador2.pokemons[0],Jogador2)
    AddLocalPokemonINIC(Jogador1.pokemons[0],Jogador1)

    player = Jogador1
    inimigo = Jogador2

    VerificaGIF(player,inimigo)

    pygame.mixer.music.load('Audio/Musicas/Partida.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    Pausa = False
    Turno = 1
    Centro = [None,None,None,None,None,None,None,None]

    Resetar_Cronometro()
    cronometro.inicio = pygame.time.get_ticks()
    cronometro.tempo_encerrado = False

def TelaPokemons(tela,eventos,estados):
    global PokemonS
    global PokemonV
    global PokemonSV
    global PokemonVV
    global provocar
    global informacao
    global player
    global inimigo

    for pokemon in inimigo.pokemons:
        if pokemon.efeitosPosi["Provocando"] > 0:
            provocar = True

    VerificaGIF(player,inimigo)

    YO = GV.animar(OP1,OP2,animaOP,tempo=250)

    try:
        if PokemonS.PodeAtacar == True:
            GV.Botao(tela, "Atacar", (1570, YO, 340, 50), VERMELHO_CLARO, PRETO, AZUL,lambda: Atacar(PokemonS,PokemonV,PokemonA,player,inimigo,Mapa,tela),Fonte40, B22, 3, None, True, eventos)
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
            
            GV.Botao(tela, "Guardar", (1570, YO + 100, 340, 50), AZUL_CLARO, PRETO, AZUL,lambda: M.GuardarPosicionar(PokemonS,player,2,Mapa.Zona),Fonte40, B23, 3, None, True, eventos)

        else:
            if PokemonS.guardado > 0:
                GV.Botao(tela, f"Posicione em {PokemonS.guardado} turnos", (1570, YO + 100, 340, 50), (123, 138, 148), PRETO, AZUL,lambda: tocar("Bloq"),Fonte40, B23, 3, None, True, eventos)
            else:
                GV.Botao(tela, "Posicionar", (1570, YO + 100, 340, 50), AZUL_CLARO, PRETO, AZUL,lambda: M.GuardarPosicionar(PokemonS,player,0,Mapa.Zona),Fonte40, B23, 3, None, True, eventos)

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
            estado_global_esquerdo=estadoPokemon, estado_global_direito=estadoVizualiza, eventos=eventos,
            funcao_esquerdo=lambda i=i: seleciona(id_poke),
            funcao_direito=lambda i=i: vizualiza(id_poke),
            desfazer_esquerdo=lambda: desseleciona(), desfazer_direito=lambda: oculta(),
            tecla_esquerda=pygame.K_1, tecla_direita=None, som=selecionaSOM)

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
            estado_global_esquerdo=estadoAlvo ,estado_global_direito=estadoVizualiza, eventos=eventos,
            funcao_esquerdo=lambda i=i: selecionaAlvo(id_poke),
            funcao_direito=lambda i=i: vizualiza(id_poke),
            desfazer_esquerdo=lambda: desselecionaAlvo(), desfazer_direito=lambda: oculta(),
            tecla_esquerda=pygame.K_1, tecla_direita=None, som=selecionaSOM)
        
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
        Status_Pokemon((XstatusS,502), tela, PokemonSV,TiposEnergiaIMG, player, eventos,"S")

    XstatusV = GV.animar(V1,V2,animaV)

    if XstatusV != 1920:
        Status_Pokemon((XstatusV,115), tela, PokemonVV,TiposEnergiaIMG, player, eventos,"V")

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
                    GV.tooltip((x + 146, 906 + j * 30,28,28),player.pokemons[0].descrição[efeito],tela,Fonte20)
                    j +=1
            for efeito,valor in Pokemon.efeitosNega.items():
                if valor > 0:
                    GV.Efeito(tela,(x + 160, 920 + j * 30),EfeitosIMG[efeito],VERMELHO,valor)
                    GV.tooltip((x + 146, 906 + j * 30,28,28),player.pokemons[0].descrição[efeito],tela,Fonte20)
                    j +=1

    for Pokemon in inimigo.pokemons:
            j = 0
            x = 1310 - Pokemon.pos * 190
            for efeito,valor in Pokemon.efeitosPosi.items():
                if valor > 0:
                    GV.Efeito(tela,(x + 150, 30 + j * 30),EfeitosIMG[efeito],VERDE,valor)
                    GV.tooltip((x + 136, 16 + j * 30,28,28),player.pokemons[0].descrição[efeito],tela,Fonte20)
                    j +=1
            for efeito,valor in Pokemon.efeitosNega.items():
                if valor > 0:
                    GV.Efeito(tela,(x + 150, 30 + j * 30),EfeitosIMG[efeito],VERMELHO,valor)
                    GV.tooltip((x + 136, 16 + j * 30,28,28),player.pokemons[0].descrição[efeito],tela,Fonte20)
                    j +=1

    atualizar_efeitos(tela)
    GPO.VerificaSituaçãoPokemon(player,inimigo)

def TelaOpções(tela,eventos,estados):
    global PokemonS
    global Visor
    global player
    global inimigo
    global ver_centro
    global Centro

    YT = GV.animar(T1,T2,animaT,300)

    GV.Botao(tela, "", (0, YT, 420, 50), PRETO, PRETO, PRETO,lambda: Troca_Terminal(),Fonte40, B20, 3, None, True, eventos)
    GV.Texto_caixa(tela,f"{player.ouro}",(350, (YT - 60), 70, 60),Fonte40,LARANJA,PRETO)
    GV.Texto_caixa(tela,player.nome,(0, YT, 420, 50),Fonte50,AZUL,PRETO) 
    GV.Terminal(tela, (0, (YT + 50), 420, 230), Fonte20, AZUL_CLARO, PRETO)

    nomes_botoes_outros = ["Inventario", "Energias", "Centro", "Lojas", "Treinador"]

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
        
        tela.blit(OutrosIMG[0],(5,(YT - 60)))
        tela.blit(OutrosIMG[1],(80,(YT - 55)))
        tela.blit(OutrosIMG[2],(140,(YT - 65)))
        tela.blit(OutrosIMG[12],(220,(YT - 55)))
        tela.blit(OutrosIMG[13],(290,(YT - 55)))

        XInvetario = GV.animar(A1,A2,animaAI)

        if XInvetario != -382:
            Inventario((XInvetario,310),tela,player,ImagensItens,estadoItens,eventos,PokemonS, Mapa, Baralho, estadoEnergias)

        XCentro = GV.animar(A5,A6,animaAC)

        if XCentro != 400:
            Centroo(tela, XCentro, 260, Centro, player, Fonte50, Fonte28, B6, estadoPokebola,estadoFruta, eventos)

        if ver_centro == "s":
            idx_pokebola = 0  
            for i, item in enumerate(player.inventario):
                if item.get("classe") == "pokebola":
                    x = 332
                    y = 262 + idx_pokebola * 60 
                    tela.blit(ImagensCaptura[item["nome"]], (x, y))
                    idx_pokebola += 1 

            
            x_inicial = 10
            y_inicial = 270

            for i in range(len(Centro)):
                coluna = i % 3        
                linha = i // 3        
                x = x_inicial + coluna * 109
                y = y_inicial + linha * 109
                tela.blit(ImagensPokemonCentro[Centro[i]["nome"]],(x,y))
    
    GV.tooltip((350, (YT - 60), 70, 60),f"Quanto mais rapido jogar, mais ouro você vai ganhar Ganho se passar turno: {2 + (tempo_restante // 25)}",tela,Fonte20,200)

def TelaOutros(tela,eventos,estados):
    global LojaItensP
    global LojaPokeP
    global LojaAmpliP
    global LojaEnerP
    global LojaEstTreP
    global player
    global inimigo
    global Baralho

    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,lambda: pausarEdespausar(), Fonte50, B1, 3, pygame.K_ESCAPE, False, eventos)

    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,lambda: Muter(), Fonte50, B1, 3, pygame.K_m, False, eventos)

    GV.Botao(tela, "Passar Turno", (10, 90, 340, 50), AMARELO_CLARO, PRETO, AZUL,lambda: passar_turno(),Fonte40, B7, 3, None, True, eventos)
    
    cronometro(tela, (0, 60, 360, 30), Mapa.tempo, Fonte40, CINZA, PRETO, AMARELO, lambda:passar_turno(),Turno)

    GV.Texto_caixa(tela,f"Turno: {Turno}",(0, 0, 360, 60),Fonte70,AMARELO,PRETO) 
    GV.Texto_caixa(tela,inimigo.nome,(1500, 0, 420, 50),Fonte50,VERMELHO_CLARO,PRETO)

    XL = GV.animar(A7,A8,animaAL)

    Loja((XL,195),tela,Baralho,ImagensItens,Turno,eventos,player,2)

def Telapausa(tela,eventos,estados):

    GV.Botao(tela, "Despausar partida", (600, 200, 720, 130), CINZA, PRETO, AZUL,lambda: pausarEdespausar(),Fonte70, B6, 5, pygame.K_ESCAPE, True, eventos)
    GV.Botao(tela, "Sair da partida", (600, 425, 720, 130), CINZA, PRETO, AZUL,lambda: A.Voltar(estados),Fonte70, B6, 5, None, True, eventos)
    GV.Botao(tela, "Sair do jogo", (600, 650, 720, 130), CINZA, PRETO, AZUL,lambda: A.fechar_jogo(estados),Fonte70, B6, 5, None, True, eventos)

def TelaTabuleiro(tela, eventos, estados):
    global Musica_Estadio_atual
    global LojaItensP
    global LojaPokeP
    global LojaEnerP
    global LojaAmpliP
    global LojaEstTreP

    LojaItensP = Mapa.PlojaI
    LojaPokeP = Mapa.PlojaP
    LojaAmpliP = Mapa.PlojaA
    LojaEnerP = Mapa.PlojaE
    LojaEstTreP = Mapa.pLojaT

    tela.blit(FundosIMG[Mapa.Fundo],(0,0))
    M.Desenhar_Casas_Disponiveis(tela, Mapa, player, inimigo, Fonte20, eventos, seleciona_peça, desseleciona_peça, PeçaS, estadoTabuleiro)  
 