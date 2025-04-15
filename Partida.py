import pygame
import random
import Tabuleiro as M
import GeradoresVisuais as GV
import Gerador2 as G
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte25, Fonte28, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO,VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA,LARANJA_CLARO, ROXO,ROXO_CLARO, ROSA, DOURADO, PRATA,)

pygame.mixer.init()

clique = pygame.mixer.Sound("Musicas/Som1.wav")
Compra = pygame.mixer.Sound("Musicas/Compra.wav")
Usou = pygame.mixer.Sound("Musicas/Usou.wav")
Bom = pygame.mixer.Sound("Musicas/Bom.wav")
Bloq = pygame.mixer.Sound("Musicas/Bloq.wav")

PokemonS = None
PokemonV = None
informacao = None
Visor = None
PokebolaSelecionada = None

mensagens_passageiras = []

PokeGifs = {}
Gifs_ativos = []

TiposEnergiaIMG = {}
ImagensPokemon38 = {}
ImagensPokemon100 = {}
ImagensPokebolas = {}
ImagensItens = {}
OutrosIMG = []

Centro = []
ver_centro = "n"

LojaItensP = 3
LojaPokeP = 4
LojaAmpliP = 3
LojaEnerP = 1

Turno = 1
tempo_restante = 0

Jogador1 = None
Jogador2 = None

player = None
inimigo = None

Vencedor = None
Perdedor = None

Pausa = False

class MensagemPassageira:
    def __init__(self, mensagem, cor, fonte, posicao, duracao=150, deslocamento=35):
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
        tela.blit(texto_surface, (x, y - y_offset))

def adicionar_mensagem_passageira(mensagens, texto, cor, fonte, posicao, duracao=60, deslocamento=30):
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

    player, inimigo = inimigo, player

    Centro = G.spawn_do_centro(Centro)
    Centro = G.spawn_do_centro(Centro)
    Turno += 1
    Fecha()
    desseleciona()
    oculta()
    GV.adicionar_mensagem(f"Novo turno de {player.nome}!")
    return player, inimigo

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
            PokemonS = player.pokemons[idx]
        else:
            PokemonS = None
            GV.adicionar_mensagem("Esse Pokémon não pode ser selecionado.")
    else:
        PokemonS = None
        GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")
        
def desseleciona():
    global PokemonS
    global estadoPokemon
    PokemonS = None
    estadoPokemon["selecionado_esquerdo"] = False

def vizualiza(ID,player,inimigo,):
    global PokemonV
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
        else:
            PokemonV = None
            GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")      
    else:
        idx = index_map[ID]
        if idx < len(inimigo.pokemons):
                PokemonV = inimigo.pokemons[idx]
        else:
            PokemonV = None
            GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")     

def oculta():
    global PokemonV
    global estadoInfo
    PokemonV = None
    estadoInfo["selecionado_direito"] = False

def informa(ID,Pokemon):
    pass

def desinforma():
    global estadoInfo
    estadoInfo["selecionado_esquerdo"] = None
    pass

def Abre(ID,player,inimigo):
    global Visor
    Visor = ID
    
def Fecha():
    global ver_centro
    global Visor
    global estadoOutros

    ver_centro = "n"
    Visor = None
    estadoOutros["selecionado_esquerdo"] =  False

def seleciona_pokebola(pokebola):
    global PokebolaSelecionada
    PokebolaSelecionada = pokebola

def desseleciona_pokebola():
    global PokebolaSelecionada
    PokebolaSelecionada = None

def PokemonCentro(ID,player):
    global PokebolaSelecionada
    global Centro
    global estadoOutros

    pokemon = Centro[ID]
    
    if PokebolaSelecionada is not None:
        player.inventario.remove(PokebolaSelecionada)
        Pokebola_usada = PokebolaSelecionada
        desseleciona_pokebola()
        maestria = random.randint(0,Pokebola_usada["poder"] * 2)
        if maestria >= pokemon["dificuldade"]:
            if len(player.pokemons) < 6:
                novo_pokemon = G.Gerador_final(pokemon["code"])
                AddIMGpokemon(novo_pokemon) 
                player.ganhar_pokemon(novo_pokemon)
                AddLocalPokemon(novo_pokemon,player)
                GV.adicionar_mensagem(f"Parabens! Capturou um {novo_pokemon.nome} usando uma {Pokebola_usada['nome']}")
                VerificaGIF()
                GV.tocar(Bom)
                Centro.remove(pokemon)
                estadoOutros["selecionado_esquerdo"] =  False
                return
            else:
                GV.tocar(Bloq)
                GV.adicionar_mensagem("sua lista de pokemon está cheia")
        else:
            GV.tocar(Bloq)
            GV.adicionar_mensagem("Voce falhou em capturar o pokemon, que pena")
        estadoOutros["selecionado_esquerdo"] =  False
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
    Pokemon.atacar(alvo,player,inimigo,"N",tela)

def atacaS(Pokemon,player,inimigo,ID,tela):
    alvo = inimigo.pokemons[ID]
    Pokemon.atacar(alvo,player,inimigo,"S",tela)

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

def AddLocalPokemon(pokemon,player):
    C = player.pokemons.index(pokemon) 
    M.Move(pokemon,11,(C+10))

def AddLocalPokemonINIC(pokemon,jogador):
    if jogador == Jogador1:
        M.Move(pokemon,11,10)
    else:
        M.Move(pokemon,3,10)

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
                "intervalo": 40  # Pode ser ajustado para cada Pokémon se necessário
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
                "intervalo": 40  # Pode ser ajustado para cada Pokémon se necessário
            })

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

estadoTabuleiro = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

estadoItens = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

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

BA = [B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19,]
#botoes de clique unico = B6

def AB(Visor,tela,eventos,player,inimigo):
    global PokemonS
    global Centro
    global ver_centro

    if Visor == "Inventario":
        GV.Inventario((0,300),tela,player,ImagensItens,estadoItens,eventos,PokemonS)

    elif Visor == "Energias":
        nomeA = f"Energias de {player.nome}"
        colunasA = ["tipo", "N", "Tipo", "N"]
        linhasA = [
        ["Vermelha",player.energias["vermelha"], "Laranja",player.energias["laranja"]],
        ["Azul", player.energias["azul"], "Marrom",player.energias["marrom"]],
        ["Amarela", player.energias["amarela"], "Rosa",player.energias["rosa"]],
        ["Verde", player.energias["verde"], "Roxa",player.energias["roxa"]],
        ["Cinza", player.energias["cinza"], "Preta",player.energias["preta"]],
        ]
        GV.Tabela(nomeA, colunasA, linhasA, tela, 0, 300, 420, Fonte28, Fonte30, AZUL_SUPER_CLARO, PRETO, AZUL_CLARO)
    
    elif Visor == "Centro":
        ver_centro = "s"
        x_inicial = 0
        y_inicial = 260
        tamanho = 110  

        for i in range(len(Centro)):
            coluna = i % 3        
            linha = i // 3        
        
            x = x_inicial + coluna * tamanho
            y = y_inicial + linha * tamanho
        
            GV.Botao(tela, "", (x, y, tamanho, tamanho), CINZA, PRETO, AZUL,
                lambda i=i: PokemonCentro(i, player), Fonte50, B6, 2, None, True, eventos)
            
        idx_pokebola = 0  # contador só para pokébolas
        for i, item in enumerate(player.inventario):
            if item.get("classe") == "pokebola":
                x = 330
                y = 260 + idx_pokebola * 60  # usa idx_pokebola para espaçamento
                GV.Botao_Selecao(
                    tela, (x, y, 60, 60),
                    f"", Fonte28,
                    cor_fundo=AZUL_SUPER_CLARO, cor_borda_normal=PRETO,
                    cor_borda_esquerda=VERMELHO, cor_borda_direita=None,
                    cor_passagem=AMARELO, id_botao=i,
                    estado_global=estadoPokebola, eventos=eventos,
                    funcao_esquerdo=lambda:seleciona_pokebola(item), funcao_direito=None,
                    desfazer_esquerdo=lambda:desseleciona_pokebola(), desfazer_direito=None,
                    tecla_esquerda=None, tecla_direita=None, grossura=1
                )
                idx_pokebola += 1 

def S(PokemonS,tela,eventos,player,inimigo):
    GV.Status_Pokemon((1560,570), tela, PokemonS,(30, 30, 30), eventos, estadoInfo)

    if PokemonS.Vida <= 0:
        pass

    else:
        for i in range(len(inimigo.pokemons)):
            BI = BA[i]
            BJ = BA[i+6]

            GV.Botao(tela, "", (1435 - i * 190, 210, 40, 55), LARANJA, PRETO, VERDE_CLARO,
                    lambda: atacaN(PokemonS,player,inimigo,BI["ID"],tela), Fonte50, BI, 2, None, True, eventos)
            GV.Botao(tela, "", (1335 - i * 190, 210, 40, 55), ROXO, PRETO, VERDE_CLARO,
                    lambda: atacaS(PokemonS,player,inimigo,BJ["ID"],tela), Fonte50, BJ, 2, None, True, eventos)
            tela.blit(OutrosIMG[7],((1435 - i * 190),220))
            tela.blit(OutrosIMG[7],((1335 - i * 190),220))   

def V(PokemonV,tela,eventos,inimigo):
    
    
    if PokemonV in inimigo.pokemons:
        GV.Status_Pokemon((1560,220), tela, PokemonV,(75, 15, 15), eventos, estadoInfo)
    else:
        GV.Status_Pokemon((1560,220), tela, PokemonV,(30, 30, 30), eventos, estadoInfo)

def Partida(tela,estados,relogio):
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

    Carregar = GV.Carregar_Imagem("imagens/fundos/carregando.jpg",(1920,1080))

    tela.blit(Carregar,(0,0))
    fonte = pygame.font.SysFont(None, 70)
    texto = fonte.render("Carregando ...", True, PRETO)
    tela.blit(texto, (tela.get_width() // 2 - 200, tela.get_height() // 2))
    pygame.display.update()

    pygame.mixer.music.load('Musicas/carregamento.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    Fundo = GV.Carregar_Imagem("imagens/fundos/fundo3.jpg", (1920,1080))
    Carregar_Imagens()
    M.Gerar_Mapa()

    from PygameAções import informaçoesp1, informaçoesp2
    Jogador1 = G.Gerador_player(informaçoesp1)
    Jogador2 = G.Gerador_player(informaçoesp2)

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

    pygame.mixer.music.load('Musicas/Partida1Theme.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    altera_musica = False

    Pausa = False
    Turno = 1
    Centro = []

    Resetar_Cronometro()
    cronometro.inicio = pygame.time.get_ticks()
    cronometro.tempo_encerrado = False

    # 3. Loop principal da partida
    while estados["Rodando_Partida"]:
        tela.fill(BRANCO)
        tela.blit(Fundo,(0,0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Partida"] = False
                estados["Rodando_Jogo"] = False
        
        if Pausa == False:
            TelaPokemons(tela,eventos,estados)
            TelaOpções(tela,eventos,estados)
            TelaOutros(tela,eventos,estados)
            # TelaTabuleiro(tela,eventos,estados)

            if Turno > 5 and not altera_musica:
                pygame.mixer.music.load("Musicas/Partida2theme.ogg")
                pygame.mixer.music.play(-1) 
                altera_musica = True  

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
            Telapausa(tela,eventos,estados)

        pygame.display.update()
        relogio.tick(120)

def Carregar_Imagens():
    global ImagensPokemon38
    global ImagensPokemon100
    global PokeGifs
    global ImagensPokebolas
    global ImagensItens
    global OutrosIMG
    global TiposEnergiaIMG

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

    SbulbasaurIMG = GV.Carregar_Imagem("imagens/pokemons/bulbasaur.png", (38,38),"PNG")
    SivysaurIMG = GV.Carregar_Imagem("imagens/pokemons/ivysaur.png", (38,38),"PNG")
    SvenusaurIMG = GV.Carregar_Imagem("imagens/pokemons/venusaur.png", (38,38),"PNG")
    ScharmanderIMG = GV.Carregar_Imagem("imagens/pokemons/charmander.png", (38,38),"PNG")
    ScharmeleonIMG = GV.Carregar_Imagem("imagens/pokemons/charmeleon.png", (38,38),"PNG")
    ScharizardIMG = GV.Carregar_Imagem("imagens/pokemons/charizard.png", (38,38),"PNG")
    SsquirtleIMG = GV.Carregar_Imagem("imagens/pokemons/squirtle.png", (38,38),"PNG")
    SwartortleIMG = GV.Carregar_Imagem("imagens/pokemons/wartortle.png", (38,38),"PNG")
    SblastoiseIMG = GV.Carregar_Imagem("imagens/pokemons/blastoise.png", (38,38),"PNG")
    SmachopIMG = GV.Carregar_Imagem("imagens/pokemons/machop.png", (38,38),"PNG")
    SmachokeIMG = GV.Carregar_Imagem("imagens/pokemons/machoke.png", (38,38),"PNG")
    SmachampIMG = GV.Carregar_Imagem("imagens/pokemons/machamp.png", (38,38),"PNG")
    SgastlyIMG = GV.Carregar_Imagem("imagens/pokemons/gastly.png", (38,38),"PNG")
    ShaunterIMG = GV.Carregar_Imagem("imagens/pokemons/haunter.png", (38,38),"PNG")
    SgengarIMG = GV.Carregar_Imagem("imagens/pokemons/gengar.png", (38,38),"PNG")
    SgeodudeIMG = GV.Carregar_Imagem("imagens/pokemons/geodude.png", (38,38),"PNG")
    SgravelerIMG = GV.Carregar_Imagem("imagens/pokemons/graveler.png", (38,38),"PNG")
    SgolemIMG = GV.Carregar_Imagem("imagens/pokemons/golem.png", (38,38),"PNG")
    ScaterpieIMG = GV.Carregar_Imagem("imagens/pokemons/caterpie.png", (38,38),"PNG")
    SmetapodIMG = GV.Carregar_Imagem("imagens/pokemons/metapod.png", (38,38),"PNG")
    SbutterfreeIMG = GV.Carregar_Imagem("imagens/pokemons/butterfree.png", (38,38),"PNG")
    SabraIMG = GV.Carregar_Imagem("imagens/pokemons/abra.png", (38,38),"PNG")
    SkadabraIMG = GV.Carregar_Imagem("imagens/pokemons/kadabra.png", (38,38),"PNG")
    SalakazamIMG = GV.Carregar_Imagem("imagens/pokemons/alakazam.png", (38,38),"PNG")
    SdratiniIMG = GV.Carregar_Imagem("imagens/pokemons/dratini.png", (38,38),"PNG")
    SdragonairIMG = GV.Carregar_Imagem("imagens/pokemons/dragonair.png", (38,38),"PNG")
    SdragoniteIMG = GV.Carregar_Imagem("imagens/pokemons/dragonite.png", (38,38),"PNG")
    SzoruaIMG = GV.Carregar_Imagem("imagens/pokemons/zorua.png", (38,38),"PNG")
    SzoroarkIMG = GV.Carregar_Imagem("imagens/pokemons/zoroark.png", (38,38),"PNG")
    SpikachuIMG = GV.Carregar_Imagem("imagens/pokemons/pikachu.png", (38,38),"PNG")
    SraichuIMG = GV.Carregar_Imagem("imagens/pokemons/raichu.png", (38,38),"PNG")
    SmagikarpIMG = GV.Carregar_Imagem("imagens/pokemons/magikarp.png", (38,38),"PNG")
    SgyaradosIMG = GV.Carregar_Imagem("imagens/pokemons/gyarados.png", (38,38),"PNG")
    SjigglypuffIMG = GV.Carregar_Imagem("imagens/pokemons/jigglypuff.png", (38,38),"PNG")
    SwigglytuffIMG = GV.Carregar_Imagem("imagens/pokemons/wigglytuff.png", (38,38),"PNG")
    SmagnemiteIMG = GV.Carregar_Imagem("imagens/pokemons/magnemite.png", (38,38),"PNG")
    SmagnetonIMG = GV.Carregar_Imagem("imagens/pokemons/magneton.png", (38,38),"PNG")
    SsnorlaxIMG = GV.Carregar_Imagem("imagens/pokemons/snorlax.png", (38,38),"PNG")
    SaerodactylIMG = GV.Carregar_Imagem("imagens/pokemons/aerodactyl.png", (38,38),"PNG")
    SjynxIMG = GV.Carregar_Imagem("imagens/pokemons/jynx.png", (38,38),"PNG")
    SmewtwoIMG = GV.Carregar_Imagem("imagens/pokemons/mewtwo.png", (38,38),"PNG")


    MbulbasaurIMG = GV.Carregar_Imagem("imagens/pokemons/bulbasaur.png", (100, 100), "PNG")
    McharmanderIMG = GV.Carregar_Imagem("imagens/pokemons/charmander.png", (100, 100), "PNG")
    MsquirtleIMG = GV.Carregar_Imagem("imagens/pokemons/squirtle.png", (100, 100), "PNG")
    MmachopIMG = GV.Carregar_Imagem("imagens/pokemons/machop.png", (100, 100), "PNG")
    MgastlyIMG = GV.Carregar_Imagem("imagens/pokemons/gastly.png", (100, 100), "PNG")
    MgeodudeIMG = GV.Carregar_Imagem("imagens/pokemons/geodude.png", (100, 100), "PNG")
    McaterpieIMG = GV.Carregar_Imagem("imagens/pokemons/caterpie.png", (100, 100), "PNG")
    MabreIMG = GV.Carregar_Imagem("imagens/pokemons/abra.png", (100, 100), "PNG")
    MdratiniIMG = GV.Carregar_Imagem("imagens/pokemons/dratini.png", (100, 100), "PNG")
    MzoruaIMG = GV.Carregar_Imagem("imagens/pokemons/zorua.png", (100, 100), "PNG")
    MpikachuIMG = GV.Carregar_Imagem("imagens/pokemons/pikachu.png", (100, 100), "PNG")
    MmagikarpIMG = GV.Carregar_Imagem("imagens/pokemons/magikarp.png", (100, 100), "PNG")
    MjigglypuffIMG = GV.Carregar_Imagem("imagens/pokemons/jigglypuff.png", (100, 100), "PNG")
    MMagnemiteIMG = GV.Carregar_Imagem("imagens/pokemons/magnemite.png", (100, 100), "PNG")
    MsnorlaxIMG = GV.Carregar_Imagem("imagens/pokemons/snorlax.png", (100, 100), "PNG")
    MaerodactylIMG = GV.Carregar_Imagem("imagens/pokemons/aerodactyl.png", (100, 100), "PNG")
    MjynxIMG = GV.Carregar_Imagem("imagens/pokemons/jynx.png", (100, 100), "PNG")
    MmewtwoIMG = GV.Carregar_Imagem("imagens/pokemons/mewtwo.png", (100, 100), "PNG")



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

    UPokeballIMG = GV.Carregar_Imagem("imagens/itens/PokeBall.png", (55,55),"PNG")
    UGreatBallIMG = GV.Carregar_Imagem("imagens/itens/GreatBall.png", (55,55),"PNG")
    UUltraBallIMG = GV.Carregar_Imagem("imagens/itens/UltraBall.png", (55,55),"PNG")
    UMasterBallIMG = GV.Carregar_Imagem("imagens/itens/MasterBall.png", (55,55),"PNG")

    InventárioIMG = GV.Carregar_Imagem("imagens/icones/inventario.png", (60,60),"PNG")
    energiasIMG = GV.Carregar_Imagem("imagens/icones/energias.png", (50,50),"PNG")
    CentroIMG = GV.Carregar_Imagem("imagens/icones/centro.png", (70,70),"PNG")
    LojaPokebolasIMG = GV.Carregar_Imagem("imagens/icones/Poke.png", (70,70),"PNG")
    LojaItensIMG = GV.Carregar_Imagem("imagens/icones/itens.png", (70,70),"PNG")
    LojaAmplificadoresIMG = GV.Carregar_Imagem("imagens/icones/amplificadores.png", (70,70),"PNG")
    LojaEnergiasIMG = GV.Carregar_Imagem("imagens/icones/energias.png", (60,60),"PNG")
    AtaqueIMG = GV.Carregar_Imagem("imagens/icones/atacar.png", (40,40),"PNG")
    NocauteIMG  = GV.Carregar_Imagem("imagens/icones/KO.png", (50,50),"PNG")

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
    "Mewtwo": SmewtwoIMG
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
    "Magnemite": MMagnemiteIMG,
    "Snorlax": MsnorlaxIMG,
    "Aerodactyl": MaerodactylIMG,
    "Jynx": MjynxIMG,
    "Mewtwo": MmewtwoIMG
    }


    ImagensPokebolas = {
    "pokebola": UPokeballIMG,
    "greatball": UGreatBallIMG,
    "ultraball": UUltraBallIMG,
    "masterball": UMasterBallIMG
    }

    ImagensItens = {
    "esmeralda": EsmeraldaIMG,
    "citrino": CitrinoIMG,
    "rubi": RubiIMG,
    "safira": SafiraIMG,
    "ametista": AmetistaIMG,
    "coletor": ColetorIMG,
    "caixa": CaixaIMG,
    "caixote": CaixoteIMG,
    "poção": PocaoIMG,
    "super poção": SuperPocaoIMG,
    "hiper poção": HiperPocaoIMG,
    "mega poção": MegaPocaoIMG,
    "pokebola": PokeballIMG,
    "greatball": GreatBallIMG,
    "ultraball": UltraBallIMG,
    "masterball": MasterBallIMG
}

    OutrosIMG = [InventárioIMG,energiasIMG,CentroIMG,LojaItensIMG,LojaPokebolasIMG,LojaAmplificadoresIMG,LojaEnergiasIMG,AtaqueIMG,NocauteIMG]

def TelaPokemons(tela,eventos,estados):
    global PokemonS
    global PokemonV
    global informacao
    global player
    global inimigo

    for i in range(6):
        x = 420 + i * 190  # ajusta a posição horizontal
        id_poke = f"Pokemon{i+1}"
        GV.Botao_Selecao(
            tela, (x, 890, 190, 190),
            "", Fonte30,
            cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
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
            cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
            cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
            cor_passagem=AMARELO, id_botao=id_poke,
            estado_global=estadoPokemon, eventos=eventos,
            funcao_esquerdo=lambda i=i: seleciona(f"inimigo{i+1}", player, inimigo),
            funcao_direito=lambda i=i: vizualiza(f"inimigo{i+1}", player, inimigo),
            desfazer_esquerdo=lambda: desseleciona(), desfazer_direito=lambda: oculta(),
            tecla_esquerda=pygame.K_1, tecla_direita=None, som=clique)

    if PokemonS is not None:
        S(PokemonS,tela,eventos,player,inimigo)
   
    if PokemonV is not None:
        V(PokemonV,tela,eventos,inimigo) 

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
        
    for i in range(len(player.pokemons)):
        barra_vida(tela, 420 + i * 190, 870, 190, 20, player.pokemons[i].Vida, player.pokemons[i].VidaMax,(100,100,100),player.pokemons[i].ID)
    
    for i in range(len(inimigo.pokemons)):
        barra_vida(tela, 1310 - i * 190, 190, 190, 20, inimigo.pokemons[i].Vida, inimigo.pokemons[i].VidaMax,(100,100,100),inimigo.pokemons[i].ID)

def TelaOpções(tela,eventos,estados):
    global PokemonS
    global Visor
    global player
    global inimigo
    global ver_centro
    global Centro

    nomes_botoes_loja = ["Inventario", "Energias", "Centro"]

    for i, nome in enumerate(nomes_botoes_loja):
        GV.Botao_Selecao(
            tela, (i * 70, 740, 70, 60),
            "", Fonte30,
            cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
            cor_borda_esquerda=VERDE, cor_borda_direita=None,
            cor_passagem=AMARELO, id_botao=nome,   
            estado_global=estadoOutros, eventos=eventos,
            funcao_esquerdo=lambda nome=nome: Abre(nome, player, inimigo), 
            funcao_direito=None,
            desfazer_esquerdo=lambda: Fecha(), desfazer_direito=None,
            tecla_esquerda=pygame.K_1, tecla_direita=None)
        
        if Visor is not None:
            AB(Visor,tela,eventos,player,inimigo)

        
        tela.blit(OutrosIMG[0],(5,740))
        tela.blit(OutrosIMG[1],(80,745))
        tela.blit(OutrosIMG[2],(140,735))

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
    global player
    global inimigo

    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,lambda: pausarEdespausar(), Fonte50, B1, 3, pygame.K_ESCAPE, False, eventos)

    GV.Botao(tela, "Passar Turno", (1620, 1000, 300, 80), CINZA, PRETO, AZUL,lambda: passar_turno(),Fonte50, B7, 3, None, True, eventos)
    
    cronometro(tela, (0, 60, 150, 40), 200, Fonte40, CINZA, PRETO, AMARELO, lambda:passar_turno(),Turno)

    GV.Texto_caixa(tela,f"Turno: {Turno}",(0, 0, 360, 60),Fonte70,AMARELO,PRETO) 
    GV.Texto_caixa(tela,player.nome,(0, 800, 420, 50),Fonte50,AZUL,PRETO) 
    GV.Texto_caixa(tela,inimigo.nome,(1500, 0, 420, 50),Fonte50,VERMELHO_CLARO,PRETO)
    GV.Texto_caixa(tela,f"Seu ouro: {player.ouro}",(210, 740, 210, 60),Fonte40,LARANJA,PRETO)

    GV.Terminal(tela, (0, 850, 420, 230), Fonte20, AZUL_CLARO, PRETO)

    itens_loja = [
        (LojaItensP, B2, 1510),
        (LojaPokeP, B3, 1590),
        (LojaAmpliP, B4, 1670),
        (LojaEnerP, B5, 1750),]

    for i, (valor, botao_dict, x) in enumerate(itens_loja):
        GV.Texto_caixa(tela, str(valor), (x + 15, 158, 50, 20), Fonte20, CINZA, PRETO, 2)

        GV.Botao(tela, "", (x, 80, 80, 80),CINZA, PRETO, VERDE_CLARO,lambda botao_dict=botao_dict, valor=valor: G.gera_item(botao_dict["ID"], player, valor),
            Fonte50, botao_dict, 3, None, True, eventos)
        
    
    tela.blit(OutrosIMG[3],(1515,85))
    tela.blit(OutrosIMG[4],(1595,85))
    tela.blit(OutrosIMG[5],(1675,85))
    tela.blit(OutrosIMG[6],(1760,88))

def Telapausa(tela,eventos,estados):

    GV.Botao(tela, "Despausar partida", (600, 200, 720, 130), CINZA, PRETO, AZUL,lambda: pausarEdespausar(),Fonte70, B6, 5, pygame.K_ESCAPE, True, eventos)
    GV.Botao(tela, "Sair da partida", (600, 425, 720, 130), CINZA, PRETO, AZUL,lambda: A.Voltar(estados),Fonte70, B6, 5, None, True, eventos)
    GV.Botao(tela, "Sair do jogo", (600, 650, 720, 130), CINZA, PRETO, AZUL,lambda: A.fechar_jogo(estados),Fonte70, B6, 5, None, True, eventos)

def TelaTabuleiro(tela,eventos,estados):
    
    M.Desenhar_Casas_Disponiveis(tela, [
    (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16),
    (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (4, 16),
    (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (5, 16),
    (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (6, 16),
    (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16),
    (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16),
    (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 16),
    (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16),
    (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (11, 16)
],player,inimigo,Fonte20,estadoTabuleiro,eventos)

