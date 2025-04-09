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

        GV.Botao(tela, "Iniciar a partida", 560, 350, 450, 120, CINZA, PRETO, DOURADO,
                 lambda: A.iniciar_partida(estados), Fonte50, B2, 4, pygame.K_a, True, eventos)

        GV.Botao(tela, "Sair do jogo", 300, 400, 320, 80, CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_o, False, eventos)

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

        GV.Botao(tela, "Sair do jogo", 300, 400, 320, 80, CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_o, False, eventos)

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

        GV.Botao(tela, "Sair do jogo", 300, 400, 320, 80, CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_o, False, eventos)

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
