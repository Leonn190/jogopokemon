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
        

PokemonS = None
PokemonV = None
informacao = None
Visor = None
PokebolaSelecionada = None


Centro = []
ver_centro = "n"

LojaItensP = 3
LojaPokeP = 4
LojaAmpliP = 3
LojaEnerP = 1

Turno = 1
tempo_restante = 0



def Ao_terminar(player,inimigo):
    global Turno
    global mensagens_terminal
    global Centro

    player.ouro += 2 + (tempo_restante // 20)

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
 
def cronometro(tela, espaço, duracao_segundos, fonte, cor_fundo, cor_borda, cor_tempo, ao_terminar, turno_atual, player, inimigo):
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

    return player, inimigo

def passar_turno(tela, texto, espaço, cor_normal, cor_borda, cor_passagem,
                        Fonte, estado_clique, player, inimigo, grossura=2,
                        tecla_atalho=None, mostrar_na_tela=True, eventos=None):

    global Turno
    global mensagens_terminal
    global Centro

    x, y, largura, altura = espaço
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    mouse_sobre = x <= mouse[0] <= x + largura and y <= mouse[1] <= y + altura

    tecla_ativada = False
    if tecla_atalho and eventos:
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == tecla_atalho:
                tecla_ativada = True

    cor_borda_atual = cor_passagem if mouse_sobre or tecla_ativada else cor_borda

    if mostrar_na_tela:
        pygame.draw.rect(tela, cor_normal, (x, y, largura, altura))
        pygame.draw.rect(tela, cor_borda_atual, (x, y, largura, altura), grossura)

        if texto:
            texto_render = Fonte.render(texto, True, (0, 0, 0))
            texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
            tela.blit(texto_render, texto_rect)

    # Clique com mouse (executa apenas uma vez)
    if mouse_sobre and clique[0] == 1:
        if not estado_clique.get("pressionado", False):
            estado_clique["pressionado"] = True
            Fecha()
            desseleciona()
            oculta()
            player.ouro += 2 + (tempo_restante // 20)
            player, inimigo = inimigo, player
            Centro = G.spawn_do_centro(Centro)
            Centro = G.spawn_do_centro(Centro)
            Turno += 1
            mensagens_terminal = []
            GV.adicionar_mensagem(f"Novo turno de {player.nome}!")
    else:
        estado_clique["pressionado"] = False

    # Clique com tecla (executa apenas uma vez)
    if tecla_ativada:
        if not estado_clique.get("pressionado_tecla", False):
            estado_clique["pressionado_tecla"] = True
            Fecha()
            desseleciona()
            oculta()
            player.ouro += 2 + (tempo_restante // 20)
            player, inimigo = inimigo, player
            Centro = G.spawn_do_centro(Centro)
            Centro = G.spawn_do_centro(Centro)
            Turno += 1
            mensagens_terminal = []
            GV.adicionar_mensagem(f"Novo turno de {player.nome}!")
    elif tecla_atalho:
        # Libera o clique da tecla ao soltar
        for evento in eventos:
            if evento.type == pygame.KEYUP and evento.key == tecla_atalho:
                estado_clique["pressionado_tecla"] = False

    
    return player, inimigo, 

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
                GV.adicionar_mensagem(f"Parabens, você capturou um {novo_pokemon.nome} utilizando uma {Pokebola_usada['nome']}")
                Centro.remove(pokemon)
                return
            else:
                GV.adicionar_mensagem("sua lista de pokemon está cheia")
        else:
            GV.adicionar_mensagem("Voce falhou em capturar o pokemon, que pena")
    else:
        GV.adicionar_mensagem("Selecione uma pokebola para capturar um pokemon")

def barra_vida(tela, x, y, largura, altura, vida_atual, vida_maxima, cor_fundo=(100, 100, 100)):
    # Proteção contra divisão por zero
    if vida_maxima <= 0:
        vida_maxima = 1

    # Calcula proporção
    proporcao = vida_atual / vida_maxima
    largura_vida = int(largura * proporcao)

    # Define cor da barra com base na porcentagem
    if proporcao > 0.6:
        cor_vida = (0, 200, 0)        # Verde
    elif proporcao > 0.3:
        cor_vida = (255, 200, 0)      # Amarelo
    else:
        cor_vida = (200, 0, 0)        # Vermelho

    cor_borda = (0, 0, 0)  # Preto

    # Barra de fundo (vazia)
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    # Barra de vida (preenchida)
    pygame.draw.rect(tela, cor_vida, (x, y, largura_vida, altura))

    # Borda
    pygame.draw.rect(tela, cor_borda, (x, y, largura, altura), 2)

def atacaN(Pokemon,player,inimigo,ID):
    alvo = inimigo.pokemons[ID]
    Pokemon.atacar(alvo,player,inimigo,"N")

def atacaS(Pokemon,player,inimigo,ID):
    alvo = inimigo.pokemons[ID]
    Pokemon.atacar(alvo,player,inimigo,"S")
    

mensagens_terminal = []

estado = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
}

estadoInfo = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
}

estadoOutros = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
}

estadoPokebola = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
}

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

def A(Visor,tela,eventos,player,inimigo):
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
            GV.Botao(tela, "", (418, (310 + i * 30), 30, 30), CINZA, PRETO, AZUL,
                 lambda: player.usar_item(i,PokemonS), Fonte50, B6, 1, None, True, eventos)

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
            
        for i, item in enumerate(player.inventario):
            if item.get("classe") == "pokebola":
                x = 330
                y = 260 + i * 60
                GV.Botao_Selecao(
                tela, (x, y, 60, 60),
                f"", Fonte28,
                cor_fundo=AZUL_SUPER_CLARO, cor_borda_normal=PRETO,
                cor_borda_esquerda=VERMELHO, cor_borda_direita=None,
                cor_passagem=AMARELO, id_botao=i,   
                estado_global=estadoPokebola, eventos=eventos,
                funcao_esquerdo=lambda:seleciona_pokebola(item), funcao_direito=None,
                desfazer_esquerdo=lambda:desseleciona_pokebola(), desfazer_direito=None,
                tecla_esquerda=None, tecla_direita=None, grossura=1)

def S(PokemonS,tela,eventos,player,inimigo):
    nomeS = f"Status do {PokemonS.nome}"

    colunasS = ["nome", "valor", "IV"]  # 3 colunas: nome, valor, IV

    # Linhas com os atributos e o valor "caju" para IV
    linhasS = [
        ["Vida", (PokemonS.Vida), "caju"],
        ["ATK", (PokemonS.Atk), "caju"],
        ["Sp ATK", (PokemonS.Atk_sp), "caju"],
        ["DEF", (PokemonS.Def), "caju"],
        ["Sp DEF", (PokemonS.Def_sp), "caju"],
        ["VEL", (PokemonS.vel), "Tipo:"],
        ["Custo", (PokemonS.custo), PokemonS.tipo[0]],
        ["XP", (PokemonS.xp_atu), PokemonS.tipo[1] if len(PokemonS.tipo) > 1 else ""]
    ]

    # Chamada da função Tabela
    GV.Tabela(nomeS, colunasS, linhasS, tela, 1570, 570, 350, Fonte28, Fonte30, AZUL_SUPER_CLARO, PRETO, AZUL_CLARO)

    GV.Botao_Selecao(
    tela, (1570, 860, 175, 30),
    f"{PokemonS.ataque_normal["nome"]}", Fonte28,
    cor_fundo=AZUL_SUPER_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Atk Norm.S",   
    estado_global=estadoInfo, eventos=eventos,
    funcao_esquerdo=lambda:informa("Atk Norm",PokemonS), funcao_direito=None,
    desfazer_esquerdo=lambda:desinforma(), desfazer_direito=None,
    tecla_esquerda=None, tecla_direita=None, grossura=1)
    GV.Botao_Selecao(
    tela, (1745, 860, 175, 30),
    f"{PokemonS.ataque_especial["nome"]}", Fonte28,
    cor_fundo=AZUL_SUPER_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Atk SP.S",   
    estado_global=estadoInfo, eventos=eventos,
    funcao_esquerdo=lambda:informa("Atk SPS",PokemonS), funcao_direito=None,
    desfazer_esquerdo=lambda:desinforma(), desfazer_direito=None,
    tecla_esquerda=None, tecla_direita=None, grossura=1)

    

    for i in range(len(inimigo.pokemons)):
        BI = BA[i]
        BJ = BA[i+6]

        GV.Botao(tela, "", (1435 - i * 190, 210, 40, 55), LARANJA, PRETO, VERDE_CLARO,
                 lambda: atacaN(PokemonS,player,inimigo,BI["ID"]), Fonte50, BI, 2, None, True, eventos)
        GV.Botao(tela, "", (1335 - i * 190, 210, 40, 55), ROXO, PRETO, VERDE_CLARO,
                 lambda: atacaS(PokemonS,player,inimigo,BJ["ID"]), Fonte50, BJ, 2, None, True, eventos)


def V(PokemonV,tela,eventos,inimigo):
    nomeV = f"Status do {PokemonV.nome}"

    colunasV = ["nome", "valor", "IV"]  # 3 colunas: nome, valor, IV

    # Linhas com os atributos e o valor "caju" para IV
    linhasV = [
        ["Vida", (PokemonV.Vida), "caju"],
        ["ATK", (PokemonV.Atk), "caju"],
        ["Sp ATK", (PokemonV.Atk_sp), "caju"],
        ["DEF", (PokemonV.Def), "caju"],
        ["Sp DEF", (PokemonV.Def_sp), "caju"],
        ["VEL", (PokemonV.vel), "Tipo:"],
        ["Custo", (PokemonV.custo), PokemonV.tipo[0]],
        ["XP", (PokemonV.xp_atu), PokemonV.tipo[1] if len(PokemonV.tipo) > 1 else ""]
    ]

    if PokemonV in inimigo.pokemons:
        GV.Tabela(nomeV, colunasV, linhasV, tela, 1570, 240, 350, Fonte28,Fonte30, VERMELHO_SUPER_CLARO, PRETO, VERMELHO_CLARO)

        GV.Botao_Selecao(
        tela, (1570, 530, 175, 30),
        f"{PokemonV.ataque_normal["nome"]}", Fonte28,
        cor_fundo=VERMELHO_SUPER_CLARO, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
        cor_passagem=AMARELO, id_botao="Atk Norm.V",   
        estado_global=estadoInfo, eventos=eventos,
        funcao_esquerdo=lambda:informa("Atk Norm.V",PokemonS), funcao_direito=None,
        desfazer_esquerdo=lambda:desinforma(), desfazer_direito=None,
        tecla_esquerda=pygame.K_1, tecla_direita=None, grossura=1)
        GV.Botao_Selecao(
        tela, (1745, 530, 175, 30),
        f"{PokemonV.ataque_especial["nome"]}", Fonte28,
        cor_fundo=VERMELHO_SUPER_CLARO, cor_borda_normal=PRETO,
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
    
def TelaPartida(tela,eventos,estados,player,inimigo):
    global PokemonS
    global PokemonV
    global informacao
    global Visor

    global LojaItensP
    global LojaPokeP
    global LojaAmpliP
    global LojaEnerP

    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B1, 3, pygame.K_ESCAPE, False, eventos)

    player, inimigo = passar_turno(tela, "Passar Turno", (1620, 1000, 300, 80), CINZA, PRETO, AZUL,
                  Fonte50, B7, player, inimigo, 3, None, True, eventos)

    GV.Terminal(tela, (0, 850, 420, 230), Fonte20, AZUL_CLARO, PRETO)

    GV.Texto_caixa(tela,player.nome,(0, 800, 420, 50),Fonte50,AZUL,PRETO) 
    GV.Texto_caixa(tela,inimigo.nome,(1500, 0, 420, 50),Fonte50,VERMELHO_CLARO,PRETO)
    GV.Texto_caixa(tela,f"Seu ouro: {player.ouro}",(210, 740, 210, 60),Fonte40,LARANJA,PRETO) 

    player, inimigo = cronometro(tela, (0, 60, 150, 40), 200, Fonte40, CINZA, PRETO, AMARELO, lambda:Ao_terminar(player,inimigo),Turno,player,inimigo)

    GV.Texto_caixa(tela,str(LojaItensP),(1525, 158, 50, 20),Fonte20,CINZA,PRETO,2)
    GV.Botao(tela, "", (1510, 80, 80, 80), CINZA, PRETO, VERDE_CLARO,
                 lambda: G.gera_item(B2["ID"],player,LojaItensP), Fonte50, B2, 3, None, True, eventos)
    
    GV.Texto_caixa(tela,str(LojaPokeP),(1605, 158, 50, 20),Fonte20,CINZA,PRETO,2)
    GV.Botao(tela, "", (1590, 80, 80, 80), CINZA, PRETO, VERDE_CLARO,
                 lambda: G.gera_item(B3["ID"],player,LojaPokeP), Fonte50, B3, 3, None, True, eventos)
    
    GV.Texto_caixa(tela,str(LojaAmpliP),(1685, 158, 50, 20),Fonte20,CINZA,PRETO,2)
    GV.Botao(tela, "", (1670, 80, 80, 80), CINZA, PRETO, VERDE_CLARO,
                 lambda: G.gera_item(B4["ID"],player,LojaAmpliP), Fonte50, B4, 3, None, True, eventos)
    
    GV.Texto_caixa(tela,str(LojaEnerP),(1765, 158, 50, 20),Fonte20,CINZA,PRETO,2)
    GV.Botao(tela, "", (1750, 80, 80, 80), CINZA, PRETO, VERDE_CLARO,
                 lambda: G.gera_item(B5["ID"],player,LojaEnerP), Fonte50, B4, 3, None, True, eventos)

    GV.Botao_Selecao(
    tela, (0, 740, 70, 60),
    "", Fonte30,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERDE, cor_borda_direita=None,
    cor_passagem=AMARELO, id_botao="Inventario",   
    estado_global=estadoOutros, eventos=eventos,
    funcao_esquerdo=lambda:Abre("Inventario",player,inimigo), funcao_direito=None,
    desfazer_esquerdo=lambda:Fecha(), desfazer_direito=None,
    tecla_esquerda=pygame.K_1, tecla_direita=None)
    GV.Botao_Selecao(
    tela, (70, 740, 70, 60),
    "", Fonte30,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERDE, cor_borda_direita=None,
    cor_passagem=AMARELO, id_botao="Energias",   
    estado_global=estadoOutros, eventos=eventos,
    funcao_esquerdo=lambda:Abre("Energias",player,inimigo), funcao_direito=None,
    desfazer_esquerdo=lambda:Fecha(), desfazer_direito=None,
    tecla_esquerda=pygame.K_1, tecla_direita=None)
    GV.Botao_Selecao(
    tela, (140, 740, 70, 60),
    "", Fonte30,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERDE, cor_borda_direita=None,
    cor_passagem=AMARELO, id_botao="Centro",   
    estado_global=estadoOutros, eventos=eventos,
    funcao_esquerdo=lambda:Abre("Centro",player,inimigo), funcao_direito=None,
    desfazer_esquerdo=lambda:Fecha(), desfazer_direito=None,
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Texto_caixa(tela,f"Turno: {Turno}",(0, 0, 360, 60),Fonte70,AMARELO,PRETO) 

    GV.Botao_Selecao(
    tela, (420, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon1",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon1",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon1",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (610, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon2",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon2",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon2",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (800, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon3",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon3",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon3",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (990, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon4",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon4",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon4",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (1180, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon5",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon5",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon5",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (1370, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon6",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon6",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon6",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame. K_1, tecla_direita=None)



    GV.Botao_Selecao(
    tela, (1310, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo1",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo1",player,inimigo), funcao_direito=lambda:vizualiza("inimigo1",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (1120, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo2",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo2",player,inimigo), funcao_direito=lambda:vizualiza("inimigo2",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (930, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo3",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo3",player,inimigo), funcao_direito=lambda:vizualiza("inimigo3",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (740, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo4",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo4",player,inimigo), funcao_direito=lambda:vizualiza("inimigo4",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (550, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo5",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo5",player,inimigo), funcao_direito=lambda:vizualiza("inimigo5",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (360, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo6",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo6",player,inimigo), funcao_direito=lambda:vizualiza("inimigo6",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona(), desfazer_direito=lambda:oculta(),
    tecla_esquerda=pygame. K_1, tecla_direita=None)

    for i in range(len(player.pokemons)):
        barra_vida(tela, 420 + i * 190, 870, 190, 20, player.pokemons[i].Vida, player.pokemons[i].VidaMax)
    
    for i in range(len(inimigo.pokemons)):
        barra_vida(tela, 1310 - i * 190, 190, 190, 20, inimigo.pokemons[i].Vida, inimigo.pokemons[i].VidaMax)

    if PokemonS is not None:
        S(PokemonS,tela,eventos,player,inimigo)
   
    if PokemonV is not None:
        V(PokemonV,tela,eventos,inimigo)

    if Visor is not None:
        A(Visor,tela,eventos,player,inimigo)
         

    return player, inimigo

def Partida(tela,estados,relogio):
    global Turno

    Fundo = GV.Carregar_Imagem("imagens/fundos/fundo3.jpg", (1920,1080),)

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
    
    imagensPokemon100 = {
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

    imagensPokemon180 = {
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


    imagenspokebolas = {
        "pokebola": UPokeballIMG,
        "greatball": UGreatBallIMG,
        "ultraball": UUltraBallIMG,
        "masterball": UMasterBallIMG
    }

    from PygameAções import informaçoesp1, informaçoesp2

    Jogador1 = G.Gerador_player(informaçoesp1)
    Jogador2 = G.Gerador_player(informaçoesp2)

    for item in informaçoesp1[3:]:
        G.gera_item(item,Jogador1)

    for item in informaçoesp2[3:]:
        G.gera_item(item,Jogador2)

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

        player,inimigo = TelaPartida(tela,eventos,estados,player,inimigo)

        for i in range(len(player.pokemons)):
            tela.blit(imagensPokemon180[player.pokemons[i].nome],((430 + i * 190),890))

        for i in range(len(inimigo.pokemons)):
            tela.blit(imagensPokemon180[inimigo.pokemons[i].nome],((1320 - i * 190),0))

        tela.blit(InventárioIMG,(5,740))
        tela.blit(energiasIMG,(80,745))
        tela.blit(CentroIMG,(140,735))

        tela.blit(LojaItensIMG,(1515,85))
        tela.blit(LojaPokebolasIMG,(1595,85))
        tela.blit(LojaAmplificadoresIMG,(1675,85))
        tela.blit(LojaEnergiasIMG,(1760,88))

        if Turno > 5 and not altera_musica:
            pygame.mixer.music.load("Musicas/Partida2theme.ogg")
            pygame.mixer.music.play(-1)  # -1 = repetir para sempre
            altera_musica = True  # garante que só toca uma vez

        if ver_centro == "s":
            for i, item in enumerate(player.inventario):
                if item.get("classe") == "pokebola":
                    x = 332
                    y = 262 + i * 60
                    tela.blit(imagenspokebolas[item["nome"]],(x,y))
            
            x_inicial = 10
            y_inicial = 270

            for i in range(len(Centro)):
                coluna = i % 3        
                linha = i // 3        
                x = x_inicial + coluna * 109
                y = y_inicial + linha * 109
                tela.blit(imagensPokemon100[Centro[i]["nome"]],(x,y))



        pygame.display.update()
        relogio.tick(60)

