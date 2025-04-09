def iniciar_partida(estados):
    print("Iniciando partida!")
    estados["Rodando_Menu"] = False
    estados["Rodando_Partida"] = True

def fechar_jogo(estados):
    print("Fechando jogo!")
    estados["Rodando_Menu"] = False
    estados["Rodando_PréPartida"] = False
    estados["Rodando_Partida"] = False
    estados["Rodando_Jogo"] = False
