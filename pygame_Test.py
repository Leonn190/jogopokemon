import pygame
import sys
import PréPartida
import Partida
import Final
import GeradoresVisuais as GV
import Gerador2 as G
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

# evita estragar a resoluçao mesmo com o zoom de 125% do meu computador
import ctypes
try:
    ctypes.windll.user32.SetProcessDPIAware()
except:
    pass

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Jogo Pokémon")
info = pygame.display.Info()
largura_tela = info.current_w
altura_tela = info.current_h

clique = pygame.mixer.Sound("Musicas/Som1.wav")

relogio = pygame.time.Clock()

B1 = {"estado": False}
B2 = {"estado": False}

estados = {
    "Rodando_Jogo": True,
    "Rodando_Menu": True,
    "Rodando_PréPartida": False,
    "Rodando_Partida": False,
    "Rodando_Final": False
}

def TelaMenu(eventos,estados):

    GV.Botao(tela, "Jogar", (700, 600, 520, 150), CINZA, PRETO, DOURADO,
                 lambda: A.iniciar_prépartida(estados), Fonte70, B1, 4, None, True, eventos,clique)

    GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

def Menu(estados):

    Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Fundo2.jpg", (1920,1080),)
    Logo_Menu = GV.Carregar_Imagem("imagens/fundos/logo.png", (800,800),"PNG")

    pygame.mixer.music.load('Musicas/MenuTheme.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    while estados["Rodando_Menu"]:
        tela.blit(Fundo_Menu, (0, 0))
        tela.blit(Logo_Menu, (560, -200))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Menu"] = False
                estados["Rodando_Jogo"] = False

        TelaMenu(eventos, estados)


        pygame.display.update()
        relogio.tick(60)

while estados["Rodando_Jogo"]:
    if estados["Rodando_Menu"]:
        Menu(estados)
    elif estados["Rodando_PréPartida"]:
        PréPartida.PréPartida(tela,estados,relogio)
    elif estados["Rodando_Partida"]:
        Partida.Partida(tela,estados,relogio)
    elif estados["Rodando_Final"]:
        Final.Final(tela,estados,relogio)

pygame.quit()
sys.exit()  
