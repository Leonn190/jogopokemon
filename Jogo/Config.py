import pygame
import os
from Visual.Sonoridade import tocar
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.Sonoridade import VerificaModoSilencioso
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte23, Fonte25, Fonte28, Fonte30, Fonte35, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA,CINZA_ESCURO, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO,VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA,LARANJA_CLARO, ROXO,ROXO_CLARO, ROSA, DOURADO, PRATA, cores_raridade)

AntigaSalva = False
Config = None
modulador = True
ConfigAntiga = None

ConfigAvançada = False

surface = None
GerouSurface = False

B1 = {"estado": False}
B2 = {"estado": False}
B3 = {"estado": False}
B4 = {"estado": False}
B5 = {"estado": False}
B6 = {"estado": False}

estadoConfigAvançada = {"selecionado_esquerdo": None}

def aplicar_acinzentamento(tela):
    largura, altura = tela.get_size()
    filtro_cinza = pygame.Surface((largura, altura), pygame.SRCALPHA)
    filtro_cinza.fill((100, 100, 100, 100))  # RGB + Alpha (transparência)
    tela.blit(filtro_cinza, (0, 0))

def aplicar_claridade(tela, claridade,):
    global GerouSurface, surface
    """
    Aplica efeito de claridade na tela.
    claridade: int de 0 a 150, 75 é neutro.
    """
    if claridade == 50:
        return  # sem alteração

    # Normaliza a diferença em relação a 75 para valor alfa entre 0 e 150
    diff = abs(claridade - 50)
    alfa = int((diff / 50) * 100)  # máximo alfa = 150
    
    if GerouSurface is False:
        surface = pygame.Surface(tela.get_size())
        surface = surface.convert_alpha()
        GerouSurface = True

    if claridade < 50:
        # Escurecer com preto semi-transparente
        surface.fill((0, 0, 0, alfa))
    else:
        # Clarear com branco semi-transparente
        surface.fill((255, 255, 255, alfa))

    tela.blit(surface, (0, 0))

def TrocaModoRapido(config):
    if config["Modo rápido"]:
        tocar("Desativa")
        config["Modo rápido"] = False
    else:
        tocar("Ativa")
        config["Modo rápido"] = True

def TrocaModoSilencioso(config):
    if config["Modo silencioso"]:
        tocar("Desativa")
        config["Modo silencioso"] = False
    else:
        tocar("Ativa")
        config["Modo silencioso"] = True
    
    VerificaModoSilencioso(config)

def TrocaMostraFpsPartida(config):
    if config["Mostrar Fps"]:
        tocar("Desativa")
        config["Mostrar Fps"] = False
    else:
        tocar("Ativa")
        config["Mostrar Fps"] = True

def TrocaDicas(config):
    if config["Dicas"]:
        tocar("Desativa")
        config["Dicas"] = False
    else:
        tocar("Ativa")
        config["Dicas"] = True

def AbreConfigAvançada():
    global ConfigAvançada
    tocar("Abre")
    ConfigAvançada = True

def FechaConfigAvançada():
    global ConfigAvançada
    tocar("Fecha")
    ConfigAvançada = False

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
    if ConfigAvançada is False:
        Config["Volume"] = GV.Slider(tela, "Volume", x + 50, y + 150, 670, Config["Volume"], 0.0, 0.8, (180, 180, 180), (255, 255, 255), eventos, "%")
        Config["Claridade"] = GV.Slider(tela, "Claridade", x + 50, y + 250, 670, Config["Claridade"], 0, 100, (180, 180, 180), (255, 255, 255), eventos, "%")
        Config["FPS"] = GV.Slider(tela, "FPS", x + 50, y + 350, 670, Config["FPS"], 20, 240, (180, 180, 180), (255, 255, 255), eventos)
    else:

        if config["Modo rápido"]:
            cor1 = VERDE
        else:
            cor1 = CINZA

        if config["Modo silencioso"]:
            cor2 = VERDE
        else:
            cor2 = CINZA

        if config["Mostrar Fps"]:
            cor3 = VERDE
        else:
            cor3 = CINZA

        if config["Dicas"]:
            cor4 = VERDE
        else:
            cor4 = CINZA
        
        GV.Botao(tela, "Modo Rápido", (x + 180, y + 140, 550, 50), cor1, PRETO, AZUL,
                lambda: TrocaModoRapido(config), Fonte40, B3, 3, None, True, eventos)
        GV.Botao(tela, "Modo Silencioso", (x + 180, y + 210, 550, 50), cor2, PRETO, AZUL,
                lambda: TrocaModoSilencioso(config), Fonte40, B4, 3, None, True, eventos)
        GV.Botao(tela, "Mostrar FPS Na Partida", (x + 180, y + 280, 550, 50), cor3, PRETO, AZUL,
                lambda: TrocaMostraFpsPartida(config), Fonte40, B5, 3, None, True, eventos)
        GV.Botao(tela, "Mostrar Dicas", (x + 180, y + 350, 550, 50), cor4, PRETO, AZUL,
                lambda: TrocaDicas(config), Fonte40, B6, 3, None, True, eventos)
        
    GV.Botao(tela, "Voltar", (x + largura - 470 - 390, y + altura - 85, 390, 70), VERDE_CLARO, PRETO, AZUL,
                    lambda: Cancelar(), Fonte50, B1, 3, None, True, eventos)
        
    GV.Botao(tela, "Salvar", (x + largura - 40 - 390, y + altura - 85, 390, 70), VERDE_CLARO, PRETO, AZUL,
                lambda: SalvarConfig(), Fonte50, B2, 3, None, True, eventos)
    
    GV.Botao_Selecao(
                tela, 
                (x + largura - 75, y + 15, 60,60),
                "+", 
                Fonte50,
                cor_fundo=CINZA, 
                cor_borda_normal=PRETO,
                cor_borda_esquerda=VERDE, 
                cor_borda_direita=None,
                cor_passagem=AMARELO, 
                id_botao="ConfigAvançada",   
                estado_global=estadoConfigAvançada, 
                eventos=eventos,
                funcao_esquerdo=lambda: AbreConfigAvançada(), 
                funcao_direito=None,
                desfazer_esquerdo=lambda: FechaConfigAvançada(), 
                desfazer_direito=None,
                tecla_esquerda=pygame.K_1, 
                tecla_direita=None)
    
    if modulador == False:
        FechaConfigAvançada()

    return modulador