import pygame
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Config import aplicar_claridade
from Visual.Sonoridade import tocar
from Visual.GeradoresVisuais import (
    Fonte15, Fonte23, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

B1 = {"estado": False}

def TelaSeleção(tela,eventos,estados,Config):

    GV.Botao(tela, "Modo Padrão", (300, 200, 540, 120), CINZA, PRETO, DOURADO,
                 lambda: A.iniciar_prépartida(estados, Config, "Padrão"), Fonte70, B1, 4, None, True, eventos,"clique")
    
    GV.Botao(tela, "Modo Online", (300, 400, 540, 120), CINZA, PRETO, DOURADO,
                 lambda: A.iniciar_prépartida(estados, Config, "Online"), Fonte70, B1, 4, None, True, eventos,"clique")
    
    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), CINZA, PRETO, AZUL,
                 lambda: A.Voltar(estados), Fonte40, B1, 3, None, True, eventos)

def Seleção(tela,estados,relogio,Config):

    pygame.mixer.music.load('Audio/Musicas/Sele.ogg')
    pygame.mixer.music.set_volume(Config["Volume"])
    pygame.mixer.music.play(-1)

    Fundo_Seleção = GV.Carregar_Imagem("imagens/fundos/FundoSeleção.jpg", (1920,1080))

    while estados["Rodando_Seleção"]:
        tela.blit(Fundo_Seleção, (0, 0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Seleção"] = False
                estados["Rodando_Jogo"] = False

        TelaSeleção(tela,eventos,estados,Config)

        aplicar_claridade(tela,Config["Claridade"])
        pygame.display.update()
        relogio.tick(Config["FPS"])