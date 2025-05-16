import pygame
from Visual.Sonoridade import tocar
import random

pygame.font.init()
pygame.mixer.init()

Compra = pygame.mixer.Sound("Audio/Sons/Compra.wav")
Bloq = pygame.mixer.Sound("Audio/Sons/Bloq.wav")

informaçoesp1 = [random.choice(["Jogador Legal","Jogador Bacanudo","Jogador Estratégico","Jogador Habilidoso"]),None,None]
informaçoesp2 = [random.choice(["Jogador Astuto","Jogador Habil","Jogador Feliz","Jogador Irado"]),None,None]

Contador1 = 0
Contador2 = 0 

def iniciar_prépartida(estados):
    global informaçoesp1, informaçoesp2,Contador1,Contador2
    estados["Rodando_Menu"] = False
    estados["Rodando_PréPartida"] = True
    informaçoesp1 = [random.choice(["Jogador Legal","Jogador Bacanudo","Jogador Estratégico","Jogador Habilidoso"]),None,None]
    informaçoesp2 = [random.choice(["Jogador Astuto","Jogador Habil","Jogador Feliz","Jogador Irado"]),None,None]
    Contador1 = 0
    Contador2 = 0

def fechar_jogo(estados):
    estados["Rodando_Menu"] = False
    estados["Rodando_PréPartida"] = False
    estados["Rodando_Partida"] = False
    estados["Rodando_Jogo"] = False

def iniciar_decks(estados):
    estados["Rodando_Menu"] = False
    estados["Rodando_Decks"] = True

def Pokemon_inicial(pokemon,Deck,player):
    global informaçoesp1
    global informaçoesp2
    
    if player == 1:
        informaçoesp1[1] = pokemon
        informaçoesp1[2] = Deck
    else:
        informaçoesp2[1] = pokemon
        informaçoesp2[2] = Deck

def Fim_da_partida(estados):
    estados["Rodando_Partida"] = False
    estados["Rodando_Final"] = True

def Voltar(estados):
    estados["Rodando_PréPartida"] = False
    estados["Rodando_Partida"] = False
    estados["Rodando_Final"] = False
    estados["Rodando_Decks"] = False
    estados["Rodando_Menu"] = True

def Remover_inicial(id_botao):
    pass

def Loja_I(ID):
    global informaçoesp1
    global informaçoesp2
    global Contador1
    global Contador2

    if ID == "PokebolasLojaIp1" and Contador1 < 3:
        tocar("Compra")
        informaçoesp1.append("pokebola")
        Contador1 += 1
    elif ID == "ItensLojaIp1" and Contador1 < 3:
        tocar("Compra")
        informaçoesp1.append("item")
        Contador1 += 1
    elif ID == "PokebolasLojaIp2" and Contador2 < 3:
        tocar("Compra")
        informaçoesp2.append("pokebola")
        Contador2 += 1
    elif ID == "ItensLojaIp2" and Contador2 < 3:
        tocar("Compra")
        informaçoesp2.append("item")
        Contador2 += 1
    else:
        tocar("Bloq")

def Iniciar_partida(estados):
    estados["Rodando_PréPartida"] = False
    estados["Rodando_Partida"] = True

def Nome_p1(texto):
    global informaçoesp1
    informaçoesp1[0] = texto

def Nome_p2(texto):
    global informaçoesp2
    informaçoesp2[0] = texto



