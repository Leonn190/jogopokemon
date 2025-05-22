import random

def VitoriaAsh(player, inimigo, Mapa, Baralho, Turno):
    player.Pontos = player.NocautesRealizados

def DerrotaAsh(player, inimigo, Mapa, Baralho, Turno):
    player.PontosSofridos = player.NocautesSofridos

def PassivaAsh(player, inimigo, Mapa, Baralho, Turno):
    player.PoderCaptura += 1

def HabilidadeAsh(player, inimigo, Mapa, Baralho, Turno):
    player.pokemon[0].Ganhar_XP(10,player)

def VitoriaMisty(player, inimigo, Mapa, Baralho, Turno):
    if inimigo.PokemonsNocauteados > 1:
        player.Pontos += 1

def DerrotaMisty(player, inimigo, Mapa, Baralho, Turno):
    total = sum(player.energias.values())
    if total < 10:
        player.PontosSofridos += 1

def PassivaMisty(player, inimigo, Mapa, Baralho, Turno):
    for chave in list(player.energias.keys()):
        player.energias[chave] += 1

def HabilidadeMisty(player, inimigo, Mapa, Baralho, Turno):
    player.energiasMax = 25

def VitoriaBrock(player, inimigo, Mapa, Baralho, Turno):
    player.Pontos = Turno

def DerrotaBrock(player, inimigo, Mapa, Baralho, Turno):
    player.NocautesSofridos = player.PontosSofridos

def PassivaBrock(player, inimigo, Mapa, Baralho, Turno):
    for pokemon in player.pokemons:
        if pokemon.local is not None:
            pokemon.barreira += 5

def HabilidadeBrock(player, inimigo, Mapa, Baralho, Turno):
    player.pokemons[0].barreira += 30

def VitoriaJessie(player, inimigo, Mapa, Baralho, Turno):
    player.Pontos = player.NocautesRealizados

def DerrotaJessie(player, inimigo, Mapa, Baralho, Turno):
    player.PontosSofridos = player.NocautesSofridos

def PassivaJessie(player, inimigo, Mapa, Baralho, Turno):
    if inimigo.itens != []:
        item = random.choice(inimigo.itens)
        player.inventario.append(item)
        inimigo.inventario.remove(item)

def HabilidadeJessie(player, inimigo, Mapa, Baralho, Turno):
    from Geradores.GeradorOutros import item_extra
    item_extra(player,"Masterball")

def VitoriaJames(player, inimigo, Mapa, Baralho, Turno):
    player.Pontos = min(9,player.PokemonsCapturados)
    player.Pontos += player.NocautesRealizados

def DerrotaJames(player, inimigo, Mapa, Baralho, Turno):
    if player.PokemonsNocauteados > 1:
        player.PontosSofridos += 1

def PassivaJames(player, inimigo, Mapa, Baralho, Turno):
    from Geradores.GeradorOutros import item_extra
    item_extra(player,"Gosma Desagradável")
    if getattr(player, "RemoveuPokemon", None):
        player.RemoveuPokemon = False

def HabilidadeJames(player, inimigo, Mapa, Baralho, Turno):
    pass

def VitoriaGiovanni(player, inimigo, Mapa, Baralho, Turno):
    player.Pontos = min(48,player.ouro)
    player.Pontos += player.NocautesRealizados

def DerrotaGiovanni(player, inimigo, Mapa, Baralho, Turno):
    player.PontosSofridos = player.PokemonsNocauteados

def PassivaGiovanni(player, inimigo, Mapa, Baralho, Turno):
    ganho = (player.ouro // 10) * 4
    player.ouro += ganho

def HabilidadeGiovanni(player, inimigo, Mapa, Baralho, Turno):
    player.ouro += player.ouro

def VitoriaRed(player, inimigo, Mapa, Baralho, Turno):
    player.Pontos = player.NocautesRealizados

def DerrotaRed(player, inimigo, Mapa, Baralho, Turno):
    pass

def PassivaRed(player, inimigo, Mapa, Baralho, Turno):
    from Geradores.GeradorOutros import item_extra
    item_extra(player,"Mega Energia")

def HabilidadeRed(player, inimigo, Mapa, Baralho, Turno):
    player.Megas = -5

def VitoriaCarvalho(player, inimigo, Mapa, Baralho, Turno):
    pass

def DerrotaCarvalho(player, inimigo, Mapa, Baralho, Turno):
    player.PontosSofridos = player.NocautesSofridos

def PassivaCarvalho(player, inimigo, Mapa, Baralho, Turno):
    for pokemon in player.pokemons:
        if pokemon.local is not None:
            pokemon.Ganhar_XP(12,player)

def HabilidadeCarvalho(player, inimigo, Mapa, Baralho, Turno):
    player.MultiplicaIV = 1.3

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
    "tempo": 170,
    "ativaTurno": 3,
    "Poder": 1,
    "Vitoria": 4,
    "Derrota": 4,
}

Misty = {
    "nome": "Misty",
    "tempo": 150,
    "ativaTurno": 3,
    "Poder": 2,
    "Vitoria": 3,
    "Derrota": 3
}

Brock = {
    "nome": "Brock",
    "tempo": 160,
    "ativaTurno": 5,
    "Poder": 2,
    "Vitoria": 30,
    "Derrota": 5,
}

Jessie = {
    "nome": "Jessie",
    "tempo": 150,
    "ativaTurno": 5,
    "Poder": 1,
    "Vitoria": 3,
    "Derrota": 3
}

James = {
    "nome": "James",
    "tempo": 160,
    "ativaTurno": 5,
    "Poder": 1,
    "Vitoria": 10,
    "Derrota": 3
}

Giovanni = {
    "nome": "Giovanni",
    "tempo": 180,
    "ativaTurno": 7,
    "Poder": 2,
    "Vitoria": 60,
    "Derrota": 3,
}

Red = {
    "nome": "Red",
    "tempo": 140,
    "ativaTurno": 7,
    "Poder": 3,
    "Vitoria": 5,
    "Derrota": 1
}

Professor_Carvalho = {
    "nome": "Professor Carvalho",
    "tempo": 190,
    "ativaTurno": 7,
    "Poder": 2,
    "Vitoria": 1,
    "Derrota": 4,
}

Treinadores_Todos = [Ash,Misty,Brock,Jessie,James,Giovanni,Red,Professor_Carvalho]