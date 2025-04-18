import pygame
import GeradoresVisuais as GV
import Gerador2 as G
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

clique = pygame.mixer.Sound("Jogo/Audio/Sons/Som1.wav")

B1 = {"estado": False}

def Final(tela,estados,relogio):

    Fundo_pré = GV.Carregar_Imagem("imagens/fundos/Fundo1.jpg", (1920,1080))

    Carregar = GV.Carregar_Imagem("imagens/fundos/carregando.jpg",(1920,1080))

    tela.blit(Carregar,(0,0))
    fonte = pygame.font.SysFont(None, 70)
    texto = fonte.render("Carregando ...", True, PRETO)
    tela.blit(texto, (tela.get_width() // 2 - 200, tela.get_height() // 2))
    pygame.display.update()

    pygame.mixer.music.load('Jogo/Audio/Musicas/pos.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    pygame.time.wait(9000)

    pygame.mixer.music.load('Jogo/Audio/Musicas/resultados.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

    from Partida import Perdedor,Vencedor

    while estados["Rodando_Final"]:
        tela.blit(Fundo_pré,(0,0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Final"] = False
                estados["Rodando_Jogo"] = False
        
            elif evento.type == pygame.USEREVENT:
                pygame.mixer.music.load('Musicas/Menu.ogg')
                pygame.mixer.music.play()
        
        GV.Texto_caixa(tela,f"{Vencedor.nome} Venceu, Parabens!", (450,200,1020,260),Fonte70, DOURADO,PRETO,4)

        GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B1, 3, pygame.K_ESCAPE, False, eventos)  
        
        GV.Botao(tela, "Voltar para o inicio", (700, 600, 520, 150), CINZA, PRETO, DOURADO,
                 lambda: A.Voltar(estados), Fonte70, B1, 4, None, True, eventos, clique)

        pygame.display.update()
        relogio.tick(60)
