import pygame
import os
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte23, Fonte25, Fonte28, Fonte30, Fonte35, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA,CINZA_ESCURO, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO,VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA,LARANJA_CLARO, ROXO,ROXO_CLARO, ROSA, DOURADO, PRATA, cores_raridade)

AntigaSalva = False
Config = None
modulador = True
ConfigAntiga = None

B1 = {"estado": False}
B2 = {"estado": False}

def aplicar_claridade(tela, claridade):
    """
    Aplica efeito de claridade na tela.
    claridade: int de 0 a 150, 75 é neutro.
    """
    if claridade == 50:
        return  # sem alteração

    # Normaliza a diferença em relação a 75 para valor alfa entre 0 e 150
    diff = abs(claridade - 50)
    alfa = int((diff / 50) * 100)  # máximo alfa = 150

    from Game import surface
    
    if claridade < 50:
        # Escurecer com preto semi-transparente
        surface.fill((0, 0, 0, alfa))
    else:
        # Clarear com branco semi-transparente
        surface.fill((255, 255, 255, alfa))

    tela.blit(surface, (0, 0))

def SalvarConfig():
    global Config, modulador, AntigaSalva
    # Abre o arquivo em modo escrita ("w"), apagando qualquer conteúdo anterior
    with open("ConfigFixa.py", "w", encoding="utf-8") as f:
        f.write("# Arquivo gerado automaticamente para armazenar configurações fixas\n\n")
        f.write(f"Config = {repr(Config)}\n")
    AntigaSalva = False
    modulador = False

def Cancelar():
    global AntigaSalva, modulador, Config

    Config = ConfigAntiga 
    AntigaSalva = False
    modulador = False

def Configuraçoes(tela, eventos, config):
    global AntigaSalva, Config, modulador, ConfigAntiga
    Config = config

    modulador = True

    if AntigaSalva is False:
        AntigaSalva = True
        ConfigAntiga = Config

    x = 510
    y = 240
    largura = 900
    altura = 600

    # Fundo do painel
    pygame.draw.rect(tela, (50, 50, 50), (x, y, largura, altura))  # Painel escuro
    pygame.draw.rect(tela, (200, 200, 200), (x, y, largura, altura), 4)  # Borda clara de espessura 4

    # Título centralizado no topo do painel
    texto_titulo = Fonte50.render("Configurações", True, (255, 255, 255))
    rect_titulo = texto_titulo.get_rect(center=(x + largura // 2, y + 40))
    tela.blit(texto_titulo, rect_titulo)

    # Sliders
    Config["Volume"] = GV.Slider(tela, "Volume", x + 50, y + 140, 660, Config["Volume"], 0.0, 0.8, (180, 180, 180), (255, 255, 255), eventos, "%")
    Config["Claridade"] = GV.Slider(tela, "Claridade", x + 50, y + 240, 660, Config["Claridade"], 0, 100, (180, 180, 180), (255, 255, 255), eventos, "%")
    Config["FPS"] = GV.Slider(tela, "FPS", x + 50, y + 340, 660, Config["FPS"], 20, 240, (180, 180, 180), (255, 255, 255), eventos)

    GV.Botao(tela, "Voltar", (x + largura - 470 - 390, y + altura - 85, 390, 70), VERDE_CLARO, PRETO, AZUL,
                    lambda: Cancelar(), Fonte50, B1, 3, None, True, eventos)
        
    GV.Botao(tela, "Salvar", (x + largura - 40 - 390, y + altura - 85, 390, 70), VERDE_CLARO, PRETO, AZUL,
                lambda: SalvarConfig(), Fonte50, B2, 3, None, True, eventos)
    
    return modulador