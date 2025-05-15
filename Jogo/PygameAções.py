import pygame
import importlib
import os
import Visual.GeradoresVisuais as GV
from Visual.Sonoridade import tocar
import random

pygame.font.init()
pygame.mixer.init()

Compra = pygame.mixer.Sound("Audio/Sons/Compra.wav")
Bloq = pygame.mixer.Sound("Audio/Sons/Bloq.wav")

ListaDecks = []

informaçoesp1 = [random.choice(["Jogador Legal","Jogador Bacanudo","Jogador Estratégico","Jogador Habilidoso"]),random.randint(1,3)]
informaçoesp2 = [random.choice(["Jogador Astuto","Jogador Habil","Jogador Feliz","Jogador Irado"]),random.randint(1,3)]

Contador1 = 0
Contador2 = 0 

def carregar_decks(pasta,ListaDecks):
    ListaDecks.clear()

    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith(".py"):
            caminho = os.path.join(pasta, nome_arquivo)
            nome_modulo = nome_arquivo[:-3]

            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)

            # Procura diretamente no módulo por dicionários
            for atributo in dir(modulo):
                valor = getattr(modulo, atributo)  # Aqui ainda usamos getattr para acessar atributos, já que não há outra forma simples
                if isinstance(valor, dict):
                    ListaDecks.append(valor)
                    break
    
    for i,deck in enumerate(ListaDecks):
        deck["ID"] = f"Deck{i + 1}"
    
    return ListaDecks

def iniciar_prépartida(estados):
    global informaçoesp1, informaçoesp2,Contador1,Contador2
    carregar_decks("Decks",ListaDecks)
    estados["Rodando_Menu"] = False
    estados["Rodando_PréPartida"] = True
    informaçoesp1 = [random.choice(["Jogador Legal","Jogador Bacanudo","Jogador Estratégico","Jogador Habilidoso"]),random.randint(1,3)]
    informaçoesp2 = [random.choice(["Jogador Astuto","Jogador Habil","Jogador Feliz","Jogador Irado"]),random.randint(1,3)]
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



