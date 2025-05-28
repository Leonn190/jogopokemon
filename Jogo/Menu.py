# Bibliotecas padrão e funções do sistema
import sys
import os
import subprocess
import time
import shutil

# Adiciona o diretório do projeto ao path para importações relativas
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# Bibliotecas do jogo
import pygame
from Visual import GeradoresVisuais as GV
from Config import Configuraçoes, aplicar_claridade
import PygameAções as A
from Visual.Efeitos import gerar_gif
from Visual.Sonoridade import tocar
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50, Fonte60, Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO, AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO, VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA, TexturasDic
)

# Inicializa Pygame e o mixer de áudio
pygame.init()
pygame.mixer.init()

# Estados de botões
B1 = {"estado": False}
B2 = {"estado": False}

# Variáveis de controle do menu
Fundo_Menu = None
Parte2 = False  # Controla a transição para o menu expandido
Config = False  # Estado da aba de configurações
Logo_Menu = None
Fundo = None

# Controle de animações e inatividade
mostrar_mensagem = False
tempo_ultimo_movimento = 0
transparencia_logo = 0
tempo_limite_ocioso = 5000  # Tempo até começar o fade-in (ms)
fade_velocidade = 5

# Controle de animações de logo e botões
AnimaMenu = 0
A1 = 1081
A2 = 1081  # Posição final dos botões

# Parâmetros para a animação da logo
LogoEscalaInicial = 1.0
LogoEscalaFinal = 0.7
LogoYInicial = -60
LogoYFinal = 10
LogoXInicial = 475
LogoXFinal = 1250

# Função genérica para animar transições de valores
def animar_valor(valor_inicial, valor_final, tempo_inicial, duracao_ms):
    tempo_decorrido = pygame.time.get_ticks() - tempo_inicial
    if tempo_decorrido >= duracao_ms:
        return valor_final
    t = tempo_decorrido / duracao_ms
    return valor_inicial + (valor_final - valor_inicial) * t

# Alterna o estado da aba de configurações
def TrocaConfig():
    global Config
    if Config == False:
        tocar("Config")
        Config = True
    else:
        Config = False

# Ativa a segunda parte do menu (com botões) e inicia a animação
def LigarParte2():
    global Parte2, AnimaMenu, A1, A2, transparencia_logo
    A1 = 1081
    A2 = 570
    AnimaMenu = pygame.time.get_ticks()
    tocar("Entrou")
    Parte2 = True

# Tela principal do menu
def TelaMenu(tela, eventos, estados, Logo_Menu):
    global transparencia_logo

    # PRIMEIRA PARTE DO MENU (logo + "aperte qualquer botão")
    if not Parte2:
        # Controle de fade-in/fade-out do logo
        if mostrar_mensagem:
            if transparencia_logo < 255:
                transparencia_logo = min(255, transparencia_logo + fade_velocidade)
        else:
            if transparencia_logo > 0:
                transparencia_logo = max(0, transparencia_logo - fade_velocidade)

        # Desenha o logo com transparência crescente
        if transparencia_logo > 0:
            Logo_Menu.set_alpha(transparencia_logo)
            tela.blit(Logo_Menu, (LogoXInicial, LogoYInicial))

            # Só mostra texto quando o logo estiver parcialmente visível
            if transparencia_logo >= 85:
                GV.TextoBorda(tela, "Aperte qualquer botão para iniciar o jogo", (960, 1000), Fonte70, AMARELO)

    # SEGUNDA PARTE DO MENU (com botões de ação)
    else:
        # Animação de movimento e escala da logo
        escala = animar_valor(LogoEscalaInicial, LogoEscalaFinal, AnimaMenu, 800)
        pos_y = animar_valor(LogoYInicial, LogoYFinal, AnimaMenu, 800)
        pos_x = animar_valor(LogoXInicial, LogoXFinal, AnimaMenu, 800)

        # Redimensiona o logo com suavidade
        nova_largura = int(Logo_Menu.get_width() * escala)
        nova_altura = int(Logo_Menu.get_height() * escala)
        logo_redimensionada = pygame.transform.smoothscale(Logo_Menu, (nova_largura, nova_altura))
        tela.blit(logo_redimensionada, (pos_x, pos_y))

        # Animação da posição vertical dos botões
        YBotoes = GV.animar(A1, A2, AnimaMenu, 320)

        # Botão "Jogar"
        GV.Botao(tela, "Jogar", (680, YBotoes, 560, 110), TexturasDic["FundoAzul"],
                 PRETO, DOURADO, lambda: A.iniciar_seleção(estados),
                 Fonte70, B1, 4, None, True, eventos, "clique")

        # Botão "Decks"
        GV.Botao(tela, "Decks", (680, YBotoes + 130, 560, 110), TexturasDic["FundoVerde"],
                 PRETO, DOURADO, lambda: A.iniciar_decks(estados),
                 Fonte70, B1, 4, None, True, eventos, "clique")

        # Botão "Configurações"
        GV.Botao(tela, "Configurações", (680, YBotoes + 260, 560, 110), TexturasDic["FundoAmarelo"],
                 PRETO, DOURADO, lambda: TrocaConfig(),
                 Fonte70, B1, 4, None, True, eventos)

        # Botão "Sair do jogo"
        GV.Botao(tela, "Sair do jogo", (680, YBotoes + 390, 560, 110), TexturasDic["FundoVermelho"],
                 PRETO, DOURADO, lambda: A.fechar_jogo(estados),
                 Fonte70, B1, 4, None, True, eventos)

# Função principal do menu inicial do jogo
def Menu(tela, estados, relogio, config):
    # Usa variáveis globais definidas fora da função
    global Parte2, Config, Fundo_Menu, Fundo, mostrar_mensagem, tempo_ultimo_movimento, tempo_atual

    # Estado inicial: menu ainda está na primeira parte (apenas logo)
    Parte2 = False

    # Carrega a imagem da logo principal do jogo
    Logo_Menu = GV.Carregar_Imagem("imagens/fundos/logo.png", (960, 712), "PNG")
    Logo_Menu.set_alpha(transparencia_logo)  # Aplica transparência inicial

    # Carrega o fundo do menu, que pode ser estático ou animado (modo lento)
    if config["Modo rápido"]:
        Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Menu.png", (1920, 1080), "PNG")
    else:
        if Fundo_Menu is None:  # Só carrega uma vez
            Fundo_Menu = GV.carregar_frames("imagens/fundos/Main_Frames")  # Animação quadro a quadro
            Fundo = gerar_gif(Fundo_Menu, (960, 540), 36, False)  # Constrói o GIF animado

    # Inicia a música de fundo do menu
    pygame.mixer.music.load('Audio/Musicas/Menu.ogg')  
    pygame.mixer.music.set_volume(config["Volume"])
    pygame.mixer.music.play(-1)  # Repete indefinidamente

    # Define o modo atual como 'None' ao entrar no menu
    config["Modo"] = None

    # Salva o tempo atual para controle de inatividade
    tempo_ultimo_movimento = pygame.time.get_ticks()

    # Marca o fim do carregamento inicial
    import Carregamento as C
    C.Carregamento = False

    # LOOP PRINCIPAL DO MENU
    while estados["Rodando_Menu"]:
        # Exibe o fundo (estático ou animado)
        if not isinstance(Fundo_Menu, list):
            tela.blit(Fundo_Menu, (0, 0))
        else:
            Fundo.atualizar(tela)

        # Atualiza tempo atual para controle de transições e animações
        tempo_atual = pygame.time.get_ticks()

        # Atualiza volume em tempo real (caso o usuário mude nas configs)
        pygame.mixer.music.set_volume(config["Volume"])

        # Coleta os eventos do sistema (mouse, teclado, etc.)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                # Se fechar a janela, encerra o jogo completamente
                estados["Rodando_Menu"] = False
                estados["Rodando_Jogo"] = False

            # Enquanto estiver na primeira parte (só a logo com fade-in)
            if not Parte2:
                if evento.type == pygame.MOUSEMOTION:
                    # Se mover o mouse, ativa a exibição da mensagem
                    mostrar_mensagem = True
                    tempo_ultimo_movimento = pygame.time.get_ticks()

                # Se clicar ou pressionar qualquer tecla após o fade-in completo, inicia a segunda parte do menu
                if mostrar_mensagem and (
                    evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.KEYDOWN
                ) and transparencia_logo == 255:
                    LigarParte2()

        # Se o usuário estiver inativo por mais de 5 segundos, some a mensagem
        if not Parte2:
            if tempo_atual - tempo_ultimo_movimento > tempo_limite_ocioso:
                mostrar_mensagem = False

        # Se a aba de configurações estiver ativa, exibe ela
        if Config:
            Config = Configuraçoes(tela, eventos, config)
        else:
            # Senão, exibe a tela principal do menu com logo e botões
            TelaMenu(tela, eventos, estados, Logo_Menu)

        # Renderiza o texto da versão do jogo no canto inferior esquerdo
        texto = Fonte40.render(f"Versão: {config['Versão']}", True, BRANCO)
        tela.blit(texto, (10, 1080 - texto.get_height()))

        # Aplica clareamento da tela se configurado
        aplicar_claridade(tela, config["Claridade"])

        # Atualiza a tela com tudo renderizado
        pygame.display.update()

        # Controla a taxa de quadros por segundo (FPS)
        relogio.tick(config["FPS"])