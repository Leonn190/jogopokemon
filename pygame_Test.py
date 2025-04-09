import pygame
import sys
import GeradoresVisuais as GV
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,
    AMARELO, VERMELHO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA)

pygame.init()

tela = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Jogo Pokémon")
info = pygame.display.Info()
largura_tela = info.current_w
altura_tela = info.current_h

mensagens_terminal = []

estado = {
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
    texto_input = ""
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

        texto_input = GV.Barra_De_Texto(
    tela,
    (50, 400, 300, 40),
    Fonte30,
    CINZA,            # cor_fundo
    PRETO,            # cor_borda
    PRETO,            # cor_texto
    eventos,
    texto_input,
    A.minha_funcao_envio,
    AZUL              # cor_selecionado
)

        GV.Terminal(tela, (0, 700, 800, 180), Fonte30, AZUL_CLARO, PRETO)

        pygame.display.update()
        relogio.tick(60)

def PréPartida(estados):
    while estados["Rodando_PréPartida"]:
        tela.fill(BRANCO)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_PréPartida"] = False
                estados["Rodando_Jogo"] = False

        GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

        GV.Botao_Selecao(
    tela,
    (50, 150, 210, 210),
    "",
    Fonte30,
    cor_fundo=AZUL_CLARO,
    cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO,   
    cor_borda_direita=None,
    cor_passagem=AMARELO,
    id_botao="BulbasaurP1",   
    estado_global=estado,
    eventos=eventos,
    funcao_esquerdo=A.acaoteste1,
    funcao_direito=None,
    desfazer_esquerdo=A.desfazteste2,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_1,
    tecla_direita=None)
        GV.Imagem(tela, "imagens/bulbasaur.png",(50,150,205,205))

        GV.Botao_Selecao(
    tela,
    (265, 150, 210, 210),
    "",
    Fonte30,
    cor_fundo=AZUL_CLARO,
    cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO,   
    cor_borda_direita=None,
    cor_passagem=AMARELO,
    id_botao="CharmanderP1",   
    estado_global=estado,
    eventos=eventos,
    funcao_esquerdo=A.acaoteste1,
    funcao_direito=None,
    desfazer_esquerdo=A.desfazteste2,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_2,
    tecla_direita=None)
        GV.Imagem(tela, "imagens/charmander.png",(265,150,205,205))
        
        GV.Botao_Selecao(
    tela,
    (480, 150, 210, 210),
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
    funcao_esquerdo=A.acaoteste1,
    funcao_direito=None,
    desfazer_esquerdo=A.desfazteste2,
    desfazer_direito=None,
    tecla_esquerda=pygame.K_3,
    tecla_direita=None)
        GV.Imagem(tela, "imagens/squirtle.png",(480,150,205,205))

        GV.Terminal(tela, (0, 700, 800, 180), Fonte30, AZUL_CLARO, PRETO)

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
