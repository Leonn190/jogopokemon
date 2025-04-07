import random

Pokebola = {
    "nome": "pokebola",
    "classe": "pokebola",
    "Descrição": "serve para capturar pokemons",
    "raridade": 1,
    "poder": 2
}

Gratball = {
    "nome": "greatball",
    "classe": "pokebola",
    "Descrição": "serve para capturar pokemons",
    "raridade": 2,
    "poder": 4
}

Ultraball = {
    "nome": "ultraball",
    "classe": "pokebola",
    "Descrição": "serve para capturar pokemons",
    "raridade": 3,
    "poder": 6
}

Masterball = {
    "nome": "masterball",
    "classe": "pokebola",
    "Descrição": "serve para capturar pokemons",
    "raridade": 5,
    "poder": 9
}

Poçao = {
    "nome": "poção",
    "classe": "consumivel",
    "Descrição": "Cura 30 de HP dos pokemon",
    "raridade": 1,
    "Cura": 30
} 

Super_Poçao = {
    "nome": "super poção",
    "classe": "consumivel",
    "Descrição": "Cura 60 de HP dos pokemon",
    "raridade": 2,
    "Cura": 60
} 

Hiper_Poçao = {
    "nome": "hiper poção",
    "classe": "consumivel",
    "Descrição": "Cura 100 de HP dos pokemon",
    "raridade": 3,
    "Cura": 100
} 

Mega_poção = {
    "nome": "mega poção",
    "classe": "consumivel",
    "Descrição": "Cura 150 de HP dos pokemon",
    "raridade": 4,
    "Cura": 150
} 

Caixa = {
    "nome": "caixa",
    "classe": "consumivel",
    "Descrição": "serve para fazer 3 compras",
    "raridade": 2,
    "Compra": 3
}

Pilha_de_caixas = {
    "nome": "pilha de caixas",
    "classe": "consumivel",
    "Descrição": "serve para fazer 5 compras",
    "raridade": 4,
    "Compra": 5
}

Citrino = {
    "nome": "citrino",
    "classe": "consumivel",
    "Descrição": "aumenta a defesa dos pokemons",
    "raridade": 3,
    "aumento": "def"
}

Safira = {
    "nome": "safira",
    "classe": "consumivel",
    "Descrição": "aumenta a defesa especial dos pokemons",
    "raridade": 3,
    "aumento": "def SP"
}

Rubi = {
    "nome": "rubi",
    "classe": "consumivel",
    "Descrição": "aumenta a ataque dos pokemons",
    "raridade": 3,
    "aumento": "atk"
}

Ametista = {
    "nome": "ametista",
    "classe": "consumivel",
    "Descrição": "aumenta a ataque especial dos pokemons",
    "raridade": 3,
    "aumento": "atk SP"
}

Esmeralda = {
    "nome": "esmeralda",
    "classe": "consumivel",
    "Descrição": "aumenta 1 de XP dos pokemon",
    "raridade": 4,
    "aumento": "XP atu"
}

itens_disponiveis = [Poçao,Super_Poçao,Hiper_Poçao,Mega_poção,Caixa,Pilha_de_caixas]
pokebolas_disponiveis = [Pokebola,Gratball,Ultraball,Masterball]
amplificadores_disponiveis = [Citrino,Safira,Rubi,Ametista,Esmeralda]

def ganhar_item(player,tipo):

    raridades = []

    if tipo == "item":
        U = itens_disponiveis
    elif tipo == "pokebola":
        U = pokebolas_disponiveis
    elif tipo == "amplificador":
        U = amplificadores_disponiveis

    for i in range(len(U)):
        for j in range(6 - U[i]["raridade"]):
            raridades.append(U[i])
    item = random.choice(raridades)
    return item
        