import Basicos
import itens
import Spawn
import random
from prettytable import PrettyTable

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

pokemon_p1 = [0]
pokemon_p2 = [0]

player1 = ["nome",pokemon_p1,inventario_p1,Energias_p1,descartaveis_p1]
player2 = ["nome",pokemon_p2,inventario_p2,Energias_p2,descartaveis_p2]

def inicio(player1, player2):

    player1[0] = input("Qual é seu nome player 1? ")
    player2[0] = input("Qual é seu nome player 2? ")

    intersecção = input("irei fornecer 20 energias para cada jogador, certo?")

    ganhar_energia(player1,20)

    intersecção = input(f"Sua vez {player2[0]}, pronto?")

    ganhar_energia(player2,12)

    while True:
        pokemon_inicial = input(f"Qual será seu Pokémon inicial {player1[0]}? Charmander, Bulbasaur ou Squirtle? ").lower()
        if pokemon_inicial == "charmander" or pokemon_inicial == "1":
            pokemon1_p1 = Basicos.gerador_charmander()
            player1[1].append(pokemon1_p1)
            print(f"Charmander com {player1[1][1]['IV']} de IV foi selecionado")
            break
        elif pokemon_inicial == "bulbasaur" or pokemon_inicial == "2":
            pokemon1_p1 = Basicos.gerador_bulbasaur()
            player1[1].append(pokemon1_p1)
            print(f"Bulbasauro com {player1[1][1]['IV']} de IV foi selecionado")
            break
        elif pokemon_inicial == "squirtle" or pokemon_inicial == "3":
            pokemon1_p1 = Basicos.gerador_squirtle()
            player1[1].append(pokemon1_p1)
            print(f"Squirtle com {player1[1][1]['IV']} de IV foi selecionado")
            break
        else:
            print("Pokémon inválido. Tente novamente.")

    while True:
        pokemon_inicial = input(f"Qual será seu Pokémon inicial {player2[0]}? Charmander, Bulbasaur ou Squirtle? ").lower()
        if pokemon_inicial == "charmander" or pokemon_inicial == "1":
            pokemon1_p2 = Basicos.gerador_charmander()
            player2[1].append(pokemon1_p2)
            print(f"Charmander com {player2[1][1]['IV']} de IV foi selecionado")
            break
        elif pokemon_inicial == "bulbasauro" or pokemon_inicial == "2":
            pokemon1_p2 = Basicos.gerador_bulbasaur()
            player2[1].append(pokemon1_p2)
            print(f"Bulbasauro com {player2[1][1]['IV']} de IV foi selecionado")
            break
        elif pokemon_inicial == "squirtle" or pokemon_inicial == "3":
            pokemon1_p2 = Basicos.gerador_squirtle()
            player2[1].append(pokemon1_p2)
            print(f"Squirtle com {player2[1][1]['IV']} de IV foi selecionado")
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
    
    ações = [0 ,"usar um pokemon", "capturar um pokemon", "usar itens", "fazer analises", "modificar energias descartaveis", "passar o turno"]
    
    if turno > 2:
        comprar(player,1)
        ganhar_energia(player,3)
    
    for i in range(len(ações)-1):
        print (f"{i+1} - {ações[i+1]}")
    desejo = input(f"Qual ação deseja realizar {player[0]}? ações disponiveis acima").lower()

    if desejo in ["usar um pokemon", "usar pokemon", "pokemon","1"]:
        opções_de_pokemon(player,inimigo)
    elif desejo in ["capturar um pokemon", "capturar pokemon", "capturar","2"]:
        capturar_pokemon(player)
        rodada(player,inimigo)
    elif desejo in ["usar itens","itens","3"]:
        usar_itens(player,inimigo)
    elif desejo in ["fazer analises", "analises", "4"]:
        analises(player,inimigo)
        rodada(player,inimigo)
    elif desejo in ["modificar energias descartaveis", "modificar energias", "5"]:
        modificar_energias_descartaveis(player)
        rodada(player,inimigo)
    elif desejo in ["passar o turno", "passar turno", "passar", "6"]:
        passar_o_turno(player, inimigo)
    else:
        print ("ação invalida, tente novamente")
        rodada(player,inimigo)

def opções_de_pokemon(player, inimigo):
    while True:
        pokemon_escolhido = int(input("Qual pokemon voce deseja escolher? escolha de 1 a 6"))
        pokemon = player[1][pokemon_escolhido]
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
    if all(player[1][i+1]["vida"] <= 0 for i in range(len(player[1])-1)):
        print (f"{player[0]} foi derrotado, a vitória é de {inimigo[0]}!")
    elif all(inimigo[1][i+1]["vida"] <= 0 for i in range(len(inimigo[1])-1)):
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
    alvo = inimigo[1][alvo_escolhido]
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
                print(f"O {pokemon['nome']} usou um ataque normal {pokemon['ataque normal']['nome']} para atacar o {alvo['nome']} inimigo!")
                print(f"A vida atual do {alvo['nome']} inimigo é {alvo['vida']}")
                pokemon["XP atu"] += 1
                break
       
        if ataque == "ataque especial" or ataque == "especial" or ataque == "2":
            foi = pokemon["ataque especial"]["fun"](pokemon, alvo, player, inimigo,pokemon["ataque especial"])
            if foi == 0:
                resposta = input("Seu ataque não teve energias o suficiente, quer tentar outro ataque?")
            else:
                print(f"O {pokemon['nome']} usou um ataque normal {pokemon['ataque especial']['nome']} para atacar o {alvo['nome']} inimigo!")
                print(f"A vida atual do {alvo['nome']} inimigo é {alvo['vida']}")
                pokemon["XP atu"] += 1
                break
        else:
            print("Ataque inválido! Tente novamente")

    passar_o_turno(player, inimigo)

def comprar(player,compras):
    for i in range(compras):
        while True:
            loja = input(f"{player[0]}, você deseja comprar em qual loja? loja de pokebolas, de itens ou de amplificadores ?").lower()
            if loja in ["loja de pokebolas", "pokebolas","1"]:
                tipo = "pokebola"
                break
            elif loja in ["loja de itens", "itens","2"]:
                tipo = "item"
                break
            elif loja in ["loja de amplificadores","amplificadores","3"]:
                tipo = "amplificador"
                break
            else:
                print("loja invalida, tente novamente")
        ganho = itens.ganhar_item(player,tipo)
        print (f"Você ganhou: {ganho['nome']}!")
        player[2].append(ganho)
    
    print (f"A compra foi realizada! seu inventário atual é:")
    for i in range(len(player[2])-1):
        print (f"{i+1} - {player[2][i+1]['nome']}") 

def capturar_pokemon(player):
    global Centro
    global LV

    print ("pokemons que estão atualmente no centro:")
    for i in range(len(Centro)-1):
        print (f"{i+1} - {Centro[i+1]['nome']}")
    pokemon_escolhido = int(input("Qual o numero do pokemon que voce deseja capturar?"))

    pokebolas_existentes = ["pokebola","greatball","ultraball","masterball"]
    
    resposta = "não"

    for i in range(len(player[2])-1):
        if player[2][i+1]["nome"] in pokebolas_existentes:
            resposta = "sim"

    if resposta == "não":
        print ("sem pokebolas disponiveis")

    while resposta == "sim" or resposta == "s" or resposta == "1":
        for i in range(len(player[2])-1):
            print (f"{i+1} - {player[2][i+1]['nome']}")
        pokebola_utilizada = int(input("escolha a pokebola que voce vai usar! escolha o numero do item no inventário mostrado acima:"))
        if player[2][pokebola_utilizada]["nome"] in pokebolas_existentes:
            maestria = random.randint(1,player[2][pokebola_utilizada]["poder"] * 2)
            if maestria > Centro[pokemon_escolhido]["dificuldade"]:
                if len(player[1]) < 7:
                    novo_pokemon = Centro[pokemon_escolhido]["gerador"]()
                    player[1].append (novo_pokemon)
                    print (f"Parabens, você capturou um {Centro[pokemon_escolhido]['nome']} utilizando uma {player[2][pokebola_utilizada]['nome']}! ele está na posição {len(player[1])-1} e tem {Centro[pokemon_escolhido]['IV']} de IV")
                    del Centro[pokemon_escolhido]
                    del player[2][pokebola_utilizada]
                    return
                else:
                    print ("sua lista de pokemon está cheia")
            else:
                print ("Voce falhou em capturar o pokemon, que pena")
        
                del player[2][pokebola_utilizada]
                resposta = input("quer tentar mais uma vez?").lower()
                
        else:
            print ("O item selecionado não é uma pokebola ou não existe")

def ganhar_energia(player,numero):
    global Energias
    for i in range(numero):
        j = random.choice(Energias)
        player[3][j] = player[3][j] + 1
        print (f"{player[0]} ganhou 1 energia de {j}")

def modificar_energias_descartaveis(player):
    global turno
    if turno == 0:
        r = "sim"
        while r in ["sim","s"]:
            escolha = input(f"qual voce quer adicionar, {player[0]}?").lower()
            if escolha in Energias and escolha not in player[4]:
                player[4].append (escolha)
                r = input("vamos adicionar mais alguma?").lower()
            else:
                print ("essa energia não existe ou já foi adicionada, tente novamente")
    else:
        resposta = "s"
        while resposta == "sim" or resposta == "s":
            decisão = input(f"{player[0]}, você deseja adicionar ou remover um tipo?").lower()
            if decisão == "adicionar" or decisão == "1":
                escolha = input("qual voce quer adicionar?").lower()
                if escolha in Energias and escolha not in player[4]:
                    player[4].append (escolha)
                    resposta = input("energia foi adicionada, deseja fazer mais alguma modificação?")
                else:
                    print ("essa energia não existe ou já está na lista, tente novamente")
            elif decisão == "remover" or decisão == "2":
                if len(player[4]) == 1:
                    print (f"existe apenas o tipo {player[4][0]} nas suas energias descartaveis, adicione mais uma para remove-lo")
                else: 
                    print ("mostrando sua lista de energias abaixo:")
                    for i in range(len(player[4])):
                        print (f"{i} - {player[4][i]}")
                    escolha = int(input("escolha o numero da energia que irá remover da lista acima"))
                    del player[4][escolha]
                    resposta = input("O tipo foi removido, deseja fazer mais alguma modificação")
    print ("mostrando sua lista de energias descartaveis abaixo após as modificações: (0 é a principal)")
    for i in range(len(player[4])):
        print (f"{i} - {player[4][i]}")

def usar_itens(player,inimigo):
    tabela = PrettyTable()

    U = player[2]

    tabela.title = f"Inventario de {player[0]}"
    tabela.field_names = ["pos", " Nome do item ", "Classe", "Descrição"]
    for i in range(len(U)-1):
        tabela.add_row ([i+1,U[i+1]["nome"],U[i+1]["classe"],U[i+1]["Descrição"]]) 
    print (tabela)
    
def analises(player,inimigo):
    global Energias

    analises_disponiveis = [0,"ver seus pokemons", "ver os pokemons inimigos", "ver suas energias", "ver as energias inimigas"]
    resposta = "sim"
    
    while resposta not in ["n","nao","não"]:
        tabela = PrettyTable()
        print ("qual analise voce deseja fazer")
        for i in range(len(analises_disponiveis)-1):
            print (f"{i+1} - {analises_disponiveis[i+1]}")
        desejo = input("qual?")
        
        Tipo = "fogo"

        if desejo in ["ver seus pokemon", "1","ver os pokemons inimigos", "2"]:
            if desejo in ["ver seus pokemon", "1"]:
                V = player
            elif desejo in ["ver os pokemons inimigos", "2"]:
                V = inimigo
            for i in range(len(V[1])-1):
                U = V[1][i+1]
                tabela.title =  f"Status do {U['nome']} de {V[0]}"
                tabela.field_names = ["Vida"," ATK ","Sp ATK"," DEF ","Sp DEF"," VEL ","custo","ataque normal","ataque especial","XP","IV"]
                tabela.add_row([U["vida"],U["atk"],U["atk SP"],U["def"],U["def SP"],U["velocidade"],U["custo"],U["ataque normal"]["nome"],U["ataque especial"]["nome"],U["XP atu"],U["IV"]])
        elif desejo in ["ver suas energias", "3","ver as energias inimigas", "4"]:
            if desejo in ["ver suas energias", "3"]:
                V = player
            elif desejo in ["ver as energias inimigas", "4"]:
                V = inimigo
            exibi = []
            for Tipo in Energias:
                exibi.append(V[3][Tipo])
            tabela.title = f"Coleção de energias do {V[0]}"
            tabela.field_names = Energias
            tabela.add_row(exibi)
        print (tabela)
        resposta = input("Deseja realizar mais alguma analise?")
        tabela = 0

inicio(player1,player2)

