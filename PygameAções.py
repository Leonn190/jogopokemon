import GeradoresVisuais as GV
import Gerador

informaçoesp1 = [0,0]
informaçoesp2 = [0,0]

def iniciar_partida(estados):
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

def Remover_inicial(id_botao):
    pass

def acaoteste1():
    GV.adicionar_mensagem("olá")

def acaoteste2():
    GV.adicionar_mensagem("eae")

    GV.adicionar_mensagem("eu desfiz esquerdo")

def Nome_p1(texto):
    global informaçoesp1
    informaçoesp1[0] = texto

def Nome_p2(texto):
    global informaçoesp2
    informaçoesp2[0] = texto


#