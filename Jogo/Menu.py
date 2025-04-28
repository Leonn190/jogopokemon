import sys
import os

# Adiciona a pasta 'GitHub/jogopokemon' ao sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import pygame
from Visual import GeradoresVisuais as GV
import Jogo.Gerador as G
import PygameAções as A
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

pygame.init()
pygame.mixer.init()

clique = pygame.mixer.Sound("Audio/Sons/Som1.wav")

B1 = {"estado": False}
B2 = {"estado": False}

Parte2 = False

def LigarParte2():
    global Parte2
    Parte2 = True

def TelaMenu(tela,eventos,estados, Logo_Menu):

    if Parte2 is False:

        GV.Botao(tela, "Jogar", (700, 600, 520, 150), CINZA, PRETO, DOURADO,
                 lambda: LigarParte2(), Fonte70, B1, 4, None, True, eventos,clique)
    
        tela.blit(Logo_Menu, (560, -200))

    else:

        GV.Botao(tela, "Modo Normal", (700, 700, 520, 150), CINZA, PRETO, DOURADO,
                 lambda: A.iniciar_prépartida(estados), Fonte70, B1, 4, None, True, eventos,clique)
    
        GV.Botao(tela, "Modo Personalizado", (700, 500, 520, 150), CINZA, PRETO, DOURADO,
                 lambda: A.iniciar_prépartida(estados), Fonte70, B1, 4, None, True, eventos,clique)

    GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

def Menu(tela,estados,relogio):
    global Parte2

    Parte2 = False
    Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Menu.png", (1920,1080))
    Logo_Menu = GV.Carregar_Imagem("imagens/fundos/logo.png", (800,800),"PNG")


    pygame.mixer.music.load('Audio/Musicas/Menu.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    while estados["Rodando_Menu"]:
        tela.blit(Fundo_Menu, (0, 0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Menu"] = False
                estados["Rodando_Jogo"] = False

        TelaMenu(tela,eventos, estados, Logo_Menu)

        pygame.display.update()
        relogio.tick(60)

