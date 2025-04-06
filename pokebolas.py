import random

Pokebola = {
    "nome": "pokebola",
    "poder": 2
}

Gratball = {
    "nome": "greatball",
    "poder": 4
}

Ultraball = {
    "nome": "ultraball",
    "poder": 6
}

Masterball = {
    "nome": "masterball",
    "poder": 9
}

pokebolas = [Pokebola,Gratball,Ultraball,Masterball]

def ganhar_pokebola(ganhador,pokebola):
    if pokebola == "aleatoria":
        tipo = random.choice(pokebolas)
    else:
        tipo = pokebola
        if tipo == "pokebola":
            tipo = Pokebola
        elif tipo == "greatball":
            tipo = Gratball
        elif tipo == "ultraball":
            tipo = Ultraball
        elif tipo == "masterball":
            tipo = Masterball

    return tipo
