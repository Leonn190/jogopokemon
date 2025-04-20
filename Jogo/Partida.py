import pygame
import random
import Tabuleiro as M
import GeradoresVisuais as GV
import Gerador2 as G
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte25, Fonte28, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA,CINZA_ESCURO, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO,VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA,LARANJA_CLARO, ROXO,ROXO_CLARO, ROSA, DOURADO, PRATA,)

pygame.mixer.init()

clique = pygame.mixer.Sound("Jogo/Audio/Sons/Som1.wav")
Compra = pygame.mixer.Sound("Jogo/Audio/Sons/Compra.wav")
Usou = pygame.mixer.Sound("Jogo/Audio/Sons/Usou.wav")
Bom = pygame.mixer.Sound("Jogo/Audio/Sons/Bom.wav")
Bloq = pygame.mixer.Sound("Jogo/Audio/Sons/Bloq.wav")

Tela = None
Mapa = None

Mute = False
PokemonS = None
PokemonSV = None
PokemonV = None
PokemonVV = None
informacao = None
Visor = None
PokebolaSelecionada = None
FrutaSelecionada = None

mensagens_passageiras = []

PokeGifs = {}
Gifs_ativos = []
efeitos_ativos = []

TiposEnergiaIMG = {}
ImagensPokemon38 = {}
ImagensPokemon100 = {}
ImagensPokebolas = {}
ImagensItens = {}
OutrosIMG = []
FundosIMG = []

Centro = []
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

class GifAtivo:
    def __init__(self, frames, posicao, velocidade, duracao, ao_terminar=None):
        self.frames = frames
        self.posicao = posicao
        self.velocidade = velocidade  # ms por frame
        self.duracao = duracao        # duração total em ms
        self.ao_terminar = ao_terminar

        self.inicio = pygame.time.get_ticks()
        self.tempo_ultimo_frame = self.inicio
        self.frame_atual = 0

    def desenhar(self, tela):
        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_frame >= self.velocidade:
            self.frame_atual += 1
            self.tempo_ultimo_frame = agora

        if self.frame_atual < len(self.frames):
            tela.blit(self.frames[self.frame_atual], self.posicao)

    def finalizado(self):
        return pygame.time.get_ticks() - self.inicio >= self.duracao

def adicionar_efeito(frames, posicao, velocidade=95, duracao=2600,ao_terminar=None):
    efeitos_ativos.append(GifAtivo(frames, posicao, velocidade, duracao, ao_terminar))

def atualizar_efeitos(tela):
    for gif in efeitos_ativos[:]:
        gif.desenhar(tela)
        if gif.finalizado():
            if gif.ao_terminar:
                gif.ao_terminar()
            efeitos_ativos.remove(gif)

class MensagemPassageira:
    def __init__(self, mensagem, cor, fonte, posicao, duracao=350, deslocamento=50):
        self.mensagem = mensagem
        self.cor = cor
        self.fonte = fonte
        self.posicao_inicial = posicao
        self.duracao = duracao
        self.deslocamento = deslocamento
        self.frame_atual = 0
        self.ativa = True

    def atualizar(self):
        self.frame_atual += 1
        if self.frame_atual >= self.duracao:
            self.ativa = False

    def desenhar(self, tela):
        if not self.ativa:
            return

        alpha = max(0, 255 - int((self.frame_atual / self.duracao) * 255))
        y_offset = int((self.frame_atual / self.duracao) * self.deslocamento)

        texto_surface = self.fonte.render(self.mensagem, True, self.cor)
        texto_surface = texto_surface.convert_alpha()
        texto_surface.set_alpha(alpha)

        x, y = self.posicao_inicial
        x_texto = x
        y_texto = y - y_offset

        largura = texto_surface.get_width() + 20
        altura = texto_surface.get_height() + 10

        # Cria a superfície com canal alpha
        fundo = pygame.Surface((largura, altura), pygame.SRCALPHA)
        
        # Cor branca com transparência proporcional
        cor_fundo = (255, 255, 255, min(200, alpha))  # branco semi-transparente

        # Desenha retângulo arredondado
        pygame.draw.rect(fundo, cor_fundo, fundo.get_rect(), border_radius=10)

        # Posiciona retângulo levemente centralizado em relação ao texto
        tela.blit(fundo, (x_texto - 10, y_texto - 5))
        tela.blit(texto_surface, (x_texto, y_texto))

def adicionar_mensagem_passageira(mensagens, texto, cor, fonte, posicao, duracao=200, deslocamento=90):
    nova_mensagem = MensagemPassageira(texto, cor, fonte, posicao, duracao, deslocamento)
    mensagens_passageiras.append(nova_mensagem)

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

    player.ouro += 2 + (tempo_restante // 20)
    GV.limpa_terminal()
    M.Inverter_Tabuleiro(player, inimigo)

    for pokemon in player.pokemons:
        if pokemon.guardado != 0 and pokemon.guardado < 3:
            pokemon.guardado += 1

    player, inimigo = inimigo, player

    for pokemon in player.pokemons:
        if pokemon.local is not None:
            pokemon.Ganhar_XP(1,player)

    Centro = G.spawn_do_centro(Centro)
    Centro = G.spawn_do_centro(Centro)
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

def seleciona(ID, player, inimigo,):
    global PokemonS
    index_map = {
        "Pokemon1": 0,
        "Pokemon2": 1,
        "Pokemon3": 2,
        "Pokemon4": 3,
        "Pokemon5": 4,
        "Pokemon6": 5,
        "inimigo1": 0,
        "inimigo2": 1,
        "inimigo3": 2,
        "inimigo4": 3,
        "inimigo5": 4,
        "inimigo6": 5
    }
    idx = index_map[ID]
    if idx < len(player.pokemons):
        if ID in ["Pokemon1","Pokemon2","Pokemon3","Pokemon4","Pokemon5","Pokemon6"]:
            if player.pokemons[idx].Vida > 0:
                PokemonS = player.pokemons[idx] 
                global S1, S2, animaS
                global AT1, AT2, animaA
                global OP1, OP2, animaOP
                S1 = 1920
                S2 = 1560
                AT1 = -60
                AT2 = 210
                OP1 = 1080
                OP2 = 980
                animaS = pygame.time.get_ticks()
                animaA = pygame.time.get_ticks()
                animaOP = pygame.time.get_ticks()
            else:
                PokemonS = None
                GV.adicionar_mensagem("Esse Pokémon não pode ser selecionado.")
        else:
            PokemonS = None
            GV.adicionar_mensagem("Esse Pokémon não pode ser selecionado.")
    else:
        PokemonS = None
        GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")

def desseleciona():
    global PokemonS
    global estadoPokemon
    global estadoInfo
    global S1, S2, animaS
    global AT1, AT2, animaA
    global OP1, OP2, animaOP
    if PokemonS is not None:
        S1 = 1560
        S2 = 1920
        AT1 = 210
        AT2 = -60
        OP1 = 980
        OP2 = 1080
        animaS = pygame.time.get_ticks()
        animaA = pygame.time.get_ticks()
        animaOP = pygame.time.get_ticks()
        PokemonS = None
    estadoPokemon["selecionado_esquerdo"] = False
    estadoInfo["inicio_animacao"] = None

def vizualiza(ID,player,inimigo,):
    global PokemonV
    global V1, V2, animaV
    index_map = {
        "Pokemon1": 0,
        "Pokemon2": 1,
        "Pokemon3": 2,
        "Pokemon4": 3,
        "Pokemon5": 4,
        "Pokemon6": 5,
        "inimigo1": 0,
        "inimigo2": 1,
        "inimigo3": 2,
        "inimigo4": 3,
        "inimigo5": 4,
        "inimigo6": 5
    }
    if ID in ["Pokemon1","Pokemon2","Pokemon3","Pokemon4","Pokemon5","Pokemon6"]:
        idx = index_map[ID]
        if idx < len(player.pokemons):
                PokemonV = player.pokemons[idx]
                V1 = 1920
                V2 = 1560
                animaV = pygame.time.get_ticks()
        else:
            PokemonV = None
            GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")      
    else:
        idx = index_map[ID]
        if idx < len(inimigo.pokemons):
                PokemonV = inimigo.pokemons[idx]
                V1 = 1920
                V2 = 1560
                animaV = pygame.time.get_ticks()
        else:
            PokemonV = None
            GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")     

def oculta():
    global PokemonV
    global estadoInfo
    global V1, V2, animaV
    if PokemonV is not None:
        V1 = 1560
        V2 = 1920
        animaV = pygame.time.get_ticks()
        PokemonV = None
    estadoInfo["selecionado_direito"] = False
    estadoPokemon["selecionado_direito"] = False

A1 = -382
A2 = -382
A3 = -382
A4 = -382
A5 = -400
A6 = -400

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
    
def Fecha():
    global A1, A2, animaAI
    global A3, A4, animaAE
    global A5, A6, animaAC
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
    estadoOutros["selecionado_esquerdo"] =  False

def seleciona_pokebola(pokebola):
    global PokebolaSelecionada
    PokebolaSelecionada = pokebola

def desseleciona_pokebola():
    global PokebolaSelecionada
    PokebolaSelecionada = None

def seleciona_fruta(fruta):
    global FrutaSelecionada
    FrutaSelecionada = fruta

def desseleciona_fruta():
    global FrutaSelecionada
    FrutaSelecionada = None

def fechar_tudo():
    global estadoPokemon
    global estadoInfo
    global estadoOutros
    global estadoPokebola
    global estadoItens
    global estadoFruta
    global S1, S2, V1, V2,AT1,AT2,T1,T2,OP1,OP2,A1, A2, A3, A4, A5, A6 

    estadoPokemon = {
        "selecionado_esquerdo": None,
        "selecionado_direito": None}
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

def PokemonCentro(ID,player):
    global Centro
    global estadoOutros

    AIV = 1
    pokemon = Centro[ID]
    
    if PokebolaSelecionada is not None:
        player.inventario.remove(PokebolaSelecionada)
        Pokebola_usada = PokebolaSelecionada
        desseleciona_pokebola()
        maestria = random.randint(0,Pokebola_usada["poder"] * 2)
        if FrutaSelecionada is not None:
            player.inventario.remove(FrutaSelecionada)
            if FrutaSelecionada["nome"] in ["Fruta Frambo","Fruta Frambo Dourada"]:
                pokemon["dificuldade"] -= FrutaSelecionada["poder"]
                AIV = 1
            elif FrutaSelecionada["nome"] in ["Fruta Caxi","Fruta Caxi Prateada"]:
                AIV = FrutaSelecionada["poder"]
            desseleciona_fruta()
        if maestria >= pokemon["dificuldade"]:
            if len(player.pokemons) < 6:
                novo_pokemon = G.Gerador_final(pokemon["code"],AIV,player)
                AddIMGpokemon(novo_pokemon) 
                M.GuardarPosicionar(novo_pokemon,player)
                GV.adicionar_mensagem(f"Parabens! Capturou um {novo_pokemon.nome} usando uma {Pokebola_usada['nome']}")
                VerificaGIF()
                GV.tocar(Bom)
                Centro.remove(pokemon)
                return
            else:
                GV.tocar(Bloq)
                GV.adicionar_mensagem("sua lista de pokemon está cheia")
        else:
            GV.tocar(Bloq)
            GV.adicionar_mensagem("Voce falhou em capturar o pokemon, que pena")
        estadoPokebola["selecionado_esquerdo"] =  False
    else:
        GV.tocar(Bloq)
        GV.adicionar_mensagem("Selecione uma pokebola para capturar um pokemon")

def barra_vida(tela, x, y, largura, altura, vida_atual, vida_maxima, cor_fundo, id_pokemon):
    if not hasattr(barra_vida, "vidas_animadas"):
        barra_vida.vidas_animadas = {}

    # Pega a vida anterior ou inicializa
    vida_animada = barra_vida.vidas_animadas.get(id_pokemon, vida_atual)

    # Animação suave
    velocidade = 1.5
    if abs(vida_animada - vida_atual) < velocidade:
        vida_animada = vida_atual
    else:
        if vida_animada < vida_atual:
            vida_animada = min(vida_animada + velocidade, vida_atual)
        elif vida_animada > vida_atual:
            vida_animada = max(vida_animada - velocidade, vida_atual)

    # Garante que a vida animada não ultrapasse a vida máxima
    vida_animada = min(vida_animada, vida_maxima)

    barra_vida.vidas_animadas[id_pokemon] = vida_animada  # Salva valor atualizado

    proporcao = vida_animada / vida_maxima
    largura_vida = min(int(largura * proporcao), largura)  # Garante que a largura não ultrapasse o máximo

    if proporcao > 0.6:
        cor_vida = (0, 200, 0)
    elif proporcao > 0.3:
        cor_vida = (255, 200, 0)
    else:
        cor_vida = (200, 0, 0)

    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
    pygame.draw.rect(tela, cor_vida, (x, y, largura_vida, altura))
    pygame.draw.rect(tela, (0, 0, 0), (x, y, largura, altura), 2)

    if vida_animada <= 0:
        img = OutrosIMG[8]
        img_rect = img.get_rect()
        img_x = x + (largura - img_rect.width) // 2
        img_y = y - img_rect.height + 12
        tela.blit(img, (img_x, img_y))

def atacaN(Pokemon,player,inimigo,ID,tela):
    alvo = inimigo.pokemons[ID]
    if Pokemon is not None and alvo.Vida >= 0:
        Pokemon.atacar(alvo,player,inimigo,"N",tela,Mapa)
    else:
        GV.tocar(Bloq)
        GV.adicionar_mensagem("pokemons nocauteados não podem atacar")

def atacaS(Pokemon,player,inimigo,ID,tela):
    alvo = inimigo.pokemons[ID]
    if Pokemon is not None and alvo.Vida >= 0:
        Pokemon.atacar(alvo,player,inimigo,"E",tela,Mapa)
    else:
        GV.tocar(Bloq)
        GV.adicionar_mensagem("pokemons nocauteados não podem atacar")

def pausarEdespausar():
    global Pausa
    if Pausa == True:
        pausaEdespausaCronometro()
        Pausa = False
    else:
        Pausa = True
        pausaEdespausaCronometro()

def AddIMGpokemon(pokemon):
    imagem = ImagensPokemon38[pokemon.nome]
    pokemon.imagem = imagem
    # para tabuleiro

def AddLocalPokemonINIC(pokemon,jogador):
    if jogador == Jogador1:
        M.Move(pokemon,11,12,player)
    else:
        M.Move(pokemon,3,12,player)

def VerificaGIF():
    global Gifs_ativos

        # Ao capturar um novo Pokémon (exemplo)
    for i in range(len(player.pokemons)):
        nome = player.pokemons[i].nome

        # Verifica se o Pokémon ainda não foi adicionado
        if nome not in [gif["nome"] for gif in Gifs_ativos]:
            Gifs_ativos.append({
                "nome": nome,
                "frames": PokeGifs[nome],
                "frame_atual": 0,
                "tempo_anterior": pygame.time.get_ticks(),
                "intervalo": 25  # Pode ser ajustado para cada Pokémon se necessário
            })
    for i in range(len(inimigo.pokemons)):
        nome = inimigo.pokemons[i].nome

        # Verifica se o Pokémon ainda não foi adicionado
        if nome not in [gif["nome"] for gif in Gifs_ativos]:
            Gifs_ativos.append({
                "nome": nome,
                "frames": PokeGifs[nome],
                "frame_atual": 0,
                "tempo_anterior": pygame.time.get_ticks(),
                "intervalo": 25  # Pode ser ajustado para cada Pokémon se necessário
            })

def Muter():
    global Mute

    if Mute is False:
        pygame.mixer.music.set_volume(0.0)
        Mute = True
    else:
        pygame.mixer.music.set_volume(0.3)
        Mute = False

def Mudar_estadio(i):
    global Mapa
    Mapa = G.Gera_Mapa(i)

def tocar_musica_do_estadio():
    global Musica_Estadio_atual

    if Mapa.Musica != Musica_Estadio_atual:
        Z = Mapa.Musica 
        # Trocar a música
        pygame.mixer.music.stop()
        
        if Mapa.Musica == 0:
            pygame.mixer.music.load("Jogo/Audio/Musicas/Partida.ogg")
        elif Mapa.Musica == 1:
            pygame.mixer.music.load("Jogo/Audio/Musicas/Mer.ogg")
        elif Mapa.Musica == 2:
            pygame.mixer.music.load("Jogo/Audio/Musicas/Shivre.ogg")
        elif Mapa.Musica == 3:
            pygame.mixer.music.load("Jogo/Audio/Musicas/Auroma.ogg")
        elif Mapa.Musica == 4:
            pygame.mixer.music.load("Jogo/Audio/Musicas/Kalos.ogg")
        elif Mapa.Musica == 5:
            pygame.mixer.music.load("Jogo/Audio/Musicas/Skyloft.ogg")
        elif Mapa.Musica == 6:
            pygame.mixer.music.load("Jogo/Audio/Musicas/Molgera.ogg")

        pygame.mixer.music.play(-1)  # -1 = loop infinito
        Musica_Estadio_atual = Z

def Centroo(tela, x_inicial, y_inicial, Centro, player, Fonte50, Fonte28, B6, estadoPokebola, estadoFruta, eventos, x_final=None, anima=None, tempo=200):
    # Tamanhos fixos e corretos
    tamanho_pokemon = 100
    tamanho_pokebola = 60
    tamanho_fruta = 50

    largura_total = 360
    altura_total = 360

    # Animação deslizante
    if x_final is not None:
        if anima is None:
            anima = pygame.time.get_ticks()
        tempo_passado = pygame.time.get_ticks() - anima
        progresso = min(tempo_passado / tempo, 1.0)
        x_inicial_animado = int(x_inicial + (x_final - x_inicial) * progresso)
    else:
        x_inicial_animado = x_inicial

    # Retângulo de fundo da área principal
    ret = pygame.Rect(x_inicial_animado, y_inicial, largura_total, altura_total)
    pygame.draw.rect(tela, (30, 30, 30), ret)
    pygame.draw.rect(tela, (255, 255, 255), ret, 3)

    # --- Grade 3x3 de Pokémon ---
    for i in range(len(Centro)):
        coluna = i % 3
        linha = i // 3
        x = x_inicial_animado + coluna * tamanho_pokemon
        y = y_inicial + 10 + linha * tamanho_pokemon  # 10px de título

        GV.Botao(
            tela, "", (x, y, tamanho_pokemon, tamanho_pokemon), CINZA, PRETO, AZUL,
            lambda i=i: PokemonCentro(i, player),
            Fonte50, B6, 2, None, True, eventos
        )
    # precisa de for diferentes pois centro perde um pokemon no botao acima
    for i in range(len(Centro)):
        coluna = i % 3        
        linha = i // 3        
        x = x_inicial_animado + coluna * 99
        y = y_inicial + linha * 99
        tela.blit(ImagensPokemon100[Centro[i]["nome"]], (x, y))

    # --- Pokébolas (lado direito) ---
    idx_pokebola = 0
    for i, item in enumerate(player.inventario):
        if item.get("classe") == "pokebola":
            x = x_inicial_animado + 300  # Começam logo ao lado da grade
            y = y_inicial + idx_pokebola * tamanho_pokebola  # Já está alinhado com o topo da área

            GV.Botao_Selecao(
                tela, (x, y, tamanho_pokebola, tamanho_pokebola),
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

            tela.blit(ImagensPokebolas[item["nome"]], (x + 2, y + 2))
            idx_pokebola += 1

    # --- Frutas (parte inferior, 6 espaços) ---
    idx_fruta = 0
    for i, item in enumerate(player.inventario):
        if item.get("classe") == "Fruta":
            x = x_inicial_animado + idx_fruta * tamanho_fruta
            y = y_inicial + 310  # 10 (título) + 300 (grade)

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

            # Desenha imagem da fruta (centralizada com leve padding)
            if item["nome"] in ImagensPokebolas:
                tela.blit(ImagensPokebolas[item["nome"]], (x + 2, y + 2))

            idx_fruta += 1

def Troca_Terminal():
    global animaT, T1, T2
    if T2 == 800:
        T1 = 800
        T2 = 1030
        animaT = pygame.time.get_ticks()
    else:
        T1 = 1030
        T2 = 800
        animaT = pygame.time.get_ticks()

def Passar_contadores():
    for pokemon in player.pokemons:
        if pokemon.efeitoNega["envenenado"] > 0:
            pokemon.atacado(10,player,"O",Tela)
        if pokemon.efeitoNega["intoxicado"] > 0:
            pokemon.atacado(20,player,"O",Tela)
            pokemon.velocidade -= 1
        if pokemon.efeitoNega["queimado"] > 0:
            pokemon.atacado(15,player,"O",Tela)
                

        for efeito, contador in pokemon.efeitosNega.items():
            if contador > 0:
                pokemon.efeitosNega[efeito] -= 1
        for efeito, contador in pokemon.efeitosPosi.items():
            if contador > 0:
                pokemon.efeitosPosi[efeito] -= 1    

estadoPokemon = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}
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
estadoEnergias = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}
estadoFruta = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}
estadoMostraAtaqueS = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
    }
estadoMostraAtaqueV = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
    }

animaS = 0
animaAI = 0
animaAE = 0
animaAC = 0
animaV = 0
animaA = 0
animaT = 0
animaOP = 0

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
            TelaPokemons(tela,eventos,estados)
            TelaOpções(tela,eventos,estados)
            TelaOutros(tela,eventos,estados)

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


        if FrutaSelecionada is not None:
            print(FrutaSelecionada)
            

        pygame.display.update()
        relogio.tick(175)

def Inicia(tela):
    global Turno
    global ImagensPokemon100
    global PokeGifs
    global ImagensPokebolas
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

    Carregar = GV.Carregar_Imagem("imagens/fundos/carregando.jpg",(1920,1080))

    tela.blit(Carregar,(0,0))
    fonte = pygame.font.SysFont(None, 70)
    texto = fonte.render("Carregando ...", True, PRETO)
    tela.blit(texto, (tela.get_width() // 2 - 200, tela.get_height() // 2))
    pygame.display.update()

    pygame.mixer.music.load('Jogo/Audio/Musicas/Carregamento.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    Tela = tela
    Mapa = G.Gera_Mapa(0)

    fechar_tudo()

    GV.limpa_terminal()

    Musica_Estadio_atual = 0
    LojaItensP = Mapa.PlojaI
    LojaPokeP = Mapa.PlojaP
    LojaAmpliP = Mapa.PlojaA
    LojaEnerP = Mapa.PlojaE
    LojaEstTreP = Mapa.pLojaT

    Carregar_Imagens()
    M.Gerar_Mapa()

    from PygameAções import informaçoesp1, informaçoesp2
    Jogador1 = G.Gerador_player(informaçoesp1)
    Jogador2 = G.Gerador_player(informaçoesp2)

    Jogador1.pokemons[0].pos = 0
    Jogador2.pokemons[0].pos = 0

    for item in informaçoesp1[3:]:
        G.gera_item(item, Jogador1)
    for item in informaçoesp2[3:]:
        G.gera_item(item, Jogador2)

    for i in range(10):
        G.gera_item("energia", Jogador1)
        G.gera_item("energia", Jogador2)

    AddIMGpokemon(Jogador1.pokemons[0])
    AddIMGpokemon(Jogador2.pokemons[0])
    AddLocalPokemonINIC(Jogador2.pokemons[0],Jogador2)
    AddLocalPokemonINIC(Jogador1.pokemons[0],Jogador1)

    player = Jogador1
    inimigo = Jogador2

    VerificaGIF()

    pygame.mixer.music.load('Jogo/Audio/Musicas/Partida.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    Pausa = False
    Turno = 1
    Centro = []

    Resetar_Cronometro()
    cronometro.inicio = pygame.time.get_ticks()
    cronometro.tempo_encerrado = False

def Carregar_Imagens():
    global ImagensPokemon38
    global ImagensPokemon100
    global PokeGifs
    global ImagensPokebolas
    global ImagensItens
    global OutrosIMG
    global FundosIMG
    global TiposEnergiaIMG

    Fundo = GV.Carregar_Imagem("imagens/fundos/fundo3.jpg", (1920,1080))
    MerFundo = GV.Carregar_Imagem("imagens/fundos/Mer.jpg", (1920, 1080))
    ShivreFundo = GV.Carregar_Imagem("imagens/fundos/Shivre.png", (1920, 1080))
    KalosFundo = GV.Carregar_Imagem("imagens/fundos/Kalos.jpg", (1920, 1080))
    PortoFundo = GV.Carregar_Imagem("imagens/fundos/Porto.jpg", (1920, 1080))
    SkyloftFundo = GV.Carregar_Imagem("imagens/fundos/Skyloft.jpg", (1920, 1080))
    AuromaFundo = GV.Carregar_Imagem("imagens/fundos/Auroma.jpg", (1920, 1080))

    Gbulbasaur = GV.carregar_frames('imagens/gifs/bulbasaur_frames')
    Givysaur = GV.carregar_frames('imagens/gifs/ivysaur_frames')
    Gvenusaur = GV.carregar_frames('imagens/gifs/venusaur_frames')
    Gcharmander = GV.carregar_frames('imagens/gifs/charmander_frames')
    Gcharmeleon = GV.carregar_frames('imagens/gifs/charmeleon_frames')
    Gcharizard = GV.carregar_frames('imagens/gifs/charizard_frames')
    Gsquirtle = GV.carregar_frames('imagens/gifs/squirtle_frames')
    Gwartortle = GV.carregar_frames('imagens/gifs/wartortle_frames')
    Gblastoise = GV.carregar_frames('imagens/gifs/blastoise_frames')
    Gmachop = GV.carregar_frames('imagens/gifs/machop_frames')
    Gmachoke = GV.carregar_frames('imagens/gifs/machoke_frames')
    Gmachamp = GV.carregar_frames('imagens/gifs/machamp_frames')
    Ggastly = GV.carregar_frames('imagens/gifs/gastly_frames')
    Ghaunter = GV.carregar_frames('imagens/gifs/haunter_frames')
    Ggengar = GV.carregar_frames('imagens/gifs/gengar_frames')
    Ggeodude = GV.carregar_frames('imagens/gifs/geodude_frames')
    Ggraveler = GV.carregar_frames('imagens/gifs/graveler_frames')
    Ggolem = GV.carregar_frames('imagens/gifs/golem_frames')
    Gcaterpie = GV.carregar_frames('imagens/gifs/caterpie_frames')
    Gmetapod = GV.carregar_frames('imagens/gifs/metapod_frames')
    Gbutterfree = GV.carregar_frames('imagens/gifs/butterfree_frames')
    Gabra = GV.carregar_frames('imagens/gifs/abra_frames')
    Gkadabra = GV.carregar_frames('imagens/gifs/kadabra_frames')
    Galakazam = GV.carregar_frames('imagens/gifs/alakazam_frames')
    Gdratini = GV.carregar_frames('imagens/gifs/dratini_frames')
    Gdragonair = GV.carregar_frames('imagens/gifs/dragonair_frames')
    Gdragonite = GV.carregar_frames('imagens/gifs/dragonite_frames')
    Gzorua = GV.carregar_frames('imagens/gifs/zorua_frames')
    Gzoroark = GV.carregar_frames('imagens/gifs/zoroark_frames')
    Gpikachu = GV.carregar_frames('imagens/gifs/pikachu_frames')
    Graichu = GV.carregar_frames('imagens/gifs/raichu_frames')
    Gmagikarp = GV.carregar_frames('imagens/gifs/magikarp_frames')
    Ggyarados = GV.carregar_frames('imagens/gifs/gyarados_frames')
    Gjigglypuff = GV.carregar_frames('imagens/gifs/jigglypuff_frames')
    Gwigglytuff = GV.carregar_frames('imagens/gifs/wigglytuff_frames')
    Gmagnemite = GV.carregar_frames('imagens/gifs/magnemite_frames')
    Gmagneton = GV.carregar_frames('imagens/gifs/magneton_frames')
    Gsnorlax = GV.carregar_frames('imagens/gifs/snorlax_frames')
    Gaerodactyl = GV.carregar_frames('imagens/gifs/aerodactyl_frames')
    Gjynx = GV.carregar_frames('imagens/gifs/jynx_frames')
    Gmewtwo = GV.carregar_frames('imagens/gifs/mewtwo_frames')
    Gmewtwo = GV.carregar_frames('imagens/gifs/mewtwo_frames')
    Gaerodactyl_mega = GV.carregar_frames('imagens/gifs/aerodactyl-mega_frames')
    Galakazam_mega = GV.carregar_frames('imagens/gifs/alakazam-mega_frames')
    Garticuno = GV.carregar_frames('imagens/gifs/articuno_frames')
    Gbeedrill = GV.carregar_frames('imagens/gifs/beedrill_frames')
    Gbeedrill_mega = GV.carregar_frames('imagens/gifs/beedrill-mega_frames')
    Gblastoise_gigantamax = GV.carregar_frames('imagens/gifs/blastoise-gigantamax_frames')
    Gblastoise_mega = GV.carregar_frames('imagens/gifs/blastoise-mega_frames')
    Gbutterfree_gmax = GV.carregar_frames('imagens/gifs/butterfree-gigantamax_frames')
    Gcharizard_gmax = GV.carregar_frames('imagens/gifs/charizard-gigantamax_frames')
    Gcharizard_megax = GV.carregar_frames('imagens/gifs/charizard-megax_frames')
    Gcharizard_megay = GV.carregar_frames('imagens/gifs/charizard-megay_frames')
    Gclefable = GV.carregar_frames('imagens/gifs/clefable_frames')
    Gclefairy = GV.carregar_frames('imagens/gifs/clefairy_frames')
    Gcloyster = GV.carregar_frames('imagens/gifs/cloyster_frames')
    Gcubone = GV.carregar_frames('imagens/gifs/cubone_frames')
    Ggengar_gigantamax = GV.carregar_frames('imagens/gifs/gengar-gigantamax_frames')
    Ggengar_mega = GV.carregar_frames('imagens/gifs/gengar-mega_frames')
    Ggolem_alola = GV.carregar_frames('imagens/gifs/golem-mega_frames')
    Ggyarados_mega = GV.carregar_frames('imagens/gifs/gyarados-mega_frames')
    Gweedle = GV.carregar_frames('imagens/gifs/weedle_frames')
    Gkakuna = GV.carregar_frames('imagens/gifs/kakuna_frames')
    Gmachamp_gigantamax = GV.carregar_frames('imagens/gifs/machamp-gigantamax_frames')
    Gmarowak = GV.carregar_frames('imagens/gifs/marowak_frames')
    Gmeowth = GV.carregar_frames('imagens/gifs/meowth_frames')
    Gmeowth_gigantamax = GV.carregar_frames('imagens/gifs/meowth-gigantamax_frames')
    Gmewtwo_megax = GV.carregar_frames('imagens/gifs/mewtwo-megax_frames')
    Gmewtwo_megay = GV.carregar_frames('imagens/gifs/mewtwo-megay_frames')
    Gmoltres = GV.carregar_frames('imagens/gifs/moltres_frames')
    Gzapdos = GV.carregar_frames('imagens/gifs/zapdos_frames')
    Gpersian = GV.carregar_frames('imagens/gifs/persian_frames')
    Gpikachu_gigantamax = GV.carregar_frames('imagens/gifs/pikachu-gigantamax_frames')
    Gpinsir = GV.carregar_frames('imagens/gifs/pinsir_frames')
    Gpinsir_mega = GV.carregar_frames('imagens/gifs/pinsir-mega_frames')
    Graticate = GV.carregar_frames('imagens/gifs/raticate_frames')
    Grattata = GV.carregar_frames('imagens/gifs/rattata_frames')
    Gshellder = GV.carregar_frames('imagens/gifs/shellder_frames')
    Gsnorlax_gigantamax = GV.carregar_frames('imagens/gifs/snorlax-gigantamax_frames')
    Gvenusaur_gigantamax = GV.carregar_frames('imagens/gifs/venusaur-gigantamax_frames')

    SbulbasaurIMG = GV.Carregar_Imagem("imagens/pokeicons/bulbasaur.png", (38,38),"PNG")
    SivysaurIMG = GV.Carregar_Imagem("imagens/pokeicons/ivysaur.png", (38,38),"PNG")
    SvenusaurIMG = GV.Carregar_Imagem("imagens/pokeicons/venusaur.png", (38,38),"PNG")
    ScharmanderIMG = GV.Carregar_Imagem("imagens/pokeicons/charmander.png", (38,38),"PNG")
    ScharmeleonIMG = GV.Carregar_Imagem("imagens/pokeicons/charmeleon.png", (38,38),"PNG")
    ScharizardIMG = GV.Carregar_Imagem("imagens/pokeicons/charizard.png", (38,38),"PNG")
    SsquirtleIMG = GV.Carregar_Imagem("imagens/pokeicons/squirtle.png", (38,38),"PNG")
    SwartortleIMG = GV.Carregar_Imagem("imagens/pokeicons/wartortle.png", (38,38),"PNG")
    SblastoiseIMG = GV.Carregar_Imagem("imagens/pokeicons/blastoise.png", (38,38),"PNG")
    SmachopIMG = GV.Carregar_Imagem("imagens/pokeicons/machop.png", (38,38),"PNG")
    SmachokeIMG = GV.Carregar_Imagem("imagens/pokeicons/machoke.png", (38,38),"PNG")
    SmachampIMG = GV.Carregar_Imagem("imagens/pokeicons/machamp.png", (38,38),"PNG")
    SgastlyIMG = GV.Carregar_Imagem("imagens/pokeicons/gastly.png", (38,38),"PNG")
    ShaunterIMG = GV.Carregar_Imagem("imagens/pokeicons/haunter.png", (38,38),"PNG")
    SgengarIMG = GV.Carregar_Imagem("imagens/pokeicons/gengar.png", (38,38),"PNG")
    SgeodudeIMG = GV.Carregar_Imagem("imagens/pokeicons/geodude.png", (38,38),"PNG")
    SgravelerIMG = GV.Carregar_Imagem("imagens/pokeicons/graveler.png", (38,38),"PNG")
    SgolemIMG = GV.Carregar_Imagem("imagens/pokeicons/golem.png", (38,38),"PNG")
    ScaterpieIMG = GV.Carregar_Imagem("imagens/pokeicons/caterpie.png", (38,38),"PNG")
    SmetapodIMG = GV.Carregar_Imagem("imagens/pokeicons/metapod.png", (38,38),"PNG")
    SbutterfreeIMG = GV.Carregar_Imagem("imagens/pokeicons/butterfree.png", (38,38),"PNG")
    SabraIMG = GV.Carregar_Imagem("imagens/pokeicons/abra.png", (38,38),"PNG")
    SkadabraIMG = GV.Carregar_Imagem("imagens/pokeicons/kadabra.png", (38,38),"PNG")
    SalakazamIMG = GV.Carregar_Imagem("imagens/pokeicons/alakazam.png", (38,38),"PNG")
    SdratiniIMG = GV.Carregar_Imagem("imagens/pokeicons/dratini.png", (38,38),"PNG")
    SdragonairIMG = GV.Carregar_Imagem("imagens/pokeicons/dragonair.png", (38,38),"PNG")
    SdragoniteIMG = GV.Carregar_Imagem("imagens/pokeicons/dragonite.png", (38,38),"PNG")
    SzoruaIMG = GV.Carregar_Imagem("imagens/pokeicons/zorua.png", (38,38),"PNG")
    SzoroarkIMG = GV.Carregar_Imagem("imagens/pokeicons/zoroark.png", (38,38),"PNG")
    SpikachuIMG = GV.Carregar_Imagem("imagens/pokeicons/pikachu.png", (38,38),"PNG")
    SraichuIMG = GV.Carregar_Imagem("imagens/pokeicons/raichu.png", (38,38),"PNG")
    SmagikarpIMG = GV.Carregar_Imagem("imagens/pokeicons/magikarp.png", (38,38),"PNG")
    SgyaradosIMG = GV.Carregar_Imagem("imagens/pokeicons/gyarados.png", (38,38),"PNG")
    SjigglypuffIMG = GV.Carregar_Imagem("imagens/pokeicons/jigglypuff.png", (38,38),"PNG")
    SwigglytuffIMG = GV.Carregar_Imagem("imagens/pokeicons/wigglytuff.png", (38,38),"PNG")
    SmagnemiteIMG = GV.Carregar_Imagem("imagens/pokeicons/magnemite.png", (38,38),"PNG")
    SmagnetonIMG = GV.Carregar_Imagem("imagens/pokeicons/magneton.png", (38,38),"PNG")
    SsnorlaxIMG = GV.Carregar_Imagem("imagens/pokeicons/snorlax.png", (38,38),"PNG")
    SaerodactylIMG = GV.Carregar_Imagem("imagens/pokeicons/aerodactyl.png", (38,38),"PNG")
    SjynxIMG = GV.Carregar_Imagem("imagens/pokeicons/jynx.png", (38,38),"PNG")
    SmewtwoIMG = GV.Carregar_Imagem("imagens/pokeicons/mewtwo.png", (38,38),"PNG")
    Saerodactyl_megaIMG = GV.Carregar_Imagem("imagens/pokeicons/aerodactyl-mega.png", (38, 38), "PNG")
    Salakazam_megaIMG = GV.Carregar_Imagem("imagens/pokeicons/alakazam-mega.png", (38, 38), "PNG")
    SarticunoIMG = GV.Carregar_Imagem("imagens/pokeicons/articuno.png", (38, 38), "PNG")
    SbeedrillIMG = GV.Carregar_Imagem("imagens/pokeicons/beedrill.png", (38, 38), "PNG")
    Sbeedrill_megaIMG = GV.Carregar_Imagem("imagens/pokeicons/beedrill-mega.png", (38, 38), "PNG")
    Sblastoise_gigantamaxIMG = GV.Carregar_Imagem("imagens/pokeicons/blastoise-gigantamax.png", (38, 38), "PNG")
    Sblastoise_megaIMG = GV.Carregar_Imagem("imagens/pokeicons/blastoise-mega.png", (38, 38), "PNG")
    Sbutterfree_gmaxIMG = GV.Carregar_Imagem("imagens/pokeicons/butterfree-gigantamax.png", (38, 38), "PNG")
    Scharizard_gmaxIMG = GV.Carregar_Imagem("imagens/pokeicons/charizard-gigantamax.png", (38, 38), "PNG")
    Scharizard_megaxIMG = GV.Carregar_Imagem("imagens/pokeicons/charizard-mega-x.png", (38, 38), "PNG")
    Scharizard_megayIMG = GV.Carregar_Imagem("imagens/pokeicons/charizard-mega-y.png", (38, 38), "PNG")
    SclefableIMG = GV.Carregar_Imagem("imagens/pokeicons/clefable.png", (38, 38), "PNG")
    SclefairyIMG = GV.Carregar_Imagem("imagens/pokeicons/clefairy.png", (38, 38), "PNG")
    ScloysterIMG = GV.Carregar_Imagem("imagens/pokeicons/cloyster.png", (38, 38), "PNG")
    ScuboneIMG = GV.Carregar_Imagem("imagens/pokeicons/cubone.png", (38, 38), "PNG")
    Sgengar_gigantamaxIMG = GV.Carregar_Imagem("imagens/pokeicons/gengar-gigantamax.png", (38, 38), "PNG")
    Sgengar_megaIMG = GV.Carregar_Imagem("imagens/pokeicons/gengar-mega.png", (38, 38), "PNG")
    Sgolem_megaIMG = GV.Carregar_Imagem("imagens/pokeicons/golem-mega.png", (38, 38), "PNG")
    Sgyarados_megaIMG = GV.Carregar_Imagem("imagens/pokeicons/gyarados-mega.png", (38, 38), "PNG")
    SkakunaIMG = GV.Carregar_Imagem("imagens/pokeicons/kakuna.png", (38, 38), "PNG")
    Smachamp_gigantamaxIMG = GV.Carregar_Imagem("imagens/pokeicons/machamp-gigantamax.png", (38, 38), "PNG")
    SmarowakIMG = GV.Carregar_Imagem("imagens/pokeicons/marowak.png", (38, 38), "PNG")
    SmeowthIMG = GV.Carregar_Imagem("imagens/pokeicons/meowth.png", (38, 38), "PNG")
    Smeowth_gigantamaxIMG = GV.Carregar_Imagem("imagens/pokeicons/meowth-gigantamax.png", (38, 38), "PNG")
    Smewtwo_megaxIMG = GV.Carregar_Imagem("imagens/pokeicons/mewtwo-mega-x.png", (38, 38), "PNG")
    Smewtwo_megayIMG = GV.Carregar_Imagem("imagens/pokeicons/mewtwo-mega-y.png", (38, 38), "PNG")
    SmoltresIMG = GV.Carregar_Imagem("imagens/pokeicons/moltres.png", (38, 38), "PNG")
    SpersianIMG = GV.Carregar_Imagem("imagens/pokeicons/persian.png", (38, 38), "PNG")
    Spikachu_gigantamaxIMG = GV.Carregar_Imagem("imagens/pokeicons/pikachu-gigantamax.png", (38, 38), "PNG")
    SpinsirIMG = GV.Carregar_Imagem("imagens/pokeicons/pinsir.png", (38, 38), "PNG")
    Spinsir_megaIMG = GV.Carregar_Imagem("imagens/pokeicons/pinsir-mega.png", (38, 38), "PNG")
    SraticateIMG = GV.Carregar_Imagem("imagens/pokeicons/raticate.png", (38, 38), "PNG")
    SrattataIMG = GV.Carregar_Imagem("imagens/pokeicons/rattata.png", (38, 38), "PNG")
    SshellderIMG = GV.Carregar_Imagem("imagens/pokeicons/shellder.png", (38, 38), "PNG")
    Ssnorlax_gigantamaxIMG = GV.Carregar_Imagem("imagens/pokeicons/snorlax-gigantamax.png", (38, 38), "PNG")
    Svenusaur_gigantamaxIMG = GV.Carregar_Imagem("imagens/pokeicons/venusaur-gigantamax.png", (38, 38), "PNG")
    SzapdosIMG = GV.Carregar_Imagem("imagens/pokeicons/zapdos.png", (38, 38), "PNG")
    SweedleIMG = GV.Carregar_Imagem("imagens/pokeicons/weedle.png", (38, 38), "PNG")




    MbulbasaurIMG = GV.Carregar_Imagem("imagens/pokemons/bulbasaur.png", (88, 88), "PNG")
    McharmanderIMG = GV.Carregar_Imagem("imagens/pokemons/charmander.png", (88, 88), "PNG")
    MsquirtleIMG = GV.Carregar_Imagem("imagens/pokemons/squirtle.png", (88, 88), "PNG")
    MmachopIMG = GV.Carregar_Imagem("imagens/pokemons/machop.png", (88, 88), "PNG")
    MgastlyIMG = GV.Carregar_Imagem("imagens/pokemons/gastly.png", (88, 88), "PNG")
    MgeodudeIMG = GV.Carregar_Imagem("imagens/pokemons/geodude.png", (88, 88), "PNG")
    McaterpieIMG = GV.Carregar_Imagem("imagens/pokemons/caterpie.png", (88, 88), "PNG")
    MabreIMG = GV.Carregar_Imagem("imagens/pokemons/abra.png", (88, 88), "PNG")
    MdratiniIMG = GV.Carregar_Imagem("imagens/pokemons/dratini.png", (88, 88), "PNG")
    MzoruaIMG = GV.Carregar_Imagem("imagens/pokemons/zorua.png", (88, 88), "PNG")
    MpikachuIMG = GV.Carregar_Imagem("imagens/pokemons/pikachu.png", (88, 88), "PNG")
    MmagikarpIMG = GV.Carregar_Imagem("imagens/pokemons/magikarp.png", (88, 88), "PNG")
    MjigglypuffIMG = GV.Carregar_Imagem("imagens/pokemons/jigglypuff.png", (88, 88), "PNG")
    MmagnemiteIMG = GV.Carregar_Imagem("imagens/pokemons/magnemite.png", (88, 88), "PNG")
    MsnorlaxIMG = GV.Carregar_Imagem("imagens/pokemons/snorlax.png", (88, 88), "PNG")
    MaerodactylIMG = GV.Carregar_Imagem("imagens/pokemons/aerodactyl.png", (88, 88), "PNG")
    MjynxIMG = GV.Carregar_Imagem("imagens/pokemons/jynx.png", (88, 88), "PNG")
    MmewtwoIMG = GV.Carregar_Imagem("imagens/pokemons/mewtwo.png", (88, 88), "PNG")
    MmeowthIMG = GV.Carregar_Imagem("imagens/pokemons/meowth.png", (88, 88), "PNG")
    McuboneIMG = GV.Carregar_Imagem("imagens/pokemons/cubone.png", (88, 88), "PNG")
    MshellderIMG = GV.Carregar_Imagem("imagens/pokemons/shellder.png", (88, 88), "PNG")
    MarticunoIMG = GV.Carregar_Imagem("imagens/pokemons/articuno.png", (88, 88), "PNG")
    MmoltresIMG = GV.Carregar_Imagem("imagens/pokemons/moltres.png", (88, 88), "PNG")
    MzapdosIMG = GV.Carregar_Imagem("imagens/pokemons/zapdos.png", (88, 88), "PNG")
    MclefairyIMG = GV.Carregar_Imagem("imagens/pokemons/clefairy.png", (88, 88), "PNG")
    MrattataIMG = GV.Carregar_Imagem("imagens/pokemons/rattata.png", (88, 88), "PNG")
    MweedleIMG = GV.Carregar_Imagem("imagens/pokemons/weedle.png", (88, 88), "PNG")
    MpinsirIMG = GV.Carregar_Imagem("imagens/pokemons/pinsir.png", (88, 88), "PNG")



    EsmeraldaIMG = GV.Carregar_Imagem("imagens/itens/esmeralda.png", (62, 62), "PNG")
    CitrinoIMG = GV.Carregar_Imagem("imagens/itens/citrino.png", (62, 62), "PNG")
    RubiIMG = GV.Carregar_Imagem("imagens/itens/rubi.png", (62, 62), "PNG")
    SafiraIMG = GV.Carregar_Imagem("imagens/itens/safira.png", (62, 62), "PNG")
    AmetistaIMG = GV.Carregar_Imagem("imagens/itens/ametista.png", (62, 62), "PNG")
    ColetorIMG = GV.Carregar_Imagem("imagens/itens/coletor.png", (62, 62), "PNG")
    CaixaIMG = GV.Carregar_Imagem("imagens/itens/caixa.png", (62, 62), "PNG")
    CaixoteIMG = GV.Carregar_Imagem("imagens/itens/caixote.png", (62, 62), "PNG")
    PocaoIMG = GV.Carregar_Imagem("imagens/itens/poçao.png", (62, 62), "PNG")
    SuperPocaoIMG = GV.Carregar_Imagem("imagens/itens/super_poçao.png", (62, 62), "PNG")
    HiperPocaoIMG = GV.Carregar_Imagem("imagens/itens/hiper_poçao.png", (62, 62), "PNG")
    MegaPocaoIMG = GV.Carregar_Imagem("imagens/itens/mega_poçao.png", (62, 62), "PNG")
    PokeballIMG = GV.Carregar_Imagem("imagens/itens/PokeBall.png", (62, 62), "PNG")
    GreatBallIMG = GV.Carregar_Imagem("imagens/itens/GreatBall.png", (62, 62), "PNG")
    UltraBallIMG = GV.Carregar_Imagem("imagens/itens/UltraBall.png", (62, 62), "PNG")
    MasterBallIMG = GV.Carregar_Imagem("imagens/itens/MasterBall.png", (62, 62), "PNG")
    FramboIMG = GV.Carregar_Imagem("imagens/itens/frambo.png", (62, 62), "PNG")
    FramboDouradaIMG = GV.Carregar_Imagem("imagens/itens/frambo_dourada.png", (62, 62), "PNG")
    CaxiIMG = GV.Carregar_Imagem("imagens/itens/caxi.png", (62, 62), "PNG")
    CaxiPrateadaIMG = GV.Carregar_Imagem("imagens/itens/caxi_prateada.png", (62, 62), "PNG")
    EstadioIMG = GV.Carregar_Imagem("imagens/itens/TP.png", (62, 62), "PNG")
    MegaIMG = GV.Carregar_Imagem("imagens/itens/mega.png", (62, 62), "PNG")
    VMaxIMG = GV.Carregar_Imagem("imagens/itens/Vstar.png", (62, 62), "PNG")
    VStarIMG = GV.Carregar_Imagem("imagens/itens/Vmax.png", (62, 62), "PNG")


    UPokeballIMG = GV.Carregar_Imagem("imagens/itens/PokeBall.png", (55,55),"PNG")
    UGreatBallIMG = GV.Carregar_Imagem("imagens/itens/GreatBall.png", (55,55),"PNG")
    UUltraBallIMG = GV.Carregar_Imagem("imagens/itens/UltraBall.png", (55,55),"PNG")
    UMasterBallIMG = GV.Carregar_Imagem("imagens/itens/MasterBall.png", (55,55),"PNG")
    UFramboIMG = GV.Carregar_Imagem("imagens/itens/frambo.png", (48, 48), "PNG")
    UFramboDouradaIMG = GV.Carregar_Imagem("imagens/itens/frambo_dourada.png", (48, 48), "PNG")
    UCaxiIMG = GV.Carregar_Imagem("imagens/itens/caxi.png", (48, 48), "PNG")
    UCaxiPrateadaIMG = GV.Carregar_Imagem("imagens/itens/caxi_prateada.png", (48, 48), "PNG")

    InventárioIMG = GV.Carregar_Imagem("imagens/icones/inventario.png", (60,60),"PNG")
    energiasIMG = GV.Carregar_Imagem("imagens/icones/energias.png", (50,50),"PNG")
    CentroIMG = GV.Carregar_Imagem("imagens/icones/centro.png", (70,70),"PNG")
    LojaPokebolasIMG = GV.Carregar_Imagem("imagens/icones/Poke.png", (70,70),"PNG")
    LojaItensIMG = GV.Carregar_Imagem("imagens/icones/itens.png", (70,70),"PNG")
    LojaAmplificadoresIMG = GV.Carregar_Imagem("imagens/icones/amplificadores.png", (70,70),"PNG")
    LojaEnergiasIMG = GV.Carregar_Imagem("imagens/icones/energias.png", (60,60),"PNG")
    LojaEstTreIMG = GV.Carregar_Imagem("imagens/icones/EstTre.png", (70,70),"PNG")
    LojaBloqIMG = GV.Carregar_Imagem("imagens/icones/cadeado.png", (68,68),"PNG")
    AtaqueIMG = GV.Carregar_Imagem("imagens/icones/atacar.png", (40,40),"PNG")
    NocauteIMG  = GV.Carregar_Imagem("imagens/icones/KO.png", (50,50),"PNG")
    GuardadoIMG = GV.Carregar_Imagem("imagens/icones/guardado.png", (40,40),"PNG") 

    Efogo = GV.Carregar_Imagem("imagens/icones/fogo.png", (30,30), "PNG")
    Eagua = GV.Carregar_Imagem("imagens/icones/agua.png", (30,30), "PNG")
    Eplanta = GV.Carregar_Imagem("imagens/icones/planta.png", (30,30), "PNG")
    Eeletrico = GV.Carregar_Imagem("imagens/icones/eletrico.png", (30,30), "PNG")
    Epsiquico = GV.Carregar_Imagem("imagens/icones/psiquico.png", (30,30), "PNG")
    Efantasma = GV.Carregar_Imagem("imagens/icones/fantasma.png", (30,30), "PNG")
    Epedra = GV.Carregar_Imagem("imagens/icones/pedra.png", (30,30), "PNG")
    Eterrestre = GV.Carregar_Imagem("imagens/icones/terrestre.png", (30,30), "PNG")
    Evoador = GV.Carregar_Imagem("imagens/icones/voador.png", (30,30), "PNG")
    Enormal = GV.Carregar_Imagem("imagens/icones/normal.png", (30,30), "PNG")
    Evenenoso = GV.Carregar_Imagem("imagens/icones/venenoso.png", (30,30), "PNG")
    Einseto = GV.Carregar_Imagem("imagens/icones/inseto.png", (30,30), "PNG")
    Elutador = GV.Carregar_Imagem("imagens/icones/lutador.png", (30,30), "PNG")
    Edragao = GV.Carregar_Imagem("imagens/icones/dragao.png", (30,30), "PNG")
    Egelo = GV.Carregar_Imagem("imagens/icones/gelo.png", (30,30), "PNG")
    Efada = GV.Carregar_Imagem("imagens/icones/fada.png", (30,30), "PNG")
    Emetal = GV.Carregar_Imagem("imagens/icones/metal.png", (30,30), "PNG")
    Esombrio = GV.Carregar_Imagem("imagens/icones/sombrio.png", (30,30), "PNG")

    TiposEnergiaIMG = {
    "fogo": Efogo,
    "agua": Eagua,
    "planta": Eplanta,
    "eletrico": Eeletrico,
    "psiquico": Epsiquico,
    "fantasma": Efantasma,
    "pedra": Epedra,
    "terrestre": Eterrestre,
    "voador": Evoador,
    "normal": Enormal,
    "venenoso": Evenenoso,
    "inseto": Einseto,
    "lutador": Elutador,
    "dragao": Edragao,
    "gelo": Egelo,
    "fada": Efada,
    "metal": Emetal,
    "sombrio": Esombrio
}

    PokeGifs = {
    "Bulbasaur": Gbulbasaur,
    "Ivysaur": Givysaur,
    "Venusaur": Gvenusaur,
    "Charmander": Gcharmander,
    "Charmeleon": Gcharmeleon,
    "Charizard": Gcharizard,
    "Squirtle": Gsquirtle,
    "Wartortle": Gwartortle,
    "Blastoise": Gblastoise,
    "Machop": Gmachop,
    "Machoke": Gmachoke,
    "Machamp": Gmachamp,
    "Gastly": Ggastly,
    "Haunter": Ghaunter,
    "Gengar": Ggengar,
    "Geodude": Ggeodude,
    "Graveler": Ggraveler,
    "Golem": Ggolem,
    "Caterpie": Gcaterpie,
    "Metapod": Gmetapod,
    "Butterfree": Gbutterfree,
    "Abra": Gabra,
    "Kadabra": Gkadabra,
    "Alakazam": Galakazam,
    "Dratini": Gdratini,
    "Dragonair": Gdragonair,
    "Dragonite": Gdragonite,
    "Zorua": Gzorua,
    "Zoroark": Gzoroark,
    "Pikachu": Gpikachu,
    "Raichu": Graichu,
    "Magikarp": Gmagikarp,
    "Gyarados": Ggyarados,
    "Jigglypuff": Gjigglypuff,
    "Wigglytuff": Gwigglytuff,
    "Magnemite": Gmagnemite,
    "Magneton": Gmagneton,
    "Snorlax": Gsnorlax,
    "Aerodactyl": Gaerodactyl,
    "Jynx": Gjynx,
    "Mewtwo": Gmewtwo,
    "Aerodactyl-Mega": Gaerodactyl_mega,
    "Alakazam-Mega": Galakazam_mega,
    "Articuno": Garticuno,
    "Beedrill": Gbeedrill,
    "Beedrill-Mega": Gbeedrill_mega,
    "Blastoise-Gigantamax": Gblastoise_gigantamax,
    "Blastoise-Mega": Gblastoise_mega,
    "Butterfree-gigantamax": Gbutterfree_gmax,
    "Charizard-gigantamax": Gcharizard_gmax,
    "Charizard-MegaX": Gcharizard_megax,
    "Charizard-MegaY": Gcharizard_megay,
    "Clefable": Gclefable,
    "Clefairy": Gclefairy,
    "Cloyster": Gcloyster,
    "Cubone": Gcubone,
    "Gengar-Gigantamax": Ggengar_gigantamax,
    "Gengar-Mega": Ggengar_mega,
    "Golem-Alola": Ggolem_alola,
    "Gyarados-Mega": Ggyarados_mega,
    "Kakuna": Gkakuna,
    "Machamp-Gigantamax": Gmachamp_gigantamax,
    "Marowak": Gmarowak,
    "Meowth": Gmeowth,
    "Meowth-Gigantamax": Gmeowth_gigantamax,
    "Mewtwo-MegaX": Gmewtwo_megax,
    "Mewtwo-MegaY": Gmewtwo_megay,
    "Moltres": Gmoltres,
    "Persian": Gpersian,
    "Pikachu-Gigantamax": Gpikachu_gigantamax,
    "Pinsir": Gpinsir,
    "Pinsir-Mega": Gpinsir_mega,
    "Raticate": Graticate,
    "Rattata": Grattata,
    "Shellder": Gshellder,
    "Snorlax-Gigantamax": Gsnorlax_gigantamax,
    "Venusaur-Gigantamax": Gvenusaur_gigantamax,
    "Zapdos": Gzapdos,
    "Weedle": Gweedle
    }

    ImagensPokemon38 = {
    "Bulbasaur": SbulbasaurIMG,
    "Ivysaur": SivysaurIMG,
    "Venusaur": SvenusaurIMG,
    "Charmander": ScharmanderIMG,
    "Charmeleon": ScharmeleonIMG,
    "Charizard": ScharizardIMG,
    "Squirtle": SsquirtleIMG,
    "Wartortle": SwartortleIMG,
    "Blastoise": SblastoiseIMG,
    "Machop": SmachopIMG,
    "Machoke": SmachokeIMG,
    "Machamp": SmachampIMG,
    "Gastly": SgastlyIMG,
    "Haunter": ShaunterIMG,
    "Gengar": SgengarIMG,
    "Geodude": SgeodudeIMG,
    "Graveler": SgravelerIMG,
    "Golem": SgolemIMG,
    "Caterpie": ScaterpieIMG,
    "Metapod": SmetapodIMG,
    "Butterfree": SbutterfreeIMG,
    "Abra": SabraIMG,
    "Kadabra": SkadabraIMG,
    "Alakazam": SalakazamIMG,
    "Dratini": SdratiniIMG,
    "Dragonair": SdragonairIMG,
    "Dragonite": SdragoniteIMG,
    "Zorua": SzoruaIMG,
    "Zoroark": SzoroarkIMG,
    "Pikachu": SpikachuIMG,
    "Raichu": SraichuIMG,
    "Magikarp": SmagikarpIMG,
    "Gyarados": SgyaradosIMG,
    "Jigglypuff": SjigglypuffIMG,
    "Wigglytuff": SwigglytuffIMG,
    "Magnemite": SmagnemiteIMG,
    "Magneton": SmagnetonIMG,
    "Snorlax": SsnorlaxIMG,
    "Aerodactyl": SaerodactylIMG,
    "Jynx": SjynxIMG,
    "Mewtwo": SmewtwoIMG,
    "Aerodactyl-mega": Saerodactyl_megaIMG,
    "Alakazam-mega": Salakazam_megaIMG,
    "Articuno": SarticunoIMG,
    "Beedrill": SbeedrillIMG,
    "Beedrill-mega": Sbeedrill_megaIMG,
    "Blastoise-gigantamax": Sblastoise_gigantamaxIMG,
    "Blastoise-mega": Sblastoise_megaIMG,
    "Butterfree-gigantamax": Sbutterfree_gmaxIMG,
    "Charizard-gigantamax": Scharizard_gmaxIMG,
    "Charizard-mega-x": Scharizard_megaxIMG,
    "Charizard-mega-y": Scharizard_megayIMG,
    "Clefable": SclefableIMG,
    "Clefairy": SclefairyIMG,
    "Cloyster": ScloysterIMG,
    "Cubone": ScuboneIMG,
    "Gengar-gigantamax": Sgengar_gigantamaxIMG,
    "Gengar-mega": Sgengar_megaIMG,
    "Golem-alola": Sgolem_megaIMG,
    "Gyarados-mega": Sgyarados_megaIMG,
    "Kakuna": SkakunaIMG,
    "Machamp-gigantamax": Smachamp_gigantamaxIMG,
    "Marowak": SmarowakIMG,
    "Meowth": SmeowthIMG,
    "Meowth-gigantamax": Smeowth_gigantamaxIMG,
    "Mewtwo-mega-x": Smewtwo_megaxIMG,
    "Mewtwo-mega-y": Smewtwo_megayIMG,
    "Moltres": SmoltresIMG,
    "Persian": SpersianIMG,
    "Pikachu-gigantamax": Spikachu_gigantamaxIMG,
    "Pinsir": SpinsirIMG,
    "Pinsir-mega": Spinsir_megaIMG,
    "Raticate": SraticateIMG,
    "Rattata": SrattataIMG,
    "Shellder": SshellderIMG,
    "Snorlax-gigantamax": Ssnorlax_gigantamaxIMG,
    "Venusaur-gigantamax": Svenusaur_gigantamaxIMG,
    "Zapdos": SzapdosIMG,
    "Weedle": SweedleIMG
}


    ImagensPokemon100 = {
    "Bulbasaur": MbulbasaurIMG,
    "Charmander": McharmanderIMG,
    "Squirtle": MsquirtleIMG,
    "Machop": MmachopIMG,
    "Gastly": MgastlyIMG,
    "Geodude": MgeodudeIMG,
    "Caterpie": McaterpieIMG,
    "Abra": MabreIMG,
    "Dratini": MdratiniIMG,
    "Zorua": MzoruaIMG,
    "Pikachu": MpikachuIMG,
    "Magikarp": MmagikarpIMG,
    "Jigglypuff": MjigglypuffIMG,
    "Magnemite": MmagnemiteIMG,
    "Snorlax": MsnorlaxIMG,
    "Aerodactyl": MaerodactylIMG,
    "Jynx": MjynxIMG,
    "Mewtwo": MmewtwoIMG,
    "Meowth": MmeowthIMG,
    "Cubone": McuboneIMG,
    "Shellder": MshellderIMG,
    "Articuno": MarticunoIMG,
    "Moltres": MmoltresIMG,
    "Zapdos": MzapdosIMG,
    "Clefairy": MclefairyIMG,
    "Rattata": MrattataIMG,
    "Weedle": MweedleIMG,
    "Pinsir": MpinsirIMG
}



    ImagensPokebolas = {
    "Pokebola": UPokeballIMG,
    "Greatball": UGreatBallIMG,
    "Ultraball": UUltraBallIMG,
    "Masterball": UMasterBallIMG,
    "Fruta Frambo": UFramboIMG,
    "Fruta Frambo Dourada": UFramboDouradaIMG,
    "Fruta Caxi": UCaxiIMG,
    "Fruta Caxi Prateada": UCaxiPrateadaIMG
    }


    ImagensItens = {
    "Esmeralda": EsmeraldaIMG,
    "Citrino": CitrinoIMG,
    "Rubi": RubiIMG,
    "Safira": SafiraIMG,
    "Ametista": AmetistaIMG,
    "Coletor": ColetorIMG,
    "Caixa": CaixaIMG,
    "Caixote": CaixoteIMG,
    "Poção": PocaoIMG,
    "Super Poção": SuperPocaoIMG,
    "Hiper Poção": HiperPocaoIMG,
    "Mega Poção": MegaPocaoIMG,
    "Pokebola": PokeballIMG,
    "Greatball": GreatBallIMG,
    "Ultraball": UltraBallIMG,
    "Masterball": MasterBallIMG,
    "Fruta Frambo": FramboIMG,
    "Fruta Frambo Dourada": FramboDouradaIMG,
    "Fruta Caxi": CaxiIMG,
    "Fruta Caxi Prateada": CaxiPrateadaIMG,
    "estadio": EstadioIMG
    }

    OutrosIMG = [InventárioIMG,energiasIMG,CentroIMG,LojaItensIMG,LojaPokebolasIMG,LojaAmplificadoresIMG,LojaEnergiasIMG,AtaqueIMG,NocauteIMG,LojaEstTreIMG,LojaBloqIMG,GuardadoIMG]

    FundosIMG = [Fundo,MerFundo,ShivreFundo,AuromaFundo,KalosFundo,SkyloftFundo,PortoFundo]

def TelaPokemons(tela,eventos,estados):
    global PokemonS
    global PokemonV
    global PokemonSV
    global PokemonVV
    global informacao
    global player
    global inimigo

    try:
        if PokemonS.local is not None:
            YA = GV.animar(AT1,AT2,animaA,tempo=250)

    
            for i in range(len(inimigo.pokemons)):
                if inimigo.pokemons[i].Vida > 0 and inimigo.pokemons[i].local is not None:
                    BI = BA[i]
                    BJ = BA[i+6]

                    GV.Botao(tela, "", (1435 - i * 190, YA, 40, 55), LARANJA, PRETO, VERDE_CLARO,
                                    lambda: atacaN(PokemonS,player,inimigo,BI["ID"],tela), Fonte50, BI, 2, None, True, eventos)
                    GV.Botao(tela, "", (1335 - i * 190, YA, 40, 55), ROXO, PRETO, VERDE_CLARO,
                                    lambda: atacaS(PokemonS,player,inimigo,BJ["ID"],tela), Fonte50, BJ, 2, None, True, eventos)
                    tela.blit(OutrosIMG[7],((1435 - i * 190),(YA + 10)))
                    tela.blit(OutrosIMG[7],((1335 - i * 190),(YA + 10)))

    except AttributeError:
        pass

    YO = GV.animar(OP1,OP2,animaOP,tempo=250)

    GV.Botao(tela, "Evoluir", (1570, YO, 340, 50), VERDE_CLARO, PRETO, AZUL,lambda: PokemonS.evoluir(player),Fonte40, B22, 3, None, True, eventos)


    try:
        if PokemonS.local is not None:
            
            GV.Botao(tela, "Guardar", (1570, YO + 50, 340, 50), CINZA, PRETO, AZUL,lambda: M.GuardarPosicionar(PokemonS,player),Fonte40, B23, 3, None, True, eventos)

        else:
            if PokemonS.guardado < 3:
                GV.Botao(tela, f"Posicionar em {3 - PokemonS.guardado}", (1570, YO + 50, 340, 50), CINZA_ESCURO, PRETO, AZUL,lambda: GV.tocar(Bloq),Fonte40, B23, 3, None, True, eventos)
            else:
                GV.Botao(tela, "Posicionar", (1570, YO + 50, 340, 50), CINZA, PRETO, AZUL,lambda: M.GuardarPosicionar(PokemonS,player),Fonte40, B23, 3, None, True, eventos)

    except AttributeError:
        pass


    for i in range(6):
        x = 420 + i * 190  # ajusta a posição horizontal
        id_poke = f"Pokemon{i+1}"
        GV.Botao_Selecao(
            tela, (x, 890, 190, 190),
            "", Fonte30,
            cor_fundo=AZUL_SUPER_CLARO, cor_borda_normal=PRETO,
            cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
            cor_passagem=AMARELO, id_botao=id_poke,
            estado_global=estadoPokemon, eventos=eventos,
            funcao_esquerdo=lambda i=i: seleciona(f"Pokemon{i+1}", player, inimigo),
            funcao_direito=lambda i=i: vizualiza(f"Pokemon{i+1}", player, inimigo),
            desfazer_esquerdo=lambda: desseleciona(), desfazer_direito=lambda: oculta(),
            tecla_esquerda=pygame.K_1, tecla_direita=None, som=clique)

    for i in range(6):
        x = 1310 - i * 190  # ajusta a posição horizontal
        id_poke = f"inimigo{i+1}"
        GV.Botao_Selecao(
            tela, (x, 0, 190, 190),
            "", Fonte30,
            cor_fundo=VERMELHO_SUPER_CLARO, cor_borda_normal=PRETO,
            cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
            cor_passagem=AMARELO, id_botao=id_poke,
            estado_global=estadoPokemon, eventos=eventos,
            funcao_esquerdo=lambda i=i: seleciona(f"inimigo{i+1}", player, inimigo),
            funcao_direito=lambda i=i: vizualiza(f"inimigo{i+1}", player, inimigo),
            desfazer_esquerdo=lambda: desseleciona(), desfazer_direito=lambda: oculta(),
            tecla_esquerda=pygame.K_1, tecla_direita=None, som=clique)

    if PokemonS is not None:
        PokemonSV = PokemonS

    if PokemonV is not None:
        PokemonVV = PokemonV

    GV.Status_Pokemon((S1,555), tela, PokemonSV,TiposEnergiaIMG, player, eventos, estadoMostraAtaqueS,S2,animaS,200,"S")

    GV.Status_Pokemon((V1,220), tela, PokemonVV,TiposEnergiaIMG, player, eventos, estadoMostraAtaqueV,V2,animaV,200,"V")

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
        
    for i in range(len(player.pokemons)):
        barra_vida(tela, 420 + i * 190, 870, 190, 20, player.pokemons[i].Vida, player.pokemons[i].VidaMax,(100,100,100),player.pokemons[i].ID)
    
    for i in range(len(inimigo.pokemons)):
        barra_vida(tela, 1310 - i * 190, 190, 190, 20, inimigo.pokemons[i].Vida, inimigo.pokemons[i].VidaMax,(100,100,100),inimigo.pokemons[i].ID)

    atualizar_efeitos(tela)

def TelaOpções(tela,eventos,estados):
    global PokemonS
    global Visor
    global player
    global inimigo
    global ver_centro
    global Centro

    YT = GV.animar(T1,T2,animaT,300)

    GV.Botao(tela, "", (0, YT, 420, 50), PRETO, PRETO, PRETO,lambda: Troca_Terminal(),Fonte40, B20, 3, None, True, eventos)
    GV.Texto_caixa(tela,f"Seu ouro: {player.ouro}",(210, (YT - 60), 210, 60),Fonte40,LARANJA,PRETO)
    GV.Texto_caixa(tela,player.nome,(0, YT, 420, 50),Fonte50,AZUL,PRETO) 
    GV.Terminal(tela, (0, (YT + 50), 420, 230), Fonte20, AZUL_CLARO, PRETO)

    nomes_botoes_outros = ["Inventario", "Energias", "Centro"]

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


        GV.Inventario((A1,300),tela,player,ImagensItens,estadoItens,eventos,PokemonS,A2,animaAI)

        GV.Tabela_Energias(tela,(A3,300),player,estadoEnergias,eventos,A4,animaAE)

        Centroo(tela, A5, 260, Centro, player, Fonte50, Fonte28, B6, estadoPokebola,estadoFruta, eventos,A6,animaAC)

        if ver_centro == "s":
            idx_pokebola = 0  
            for i, item in enumerate(player.inventario):
                if item.get("classe") == "pokebola":
                    x = 332
                    y = 262 + idx_pokebola * 60 
                    tela.blit(ImagensPokebolas[item["nome"]], (x, y))
                    idx_pokebola += 1 

            
            x_inicial = 10
            y_inicial = 270

            for i in range(len(Centro)):
                coluna = i % 3        
                linha = i // 3        
                x = x_inicial + coluna * 109
                y = y_inicial + linha * 109
                tela.blit(ImagensPokemon100[Centro[i]["nome"]],(x,y))

def TelaOutros(tela,eventos,estados):
    global LojaItensP
    global LojaPokeP
    global LojaAmpliP
    global LojaEnerP
    global LojaEstTreP
    global player
    global inimigo

    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,lambda: pausarEdespausar(), Fonte50, B1, 3, pygame.K_ESCAPE, False, eventos)

    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,lambda: Muter(), Fonte50, B1, 3, pygame.K_m, False, eventos)

    GV.Botao(tela, "Passar Turno", (10, 90, 340, 50), AMARELO_CLARO, PRETO, AZUL,lambda: passar_turno(),Fonte40, B7, 3, None, True, eventos)
    
    cronometro(tela, (0, 60, 360, 30), Mapa.tempo, Fonte40, CINZA, PRETO, AMARELO, lambda:passar_turno(),Turno)

    GV.Texto_caixa(tela,f"Turno: {Turno}",(0, 0, 360, 60),Fonte70,AMARELO,PRETO) 
    GV.Texto_caixa(tela,inimigo.nome,(1500, 0, 420, 50),Fonte50,VERMELHO_CLARO,PRETO)

    itens_loja = [
        (LojaItensP, B2, 1510),
        (LojaPokeP, B3, 1590),
        (LojaEnerP, B5, 1670),
        (LojaAmpliP, B4, 1750),
        (LojaEstTreP,B20,1830)]

    for i, (valor, botao_dict, x) in enumerate(itens_loja):
        GV.Texto_caixa(tela, str(valor), (x + 15, 159, 50, 20), Fonte20, CINZA, PRETO, 2)

        GV.Botao(tela, "", (x, 80, 80, 80),CINZA, PRETO, VERDE_CLARO,lambda botao_dict=botao_dict, valor=valor: G.gera_item(botao_dict["ID"], player, valor, Turno),
            Fonte50, botao_dict, 3, None, True, eventos)
    
    tela.blit(OutrosIMG[3],(1515,85))
    tela.blit(OutrosIMG[4],(1595,85))
    tela.blit(OutrosIMG[6],(1681,88))

    if Turno > 3:
        tela.blit(OutrosIMG[5],(1756,85))
        if Turno > 5:
            tela.blit(OutrosIMG[9],(1834,88))
        else:
            tela.blit(OutrosIMG[10],(1835,85))
    else:
        tela.blit(OutrosIMG[10],(1755,85))
        tela.blit(OutrosIMG[10],(1835,85))

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
    M.Desenhar_Casas_Disponiveis(tela, Mapa.area, player, inimigo, Fonte20, eventos, Mapa.cores, Mapa.Metros)