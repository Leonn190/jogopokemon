import pygame
import sys
import ctypes
import subprocess

# evita estragar a resoluçao mesmo com o zoom de 125% do meu computador

# comando foda abaixo

# $arquivosPython = Get-ChildItem -Recurse -File -Filter "*.py"
# $numeroArquivosPython = $arquivosPython.Count
# $arquivosTotais = Get-ChildItem -Recurse -File | Measure-Object | Select-Object -ExpandProperty Count
# $linhasPython = $arquivosPython | Get-Content | Measure-Object -Line
# "Arquivos totais: $arquivosTotais"
# "Arquivos Python: $numeroArquivosPython"
# "Linhas totais Python: $($linhasPython.Lines)"

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
import SetorDecks

relogio = pygame.time.Clock()

# Config = {
#     "Volume": 0.35,
#     "Fps": 100,
#     "Claridade": 50,
#     "Modo rápido": False,
#     "Dicas": True,
#     "Modo silencioso": False,
#     "Mostrar Fps": True
#     "Versão"
# }

estados = {
    "Rodando_Jogo": True,
    "Rodando_Menu": True,
    "Rodando_PréPartida": False,
    "Rodando_Partida": False,
    "Rodando_Final": False,
    "Rodando_Decks": False
}

while estados["Rodando_Jogo"]:

    if estados["Rodando_Menu"]:
        Menu.Menu(tela,estados,relogio)
    elif estados["Rodando_Decks"]:
        SetorDecks.Decks(tela,estados,relogio)
    elif estados["Rodando_PréPartida"]:
        PréPartida.PréPartida(tela,estados,relogio)
    elif estados["Rodando_Partida"]:
        Partida.Partida(tela,estados,relogio)
    elif estados["Rodando_Final"]:
        Final.Final(tela,estados,relogio)

pygame.quit()
sys.exit()  