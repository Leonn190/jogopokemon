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

Energias_p1 = { "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "veneno": 0,
                "terra": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0,
                "sombrio": 0, "aço": 0, "fada": 0}

Energias_p2 = { "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "veneno": 0,
                "terra": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0,
                "sombrio": 0, "aço": 0, "fada": 0}

Energias = ["fogo", "agua", "eletrico", "planta", "gelo", "lutador", "veneno", "terra", "voador", "psiquico", "inseto", "pedra", "fantasma", "dragao", "sombrio", "aço", "fada"]

descartaveis_p1 = []
descartaveis_p2 = []

player1 = ["nome",LV,LV,LV,LV,LV,LV,inventario_p1,Energias_p1,descartaveis_p1]
player2 = ["nome",LV,LV,LV,LV,LV,LV,inventario_p2,Energias_p2,descartaveis_p2]

def inicio(player1, player2):

    player1[0] = input("Qual é seu nome player 1? ")
    player2[0] = input("Qual é seu nome player 2? ")

    intersecção = input("irei fornecer 12 energias para cada jogador, certo?")

    ganhar_energia(player1,12)

    intersecção = input(f"Sua vez {player2[0]}, pronto?")

    ganhar_energia(player2,12)

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
            print(f"Charmander com {player2[1]['IV']} de IV foi selecionado")
            break
        elif pokemon_inicial == "bulbasauro" or pokemon_inicial == "2":
            player2[1] = Basicos.gerador_bulbasaur()
            print(f"Bulbasauro com {player2[1]['IV']} de IV foi selecionado")
            break
        elif pokemon_inicial == "squirtle" or pokemon_inicial == "3":
            player2[1] = Basicos.gerador_squirtle()
            print(f"Squirtle com {player2[1]['IV']} de IV foi selecionado")
            break
        else:
            print("Pokémon inválido. Tente novamente.")
    
    print ("Agora que todos escolheram o pokemon inicial, vamos fazer as 6 compras iniciais!")
    comprar(player1,6)
    comprar(player2,6)

    intersecção = input("Por fim precisamos definir as energias descartaveis de cada jogador, essas energias serão usadas na ordem que voce posicionar elas, certo?")

    modificar_energias_descartaveis(player1)
    modificar_energias_descartaveis(player2)

    passar_o_turno(player2, player1)

def rodada(player,inimigo):
    global turno
    if turno > 2:
        comprar(player,1)
    
    desejo = input(f"Qual ação deseja realizar {player[0]}? Usar um pokemon, capturar um pokemon, passar o turno?").lower()
    if desejo == "usar um pokemon" or desejo == "usar pokemon" or desejo =="1":
        opções_de_pokemon(player,inimigo)
    elif desejo == "capturar um pokemon" or desejo == "capturar" or desejo == "2":
        capturar_pokemon(player)
        rodada(player,inimigo)
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
    alvo_escolhido = int(input("escolha seu alvo, 1 a 6"))
    alvo = inimigo[alvo_escolhido]
    resposta = "1"
   
    while resposta == "sim" or resposta == "s" or resposta == "1":
        print (f"ataques de {pokemon['nome']} disponiveis")
        print (f"1 - Ataque normal - {pokemon['ataque normal']['nome']} - Custo: ({pokemon['ataque normal']['custo']})")
        print (f"2 - Ataque especial - {pokemon['ataque especial']['nome']} - Custo: ({pokemon['ataque especial']['custo']})")
        ataque = input(f"Quer atacar o {alvo['nome']} com o ataque normal ou o ataque especial?").lower()
        
        if ataque == "ataque normal" or ataque == "normal" or ataque == "1":
            foi = pokemon["ataque normal"]["fun"](pokemon, alvo, player, inimigo,pokemon["ataque normal"])
            if foi == 0:
                resposta = input("Seu ataque não teve energias o suficiente, quer tentar outro ataque?")
            else:
                print(f"O {pokemon['nome']} usou um ataque normal para atacar o {alvo['nome']} inimigo!")
                print(f"A vida atual do {alvo['nome']} inimigo é {alvo['vida']}")
                pokemon["XP atu"] += 1
                break
       
        if ataque == "ataque especial" or ataque == "especial" or ataque == "2":
            foi = pokemon["ataque especial"]["fun"](pokemon, alvo, player, inimigo,pokemon["ataque especial"])
            if foi == 0:
                resposta = input("Seu ataque não teve energias o suficiente, quer tentar outro ataque?")
            else:
                print(f"O {pokemon['nome']} usou um ataque normal para atacar o {alvo['nome']} inimigo!")
                print(f"A vida atual do {alvo['nome']} inimigo é {alvo['vida']}")
                pokemon["XP atu"] += 1
                break
        else:
            print("Ataque inválido! Tente novamente")

    passar_o_turno(player, inimigo)

def comprar(player,compras):
    for i in range(compras):
        while True:
            loja = input(f"{player[0]}, você deseja comprar em qual loja? loja de pokebolas, de itens ?").lower()
            if loja == "loja de pokebolas" or loja == "pokebolas" or loja == "1":
                player[7].append (pokebolas.ganhar_pokebola(player,"aleatoria"))
                print ("compra realizada na loja de pokebolas")
                break
            else:
                print("loja invalida, tente novamente")
    
    print (f"A compra foi realizada! seu inventário atual é:")
    for i in range(len(player[7])-1):
        print (f"{i+1} - {player[7][i+1]['nome']}") 

def capturar_pokemon(player):
    global Centro
    global LV

    print ("pokemons que estão atualmente no centro:")
    for i in range(len(Centro)-1):
        print (f"{i+1} - {Centro[i+1]['nome']}")
    pokemon_escolhido = int(input("Qual o numero do pokemon que voce deseja capturar?"))

    pokebolas_existentes = ["pokebola","greatball","ultraball","masterball"]
    
    resposta = "não"

    for i in range(len(player[7])-1):
        if player[7][i+1]["nome"] in pokebolas_existentes:
            resposta = "sim"

    if resposta == "não":
        print ("sem pokebolas disponiveis")

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
                            return
                else:
                    print ("sua lista de pokemon está cheia")
            else:
                print ("Voce falhou em capturar o pokemon, que pena")
        
            del player[7][pokebola_utilizada]
            resposta = input("quer tentar mais uma vez?").lower()
                
        else:
            print ("O item selecionado não é uma pokebola ou não existe")

def ganhar_energia(player,numero):
    global Energias
    for i in range(numero):
        j = random.choice(Energias)
        player[8][j] = player[8][j] + 1
        print (f"{player[0]} ganhou 1 energia de {j}")

def modificar_energias_descartaveis(player):
    global turno
    if turno == 0:
        r = "sim"
        while r in ["sim","s"]:
            escolha = input(f"qual voce quer adicionar, {player[0]}?").lower()
            if escolha in Energias and escolha not in player[9]:
                player[9].append (escolha)
                r = input("vamos adicionar mais alguma?").lower()
            else:
                print ("essa energia não existe ou já foi adicionada, tente novamente")
    else:
        resposta = "s"
        while resposta == "sim" or resposta == "s":
            decisão = input(f"{player[0]}, você deseja adicionar ou remover um tipo?").lower()
            if decisão == "adicionar" or decisão == "1":
                escolha = input("qual voce quer adicionar?").lower()
                if escolha in Energias and escolha not in player[9]:
                    player[9].append (escolha)
                    resposta = input("energia foi adicionada, deseja fazer mais alguma modificação?")
                else:
                    print ("essa energia não existe ou já está na lista, tente novamente")
            elif decisão == "remover" or decisão == "2":
                if len(player[9]) == 1:
                    print (f"existe apenas o tipo {player[9][0]} nas suas energias descartaveis, adicione mais uma para remove-lo")
                else: 
                    print ("mostrando sua lista de energias abaixo:")
                    for i in range(len(player[9])):
                        print (f"{i} - {player[9][i]}")
                    escolha = int(input("escolha o numero da energia que irá remover da lista acima"))
                    del player[9][escolha]
                    resposta = input("O tipo foi removido, deseja fazer mais alguma modificação")
    print ("mostrando sua lista de energias descartaveis abaixo após as modificações: (0 é a)")
    for i in range(len(player[9])):
        print (f"{i} - {player[9][i]}")


inicio(player1,player2)

