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

def seleciona(ID, player, inimigo, Visor):
    global PokemonS
    index_map = {
        "Pokemon1": 0,
        "Pokemon2": 1,
        "Pokemon3": 2,
        "Pokemon4": 3,
        "Pokemon5": 4,
        "Pokemon6": 5
    }
    idx = index_map[ID]
    if idx < len(player.pokemons):
            PokemonS = player.pokemons[idx]
    else:
        PokemonS = None
        GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")
        
def desseleciona(ID,player,inimigo,Visor):
    global PokemonS
    PokemonS = None

def vizualiza(ID,player,inimigo,Visor):
    global PokemonV
    index_map = {
        "Pokemon1": 0,
        "Pokemon2": 1,
        "Pokemon3": 2,
        "Pokemon4": 3,
        "Pokemon5": 4,
        "Pokemon6": 5
    }
    idx = index_map[ID]
    if idx < len(player.pokemons):
            PokemonV = player.pokemons[idx]
    else:
        PokemonV = None
        GV.adicionar_mensagem("Esse Pokémon ainda não foi adicionado.")      

def oculta(ID,player,inimigo,Visor):
    global PokemonV
    PokemonV = None
#

Visor = []

Visual = []

mensagens_terminal = []

estado = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
}

B1 = {"estado": False}
B2 = {"estado": False}

def caju(PokemonS,tela):
    nomeS = f"Status do {PokemonS.nome}"

    colunasS = ["nome", "valor", "IV"]  # 3 colunas: nome, valor, IV

    # Linhas com os atributos e o valor "caju" para IV
    linhasS = [
        ["Vida", str(PokemonS.Vida), "caju"],
        ["ATK", str(PokemonS.Atk), "caju"],
        ["Sp ATK", str(PokemonS.Atk_sp), "caju"],
        ["DEF", str(PokemonS.Def), "caju"],
        ["Sp DEF", str(PokemonS.Def_sp), "caju"],
        ["VEL", str(PokemonS.vel), "caju"],
        ["Custo", str(PokemonS.custo), "caju"],
        ["XP", str(PokemonS.xp_atu), "caju"]
    ]

    # Chamada da função Tabela
    GV.Tabela(nomeS, colunasS, linhasS, tela, 1520, 500, 400, Fonte25, AZUL_CLARO, PRETO, AMARELO)

estado1 = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
}

def TelaPartida(tela,eventos,estados,player,inimigo):
    global Visor
    global PokemonS

    GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

    player, inimigo = GV.passar_turno(tela, "Passar Turno", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                  Fonte50, B2, player, inimigo, 3, None, True, eventos)

    GV.Terminal(tela, (0, 850, 420, 230), Fonte25, AZUL_CLARO, PRETO)

    GV.Texto_caixa(tela,player.nome,(0, 800, 420, 50),Fonte50,AZUL,) 

    GV.Botao_Selecao(
    tela, (420, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon1",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon1",player,inimigo,Visor), funcao_direito=lambda:A.vizualiza("Pokemon1",player,inimigo,Visor),
    desfazer_esquerdo=lambda:desseleciona("Pokemon1",player,inimigo,Visor), desfazer_direito=lambda:A.oculta("Pokemon1",player,inimigo,Visor),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (610, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon2",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon2",player,inimigo,Visor), funcao_direito=lambda:A.vizualiza("Pokemon2",player,inimigo,Visor),
    desfazer_esquerdo=lambda:desseleciona(0,0,0,0), desfazer_direito=lambda:A.oculta(0,0,0,0),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (800, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon3",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon3",player,inimigo,Visor), funcao_direito=lambda:A.vizualiza("Pokemon3",player,inimigo,Visor),
    desfazer_esquerdo=lambda:desseleciona("Pokemon3",player,inimigo,Visor), desfazer_direito=lambda:A.oculta("Pokemon3",player,inimigo,Visor),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (990, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon4",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon4",player,inimigo,Visor), funcao_direito=lambda:A.vizualiza("Pokemon4",player,inimigo,Visor),
    desfazer_esquerdo=lambda:desseleciona("Pokemon4",player,inimigo,Visor), desfazer_direito=lambda:A.oculta("Pokemon4",player,inimigo,Visor),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (1180, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon5",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon5",player,inimigo,Visor), funcao_direito=lambda:A.vizualiza("Pokemon5",player,inimigo,Visor),
    desfazer_esquerdo=lambda:desseleciona("Pokemon5",player,inimigo,Visor), desfazer_direito=lambda:A.oculta("Pokemon5",player,inimigo,Visor),
    tecla_esquerda=pygame.K_1, tecla_direita=None)

    GV.Botao_Selecao(
    tela, (1370, 890, 190, 190),
    "", Fonte30,
    cor_fundo=AMARELO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL,
    cor_passagem=AMARELO, id_botao="Pokemon6",   
    estado_global=estado, eventos=eventos,
    funcao_esquerdo=lambda:seleciona("Pokemon6",player,inimigo,Visor), funcao_direito=lambda:A.vizualiza("Pokemon6",player,inimigo,Visor),
    desfazer_esquerdo=lambda:desseleciona("Pokemon6",player,inimigo,Visor), desfazer_direito=lambda:A.oculta("Pokemon",player,inimigo,Visor),
    tecla_esquerda=pygame. K_1, tecla_direita=None)


    if PokemonS is not None:
        S(PokemonS,tela)
    
    if PokemonV is not None:
         

    if Pok

    return player, inimigo

def Partida(tela,estados,relogio):
    global Visor

    bulbasaurIMG = GV.Carregar_Imagem("imagens/bulbasaur.png", (180,180),"PNG")
    charmanderIMG = GV.Carregar_Imagem("imagens/charmander.png", (180,180),"PNG")
    squirtleIMG = GV.Carregar_Imagem("imagens/squirtle.png", (180,180),"PNG")

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

        pygame.display.update()
        relogio.tick(60)

