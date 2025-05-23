import sys
import os
import subprocess
import time
import shutil

# Adiciona a pasta 'GitHub/jogopokemon' ao sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import pygame
from Visual import GeradoresVisuais as GV
from Config import Configuraçoes, aplicar_claridade
import PygameAções as A
from Visual.Efeitos import Fundo
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
Config = False

def TrocaConfig():
    global Config
    if Config == False:
        Config = True
    else:
        Config = False

def LigarParte2():
    global Parte2
    Parte2 = True

def TelaMenu(tela,eventos,estados, Logo_Menu):

    if Parte2 is False:

        GV.Botao(tela, "Jogar", (700, 600, 520, 150), CINZA, PRETO, DOURADO,
                 lambda: LigarParte2(), Fonte70, B1, 4, None, True, eventos,clique)
    
        tela.blit(Logo_Menu, (560, -200))

    else:

        GV.Botao(tela, "Jogar", (700, 400, 520, 150), CINZA, PRETO, DOURADO,
                 lambda: A.iniciar_prépartida(estados), Fonte70, B1, 4, None, True, eventos,clique)
    
        GV.Botao(tela, "Decks", (700, 600, 520, 150), CINZA, PRETO, DOURADO,
                 lambda: A.iniciar_decks(estados), Fonte70, B1, 4, None, True, eventos,clique)
        
        GV.Botao(tela, "Configurações", (700, 800, 520, 150), CINZA, PRETO, DOURADO,
                 lambda: TrocaConfig(), Fonte70, B1, 4, None, True, eventos,clique)

    GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)

def Menu(tela, estados, relogio, config):
    global Parte2, Config

    # Inicia subprocesso que gera os frames
    # processo_video = subprocess.Popen(["python", "video.py"])
    # time.sleep(0.2)

    Parte2 = False
    Logo_Menu = GV.Carregar_Imagem("imagens/fundos/logo.png", (800, 800), "PNG")
    Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Menu.png", (1920,1080))

    pygame.mixer.music.load('Audio/Musicas/Menu.ogg')  
    pygame.mixer.music.set_volume(config["Volume"])
    pygame.mixer.music.play(-1)

    i = 1
    frame = 0

    # try:
    while estados["Rodando_Menu"]:
        tela.blit(Fundo_Menu,(0,0))
        pygame.mixer.music.set_volume(config["Volume"])
            # if frame % 2 == 0:
            #     tela.fill((255, 255, 255)) 
            #     fundo = GV.Carregar_Imagem(f"imagens/FundosAnimados/VID_frames/{i}.jpg", (1920,1080))
            #     tela.blit(fundo,(0,0))
            #     os.remove(f"imagens/FundosAnimados/VID_frames/{i}.jpg")
            #     i += 1
            #     if i > 8800:
            #         i = 1
        eventos = pygame.event.get()
        for evento in eventos:
                if evento.type == pygame.QUIT:
                    estados["Rodando_Menu"] = False
                    estados["Rodando_Jogo"] = False

        
        if Config:
            Config = Configuraçoes(tela,eventos,config)
        
        else:
            TelaMenu(tela, eventos, estados, Logo_Menu)

        texto = Fonte70.render(f"Ver: {config["Versão"]}", True, BRANCO)  # Branco
        tela.blit(texto, (10, 1080 - texto.get_height() - 10))
        
        aplicar_claridade(tela,config["Claridade"])
        pygame.display.update()
        relogio.tick(config["FPS"])
        frame += 1

    # finally:
    #     # Encerra os subprocessos
    #     if processo_video.poll() is None:
    #         processo_video.terminate()

    #     if os.path.exists("imagens/FundosAnimados/VID_frames"):
    #         shutil.rmtree("imagens/FundosAnimados/VID_frames")
