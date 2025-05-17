def VitoriaAsh(player, inimigo, Mapa, Baralho):
    if player.NocautesRealizados > 4:
        return True
    return False

def DerrotaAsh(player, inimigo, Mapa, Baralho):
    if player.NocautesSofridos > 4:
        return True
    return False

def PassivaAsh(player, inimigo, Mapa, Baralho):
    for pokemon in player.pokemons:
        pokemon.Ganhar_XP(5,player)

def HabilidadeAsh(player, inimigo, Mapa, Baralho):
    player.PoderCaptura = 2

def VitoriaMisty(player, inimigo, Mapa, Baralho):
    Nocauteados = 0
    for pokemon in inimigo.pokemons:
        if pokemon.Vida == 0:
            Nocauteados += 1
    if Nocauteados > 2:
        return True
    return False

def DerrotaMisty(player, inimigo, Mapa, Baralho):
    total = sum(player.energias.values())
    if total < 7:
        return True
    return False

def PassivaMisty(player, inimigo, Mapa, Baralho):
    for chave in list(player.energias.keys()):
        player.energias[chave] += 1

def HabilidadeMisty(player, inimigo, Mapa, Baralho):
    player.energiasMax = 25

def VitoriaBrock(player, inimigo, Mapa, Baralho):
    pass

def DerrotaBrock(player, inimigo, Mapa, Baralho):
    pass

def PassivaBrock(player, inimigo, Mapa, Baralho):
    pass

def HabilidadeBrock(player, inimigo, Mapa, Baralho):
    pass

def VitoriaJessie(player, inimigo, Mapa, Baralho):
    pass

def DerrotaJessie(player, inimigo, Mapa, Baralho):
    pass

def PassivaJessie(player, inimigo, Mapa, Baralho):
    pass

def HabilidadeJessie(player, inimigo, Mapa, Baralho):
    pass

def VitoriaJames(player, inimigo, Mapa, Baralho):
    pass

def DerrotaJames(player, inimigo, Mapa, Baralho):
    pass

def PassivaJames(player, inimigo, Mapa, Baralho):
    pass

def HabilidadeJames(player, inimigo, Mapa, Baralho):
    pass

def VitoriaGiovanni(player, inimigo, Mapa, Baralho):
    pass

def DerrotaGiovanni(player, inimigo, Mapa, Baralho):
    pass

def PassivaGiovanni(player, inimigo, Mapa, Baralho):
    pass

def HabilidadeGiovanni(player, inimigo, Mapa, Baralho):
    pass

def VitoriaRed(player, inimigo, Mapa, Baralho):
    pass

def DerrotaRed(player, inimigo, Mapa, Baralho):
    pass

def PassivaRed(player, inimigo, Mapa, Baralho):
    pass

def HabilidadeRed(player, inimigo, Mapa, Baralho):
    pass

def VitoriaCarvalho(player, inimigo, Mapa, Baralho):
    pass

def DerrotaCarvalho(player, inimigo, Mapa, Baralho):
    pass

def PassivaCarvalho(player, inimigo, Mapa, Baralho):
    pass

def HabilidadeCarvalho(player, inimigo, Mapa, Baralho):
    pass

Habilidades = {
    "Ash": HabilidadeAsh,
    "Misty": HabilidadeMisty,
    "Brock": HabilidadeBrock,
    "Jessie": HabilidadeJessie,
    "James": HabilidadeJames,
    "Giovanni": HabilidadeGiovanni,
    "Red": HabilidadeRed,
    "Carvalho": HabilidadeCarvalho,
}

Passivas = {
    "Ash": PassivaAsh,
    "Misty": PassivaMisty,
    "Brock": PassivaBrock,
    "Jessie": PassivaJessie,
    "James": PassivaJames,
    "Giovanni": PassivaGiovanni,
    "Red": PassivaRed,
    "Carvalho": PassivaCarvalho,
}

Vitorias = {
    "Ash": VitoriaAsh,
    "Misty": VitoriaMisty,
    "Brock": VitoriaBrock,
    "Jessie": VitoriaJessie,
    "James": VitoriaJames,
    "Giovanni": VitoriaGiovanni,
    "Red": VitoriaRed,
    "Carvalho": VitoriaCarvalho,
}

Derrotas = {
    "Ash": DerrotaAsh,
    "Misty": DerrotaMisty,
    "Brock": DerrotaBrock,
    "Jessie": DerrotaJessie,
    "James": DerrotaJames,
    "Giovanni": DerrotaGiovanni,
    "Red": DerrotaRed,
    "Carvalho": DerrotaCarvalho,
}

Ash = {
    "nome": "Ash",
    "tempo": 180,
    "ativaTurno": 3
}

Misty = {
    "nome": "Misty",
    "tempo": 160,
    "ativaTurno": 3
}

Brock = {
    "nome": "Brock",
    "tempo": 190,
    "ativaTurno": 5
}

Jessie = {
    "nome": "Jessie",
    "tempo": 190,
    "ativaTurno": 5
}

James = {
    "nome": "James",
    "tempo": 170,
    "ativaTurno": 5
}

Giovanni = {
    "nome": "Giovanni",
    "tempo": 200,
    "ativaTurno": 7
}

Red = {
    "nome": "Red",
    "tempo": 180,
    "ativaTurno": 7
}

Professor_Carvalho = {
    "nome": "Professor Carvalho",
    "tempo": 210,
    "ativaTurno": 7
}

Treinadores_Todos = [Ash,Misty,Brock,Jessie,James,Giovanni,Red,Professor_Carvalho]