import Basicos
import pokebolas
import Spawn
import random

LV = {
    "vida": 0,
    "custo": -50
}

Centro = [0]

turno = 0

inventario_p1 = [0,]
inventario_p2 = [0,]

player1 = ["nome",LV,LV,LV,LV,LV,LV,inventario_p1]
player2 = ["nome",LV,LV,LV,LV,LV,LV,inventario_p2]

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
    
    print ("Agora que todos escolheram o pokemon inicial, vamos fazer a compra inicial!")
    comprar(player1,6)
    comprar(player2,6)

    passar_o_turno(player2, player1)

def rodada(player,inimigo):
    desejo = input(f"Qual ação deseja realizar {player[0]}? Usar um pokemon, capturar um pokemon, passar o turno?").lower()
    if desejo == "usar um pokemon" or desejo == "usar pokemon" or desejo =="1":
        opções_de_pokemon(player,inimigo)
    elif desejo == "capturar um pokemon" or desejo == "capturar" or desejo == "2":
        capturar_pokemon(player,inimigo)
    elif desejo == "passar o turno" or desejo == "passar turno" or desejo == "3":
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
    global turno
    global Centro
    if all(player[i]["vida"] <= 0 for i in range(1, 7)):
        print (f"{player[0]} foi derrotado, a vitória é de {inimigo[0]}!")
    elif all(inimigo[i]["vida"] <= 0 for i in range(1, 7)):
        print (f"{inimigo[0]} foi derrotado, a vitória é de {player[0]}!")
    else:
        turno += 1
        print(f"Iniciando o turno {turno}, Vez de {inimigo[0]}")
        if turno == 1:
            for i in range(1,4):
                Spawn.spawn_do_centro(Centro)
        else:
            Spawn.spawn_do_centro(Centro)
        
        rodada(inimigo,player)

def atacar(pokemon, inimigo, player):
    alvo_escolhido = int(input("escolha seu alvo, 1 ou 2"))
    alvo = inimigo[alvo_escolhido]
    while True:
        ataque = input(f"Quer atacar o {alvo['nome']} com o ataque normal ou o ataque especial?").lower()
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

def comprar(player,compras):
    for i in range(compras):
        while True:
            loja = input(f"{player[0]}, você deseja comprar em qual loja? loja de pokebolas?").lower()
            if loja == "loja de pokebolas" or loja == "pokebolas" or loja == "1":
                player[7].append (pokebolas.ganhar_pokebola(player,"aleatoria"))
                print ("compra realizada")
                break
            else:
                print("loja invalida, tente novamente")
    
    print (f"A compra foi realizada! seu inventário atual é:")
    for i in range(len(player[7])-1):
        print (f"{i+1} - {player[7][i+1]['nome']}") 

def capturar_pokemon(player,inimigo):
    global Centro
    global LV

    print ("pokemons que estão atualmente no centro:")
    for i in range(len(Centro)-1):
        print (f"{i+1} - {Centro[i+1]['nome']}")
    pokemon_escolhido = int(input("Qual o numero do pokemon que voce deseja capturar?"))

    pokebolas_existentes = ["pokebola","greatball","ultraball","masterball"]
    
    resposta = 2

    for i in range(len(player[7])-1):
        if player[7][i+1]["nome"] in pokebolas_existentes:
            resposta = "sim"

    if resposta == 2:
        print ("sem pokebolas disponiveis")

    print (resposta)
    while resposta == "sim" or resposta == "s" or resposta == "1":
        for i in range(len(player[7])-1):
            print (f"{i+1} - {player[7][i+1]['nome']}")
        pokebola_utilizada = int(input("escolha a pokebola que voce vai usar! escolha o numero do item no inventário mostrado acima:"))
        if player[7][pokebola_utilizada]["nome"] in pokebolas_existentes:
            maestria = random.randint(1,player[7][pokebola_utilizada]["poder"] * 2)
            if maestria > Centro[pokemon_escolhido]["dificuldade"]:
                if LV in player:
                    for i in range(len(player)-2):
                        if player[i+1]["custo"] == -50:
                            player[i+1] = Centro[pokemon_escolhido]["gerador"]()
                            print (f"Parabens, você capturou um {Centro[pokemon_escolhido]['nome']} utilizando uma {player[7][pokebola_utilizada]['nome']}! ele está na posição {i+1}")
                            del Centro[pokemon_escolhido]
                            del player[7][pokebola_utilizada]
                            rodada(player,inimigo)
                else:
                    print ("sua lista de pokemon está cheia")
            else:
                print ("Voce falhou em capturar o pokemon, que pena")
        
            del player[7][pokebola_utilizada]
            resposta = input("quer tentar mais uma vez?")
                
        else:
            print ("O item selecionado não é uma pokebola ou não existe")
    rodada(player,inimigo)
    


inicio(player1,player2)

