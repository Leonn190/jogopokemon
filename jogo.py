def golpe_de_fogo(atacante, alvo):
    if alvo['Def'] > 50:
        alvo['Def'] = 50
    dano = 50 - alvo["Def"]
    alvo["Vida"] -= dano

def Disparo_quente(atacante, alvo):
    if alvo['Def'] > 10:
        alvo['Def'] = 10
    dano = 10 - alvo["Def"]
    alvo["Vida"] -= dano

def fogo_puro(atacante, alvo):
    if alvo['Def SP'] > 60:
        alvo['Def SP'] = 60
    dano = 60 - alvo["Def SP"]
    alvo["Vida"] -= dano

def defesa_flamejante(atacante, alvo):
    if alvo['Def SP'] > 60:
        alvo['Def SP'] = 60
    dano = 40 - alvo["Def SP"]
    alvo["Vida"] -= dano
    atacante["Def"] += 10

pokemon1 = {
    "nome": "Charmander",
    "Vida": 100,
    "Def": 20,
    "Def SP": 10,
    "Velocidade": 3,
    "ataque 1": golpe_de_fogo,
    "ataque 2": fogo_puro
}

pokemon2 = {
    "nome": "Litten",
    "Vida": 120,
    "Def": 40,
    "Def SP": 0,
    "Velocidade": 3,
    "ataque 1": Disparo_quente,
    "ataque 2": defesa_flamejante
}

pokemon3 = {
    "nome": "Fenikin",
    "Vida": 90,
    "Def": 30,
    "Def SP": 20,
    "Velocidade": 3,
    "ataque 1": Disparo_quente,
    "ataque 2": fogo_puro
}

pokemon4 = {
    "nome": "Slugma",
    "Vida": 130,
    "Def": 10,
    "Def SP": 30,
    "Velocidade": 3,
    "ataque 1": golpe_de_fogo,
    "ataque 2": defesa_flamejante
}


player1 = ["leon",pokemon1,pokemon2]
player2 = ["jonas",pokemon3,pokemon4]

def opções_de_pokemon(player, inimigo):
    pokemon_escolhido = int(input("Qual pokemon voce deseja escolher? O 1 ou 2"))
    pokemon = player[pokemon_escolhido]
    desejo = input(f"O que {pokemon['nome']} deseja fazer? Atacar, Mover ou Passar o turno?")
    if desejo == "atacar":
        atacar(pokemon, inimigo, player)
    elif desejo == "mover":
        print("Movimentação ainda não configurada.")
    elif desejo == "passar o turno":
        passar_o_turno(inimigo, player)

def passar_o_turno(player, inimigo):
    print(f"Novo turno de {player[0]}")
    opções_de_pokemon(player, inimigo)

def atacar(pokemon, inimigo, player):
    alvo_escolhido = int(input("escolha seu alvo, 1 ou 2"))
    alvo = inimigo[alvo_escolhido]
    ataque = input("Quer usar o ataque 1 ou o ataque 2? ")
    if ataque in pokemon:
        pokemon[ataque](pokemon, alvo)
        print(f"A vida atual de {alvo['nome']} é {alvo['Vida']}")
    else:
        print("Ataque inválido!")

    passar_o_turno(inimigo, player)

opções_de_pokemon(player1, player2)
