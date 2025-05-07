import random
from Dados.Gen1.V import Snorlax_V,Meowth_V,Pikachu_V
from Dados.Gen1.Mega import Mega_Aerodactyl,Mega_Pinsir,Mega_Mewtwo_X,Mega_Mewtwo_Y
from Dados.Gen1.Evo1 import Ivysaur,Charmeleon,Wartortle,Machoke,Haunter,Graveler,Metapod,Kadabra,Dragonair,Raichu,Zoroark,Gyarados,Wigglytuff,Magneton,Raticate,Kakuna,Clefable,Persian,Marowak,Cloyster

Bulbasaur = {
    "nome": "Bulbasaur",
    "raridade": 4,
    "dificuldade": 3,
    "code": 1,
    "tipo": ["planta", "venenoso"],
    "evolução": Ivysaur,
    "FF": None,
    "vida": 80,
    "atk": 17,
    "atk SP": 24,
    "def": 15,
    "def SP": 22,
    "velocidade": 23,
    "XP": 25,
    "custo": 1,
    "MoveList": ["Cabeçada", "Ácido", "Disparo de Semente", "Dreno", "Energia", "Crescer"],
    "Moves": 2,
    "H": 0.58,
    "W": 7.5
}

Charmander = {
    "nome": "Charmander",
    "raridade": 4,
    "dificuldade": 3,
    "code": 2,
    "tipo": ["fogo"],
    "evolução": Charmeleon,
    "FF": None,
    "vida": 75,
    "atk": 21,
    "atk SP": 23,
    "def": 17,
    "def SP": 18,
    "velocidade": 24,
    "XP": 25,
    "custo": 1,
    "MoveList": ["Tapa", "Queimar", "Superaquecer", "Mordida", "Crescer", "Brasa"],
    "Moves": 2,
    "H": 0.7,   
    "W": 8.5
}

Squirtle = {
    "nome": "Squirtle",
    "raridade": 4,
    "dificuldade": 3,
    "code": 3,
    "tipo": ["agua"],
    "evolução": Wartortle,
    "FF": None,
    "vida": 77,
    "atk": 19,
    "atk SP": 17,
    "def": 23,
    "def SP": 22,
    "velocidade": 20,
    "XP": 25,
    "custo": 1,
    "MoveList": ["Investida", "Jato de Água", "Bolhas", "Vasculhar no Rio", "Provocar", "Crescer"],
    "Moves": 2,
    "H": 0.67,
    "W": 10
}

Machop = {
    "nome": "Machop",
    "raridade": 3,
    "dificuldade": 3,
    "code": 4,
    "tipo": ["lutador"],
    "evolução": Machoke,
    "FF": None,
    "vida": 94,
    "atk": 24,
    "atk SP": 15,
    "def": 23,
    "def SP": 20,
    "velocidade": 20,
    "XP": 25,
    "custo": 2,
    "MoveList": ["Treinar", "Soco", "Provocar", "Pedregulho", "Crescer", "Tapa Especial"],
    "Moves": 2,
    "H": 0.9,
    "W": 20
}

Gastly = {
    "nome": "Gastly",
    "raridade": 3,
    "dificuldade": 3,
    "code": 5,
    "tipo": ["fantasma", "venenoso"],
    "evolução": Haunter,
    "FF": None,
    "vida": 62,
    "atk": 16,
    "atk SP": 27,
    "def": 15,
    "def SP": 18,
    "velocidade": 25,
    "XP": 20,
    "custo": 0,
    "MoveList": ["Lambida", "Ácido", "Envenenar", "Assombrar", "Energia", "Atravessar"],
    "Moves": 2,
    "H": 0.6,
    "W": 0.2
}

Geodude = {
    "nome": "Geodude",
    "raridade": 2,
    "dificuldade": 3,
    "code": 6,
    "tipo": ["pedra", "terrestre"],
    "evolução": Graveler,
    "FF": None,
    "vida": 85,
    "atk": 22,
    "atk SP": 17,
    "def": 26,
    "def SP": 22,
    "velocidade": 17,
    "XP": 30,
    "custo": 2,
    "MoveList": ["Soco", "Pedregulho", "Provocar", "Investida", "Esbravejar", "Tremor"],
    "Moves": 2,
    "H": 0.51,
    "W": 23
}

Caterpie = {
    "nome": "Caterpie",
    "raridade": 1,
    "dificuldade": 1,
    "code": 7,
    "tipo": ["inseto"],
    "evolução": Metapod,
    "FF": None,
    "vida": 68,
    "atk": 18,
    "atk SP": 19,
    "def": 17,
    "def SP": 18,
    "velocidade": 18,
    "XP": 15,
    "custo": 1,
    "MoveList": ["Seda", "Cabeçada", "Mordida", "Minhocagem", "Coleta", "Energia"],
    "Moves": 2,
    "H": 0.31,
    "W": 3.3
}

Abra = {
    "nome": "Abra",
    "raridade": 4,
    "dificuldade": 4,
    "code": 8,
    "tipo": ["psiquico"],
    "evolução": Kadabra,
    "FF": None,
    "vida": 57,
    "atk": 14,
    "atk SP": 29,
    "def": 13,
    "def SP": 19,
    "velocidade": 24,
    "XP": 25,
    "custo": 0,
    "MoveList": ["Teleporte", "Ampliação Mental", "Confusão", "Psíquico Desgastante", "Tapa Especial", "Tapa"],
    "Moves": 2,
    "H": 1,
    "W": 20
}

Dratini = {
    "nome": "Dratini",
    "raridade": 5,
    "dificuldade": 3,
    "code": 9,
    "tipo": ["dragao"],
    "evolução": Dragonair,
    "FF": None,
    "vida": 82,
    "atk": 22,
    "atk SP": 18,
    "def": 21,
    "def SP": 21,
    "velocidade": 21,
    "XP": 30,
    "custo": 1,
    "MoveList": ["Ultraje", "Sopro do Dragão", "Cabeçada", "Mordida", "Crescer", "Bolhas"],
    "Moves": 2,
    "H": 1.81,
    "W": 3.4
}

Pikachu = {
    "nome": "Pikachu",
    "raridade": 3,
    "dificuldade": 2,
    "code": 10,
    "tipo": ["eletrico"],
    "evolução": [Raichu, Pikachu_V],
    "FF": None,
    "vida": 92,
    "atk": 20,
    "atk SP": 28,
    "def": 22,
    "def SP": 20,
    "velocidade": 34,
    "XP": 40,
    "custo": 1,
    "MoveList": ["Cauda de Ferro", "Ataque Rápido", "Choque do Trovão", "Faisca", "Bola Elétrica", "Energizar"],
    "Moves": 3,
    "H": 0.51,
    "W": 6.3
}

Zorua = {
    "nome": "Zorua",
    "raridade": 5,
    "dificuldade": 4,
    "code": 11,
    "tipo": ["sombrio"],
    "evolução": Zoroark,
    "FF": None,
    "vida": 86,
    "atk": 23,
    "atk SP": 27,
    "def": 19,
    "def SP": 19,
    "velocidade": 30,
    "XP": 40,
    "custo": 1,
    "MoveList": ["Investida", "Nas Sombras", "Bola Sombria", "Vasculhar", "Energia", "Crescer"],
    "Moves": 2,
    "H": 0.68,
    "W": 10.2
}

Magikarp = {
    "nome": "Magikarp",
    "raridade": 2,
    "dificuldade": 2,
    "code": 12,
    "tipo": ["agua"],
    "evolução": Gyarados,
    "FF": None,
    "vida": 66,
    "atk": 11,
    "atk SP": 13,
    "def": 25,
    "def SP": 15,
    "velocidade": 26,
    "XP": 50,
    "custo": 1,
    "MoveList": ["Splash", "Vasculhar", "Vasculhar no Rio", "Splash", "Splash", "Splash"],
    "Moves": 2,
    "H": 0.85,
    "W": 9.1
}

Jigglypuff = {
    "nome": "Jigglypuff",
    "raridade": 3,
    "dificuldade": 1,
    "code": 13,
    "tipo": ["fada", "normal"],
    "evolução": Wigglytuff,
    "FF": None,
    "vida": 140,
    "atk": 23,
    "atk SP": 16,
    "def": 20,
    "def SP": 21,
    "velocidade": 20,
    "XP": 35,
    "custo": 1,
    "MoveList": ["Tapa", "Cura Natural", "Brilho", "Energia", "Busca Alegre", "Tapa Especial"],
    "Moves": 2,
    "H": 0.56,
    "W": 6.7
}

Clefairy = {
    "nome": "Clefairy",
    "raridade": 3,
    "dificuldade": 1,
    "code": 14,
    "tipo": ["fada"],
    "evolução": Clefable,
    "FF": None,
    "vida": 107,
    "atk": 17,
    "atk SP": 22,
    "def": 20,
    "def SP": 26,
    "velocidade": 14,
    "XP": 35,
    "custo": 2,
    "MoveList": ["Provocar", "Vento Fada", "Brilho", "Benção", "Investida", "Energia"],
    "Moves": 2,
    "H": 0.62,
    "W": 8.9

}

Meowth = {
    "nome": "Meowth",
    "raridade": 2,
    "dificuldade": 2,
    "code": 15,
    "tipo": ["normal"],
    "evolução": [Persian, Meowth_V],
    "FF": None,
    "vida": 81,
    "atk": 22,
    "atk SP": 19,
    "def": 18,
    "def SP": 18,
    "velocidade": 29,
    "XP": 35,
    "custo": 1,
    "MoveList": ["Tapa", "Tapa Especial", "Vasculhar", "Arranhar", "Crescer", "Busca Gananciosa"],
    "Moves": 2,
    "H": 0.63,
    "W": 5.1
}

Cubone = {
    "nome": "Cubone",
    "raridade": 2,
    "dificuldade": 4,
    "code": 16,
    "tipo": ["terrestre"],
    "evolução": Marowak,
    "FF": None,
    "vida": 77,
    "atk": 19,
    "atk SP": 18,
    "def": 27,
    "def SP": 21,
    "velocidade": 19,
    "XP": 30,
    "custo": 1,
    "MoveList": ["Provocar", "Pedregulho", "Soco", "Arremesso de Terra", "Tremor", "Crescer"],
    "Moves": 2,
    "H": 0.42,
    "W": 7.1

}

Shellder = {
    "nome": "Shellder",
    "raridade": 3,
    "dificuldade": 2,
    "code": 17,
    "tipo": ["agua"],
    "evolução": Cloyster,
    "FF": None,
    "vida": 65,
    "atk": 25,
    "atk SP": 18,
    "def": 29,
    "def SP": 19,
    "velocidade": 21,
    "XP": 40,
    "custo": 1,
    "MoveList": ["Lambida", "Provocar", "Jato de Água", "Bolhas", "Energia", "Golpe de Concha"],
    "Moves": 2,
    "H": 0.33,
    "W": 4

}

Magnemite = {
    "nome": "Magnemite",
    "raridade": 2,
    "dificuldade": 2,
    "code": 18,
    "tipo": ["eletrico", "metal"],
    "evolução": Magneton,
    "FF": None,
    "vida": 51,
    "atk": 19,
    "atk SP": 26,
    "def": 25,
    "def SP": 23,
    "velocidade": 20,
    "XP": 35,
    "custo": 1,
    "MoveList": ["Reforçar", "Faisca", "Energia", "Energizar", "Projétil Metalico", "Onda Elétrica"],
    "Moves": 2,
    "H": 0.29,
    "W": 6.7

}

Rattata = {
    "nome": "Rattata",
    "raridade": 1,
    "dificuldade": 1,
    "code": 19,
    "tipo": ["normal"],
    "evolução": Raticate,
    "FF": None,
    "vida": 67,
    "atk": 22,
    "atk SP": 13,
    "def": 19,
    "def SP": 15,
    "velocidade": 28,
    "XP": 30,
    "custo": 0,
    "MoveList": ["Mordida", "Investida", "Nas Sombras", "Vasculhar", "Crescer", "Envenenar"],
    "Moves": 2,
    "H": 0.34,
    "W": 3.3
}

Weedle = {
    "nome": "Weedle",
    "raridade": 1,
    "dificuldade": 1,
    "code": 20,
    "tipo": ["inseto"],
    "evolução": Kakuna,
    "FF": None,
    "vida": 58,
    "atk": 20,
    "atk SP": 19,
    "def": 18,
    "def SP": 19,
    "velocidade": 17,
    "XP": 15,
    "custo": 1,
    "MoveList": ["Minhocagem", "Seda", "Picada", "Vasculhar", "Envenenar", "Coleta"],
    "Moves": 2,
    "H": 0.26,
    "W": 2.5

}

Snorlax = {
    "nome": "Snorlax",
    "raridade": 7,
    "dificuldade": 5,
    "code": 21,
    "tipo": ["normal"],
    "evolução": Snorlax_V,
    "FF": None,
    "vida": 243,
    "atk": 39,
    "atk SP": 30,
    "def": 31,
    "def SP": 33,
    "velocidade": 14,
    "XP": 45,
    "custo": 4,
    "MoveList": ["Arranhar", "Tapa", "Tapa Especial", "Provocar", "Esmagar", "Descansar"],
    "Moves": 4,
    "H": 2.15,
    "W": 485

}

Aerodactyl = {
    "nome": "Aerodactyl",
    "raridade": 7,
    "dificuldade": 6,
    "code": 22,
    "tipo": ["pedra", "voador"],
    "evolução": None,
    "FF": [Mega_Aerodactyl],
    "vida": 151,
    "atk": 44,
    "atk SP": 32,
    "def": 30,
    "def SP": 27,
    "velocidade": 50,
    "XP": 50,
    "custo": 3,
    "MoveList": ["Voar", "Ataque de Asa", "Investida Aérea", "Pedra Especial", "Barragem Rochosa", "Mordida"],
    "Moves": 4,
    "H": 1.8,
    "W": 60

}

Jynx = {
    "nome": "Jynx",
    "raridade": 6,
    "dificuldade": 4,
    "code": 23,
    "tipo": ["psiquico", "gelo"],
    "evolução": None,
    "FF": None,
    "vida": 138,
    "atk": 21,
    "atk SP": 35,
    "def": 23,
    "def SP": 29,
    "velocidade": 24,
    "XP": 0,
    "custo": 2,
    "MoveList": ["Cristalizar", "Reinado de Gelo", "Magia de Gelo", "Bola Psíquica", "Mente Forte", "Tapa Especial"],
    "Moves": 4,
    "H": 1.34,
    "W": 38.8
}

Pinsir = {
    "nome": "Pinsir",
    "raridade": 6,
    "dificuldade": 4,
    "code": 24,
    "tipo": ["inseto"],
    "evolução": None,
    "FF": [Mega_Pinsir],
    "vida": 124,
    "atk": 50,
    "atk SP": 20,
    "def": 28,
    "def SP": 24,
    "velocidade": 25,
    "XP": 45,
    "custo": 2,
    "MoveList": ["Seda", "Mordida", "Tesoura X", "Bola Psiquica", "Mente Forte", "Tapa Especial"],
    "Moves": 4,
    "H": 1.55,
    "W": 53

}

Mewtwo = {
    "nome": "Mewtwo",
    "raridade": 10,
    "dificuldade": 9,
    "code": 25,
    "tipo": ["psiquico"],
    "evolução": None,
    "FF": random.choice([Mega_Mewtwo_X, Mega_Mewtwo_Y]),
    "vida": 196,
    "atk": 64,
    "atk SP": 76,
    "def": 50,
    "def SP": 56,
    "velocidade": 68,
    "XP": 55,
    "custo": 3,
    "MoveList": ["Teleporte", "Corrosão Psíquica", "Psicorte Duplo", "Ampliação Mental", "Mente Forte", "Confusão"],
    "Moves": 4,
    "H": 1.9,
    "W": 95
}

Articuno = {
    "nome": "Articuno",
    "raridade": 10,
    "dificuldade": 8,
    "code": 26,
    "tipo": ["voador", "gelo"],
    "evolução": None,
    "FF": None,
    "vida": 192,
    "atk": 40,
    "atk SP": 62,
    "def": 56,
    "def SP": 70,
    "velocidade": 60,
    "XP": 55,
    "custo": 4,
    "MoveList": ["Raio de Gelo", "Reinado de Gelo", "Voar", "Ataque de Asa", "Provocar", "Gelo Verdadeiro"],
    "Moves": 4,
    "H": 1.83,
    "W": 73
}

Moltres = {
    "nome": "Moltres",
    "raridade": 10,
    "dificuldade": 8,
    "code": 27,
    "tipo": ["voador", "fogo"],
    "evolução": None,
    "FF": None,
    "vida": 202,
    "atk": 48,
    "atk SP": 72,
    "def": 58,
    "def SP": 46,
    "velocidade": 53,
    "XP": 0,
    "custo": 3,
    "MoveList": ["Ondas de Calor", "Raio de Fogo", "Voar", "Investida Aérea", "Provocar", "Superaquecer"],
    "Moves": 4,
    "H": 1.98,
    "W": 81
}

Zapdos = {
    "nome": "Zapdos",
    "raridade": 10,
    "dificuldade": 8,
    "code": 28,
    "tipo": ["voador", "eletrico"],
    "evolução": None,
    "FF": None,
    "vida": 191,
    "atk": 52,
    "atk SP": 70,
    "def": 45,
    "def SP": 58,
    "velocidade": 57,
    "XP": 0,
    "custo": 3,
    "MoveList": ["Tempestade de Raios", "Choque do Trovão", "Voar", "Rasante", "Bola Elétrica", "Bico Broca"],
    "Moves": 4,
    "H": 1.72,
    "W": 69
}

Pokemons_Todos = [0,
    Bulbasaur, Charmander, Squirtle, Machop, Gastly, Geodude, Caterpie, Abra, Dratini, Pikachu,
    Zorua, Magikarp, Jigglypuff, Clefairy, Meowth, Cubone, Shellder, Magnemite, Rattata, Weedle, Snorlax, Aerodactyl, Jynx, Pinsir, Mewtwo, Articuno,Moltres,Zapdos]