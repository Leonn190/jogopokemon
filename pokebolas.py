import random

Pokebola = {

}

Gratball = {

}

Ultraball = {

}

Masterball = {

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