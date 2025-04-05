import Basicos

LV = {
    "vida": 0
}

player1 = ["nome",LV,LV,LV,LV,LV,LV]
player2 = ["nome",LV,LV,LV,LV,LV,LV]

def inicio(player1, player2):

    player1[0] = input("Qual é seu nome player 1? ")
    player2[0] = input("Qual é seu nome player 2? ")

    while True:
        pokemon_inicial = input(f"Qual será seu Pokémon inicial {player1[0]}? Charmander, Bulbasaur ou Squirtle? ").lower()
        if pokemon_inicial == "charmander" or pokemon_inicial == "1":
            player1[1] = Basicos.gerador_charmander()
            print(f"Charmander com {player1[1]['IV']} de IV foi selecionado")
            break
        elif pokemon_inicial == "bulbasaur" or pokemon_inicial == "2":
            player1[1] = Basicos.gerador_bulbasaur()
            print(f"Bulbasauro com {player1[1]['IV']} de IV foi selecionado")
            break
        elif pokemon_inicial == "squirtle" or pokemon_inicial == "3":
            player1[1] = Basicos.gerador_squirtle()
            print(f"Squirtle com {player1[1]['IV']} de IV foi selecionado")
            break
        else:
            print("Pokémon inválido. Tente novamente.")

    while True:
        pokemon_inicial = input(f"Qual será seu Pokémon inicial {player2[0]}? Charmander, Bulbasaur ou Squirtle? ").lower()
        if pokemon_inicial == "charmander" or pokemon_inicial == "1":
            player2[1] = Basicos.gerador_charmander()
            print(f"Charmander com {player2[1]['IV']}% de IV foi selecionado")
            break
        elif pokemon_inicial == "bulbasauro" or pokemon_inicial == "2":
            player2[1] = Basicos.gerador_bulbasaur()
            print(f"Bulbasauro com {player2[1]['IV']}% de IV foi selecionado")
            break
        elif pokemon_inicial == "squirtle" or pokemon_inicial == "3":
            player2[1] = Basicos.gerador_squirtle()
            print(f"Squirtle com {player2[1]['IV']}% de IV foi selecionado")
            break
        else:
            print("Pokémon inválido. Tente novamente.")

    rodada(player1, player2)

def rodada(player,inimigo):
    desejo = input(f"Qual ação deseja realizar {player[0]}? Usar um pokemon ou passar o turno?").lower()
    if desejo == "usar um pokemon" or desejo == "usar pokemon" or desejo =="1":
        opções_de_pokemon(player,inimigo)
    elif desejo == "passar o turno" or desejo == "passar turno" or desejo == "2":
        passar_o_turno(player, inimigo)
    else:
        print ("ação invalida, tente novamente")
        rodada(player,inimigo)

def opções_de_pokemon(player, inimigo):
    while True:
        pokemon_escolhido = int(input("Qual pokemon voce deseja escolher? escolha de 1 a 6"))
        pokemon = player[pokemon_escolhido]
        if pokemon != 0:
            break
        else:
            print ("esse pokemon não existe! Tente novamente")
    while True:
        desejo = input(f"O que {pokemon['nome']} deseja fazer? Atacar, Mover ou Evoluir?").lower()
        if desejo == "atacar" or desejo == "1":
            atacar(pokemon, inimigo, player)
            break
        elif desejo == "mover" or desejo == "2":
            print("Movimentação ainda não configurada, tente apenas atacar.")
        elif desejo == "evoluir" or desejo == "3":
            if pokemon["XP atu"] >= pokemon["XP"]:
                nome_antigo = pokemon['nome']
                player1[pokemon_escolhido] = pokemon["evolução"](pokemon)
                pokemon = player1[pokemon_escolhido]
                print (f"Seu {nome_antigo} evoluiu para um {pokemon['nome']}!")
            else:
                print (f"Ainda não tem o XP necessário para evoluir, Seu XP é {pokemon['XP atu']} e precisa de {pokemon['XP']} para evoluir")
        else:
            print("Ação invalida! Tente novamente")

def passar_o_turno(player, inimigo):
    if all(player[i]["vida"] <= 0 for i in range(1, 7)):
        print (f"{player[0]} foi derrotado, a vitória é de {inimigo[0]}!")
    elif all(inimigo[i]["vida"] <= 0 for i in range(1, 7)):
        print (f"{inimigo[0]} foi derrotado, a vitória é de {player[0]}!")
    else:
        print(f"Novo turno de {inimigo[0]}")
        rodada(inimigo,player)

def atacar(pokemon, inimigo, player):
    alvo_escolhido = int(input("escolha seu alvo, 1 ou 2"))
    alvo = inimigo[alvo_escolhido]
    ataque = input(f"Quer atacar o {alvo['nome']} com o ataque normal ou o ataque especial?").lower()
    while True:
        if ataque == "ataque normal" or ataque == "normal" or ataque == "1":
            pokemon["ataque normal"](pokemon, alvo, player, inimigo)
            print(f"O {pokemon['nome']} usou um ataque normal para atacar o {alvo['nome']} inimigo!")
            print(f"A vida atual do {alvo['nome']} inimigo é {alvo['vida']}")
            pokemon["XP atu"] += 1
            break
        if ataque == "ataque especial" or ataque == "especial" or ataque == "2":
            pokemon["ataque especial"](pokemon, alvo, player, inimigo)
            print(f"O {pokemon['nome']} usou um ataque especial para atacar o {alvo['nome']} inimigo!")
            print(f"A vida atual do {alvo['nome']} inimigo é {alvo['vida']}")
            pokemon["XP atu"] += 1
            break
        else:
            print("Ataque inválido! Tente novamente")

    passar_o_turno(player, inimigo)

inicio(player1,player2)

