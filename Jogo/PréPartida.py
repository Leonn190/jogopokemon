import pygame
import GeradoresVisuais as GV
import Gerador2 as G
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

pygame.mixer.init()

clique = pygame.mixer.Sound("Jogo/Audio/Sons/Som1.wav")
Compra = pygame.mixer.Sound("Jogo/Audio/Sons/Compra.wav")
Escolha = pygame.mixer.Sound("Jogo/Audio/Sons/EscolhaPoke.wav")

estado1 = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

estado2 = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

B2 = {"estado": False}
B3 = {"estado": False, "ID": "PokebolasLojaIp1"}
B4 = {"estado": False, "ID": "ItensLojaIp1"}
B5 = {"estado": False, "ID": "ItensLojaIp2"}
B6 = {"estado": False, "ID": "PokebolasLojaIp2"}
B7 = {"estado": False}
B8 = {"estado": False}

def TelaPréPartida(tela,eventos,estados):

    GV.Texto(tela, "Jogador 1", (360, 50), Fonte70, PRETO)
    GV.Texto(tela, "Jogador 2", (1320, 50), Fonte70, PRETO)
    GV.Texto(tela, "Escreva seu Nome:", (190, 485), Fonte40, PRETO)
    GV.Texto(tela, "Escreva seu Nome:", (1170, 485), Fonte40, PRETO)
    GV.Texto(tela, "Faça 3 compras na loja", (325, 665), Fonte40, PRETO)
    GV.Texto(tela, "Faça 3 compras na loja", (1285, 665), Fonte40, PRETO)
    GV.Reta_Central(tela, 1920, 1080, PRETO, 4)

    GV.Botao(tela, "Sair do jogo", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: A.fechar_jogo(estados), Fonte50, B2, 3, pygame.K_ESCAPE, False, eventos)  
    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), CINZA, PRETO, AZUL,
                 lambda: A.Voltar(estados), Fonte40, B8, 3, None, True, eventos)

    GV.Botao_Selecao(
    tela, (80, 150, 240, 240),
    "", Fonte30,
    cor_fundo=VERDE_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO, cor_borda_direita=None,
    cor_passagem=AMARELO, id_botao="BulbasaurP1",   
    estado_global=estado1, eventos=eventos,
    funcao_esquerdo=lambda :A.Pokemon_inicial("BulbasaurP1"), funcao_direito=None,
    desfazer_esquerdo=lambda:A.Remover_inicial("BulbasaurP1"), desfazer_direito=None,
    tecla_esquerda=pygame.K_1, tecla_direita=None,som=Escolha)

    GV.Botao_Selecao(
    tela, (350, 150, 240, 240),
    "", Fonte30,
    cor_fundo=VERMELHO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO, cor_borda_direita=None,
    cor_passagem=AMARELO, id_botao="CharmanderP1",   
    estado_global=estado1, eventos=eventos,
    funcao_esquerdo=lambda:A.Pokemon_inicial("CharmanderP1"), funcao_direito=None,
    desfazer_esquerdo=lambda:A.Remover_inicial("CharmanderP1"), desfazer_direito=None,
    tecla_esquerda=pygame.K_2, tecla_direita=None,som=Escolha)
        
    GV.Botao_Selecao(
    tela, (620, 150, 240, 240),
    "", Fonte30, 
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO, cor_borda_direita=None,
    cor_passagem=AMARELO, id_botao="SquirtleP1",   
    estado_global=estado1, eventos=eventos,
    funcao_esquerdo=lambda:A.Pokemon_inicial("SquirtleP1"), funcao_direito=None,
    desfazer_esquerdo=lambda:A.Remover_inicial("SquirtleP1"), desfazer_direito=None,
    tecla_esquerda=pygame.K_3, tecla_direita=None,som=Escolha)

    GV.Botao_Selecao(
    tela, (1600, 150, 240, 240),
    "", Fonte30,
    cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO, cor_borda_direita=None,
    cor_passagem=AMARELO, id_botao="Squirtlep2",   
    estado_global=estado2, eventos=eventos,
    funcao_esquerdo=lambda:A.Pokemon_inicial("Squirtlep2"), funcao_direito=None,
    desfazer_esquerdo=lambda:A.Remover_inicial("Squirtlep2"), desfazer_direito=None,
    tecla_esquerda=pygame.K_9, tecla_direita=None,som=Escolha)

    GV.Botao_Selecao(
    tela, (1330, 150, 240, 240),
    "", Fonte30,
    cor_fundo=VERMELHO_CLARO, cor_borda_normal=PRETO,
    cor_borda_esquerda=AMARELO, cor_borda_direita=None,
    cor_passagem=AMARELO, id_botao="CharmanderP2",   
    estado_global=estado2, eventos=eventos,
    funcao_esquerdo=lambda:A.Pokemon_inicial("CharmanderP2"), funcao_direito=None,
    desfazer_esquerdo=lambda:A.Remover_inicial("CharmanderP2"), desfazer_direito=None,
    tecla_esquerda=pygame.K_8, tecla_direita=None,som=Escolha)
        
    GV.Botao_Selecao(
    tela, (1060, 150, 240, 240),
    "", Fonte30,
    cor_fundo=VERDE_CLARO, cor_borda_normal=PRETO, 
    cor_borda_esquerda=AMARELO, cor_borda_direita=None,
    cor_passagem=AMARELO,id_botao="BulbasaurP2", 
    estado_global=estado2,eventos=eventos, 
    funcao_esquerdo=lambda:A.Pokemon_inicial("BulbasaurP2"), funcao_direito=None, 
    desfazer_esquerdo=lambda:A.Remover_inicial("BulbasaurP2"), desfazer_direito=None,
    tecla_esquerda=pygame.K_7, tecla_direita=None,som=Escolha)
    
    #itensp1
    GV.Botao(tela, "", (250, 700, 200, 200), CINZA, PRETO, DOURADO,
                 lambda: A.Loja_I(B4["ID"]), Fonte50, B4, 4, None, True, eventos,)

    #pokep1
    GV.Botao(tela, "", (510, 700, 200, 200), CINZA, PRETO, DOURADO,
                 lambda: A.Loja_I(B3["ID"]), Fonte50, B3, 4, None, True, eventos,)

    #itensp2
    GV.Botao(tela, "", (1210, 700, 200, 200), CINZA, PRETO, DOURADO,    
                 lambda: A.Loja_I(B5["ID"]), Fonte50, B5, 4, None, True, eventos,)

    #pokep2
    GV.Botao(tela, "", (1470, 700, 200, 200), CINZA, PRETO, DOURADO,
                 lambda: A.Loja_I(B6["ID"]), Fonte50, B6, 4, None, True, eventos,)        

    GV.Botao(tela, "Iniciar Partida", (770, 880, 380, 110), AMARELO_CLARO, PRETO, DOURADO,
                 lambda: A.Iniciar_partida(estados), Fonte70, B7, 4, None, True, eventos, clique)

def PréPartida(tela,estados,relogio):
    # itens para deixar as barras de texto funcionais
    texto1 = ""
    selecionado1 = False

    texto2 = ""
    selecionado2 = False

    pygame.mixer.music.load('Jogo/Audio/Musicas/PréPartida.ogg')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    Fundo_pré = GV.Carregar_Imagem("imagens/fundos/Fundo1.jpg", (1920,1080))
    bulbasaurIMG = GV.Carregar_Imagem("imagens/pokemons/bulbasaur.png", (235,235),"PNG")
    charmanderIMG = GV.Carregar_Imagem("imagens/pokemons/charmander.png", (235,235),"PNG")
    squirtleIMG = GV.Carregar_Imagem("imagens/pokemons/squirtle.png", (235,235),"PNG")
    Loja_pokebolas = GV.Carregar_Imagem("imagens/icones/itens.png", (180,180),"PNG")
    Loja_itens = GV.Carregar_Imagem("imagens/icones/poke.png", (180,180),"PNG")

    while estados["Rodando_PréPartida"]:
        tela.blit(Fundo_pré, (0, 0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_PréPartida"] = False
                estados["Rodando_Jogo"] = False

        TelaPréPartida(tela,eventos,estados)

        tela.blit(bulbasaurIMG, (80, 150))
        tela.blit(charmanderIMG, (355, 150))
        tela.blit(squirtleIMG, (630, 150))
        tela.blit(bulbasaurIMG, (1060, 150))
        tela.blit(charmanderIMG, (1335, 150))
        tela.blit(squirtleIMG, (1610, 150))
        
        tela.blit(Loja_itens, (260, 710))
        tela.blit(Loja_pokebolas, (520, 710))
        tela.blit(Loja_itens, (1220, 710))
        tela.blit(Loja_pokebolas, (1480, 710))

        texto1, selecionado1 = GV.Barra_De_Texto(
    tela, (500, 480, 300, 40), Fonte30, 
    CINZA, PRETO, PRETO, eventos, texto1,
    A.Nome_p1, AZUL,selecionado1)

        texto2, selecionado2 = GV.Barra_De_Texto(
    tela, (1470, 480, 300, 40), Fonte30, 
    CINZA, PRETO, PRETO, eventos, texto2,
    A.Nome_p2, AZUL,selecionado2)

        pygame.display.update()
        relogio.tick(50)

