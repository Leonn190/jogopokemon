import GeradoresVisuais as GV


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

def acaoteste1():
    GV.adicionar_mensagem("olá")

def acaoteste2():
    GV.adicionar_mensagem("eae")

def desfazteste1():
    GV.adicionar_mensagem("eu desfiz direito")

def desfazteste2():
    GV.adicionar_mensagem("eu desfiz esquerdo")

def minha_funcao_envio(texto):
    global texto_input
    GV.adicionar_mensagem(texto)


#