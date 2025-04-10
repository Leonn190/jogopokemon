import GeradoresVisuais as GV
import Gerador
import random

informaçoesp1 = [random.choice(["Jogador_Legal","Jogador_Bacanudo","Jogador_Estratégico","Jogador_Habilidoso"]),random.randint(1,3)]
informaçoesp2 = [random.choice(["Jogador_Astuto","Jogador_Habil","Jogador_Feliz","Jogador_Irado"]),random.randint(1,3)]

Contador1 = 0
Contador2 = 0 

def iniciar_prépartida(estados):
    print("Iniciando partida!")
    estados["Rodando_Menu"] = False
    estados["Rodando_PréPartida"] = True

def fechar_jogo(estados):
    print("Fechando jogo!")
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

def Voltar(estados):
    global informaçoesp1
    global informaçoesp2
    if estados["Rodando_PréPartida"] == True:
        estados["Rodando_PréPartida"] = False
        estados["Rodando_Menu"] = True
        informaçoesp1 = [0,random.randint(1,3)]
        informaçoesp2 = [0,random.randint(1,3)]

def Remover_inicial(id_botao=None):
    pass

def Loja_I(ID):
    global informaçoesp1
    global informaçoesp2
    global Contador1
    global Contador2

    if ID == "PokebolasLojaIp1" and Contador1 < 5:
        informaçoesp1.append("pokebola")
        Contador1 += 1
        print("P1 comprou pokebola")
    elif ID == "ItensLojaIp1" and Contador1 < 5:
        informaçoesp1.append("item")
        Contador1 += 1
        print("P1 comprou item")
    elif ID == "PokebolasLojaIp2" and Contador2 < 5:
        informaçoesp2.append("pokebola")
        Contador2 += 1
        print("P2 comprou pokebola")
    elif ID == "ItensLojaIp2" and Contador2 < 5:
        informaçoesp2.append("item")
        Contador2 += 1
        print("P2 comprou item")

def Iniciar_partida(estados):
    print (informaçoesp1)
    print (informaçoesp2)
    estados["Rodando_PréPartida"] = False
    estados["Rodando_Partida"] = True

def Nome_p1(texto):
    global informaçoesp1
    informaçoesp1[0] = texto

def Nome_p2(texto):
    global informaçoesp2
    informaçoesp2[0] = texto

def seleciona(Id_botao):
    pass

def desseleciona(id_botao):
    pass

def vizualiza(id_botao):
    pass

def oculta(id_botao):
    pass

#