def golpe_de_fogo(atacante, alvo):
    if alvo['Def'] > 50:
        alvo['Def'] = 50
    dano = 50 - alvo["Def"]
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
    "nome": "Bulbasaur",
    "Vida": 120,
    "Def": 40,
    "Def SP": 0,
    "Velocidade": 3,
    "ataque 1": golpe_de_fogo,
    "ataque 2": defesa_flamejante
}

def opções(player, inimigo):
    desejo = input(f"O que {player['nome']} deseja fazer? Atacar, Mover ou Passar o turno? ")
    if desejo == "atacar":
        atacar(player, inimigo)
    elif desejo == "mover":
        print("Movimentação ainda não configurada.")
    elif desejo == "passar o turno":
        passar_o_turno(inimigo, player)

def passar_o_turno(player, inimigo):
    print(f"\n--- Novo turno de {player['nome']} ---")
    opções(player, inimigo)

def atacar(player, inimigo):
    ataque = input("Quer usar o ataque 1 ou o ataque 2? ")
    if ataque in player:
        player[ataque](player, inimigo)
        print(f"A vida atual de {inimigo['nome']} é {inimigo['Vida']}")
    else:
        print("Ataque inválido!")

    passar_o_turno(inimigo, player)

opções(pokemon1, pokemon2)
