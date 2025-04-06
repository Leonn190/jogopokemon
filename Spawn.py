import Basicos
import random

charmander = {
    "nome": "charmander",
    "raridade": 3,
    "dificuldade": 3,
    "gerador": Basicos.gerador_charmander
}
bulbasaur = {
    "nome": "bulbasaur",
    "raridade": 3,
    "dificuldade": 3,
    "gerador": Basicos.gerador_bulbasaur
}
squirtle = {
    "nome": "squirtle",
    "raridade": 3,
    "dificuldade": 3,
    "gerador": Basicos.gerador_squirtle
}

pokemons_possiveis = [charmander,bulbasaur,squirtle]

def spawn_do_centro(centro):
    raridades = []
    for i in range(len(pokemons_possiveis)):
        for j in range(10 - pokemons_possiveis[i]["raridade"]):
            raridades.append(pokemons_possiveis[i])
    pokemon_apareceu = random.choice(raridades)
    centro.append(pokemon_apareceu)
    print (f"Um {pokemon_apareceu['nome']} selvagem apareceu no centro!")
    return centro
            
