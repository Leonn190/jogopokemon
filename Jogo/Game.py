import pygame
import sys
import ctypes

# evita estragar a resoluçao mesmo com o zoom de 125% do meu computador

try:
    ctypes.windll.user32.SetProcessDPIAware()
except:
    pass

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Jogo Pokémon")

# Ícone da janela (comum)
icone_surface = pygame.image.load("imagens/icones/Icone.png")
pygame.display.set_icon(icone_surface)

import Menu
import PréPartida
import Partida
import Final

relogio = pygame.time.Clock()

estados = {
    "Rodando_Jogo": True,
    "Rodando_Menu": True,
    "Rodando_PréPartida": False,
    "Rodando_Partida": False,
    "Rodando_Final": False
}

while estados["Rodando_Jogo"]:

    if estados["Rodando_Menu"]:
        Menu.Menu(tela,estados,relogio)
    elif estados["Rodando_PréPartida"]:
        PréPartida.PréPartida(tela,estados,relogio)
    elif estados["Rodando_Partida"]:
        Partida.Partida(tela,estados,relogio)
    elif estados["Rodando_Final"]:
        Final.Final(tela,estados,relogio)

pygame.quit()
sys.exit()  