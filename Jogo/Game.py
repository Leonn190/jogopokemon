import pygame
import sys
import ctypes
import threading
import os

# Corrige problema de resolução em telas com escala de zoom no Windows (ex: 125%)
try:
    ctypes.windll.user32.SetProcessDPIAware()
except:
    pass

# Inicializa os módulos principais do pygame
pygame.init()
pygame.mixer.init()  # Som

# Cria a janela do jogo em modo tela cheia com resolução 1920x1080
tela = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Jogo Pokémon")

# Define o ícone da janela
icone_surface = pygame.image.load("imagens/icones/Icone.png")
pygame.display.set_icon(icone_surface)

# Superfície base para desenho, com transparência (canal alpha)
Surface = pygame.Surface(tela.get_size(), pygame.SRCALPHA)

# Importa a função de carregamento (executada em thread)
from Carregamento import TelaCarregamento

# Importa os módulos das diferentes telas do jogo
import Menu 
import PréPartida
import Jogo.Partida.Local as Partida
import Jogo.Partida.Online as Online
import Final
import SetorDecks
import SeleçãoJogo
import Fila

# Relógio usado para controlar o FPS
relogio = pygame.time.Clock()

# Configurações iniciais padrão
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

# Caso exista um arquivo com configurações fixas, ele sobrescreve as padrões
if os.path.exists("ConfigFixa.py"):
    try:
        from ConfigFixa import Config as ConfigSalva
        Config = ConfigSalva
    except Exception as e:
        pass  # Silenciosamente ignora erro

# Informações extras da configuração
Config["Modo"] = None
Config["Versão"] = "Beta 1.2.4"

# Verifica se o modo silencioso está ativado para ajustar o som do jogo
from Visual.Sonoridade import VerificaModoSilencioso
VerificaModoSilencioso(Config)

# Se não estiver no modo rápido, executa a tela de carregamento em uma thread separada
if Config["Modo rápido"] is not True:
    thread_carregamento = threading.Thread(target=TelaCarregamento, args=(tela, relogio, Config, Surface))
    thread_carregamento.start()

# Dicionário que controla o estado atual do jogo (qual tela ou loop está ativo)
estados = {
    "Rodando_Jogo": True,         # Loop principal do jogo
    "Rodando_Menu": True,         # Tela inicial/menu principal
    "Rodando_Seleção": False,     # Tela de seleção de modo de jogo
    "Rodando_PréPartida": False,  # Tela de preparação antes da partida
    "Rodando_Fila": False,        # Tela de espera para modo online
    "Rodando_Partida": False,     # Partida local
    "Rodando_PartidaOnline": False,  # Partida online
    "Rodando_Final": False,       # Tela final após a partida
    "Rodando_Decks": False        # Tela de seleção e edição de decks
}

# Loop principal do jogo, alterna entre os estados definidos acima
while estados["Rodando_Jogo"]:

    if estados["Rodando_Menu"]:
        Menu.Menu(tela, estados, relogio, Config)
    elif estados["Rodando_Decks"]:
        SetorDecks.Decks(tela, estados, relogio, Config)
    elif estados["Rodando_Seleção"]:
        SeleçãoJogo.Seleção(tela, estados, relogio, Config)
    elif estados["Rodando_PréPartida"]:
        PréPartida.PréPartida(tela, estados, relogio, Config)
    elif estados["Rodando_Fila"]:
        Fila.Fila(tela, estados, relogio, Config)
    elif estados["Rodando_PartidaOnline"]:
        Online.PartidaOnlineLoop(tela, estados, relogio, Config)
    elif estados["Rodando_Partida"]:
        Partida.PartidaLoop(tela, estados, relogio, Config)
    elif estados["Rodando_Final"]:
        Final.Final(tela, estados, relogio, Config)

# Quando o loop principal termina, o pygame é encerrado e o programa é fechado
pygame.quit()
sys.exit()
