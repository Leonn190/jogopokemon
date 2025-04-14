import pygame
import random
import GeradoresVisuais as GV
import Gerador2 as G
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte25, Fonte28, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO,VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

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

ImagensPokemon100 = {}
ImagensPokemon180 = {}
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

estado_animacao_status = {
    "ativo": False,
    "x_tabela": 2000,
    "x_botao1": 2000,
    "x_botao2": 2000
}

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

    # Calcula tempo restante
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

def passar_turno():
    global Turno
    global Centro
    global player
    global inimigo

    player.ouro += 2 + (tempo_restante // 20)
    GV.limpa_terminal()

    player, inimigo = inimigo, player

    Centro = G.spawn_do_centro(Centro)
    Centro = G.spawn_do_centro(Centro)
    Turno += 1
    Fecha()
    desseleciona()
    oculta()
    mensagens_terminal = []
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
    PokemonS = None

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
    estadoInfo["selecionado_esquerdo"] = None

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

    ver_centro = "n"
    Visor = None

def seleciona_pokebola(pokebola):
    global PokebolaSelecionada
    PokebolaSelecionada = pokebola

def desseleciona_pokebola():
    global PokebolaSelecionada
    PokebolaSelecionada = None

def PokemonCentro(ID,player):
    global PokebolaSelecionada
    global Centro

    pokemon = Centro[ID]
    
    if PokebolaSelecionada is not None:
        player.inventario.remove(PokebolaSelecionada)
        Pokebola_usada = PokebolaSelecionada
        desseleciona_pokebola()
        maestria = random.randint(0,Pokebola_usada["poder"] * 2)
        if maestria >= pokemon["dificuldade"]:
            if len(player.pokemons) < 7:
                novo_pokemon = G.Gerador_final(pokemon["code"])
                player.ganhar_pokemon(novo_pokemon)
                GV.adicionar_mensagem(f"Parabens! Capturou um {novo_pokemon.nome} usando uma {Pokebola_usada['nome']}")
                GV.tocar(Bom)
                Centro.remove(pokemon)
                return
            else:
                GV.tocar(Bloq)
                GV.adicionar_mensagem("sua lista de pokemon está cheia")
        else:
            GV.tocar(Bloq)
            GV.adicionar_mensagem("Voce falhou em capturar o pokemon, que pena")
    else:
        GV.tocar(Bloq)
        GV.adicionar_mensagem("Selecione uma pokebola para capturar um pokemon")

def barra_vida(tela, x, y, largura, altura, vida_atual, vida_maxima, cor_fundo,id_pokemon):
    if not hasattr(barra_vida, "vidas_animadas"):
        barra_vida.vidas_animadas = {}

    # Pega a vida anterior ou inicializa
    vida_animada = barra_vida.vidas_animadas.get(id_pokemon, vida_atual)

    # Animação suave
    velocidade = 1.5
    if vida_animada < vida_atual:
        vida_animada = min(vida_animada + velocidade, vida_atual)
    elif vida_animada > vida_atual:
        vida_animada = max(vida_animada - velocidade, vida_atual)

    barra_vida.vidas_animadas[id_pokemon] = vida_animada  # Salva valor atualizado

    proporcao = vida_animada / vida_maxima
    largura_vida = int(largura * proporcao)

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

estado = {
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
        nomeA = f"Inventário de {player.nome}"
        colunasA = ["Nome", "Descrição"]
        linhasA = []
        for item in player.inventario:
            linhasA.append([item["nome"], item["Descrição"]])
        GV.Tabela(nomeA, colunasA, linhasA, tela, 0, 250, 420, Fonte20, Fonte28, AZUL_SUPER_CLARO, PRETO, AZUL_CLARO)

        for i in range(len(player.inventario)):
            indice_item = i  # salvando o índice em uma variável fixa pra capturar no lambda

            GV.Botao(
                tela, "", (418, (310 + indice_item * 30), 30, 30), CINZA, PRETO, AZUL,
                lambda i=indice_item: player.usar_item(i, PokemonS),
                Fonte50, B6, 1, None, True, eventos,
            )

            try:
                tela.blit(ImagensItens[player.inventario[indice_item]["nome"]], (418, (310 + indice_item * 30)))
            except IndexError:
                pass  # item já foi removido

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
    nomeS = f"Status do {PokemonS.nome}"

    colunasS = ["    nome    ", "valor", "IV"]  # 3 colunas: nome, valor, IV

    # Linhas com os atributos e o valor "caju" para IV
    linhasS = [
        ["Vida", PokemonS.Vida, PokemonS.IV_vida],
        ["ATK", PokemonS.Atk, PokemonS.IV_atk],
        ["Sp ATK", PokemonS.Atk_sp, PokemonS.IV_atkSP],
        ["DEF", PokemonS.Def, PokemonS.IV_def],
        ["Sp DEF", PokemonS.Def_sp, PokemonS.IV_defSP],
        ["VEL", PokemonS.vel, f"IV:{PokemonS.IV}"],
        ["Custo", PokemonS.custo, PokemonS.tipo[0]],
        ["XP", PokemonS.xp_atu, PokemonS.tipo[1] if len(PokemonS.tipo) > 1 else ""]
    ]

    # Chamada da função Tabela
    GV.Tabela(nomeS, colunasS, linhasS, tela, 1570, 570, 350, Fonte28, Fonte30, AZUL_SUPER_CLARO, PRETO, AZUL_CLARO)

    GV.Botao_Selecao(
    tela, (1570, 860, 175, 30),
    f"{PokemonS.ataque_normal["nome"]}", Fonte28,
    cor_fundo=LARANJA, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Atk Norm.S",   
    estado_global=estadoInfo, eventos=eventos,
    funcao_esquerdo=lambda:informa("Atk Norm",PokemonS), funcao_direito=None,
    desfazer_esquerdo=lambda:desinforma(), desfazer_direito=None,
    tecla_esquerda=None, tecla_direita=None, grossura=1)
    GV.Botao_Selecao(
    tela, (1745, 860, 175, 30),
    f"{PokemonS.ataque_especial["nome"]}", Fonte28,
    cor_fundo=ROXO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Atk SP.S",   
    estado_global=estadoInfo, eventos=eventos,
    funcao_esquerdo=lambda:informa("Atk SPS",PokemonS), funcao_direito=None,
    desfazer_esquerdo=lambda:desinforma(), desfazer_direito=None,
    tecla_esquerda=None, tecla_direita=None, grossura=1)

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
    nomeV = f"Status do {PokemonV.nome}"

    colunasV = ["    nome    ", "valor", "IV"]  # 3 colunas: nome, valor, IV

    # Linhas com os atributos e o valor "caju" para IV
    linhasV = [
        ["Vida", PokemonV.Vida, PokemonV.IV_vida],
        ["ATK", PokemonV.Atk, PokemonV.IV_atk],
        ["Sp ATK", PokemonV.Atk_sp, PokemonV.IV_atkSP],
        ["DEF", PokemonV.Def, PokemonV.IV_def],
        ["Sp DEF", PokemonV.Def_sp, PokemonV.IV_defSP],
        ["VEL", PokemonV.vel, f"IV:{PokemonV.IV}"],
        ["Custo", (PokemonV.custo), PokemonV.tipo[0]],
        ["XP", (PokemonV.xp_atu), PokemonV.tipo[1] if len(PokemonV.tipo) > 1 else ""]
    ]

    if PokemonV in inimigo.pokemons:
        GV.Tabela(nomeV, colunasV, linhasV, tela, 1570, 240, 350, Fonte28,Fonte30, VERMELHO_SUPER_CLARO, PRETO, VERMELHO_CLARO)

        GV.Botao_Selecao(
        tela, (1570, 530, 175, 30),
        f"{PokemonV.ataque_normal["nome"]}", Fonte28,
        cor_fundo=LARANJA, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
        cor_passagem=AMARELO, id_botao="Atk Norm.V",   
        estado_global=estadoInfo, eventos=eventos,
        funcao_esquerdo=lambda:informa("Atk Norm.V",PokemonS), funcao_direito=None,
        desfazer_esquerdo=lambda:desinforma(), desfazer_direito=None,
        tecla_esquerda=pygame.K_1, tecla_direita=None, grossura=1)
        GV.Botao_Selecao(
        tela, (1745, 530, 175, 30),
        f"{PokemonV.ataque_especial["nome"]}", Fonte28,
        cor_fundo=ROXO, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
        cor_passagem=AMARELO, id_botao="Atk SP.V",   
        estado_global=estadoInfo, eventos=eventos,
        funcao_esquerdo=lambda:informa("Atk Norm.V",PokemonS), funcao_direito=None,
        desfazer_esquerdo=lambda:desinforma(), desfazer_direito=None,
        tecla_esquerda=pygame.K_1, tecla_direita=None, grossura=1)

    else:
        GV.Tabela(nomeV, colunasV, linhasV, tela, 1570, 240, 350, Fonte28,Fonte30, AZUL_SUPER_CLARO, PRETO,AZUL_CLARO)

        GV.Botao_Selecao(
        tela, (1570, 530, 175, 30),
        f"{PokemonV.ataque_normal["nome"]}", Fonte28,
        cor_fundo=AZUL_SUPER_CLARO, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
        cor_passagem=AMARELO, id_botao="Atk Norm.V",   
        estado_global=estadoInfo, eventos=eventos,
        funcao_esquerdo=lambda:informa("Atk Norm.V",PokemonS), funcao_direito=None,
        desfazer_esquerdo=lambda:desinforma("Atk Norm.V",PokemonS), desfazer_direito=None,
        tecla_esquerda=pygame.K_1, tecla_direita=None, grossura=1)
        GV.Botao_Selecao(
        tela, (1745, 530, 175, 30),
        f"{PokemonV.ataque_especial["nome"]}", Fonte28,
        cor_fundo=AZUL_SUPER_CLARO, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
        cor_passagem=AMARELO, id_botao="Atk SP.V",   
        estado_global=estadoInfo, eventos=eventos,
        funcao_esquerdo=lambda:informa("Atk Norm.V",PokemonS), funcao_direito=None,
        desfazer_esquerdo=lambda:desinforma("Atk Norm.V",PokemonS), desfazer_direito=None,
        tecla_esquerda=pygame.K_1, tecla_direita=None, grossura=1)
    
def Partida(tela,estados,relogio):
    global Turno
    global ImagensPokemon100
    global ImagensPokemon180
    global ImagensPokebolas
    global Jogador1
    global Jogador2
    global player
    global inimigo
    global Vencedor
    global Perdedor

    Fundo = GV.Carregar_Imagem("imagens/fundos/fundo3.jpg", (1920,1080),)
    Carregar_Imagens()

    click_sound = pygame.mixer.Sound("Musicas/Som1.wav")  

    from PygameAções import informaçoesp1, informaçoesp2
    Jogador1 = G.Gerador_player(informaçoesp1)
    Jogador2 = G.Gerador_player(informaçoesp2)

    for item in informaçoesp1[3:]:
        G.gera_item(item,Jogador1)
    for item in informaçoesp2[3:]:
        G.gera_item(item,Jogador2)

    for i in range(12):
        G.gera_item("energia",Jogador1)
        G.gera_item("energia",Jogador2)

    player = Jogador1
    inimigo = Jogador2

    pygame.mixer.music.load('Musicas/Partida1Theme.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    altera_musica = False

    cronometro.inicio = pygame.time.get_ticks()
    cronometro.tempo_encerrado = False

    while estados["Rodando_Partida"]:
        tela.fill(BRANCO)
        tela.blit(Fundo,(0,0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Partida"] = False
                estados["Rodando_Jogo"] = False
        
        TelaPokemons(tela,eventos,estados)
        TelaOpções(tela,eventos,estados)
        TelaOutros(tela,eventos,estados)

        if Turno > 5 and not altera_musica:
            pygame.mixer.music.load("Musicas/Partida2theme.ogg")
            pygame.mixer.music.play(-1) 
            altera_musica = True  

        VidaTotal1 = 0
        for i in range(len(Jogador1.pokemons)):
            VidaTotal1 += Jogador1.pokemons[i].Vida
        if VidaTotal1 <= 0:
            Vencedor = Jogador2
            Perdedor = Jogador1
            A.Fim_da_partida(estados)

        VidaTotal2 = 0
        for i in range(len(Jogador2.pokemons)):
            VidaTotal2 += Jogador2.pokemons[i].Vida
        if VidaTotal2 <= 0:
            Vencedor = Jogador1
            Perdedor = Jogador2
            A.Fim_da_partida(estados)

        for mensagem in mensagens_passageiras[:]:
                mensagem.desenhar(tela)
                mensagem.atualizar()
                if not mensagem.ativa:
                    mensagens_passageiras.remove(mensagem)

        pygame.display.update()
        relogio.tick(60)

def Carregar_Imagens():
    global ImagensPokemon100
    global ImagensPokemon180
    global ImagensPokebolas
    global ImagensItens
    global OutrosIMG

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

    GbulbasaurIMG = GV.Carregar_Imagem("imagens/pokemons/bulbasaur.png", (180,180),"PNG")
    GivysaurIMG = GV.Carregar_Imagem("imagens/pokemons/ivysaur.png", (180,180),"PNG")
    GvenusaurIMG = GV.Carregar_Imagem("imagens/pokemons/venusaur.png", (180,180),"PNG")
    GcharmanderIMG = GV.Carregar_Imagem("imagens/pokemons/charmander.png", (180,180),"PNG")
    GcharmeleonIMG = GV.Carregar_Imagem("imagens/pokemons/charmeleon.png", (180,180),"PNG")
    GcharizardIMG = GV.Carregar_Imagem("imagens/pokemons/charizard.png", (180,180),"PNG")
    GsquirtleIMG = GV.Carregar_Imagem("imagens/pokemons/squirtle.png", (180,180),"PNG")
    GwartortleIMG = GV.Carregar_Imagem("imagens/pokemons/wartortle.png", (180,180),"PNG")
    GblastoiseIMG = GV.Carregar_Imagem("imagens/pokemons/blastoise.png", (180,180),"PNG")
    GmachopIMG = GV.Carregar_Imagem("imagens/pokemons/machop.png", (180,180),"PNG")
    GmachokeIMG = GV.Carregar_Imagem("imagens/pokemons/machoke.png", (180,180),"PNG")
    GmachampIMG = GV.Carregar_Imagem("imagens/pokemons/machamp.png", (180,180),"PNG")
    GgastlyIMG = GV.Carregar_Imagem("imagens/pokemons/gastly.png", (180,180),"PNG")
    GhaunterIMG = GV.Carregar_Imagem("imagens/pokemons/haunter.png", (180,180),"PNG")
    GgengarIMG = GV.Carregar_Imagem("imagens/pokemons/gengar.png", (180,180),"PNG")
    GgeodudeIMG = GV.Carregar_Imagem("imagens/pokemons/geodude.png", (180,180),"PNG")
    GgravelerIMG = GV.Carregar_Imagem("imagens/pokemons/graveler.png", (180,180),"PNG")
    GgolemIMG = GV.Carregar_Imagem("imagens/pokemons/golem.png", (180,180),"PNG")
    GcaterpieIMG = GV.Carregar_Imagem("imagens/pokemons/caterpie.png", (180,180),"PNG")
    GmetapodIMG = GV.Carregar_Imagem("imagens/pokemons/metapod.png", (180,180),"PNG")
    GbutterfreeIMG = GV.Carregar_Imagem("imagens/pokemons/butterfree.png", (180,180),"PNG")
    GabraIMG = GV.Carregar_Imagem("imagens/pokemons/abra.png", (180,180),"PNG")
    GkadabraIMG = GV.Carregar_Imagem("imagens/pokemons/kadabra.png", (180,180),"PNG")
    GalakazamIMG = GV.Carregar_Imagem("imagens/pokemons/alakazam.png", (180,180),"PNG")
    GdratiniIMG = GV.Carregar_Imagem("imagens/pokemons/dratini.png", (180,180),"PNG")
    GdragonairIMG = GV.Carregar_Imagem("imagens/pokemons/dragonair.png", (180,180),"PNG")
    GdragoniteIMG = GV.Carregar_Imagem("imagens/pokemons/dragonite.png", (180,180),"PNG")
    GzoruaIMG = GV.Carregar_Imagem("imagens/pokemons/zorua.png", (180,180),"PNG")
    GzoroarkIMG = GV.Carregar_Imagem("imagens/pokemons/zoroark.png", (180,180),"PNG")
    GpikachuIMG = GV.Carregar_Imagem("imagens/pokemons/pikachu.png", (180,180),"PNG")
    GraichuIMG = GV.Carregar_Imagem("imagens/pokemons/raichu.png", (180,180),"PNG")
    GmagikarpIMG = GV.Carregar_Imagem("imagens/pokemons/magikarp.png", (180,180),"PNG")
    GyaradosIMG = GV.Carregar_Imagem("imagens/pokemons/gyarados.png", (180,180),"PNG")
    GjigglypuffIMG = GV.Carregar_Imagem("imagens/pokemons/jigglypuff.png", (180,180),"PNG")
    GwigglytuffIMG = GV.Carregar_Imagem("imagens/pokemons/wigglytuff.png", (180,180),"PNG")
    GmagnemiteIMG = GV.Carregar_Imagem("imagens/pokemons/magnemite.png", (180,180),"PNG")
    GmagnetonIMG = GV.Carregar_Imagem("imagens/pokemons/magneton.png", (180,180),"PNG")
    GsnorlaxIMG = GV.Carregar_Imagem("imagens/pokemons/snorlax.png", (180,180),"PNG")
    GaerodactylIMG = GV.Carregar_Imagem("imagens/pokemons/aerodactyl.png", (180,180),"PNG")
    GjynxIMG = GV.Carregar_Imagem("imagens/pokemons/jynx.png", (180,180),"PNG")
    GmewtwoIMG = GV.Carregar_Imagem("imagens/pokemons/mewtwo.png", (180,180),"PNG")

    EsmeraldaIMG = GV.Carregar_Imagem("imagens/itens/esmeralda.png", (30,30), "PNG")
    CitrinoIMG = GV.Carregar_Imagem("imagens/itens/citrino.png", (30,30), "PNG")
    RubiIMG = GV.Carregar_Imagem("imagens/itens/rubi.png", (30,30), "PNG")
    SafiraIMG = GV.Carregar_Imagem("imagens/itens/safira.png", (30,30), "PNG")
    AmetistaIMG = GV.Carregar_Imagem("imagens/itens/ametista.png", (30,30), "PNG")
    ColetorIMG = GV.Carregar_Imagem("imagens/itens/coletor.png", (30,30), "PNG")
    CaixaIMG = GV.Carregar_Imagem("imagens/itens/caixa.png", (30,30), "PNG")
    CaixoteIMG = GV.Carregar_Imagem("imagens/itens/caixote.png", (30,30), "PNG")
    PocaoIMG = GV.Carregar_Imagem("imagens/itens/poçao.png", (30,30), "PNG")
    SuperPocaoIMG = GV.Carregar_Imagem("imagens/itens/super_poçao.png", (30,30), "PNG")
    HiperPocaoIMG = GV.Carregar_Imagem("imagens/itens/hiper_poçao.png", (30,30), "PNG")
    MegaPocaoIMG = GV.Carregar_Imagem("imagens/itens/mega_poçao.png", (30,30), "PNG")
    PokeballIMG = GV.Carregar_Imagem("imagens/itens/PokeBall.png", (30,30),"PNG")
    GreatBallIMG = GV.Carregar_Imagem("imagens/itens/GreatBall.png", (30,30),"PNG")
    UltraBallIMG = GV.Carregar_Imagem("imagens/itens/UltraBall.png", (30,30),"PNG")
    MasterBallIMG = GV.Carregar_Imagem("imagens/itens/MasterBall.png", (30,30),"PNG")


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

    ImagensPokemon100 = {
    "bulbasaur": MbulbasaurIMG,
    "charmander": McharmanderIMG,
    "squirtle": MsquirtleIMG,
    "machop": MmachopIMG,
    "gastly": MgastlyIMG,
    "geodude": MgeodudeIMG,
    "caterpie": McaterpieIMG,
    "abra": MabreIMG,
    "dratini": MdratiniIMG,
    "zorua": MzoruaIMG,
    "pikachu": MpikachuIMG,
    "magikarp": MmagikarpIMG,
    "jigglypuff": MjigglypuffIMG,
    "magnemite": MMagnemiteIMG,
    "snorlax": MsnorlaxIMG,
    "aerodactyl": MaerodactylIMG,
    "jynx": MjynxIMG,
    "mewtwo": MmewtwoIMG
    }

    ImagensPokemon180 = {
    "bulbasaur": GbulbasaurIMG,
    "ivysaur": GivysaurIMG,
    "venusaur": GvenusaurIMG,
    "charmander": GcharmanderIMG,
    "charmeleon": GcharmeleonIMG,
    "charizard": GcharizardIMG,
    "squirtle": GsquirtleIMG,
    "wartortle": GwartortleIMG,
    "blastoise": GblastoiseIMG,
    "machop": GmachopIMG,
    "machoke": GmachokeIMG,
    "machamp": GmachampIMG,
    "gastly": GgastlyIMG,
    "haunter": GhaunterIMG,
    "gengar": GgengarIMG,
    "geodude": GgeodudeIMG,
    "graveler": GgravelerIMG,
    "golem": GgolemIMG,
    "caterpie": GcaterpieIMG,
    "metapod": GmetapodIMG,
    "butterfree": GbutterfreeIMG,
    "abra": GabraIMG,
    "kadabra": GkadabraIMG,
    "alakazam": GalakazamIMG,
    "dratini": GdratiniIMG,
    "dragonair": GdragonairIMG,
    "dragonite": GdragoniteIMG,
    "zorua": GzoruaIMG,
    "zoroark": GzoroarkIMG,
    "pikachu": GpikachuIMG,
    "raichu": GraichuIMG,
    "magikarp": GmagikarpIMG,
    "gyarados": GyaradosIMG,
    "jigglypuff": GjigglypuffIMG,
    "wigglytuff": GwigglytuffIMG,
    "magnemite": GmagnemiteIMG,
    "magneton": GmagnetonIMG,
    "snorlax": GsnorlaxIMG,
    "aerodactyl": GaerodactylIMG,
    "jynx": GjynxIMG,
    "mewtwo": GmewtwoIMG
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
            estado_global=estado, eventos=eventos,
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
            estado_global=estado, eventos=eventos,
            funcao_esquerdo=lambda i=i: seleciona(f"inimigo{i+1}", player, inimigo),
            funcao_direito=lambda i=i: vizualiza(f"inimigo{i+1}", player, inimigo),
            desfazer_esquerdo=lambda: desseleciona(), desfazer_direito=lambda: oculta(),
            tecla_esquerda=pygame.K_1, tecla_direita=None, som=clique)

    if PokemonS is not None:
        estado_animacao_status["ativo"] = True
        estado_animacao_status["x_tabela"] = 2000
        estado_animacao_status["x_botao1"] = 2000
        estado_animacao_status["x_botao2"] = 2000

        S(PokemonS,tela,eventos,player,inimigo)
   
    if PokemonV is not None:
        V(PokemonV,tela,eventos,inimigo) 
    
    for i in range(len(player.pokemons)):
        tela.blit(ImagensPokemon180[player.pokemons[i].nome],((425 + i * 190),890))

    for i in range(len(inimigo.pokemons)):
        tela.blit(ImagensPokemon180[inimigo.pokemons[i].nome],((1315 - i * 190),0))

    for i in range(len(player.pokemons)):
        barra_vida(tela, 420 + i * 190, 870, 190, 20, player.pokemons[i].Vida, player.pokemons[i].VidaMax,(100,100,100),player.pokemons[i].nome)
    
    for i in range(len(inimigo.pokemons)):
        barra_vida(tela, 1310 - i * 190, 190, 190, 20, inimigo.pokemons[i].Vida, inimigo.pokemons[i].VidaMax,(100,100,100),inimigo.pokemons[i].nome)

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

    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,lambda: A.fechar_jogo(estados), Fonte50, B1, 3, pygame.K_ESCAPE, False, eventos)

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
