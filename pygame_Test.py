import pygame
import sys
import GeradoresVisuais as GV
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,
    AMARELO, VERMELHO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA
)

pygame.init()

tela = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Jogo pokemon")
info = pygame.display.Info()
largura_tela = info.current_w
altura_tela = info.current_h

mensagens_terminal = []

B1 = {"estado": False}
B2 = {"estado": False}

relogio = pygame.time.Clock()
rodando = True

def acao1():
    GV.adicionar_mensagem("Jogador 1 atacou com raio!", 8)

def acao2():
    GV.adicionar_mensagem("Jogador 2 perdeu 5 de vida!", 8)

def acao3():
    global rodando
    rodando = False

while rodando:
    tela.fill(BRANCO)
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False

    GV.Botao(tela, "Passar turno", 15, 630, 200, 60, CINZA, PRETO, AZUL, acao1, Fonte30, B2, 3, pygame.K_a, True, eventos)
    GV.Botao(tela, "", 230, 630, 200, 60, CINZA, PRETO, AZUL, acao2, Fonte30, B2, 3, None, True, eventos)
    GV.Botao(tela, "", 460, 630, 200, 60, CINZA, PRETO, AZUL, acao2, Fonte30, B2, 3, pygame.K_b, False, eventos)

    GV.Terminal(tela, x=0, y=700, largura=1200, altura=230, fonte=Fonte30, cor_fundo=CINZA, cor_texto=PRETO)
    GV.Imagem(tela, "imagens/pikachu.png", 100, 150, 100, 100)

    pygame.display.update()
    relogio.tick(60)

pygame.quit()
sys.exit()
