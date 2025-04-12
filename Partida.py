import pygame
import GeradoresVisuais as GV
import Gerador2 as G
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte25, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)
        

PokemonS = None
PokemonV = None
informacao = None
Visor = None

Turno = 1

def passar_turno(tela, texto, espaço, cor_normal, cor_borda, cor_passagem,
                        Fonte, estado_clique, player, inimigo, grossura=2,
                        tecla_atalho=None, mostrar_na_tela=True, eventos=None):

    global Turno
    global mensagens_terminal

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
            player, inimigo = inimigo, player
            Turno += 1
            mensagens_terminal = []
            GV.adicionar_mensagem(f"Novo turno de {player.nome}!")
    else:
        estado_clique["pressionado"] = False

    # Clique com tecla (executa apenas uma vez)
    if tecla_ativada:
        if not estado_clique.get("pressionado_tecla", False):
            estado_clique["pressionado_tecla"] = True
            player, inimigo = inimigo, player
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
        
def desseleciona(ID,player,inimigo,):
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

def oculta(ID,player,inimigo,):
    global PokemonV
    global estadoInfo
    PokemonV = None
    estadoInfo["selecionado_esquerdo"] = None

def informa(ID,Pokemon):
    pass

def desinforma(ID,Pokemon):
    global estadoInfo
    estadoInfo["selecionado_esquerdo"] = None
    pass

def Abre(ID,player,inimigo):
    pass

def Fecha(ID,player,inimigo):
    pass

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


B1 = {"estado": False}
B2 = {"estado": False}

def S(PokemonS,tela,eventos):
    nomeS = f"Status do {PokemonS.nome}"

    colunasS = ["nome", "valor", "IV"]  # 3 colunas: nome, valor, IV

    # Linhas com os atributos e o valor "caju" para IV
    linhasS = [
        ["Vida", str(PokemonS.Vida), "caju"],
        ["ATK", str(PokemonS.Atk), "caju"],
        ["Sp ATK", str(PokemonS.Atk_sp), "caju"],
        ["DEF", str(PokemonS.Def), "caju"],
        ["Sp DEF", str(PokemonS.Def_sp), "caju"],
        ["VEL", str(PokemonS.vel), "Tipo:"],
        ["Custo", str(PokemonS.custo), PokemonS.tipo[0]],
        ["XP", str(PokemonS.xp_atu), PokemonS.tipo[1] if len(PokemonS.tipo) > 1 else ""]
    ]

    # Chamada da função Tabela
    GV.Tabela(nomeS, colunasS, linhasS, tela, 1570, 500, 350, Fonte25, AZUL_CLARO, PRETO, PRETO)

    GV.Botao_Selecao(
    tela, (1570, 790, 175, 30),
    f"{PokemonS.ataque_normal["nome"]}", Fonte25,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Atk Norm.S",   
    estado_global=estadoInfo, eventos=eventos,
    funcao_esquerdo=lambda:informa("Atk Norm",PokemonS), funcao_direito=None,
    desfazer_esquerdo=lambda:desinforma("Atk Norm",PokemonS), desfazer_direito=None,
    tecla_esquerda=None, tecla_direita=None)
    GV.Botao_Selecao(
    tela, (1745, 790, 175, 30),
    f"{PokemonS.ataque_especial["nome"]}", Fonte25,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Atk SP.S",   
    estado_global=estadoInfo, eventos=eventos,
    funcao_esquerdo=lambda:informa("Atk SPS",PokemonS), funcao_direito=None,
    desfazer_esquerdo=lambda:desinforma("Atk SP",PokemonS), desfazer_direito=None,
    tecla_esquerda=None, tecla_direita=None)

def V(PokemonV,tela,eventos):
    nomeS = f"Status do {PokemonV.nome}"

    colunasS = ["nome", "valor", "IV"]  # 3 colunas: nome, valor, IV

    # Linhas com os atributos e o valor "caju" para IV
    linhasS = [
        ["Vida", str(PokemonV.Vida), "caju"],
        ["ATK", str(PokemonV.Atk), "caju"],
        ["Sp ATK", str(PokemonV.Atk_sp), "caju"],
        ["DEF", str(PokemonV.Def), "caju"],
        ["Sp DEF", str(PokemonV.Def_sp), "caju"],
        ["VEL", str(PokemonV.vel), "Tipo:"],
        ["Custo", str(PokemonV.custo), PokemonV.tipo[0]],
        ["XP", str(PokemonV.xp_atu), PokemonV.tipo[1] if len(PokemonV.tipo) > 1 else ""]
    ]

    # Chamada da função Tabela
    GV.Tabela(nomeS, colunasS, linhasS, tela, 1570, 0, 350, Fonte25, AZUL_CLARO, PRETO, PRETO)

    GV.Botao_Selecao(
    tela, (1570, 290, 175, 30),
    f"{PokemonV.ataque_normal["nome"]}", Fonte25,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Atk Norm.V",   
    estado_global=estadoInfo, eventos=eventos,
    funcao_esquerdo=lambda:informa("Atk Norm.V",PokemonS), funcao_direito=None,
    desfazer_esquerdo=lambda:desinforma("Atk Norm.V",PokemonS), desfazer_direito=None,
    tecla_esquerda=pygame.K_1, tecla_direita=None)
    GV.Botao_Selecao(
    tela, (1745, 290, 175, 30),
    f"{PokemonS.ataque_especial["nome"]}", Fonte25,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Atk SP.V",   
    estado_global=estadoInfo, eventos=eventos,
    funcao_esquerdo=lambda:informa("Atk Norm.V",PokemonS), funcao_direito=None,
    desfazer_esquerdo=lambda:desinforma("Atk Norm.V",PokemonS), desfazer_direito=None,
    tecla_esquerda=pygame.K_1, tecla_direita=None)
    
def TelaPartida(tela,eventos,estados,player,inimigo):
    global PokemonS
    global PokemonV
    global informacao
    global Visor

    GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

    player, inimigo = passar_turno(tela, "Passar Turno", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                  Fonte50, B2, player, inimigo, 3, None, True, eventos)

    GV.Terminal(tela, (0, 850, 420, 230), Fonte25, AZUL_CLARO, PRETO)

    GV.Texto_caixa(tela,player.nome,(0, 800, 420, 50),Fonte50,AZUL,PRETO) 
    GV.Texto_caixa(tela,inimigo.nome,(0, 0, 420, 50),Fonte50,VERMELHO_CLARO,PRETO) 

    GV.Botao_Selecao(
    tela, (0, 740, 70, 60),
    "", Fonte30,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERDE, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Inventario",   
    estado_global=estadoOutros, eventos=eventos,
    funcao_esquerdo=lambda:Abre("Inventario",player,inimigo), funcao_direito=None,
    desfazer_esquerdo=lambda:Fecha("Inventario",player,inimigo), desfazer_direito=None,
    tecla_esquerda=pygame.K_1, tecla_direita=None)
    GV.Botao_Selecao(
    tela, (70, 740, 70, 60),
    "", Fonte30,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERDE, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Energias",   
    estado_global=estadoOutros, eventos=eventos,
    funcao_esquerdo=lambda:Abre("Energias",player,inimigo), funcao_direito=None,
    desfazer_esquerdo=lambda:Fecha("Energias",player,inimigo), desfazer_direito=None,
    tecla_esquerda=pygame.K_1, tecla_direita=None)
    GV.Botao_Selecao(
    tela, (140, 740, 70, 60),
    "", Fonte30,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERDE, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Centro",   
    estado_global=estadoOutros, eventos=eventos,
    funcao_esquerdo=lambda:Abre("Centro",player,inimigo), funcao_direito=None,
    desfazer_esquerdo=lambda:Fecha("Centro",player,inimigo), desfazer_direito=None,
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Texto_caixa(tela,f"Turno: {Turno}",(0, 500, 420, 50),Fonte50,AZUL,PRETO) 

    GV.Botao_Selecao(
    tela, (420, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon1",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon1",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon1",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("Pokemon1",player,inimigo), desfazer_direito=lambda:oculta("Pokemon1",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (610, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon2",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon2",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon2",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("Pokemon2",player,inimigo), desfazer_direito=lambda:oculta("Pokemon2",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (800, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon3",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon3",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon3",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("Pokemon3",player,inimigo), desfazer_direito=lambda:oculta("Pokemon3",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (990, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon4",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon4",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon4",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("Pokemon4",player,inimigo), desfazer_direito=lambda:oculta("Pokemon4",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (1180, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon5",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon5",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon5",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("Pokemon5",player,inimigo), desfazer_direito=lambda:oculta("Pokemon5",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (1370, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon6",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon6",player,inimigo), funcao_direito=lambda:vizualiza("Pokemon6",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("Pokemon6",player,inimigo), desfazer_direito=lambda:oculta("Pokemon",player,inimigo),
    tecla_esquerda=pygame. K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (420, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo1",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo1",player,inimigo), funcao_direito=lambda:vizualiza("inimigo1",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("inimigo1",player,inimigo), desfazer_direito=lambda:oculta("inimigo1",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (610, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo2",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo2",player,inimigo), funcao_direito=lambda:vizualiza("inimigo2",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("inimigo2",player,inimigo), desfazer_direito=lambda:oculta("inimigo2",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (800, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo3",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo3",player,inimigo), funcao_direito=lambda:vizualiza("inimigo3",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("inimigo3",player,inimigo), desfazer_direito=lambda:oculta("inimigo3",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (990, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo4",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo4",player,inimigo), funcao_direito=lambda:vizualiza("inimigo4",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("inimigo4",player,inimigo), desfazer_direito=lambda:oculta("inimigo4",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (1180, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo5",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo5",player,inimigo), funcao_direito=lambda:vizualiza("inimigo5",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("inimigo5",player,inimigo), desfazer_direito=lambda:oculta("inimigo5",player,inimigo),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (1370, 0, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="inimigo6",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("inimigo6",player,inimigo), funcao_direito=lambda:vizualiza("inimigo6",player,inimigo),
    desfazer_esquerdo=lambda:desseleciona("inimigo6",player,inimigo), desfazer_direito=lambda:oculta("inimigo6",player,inimigo),
    tecla_esquerda=pygame. K_1, tecla_direita=None)

    if PokemonS is not None:
        S(PokemonS,tela,eventos)
     
   
    if PokemonV is not None:
        V(PokemonV,tela,eventos)
         

    return player, inimigo

def Partida(tela,estados,relogio):

    bulbasaurIMG = GV.Carregar_Imagem("imagens/bulbasaur.png", (180,180),"PNG")
    charmanderIMG = GV.Carregar_Imagem("imagens/charmander.png", (180,180),"PNG")
    squirtleIMG = GV.Carregar_Imagem("imagens/squirtle.png", (180,180),"PNG")

    InventárioIMG = GV.Carregar_Imagem("imagens/inventario.png", (60,60),"PNG")
    energiasIMG = GV.Carregar_Imagem("imagens/energias.png", (50,50),"PNG")
    CentroIMG = GV.Carregar_Imagem("imagens/centro.png", (70,70),"PNG")

    imagens = {
    "bulbasaur": bulbasaurIMG,
    "charmander": charmanderIMG,
    "squirtle": squirtleIMG
}

    from PygameAções import informaçoesp1, informaçoesp2

    Jogador1 = G.Gerador_player(informaçoesp1)
    Jogador2 = G.Gerador_player(informaçoesp2)

    player = Jogador1
    inimigo = Jogador2

    pygame.mixer.music.load('Musicas/PartidaTheme.ogg')  
    pygame.mixer.music.set_volume(0.0)
    pygame.mixer.music.play(-1)

    while estados["Rodando_Partida"]:
        tela.fill(BRANCO)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Partida"] = False
                estados["Rodando_Jogo"] = False

        player,inimigo = TelaPartida(tela,eventos,estados,player,inimigo)

        for i in range(len(player.pokemons)):
            tela.blit(imagens[player.pokemons[i].nome],((420 + i * 200),890))

        for i in range(len(inimigo.pokemons)):
            tela.blit(imagens[inimigo.pokemons[i].nome],((420 + i * 200),0))

        tela.blit(InventárioIMG,(5,740))
        tela.blit(energiasIMG,(80,745))
        tela.blit(CentroIMG,(140,735))

        pygame.display.update()
        relogio.tick(60)

