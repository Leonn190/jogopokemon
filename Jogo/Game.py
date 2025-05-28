import pygame
import sys
import ctypes
import threading
import os

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
Surface = pygame.Surface(tela.get_size(), pygame.SRCALPHA)

from Carregamento import TelaCarregamento

import Menu 
import PréPartida
import Jogo.Partida.Local as Partida
import Jogo.Partida.Online as Online
import Final
import SetorDecks
import SeleçãoJogo
import Fila

relogio = pygame.time.Clock()

Config = {
    "Volume": 0.4,
    "FPS": 130,
    "Claridade": 50,
    "OnlineRapido": False,
    "Modo rápido": False,
    "Dicas": True,
    "Modo silencioso": False,
    "Mostrar Fps": True,
}

if os.path.exists("ConfigFixa.py"):
    try:
        from ConfigFixa import Config as ConfigSalva
        Config = ConfigSalva
    except Exception as e:
        pass

Config["Modo"] = None
Config["Versão"] = "Beta 1.2.4"

from Visual.Sonoridade import VerificaModoSilencioso
VerificaModoSilencioso(Config)

if Config["Modo rápido"] is not True:
    thread_carregamento = threading.Thread(target=TelaCarregamento, args=(tela, relogio, Config, Surface))
    thread_carregamento.start()

estados = {
    "Rodando_Jogo": True,
    "Rodando_Menu": True,
    "Rodando_Seleção": False,
    "Rodando_PréPartida": False,
    "Rodando_Fila": False,
    "Rodando_Partida": False,
    "Rodando_PartidaOnline": False,
    "Rodando_Final": False,
    "Rodando_Decks": False
}

while estados["Rodando_Jogo"]:

    if estados["Rodando_Menu"]:
        Menu.Menu(tela,estados,relogio,Config)
    elif estados["Rodando_Decks"]:
        SetorDecks.Decks(tela,estados,relogio,Config)
    elif estados["Rodando_Seleção"]:
        SeleçãoJogo.Seleção(tela,estados,relogio,Config)
    elif estados["Rodando_PréPartida"]:
        PréPartida.PréPartida(tela,estados,relogio,Config)
    elif estados["Rodando_Fila"]:
        Fila.Fila(tela,estados,relogio,Config)
    elif estados["Rodando_PartidaOnline"]:
        Online.PartidaOnlineLoop(tela,estados,relogio,Config)
    elif estados["Rodando_Partida"]:
        Partida.PartidaLoop(tela,estados,relogio,Config)
    elif estados["Rodando_Final"]:
        Final.Final(tela,estados,relogio,Config)

pygame.quit()
sys.exit()  