import pygame
import GeradoresVisuais as GV
import Gerador2 as G
import random

pygame.font.init()
pygame.mixer.init()

Compra = pygame.mixer.Sound("Musicas/Compra.wav")
Bloq = pygame.mixer.Sound("Musicas/Bloq.wav")


informaçoesp1 = [random.choice(["Jogador Legal","Jogador Bacanudo","Jogador Estratégico","Jogador Habilidoso"]),random.randint(1,3)]
informaçoesp2 = [random.choice(["Jogador Astuto","Jogador Habil","Jogador Feliz","Jogador Irado"]),random.randint(1,3)]

Contador1 = 0
Contador2 = 0 

def iniciar_prépartida(estados):
    estados["Rodando_Menu"] = False
    estados["Rodando_PréPartida"] = True

def fechar_jogo(estados):
    estados["Rodando_Menu"] = False
    estados["Rodando_PréPartida"] = False
    estados["Rodando_Partida"] = False
    estados["Rodando_Jogo"] = False

def Pokemon_inicial(id_botao):
    global informaçoesp1
    global informaçoesp2
    
    if id_botao == "BulbasaurP1":
        informaçoesp1[1] = 1
    elif id_botao == "CharmanderP1":
        informaçoesp1[1] = 2
    elif id_botao == "SquirtleP1":
        informaçoesp1[1] = 3
    elif id_botao == "BulbasaurP2":
        informaçoesp2[1] = 1
    elif id_botao == "CharmanderP2":
        informaçoesp2[1] = 2
    elif id_botao == "SquirtleP2":
        informaçoesp2[1] = 3

def Fim_da_partida(estados):
    estados["Rodando_Partida"] = False
    estados["Rodando_Final"] = True

def Voltar(estados):
    if estados["Rodando_PréPartida"] == True:
        estados["Rodando_PréPartida"] = False
        estados["Rodando_Menu"] = True
    elif estados["Rodando_Partida"] == True:
        estados["Rodando_Partida"] = False
        estados["Rodando_Menu"] = True
    elif estados["Rodando_Final"] == True:
        estados["Rodando_Final"] = False
        estados["Rodando_Menu"] = True

def Remover_inicial(id_botao):
    pass

def Loja_I(ID):
    global informaçoesp1
    global informaçoesp2
    global Contador1
    global Contador2

    if ID == "PokebolasLojaIp1" and Contador1 < 3:
        GV.tocar(Compra)
        informaçoesp1.append("pokebola")
        Contador1 += 1
    elif ID == "ItensLojaIp1" and Contador1 < 3:
        GV.tocar(Compra)
        informaçoesp1.append("item")
        Contador1 += 1
    elif ID == "PokebolasLojaIp2" and Contador2 < 3:
        GV.tocar(Compra)
        informaçoesp2.append("pokebola")
        Contador2 += 1
    elif ID == "ItensLojaIp2" and Contador2 < 3:
        GV.tocar(Compra)
        informaçoesp2.append("item")
        Contador2 += 1
    else:
        GV.tocar(Bloq)

def Iniciar_partida(estados):
    estados["Rodando_PréPartida"] = False
    estados["Rodando_Partida"] = True

def Nome_p1(texto):
    global informaçoesp1
    informaçoesp1[0] = texto

def Nome_p2(texto):
    global informaçoesp2
    informaçoesp2[0] = texto



