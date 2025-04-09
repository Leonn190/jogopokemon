import pygame
import sys
import GeradoresVisuais as GV
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA)

# evita estragar a resoluçao mesmo com o zoom de 125% do meu computador
import ctypes
try:
    ctypes.windll.user32.SetProcessDPIAware()
except:
    pass

pygame.init()

tela = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Jogo Pokémon")
info = pygame.display.Info()
largura_tela = info.current_w
altura_tela = info.current_h

mensagens_terminal = []

informaçoesp1 = []
informaçoesp2 = []

estado = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
}

estado2 = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
}

B1 = {"estado": False}
B2 = {"estado": False}

relogio = pygame.time.Clock()

estados = {
    "Rodando_Jogo": True,
    "Rodando_Menu": True,
    "Rodando_PréPartida": False,
    "Rodando_Partida": False,
}

def Menu(estados):
    while estados["Rodando_Menu"]:
        tela.fill(BRANCO)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Menu"] = False
                estados["Rodando_Jogo"] = False

        GV.Botao(tela, "Iniciar a partida", (560, 350, 500, 140), CINZA, PRETO, DOURADO,
                 lambda: A.iniciar_partida(estados), Fonte50, B1, 4, None, True, eventos)

        GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

        GV.Terminal(tela, (0, 700, 800, 180), Fonte30, AZUL_CLARO, PRETO)

        pygame.display.update()
        relogio.tick(60)

def PréPartida(estados):
    # itens para deixar as barras de texto funcionais
    texto1 = ""
    selecionado1 = False

    texto2 = ""
    selecionado2 = False

    while estados["Rodando_PréPartida"]:
        tela.fill(AZUL_SUPER_CLARO)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_PréPartida"] = False
                estados["Rodando_Jogo"] = False

        GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

        GV.Texto(tela, "Jogador 1", (360, 50), Fonte70, PRETO)
        GV.Texto(tela, "Jogador 2", (1320, 50), Fonte70, PRETO)

        GV.Texto(tela, "Escreva seu Nome:", (190, 485), Fonte40, PRETO)
        GV.Texto(tela, "Escreva seu Nome:", (1170, 485), Fonte40, PRETO)

        texto1, selecionado1 = GV.Barra_De_Texto(
    tela, (500, 480, 300, 40), Fonte30, 
    CINZA, PRETO, PRETO, eventos, texto1,
    A.Nome_p1, AZUL,selecionado1)

        texto2, selecionado2 = GV.Barra_De_Texto(
    tela, (1470, 480, 300, 40), Fonte30, 
    CINZA, PRETO, PRETO, eventos, texto2,
    A.Nome_p2, AZUL,selecionado2)

        GV.Botao_Selecao(
    tela,
    (80, 150, 240, 240),
    "",
    Fonte30,
    cor_fundo=VERDE_CLARO,
    cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO,   
    cor_borda_direita=None,
    cor_passagem=AMARELO,
    id_botao="BulbasaurP1",   
    estado_global=estado,
    eventos=eventos,
    funcao_esquerdo=A.Pokemon_inicial,
    funcao_direito=None,
    desfazer_esquerdo=A.Remover_inicial,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_1,
    tecla_direita=None)
        GV.Imagem(tela, "imagens/bulbasaur.png",(80,150,235,235))

        GV.Botao_Selecao(
    tela,
    (350, 150, 240, 240),
    "",
    Fonte30,
    cor_fundo=VERMELHO_CLARO,
    cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO,   
    cor_borda_direita=None,
    cor_passagem=AMARELO,
    id_botao="CharmanderP1",   
    estado_global=estado,
    eventos=eventos,
    funcao_esquerdo=A.Pokemon_inicial,
    funcao_direito=None,
    desfazer_esquerdo=A.Remover_inicial,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_2,
    tecla_direita=None)
        GV.Imagem(tela, "imagens/charmander.png",(350,150,235,235))
        
        GV.Botao_Selecao(
    tela,
    (620, 150, 240, 240),
    "",
    Fonte30,
    cor_fundo=AZUL_CLARO,
    cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO,   
    cor_borda_direita=None,
    cor_passagem=AMARELO,
    id_botao="SquirtleP1",   
    estado_global=estado,
    eventos=eventos,
    funcao_esquerdo=A.Pokemon_inicial,
    funcao_direito=None,
    desfazer_esquerdo=A.Remover_inicial,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_3,
    tecla_direita=None)
        GV.Imagem(tela, "imagens/squirtle.png",(620,150,235,235))

        for i in range(5):
            GV.Botao_Selecao(
    tela,
    (((i + 1 * 60) + (i * 160)), 650, 150, 150),
    "",
    Fonte30,
    cor_fundo=AZUL_CLARO,
    cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO,   
    cor_borda_direita=None,
    cor_passagem=AMARELO,
    id_botao="SquirtleP1",   
    estado_global=estado,
    eventos=eventos,
    funcao_esquerdo=A.Pokemon_inicial,
    funcao_direito=None,
    desfazer_esquerdo=A.Remover_inicial,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_3,
    tecla_direita=None)
            GV.Imagem(tela, "imagens/loja.png",(((i + 1 * 72) + (i * 160)),660,120,120))

    # outro lado
        GV.Reta_Central(tela, 1920, 1080, PRETO, 4)

        GV.Botao_Selecao(
    tela,
    (1600, 150, 240, 240),
    "",
    Fonte30,
    cor_fundo=AZUL_CLARO,
    cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO,   
    cor_borda_direita=None,
    cor_passagem=AMARELO,
    id_botao="Squirtlep2",   
    estado_global=estado2,
    eventos=eventos,
    funcao_esquerdo=A.Pokemon_inicial,
    funcao_direito=None,
    desfazer_esquerdo=A.Remover_inicial,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_9,
    tecla_direita=None)
        GV.Imagem(tela, "imagens/squirtle.png",(1600,150,235,235))

        GV.Botao_Selecao(
    tela,
    (1330, 150, 240, 240),
    "",
    Fonte30,
    cor_fundo=VERMELHO_CLARO,
    cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO,   
    cor_borda_direita=None,
    cor_passagem=AMARELO,
    id_botao="CharmanderP2",   
    estado_global=estado2,
    eventos=eventos,
    funcao_esquerdo=A.Pokemon_inicial,
    funcao_direito=None,
    desfazer_esquerdo=A.Remover_inicial,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_8,
    tecla_direita=None)
        GV.Imagem(tela, "imagens/charmander.png",(1330,150,235,235))
        
        GV.Botao_Selecao(
    tela,
    (1060, 150, 240, 240),
    "",
    Fonte30,
    cor_fundo=VERDE_CLARO,
    cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO,   
    cor_borda_direita=None,
    cor_passagem=AMARELO,
    id_botao="BulbasaurP2",   
    estado_global=estado2,
    eventos=eventos,
    funcao_esquerdo=A.Pokemon_inicial,
    funcao_direito=None,
    desfazer_esquerdo=A.Remover_inicial,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_7,
    tecla_direita=None)
        GV.Imagem(tela, "imagens/Bulbasaur.png",(1060,150,235,235))

        GV.Terminal(tela, (0, 900, 960, 180), Fonte30, AZUL_CLARO, PRETO)

        pygame.display.update()
        relogio.tick(60)

def Partida(estados):
    while estados["Rodando_Partida"]:
        tela.fill(BRANCO)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Partida"] = False
                estados["Rodando_Jogo"] = False

        GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

        GV.Terminal(tela, (0, 700, 800, 250), Fonte30, AZUL_CLARO, PRETO)

        pygame.display.update()
        relogio.tick(60)

while estados["Rodando_Jogo"]:
    if estados["Rodando_Menu"]:
        Menu(estados)
    elif estados["Rodando_PréPartida"]:
        PréPartida(estados)
    elif estados["Rodando_Partida"]:
        Partida(estados)

pygame.quit()
sys.exit()
