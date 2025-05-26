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
from Visual.Efeitos import gerar_gif
from Visual.Sonoridade import tocar
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50, Fonte60, Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA, TexturasDic)

pygame.init()
pygame.mixer.init()

B1 = {"estado": False}
B2 = {"estado": False}

Fundo_Menu = None
Parte2 = False
Config = False
Logo_Menu = None
Fundo = None

mostrar_mensagem = False
tempo_ultimo_movimento = 0
transparencia_logo = 0
tempo_limite_ocioso = 4500  # 5 segundos
fade_velocidade = 5

AnimaMenu = 0
A1 = 1081
A2 = 1081

LogoEscalaInicial = 1.0
LogoEscalaFinal = 0.7
LogoYInicial = -60
LogoYFinal = 10
LogoXInicial = 475
LogoXFinal = 1250

def animar_valor(valor_inicial, valor_final, tempo_inicial, duracao_ms):
    tempo_decorrido = pygame.time.get_ticks() - tempo_inicial
    if tempo_decorrido >= duracao_ms:
        return valor_final
    t = tempo_decorrido / duracao_ms
    return valor_inicial + (valor_final - valor_inicial) * t

def TrocaConfig():
    global Config
    if Config == False:
        tocar("Config")
        Config = True
    else:
        Config = False

def LigarParte2():
    global Parte2, AnimaMenu, A1, A2, transparencia_logo
    A1 = 1081
    A2 = 570
    AnimaMenu = pygame.time.get_ticks()
    tocar("Entrou")

    Parte2 = True

def TelaMenu(tela,eventos,estados, Logo_Menu):
    global transparencia_logo

    if not Parte2:
    # Fade-in ou fade-out conforme o estado
        if mostrar_mensagem:
            if transparencia_logo < 255:
                transparencia_logo = min(255, transparencia_logo + fade_velocidade)
        else:
            if transparencia_logo > 0:
                transparencia_logo = max(0, transparencia_logo - fade_velocidade)

        if transparencia_logo > 0:
            Logo_Menu.set_alpha(transparencia_logo)
            tela.blit(Logo_Menu, (LogoXInicial, LogoYInicial))

            if transparencia_logo >= 50:  # só mostra texto após o logo aparecer minimamente
                GV.TextoBorda(tela,"Aperte qualquer botão para iniciar o jogo",(960,1000),Fonte70,AMARELO)

    else:
        transparencia_logo = 255

        # Animação de escala e posição da logo
        escala = animar_valor(LogoEscalaInicial, LogoEscalaFinal, AnimaMenu, 800)
        pos_y = animar_valor(LogoYInicial, LogoYFinal, AnimaMenu, 800)
        pos_x = animar_valor(LogoXInicial, LogoXFinal, AnimaMenu, 800)

        # Redimensiona logo proporcionalmente
        nova_largura = int(Logo_Menu.get_width() * escala)
        nova_altura = int(Logo_Menu.get_height() * escala)
        logo_redimensionada = pygame.transform.smoothscale(Logo_Menu, (nova_largura, nova_altura))

        tela.blit(logo_redimensionada, (pos_x, pos_y))

        YBotoes = GV.animar(A1,A2,AnimaMenu, 320)

        GV.Botao(tela, "Jogar", (680, YBotoes, 560, 110), TexturasDic["FundoAmarelo1"], PRETO, DOURADO,
                 lambda: A.iniciar_seleção(estados), Fonte70, B1, 4, None, True, eventos,"clique")
    
        GV.Botao(tela, "Decks", (680, YBotoes + 130, 560, 110), TexturasDic["FundoAmarelo1"], PRETO, DOURADO,
                 lambda: A.iniciar_decks(estados), Fonte70, B1, 4, None, True, eventos,"clique")
        
        GV.Botao(tela, "Configurações", (680, YBotoes + 260, 560, 110), TexturasDic["FundoAmarelo1"], PRETO, DOURADO,
                 lambda: TrocaConfig(), Fonte70, B1, 4, None, True, eventos,)
        
        GV.Botao(tela, "Sair do jogo", (680, YBotoes + 390, 560, 110), TexturasDic["FundoAmarelo1"], PRETO, DOURADO,
                 lambda: A.fechar_jogo(estados), Fonte70, B1, 4, None, True, eventos,)


def Menu(tela, estados, relogio, config):
    global Parte2, Config, Fundo_Menu, Fundo, mostrar_mensagem, tempo_ultimo_movimento, tempo_atual

    Parte2 = False
    Logo_Menu = GV.Carregar_Imagem("imagens/fundos/logo.png", (960, 712), "PNG")
    Logo_Menu.set_alpha(transparencia_logo)
    if config["Modo rápido"]:
        Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Menu.png", (1920, 1080), "PNG")
    else:
        if Fundo_Menu is None:
            Fundo_Menu = GV.carregar_frames("imagens/fundos/Main_Frames")
            Fundo = gerar_gif(Fundo_Menu,(960,540),36,False)

    pygame.mixer.music.load('Audio/Musicas/Menu.ogg')  
    pygame.mixer.music.set_volume(config["Volume"])
    pygame.mixer.music.play(-1)

    config["Modo"] = None

    tempo_ultimo_movimento = pygame.time.get_ticks()

    while estados["Rodando_Menu"]:
        if not isinstance(Fundo_Menu, list):
            tela.blit(Fundo_Menu,(0,0))
        else:
            Fundo.atualizar(tela)

        tempo_atual = pygame.time.get_ticks()

        pygame.mixer.music.set_volume(config["Volume"])
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Menu"] = False
                estados["Rodando_Jogo"] = False

            if not Parte2:
                if evento.type == pygame.MOUSEMOTION:
                    mostrar_mensagem = True
                    tempo_ultimo_movimento = pygame.time.get_ticks()

                if mostrar_mensagem and (evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.KEYDOWN):
                    LigarParte2()
        if not Parte2:
            if tempo_atual - tempo_ultimo_movimento > tempo_limite_ocioso:
                mostrar_mensagem = False

        if Config:
            Config = Configuraçoes(tela,eventos,config)
        
        else:
            TelaMenu(tela, eventos, estados, Logo_Menu)

        texto = Fonte40.render(f"Versão: {config["Versão"]}", True, BRANCO)  # Branco
        tela.blit(texto, (10, 1080 - texto.get_height()))

        aplicar_claridade(tela,config["Claridade"])
        pygame.display.update()
        relogio.tick(config["FPS"])

