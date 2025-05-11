# === Início de Basicos.py ===
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
    "MoveList": ["Tapa", "Tapa Especial", "Vasculhar", "Arranhar", "Crescer", "Coleta Gananciosa"],
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
    "MoveList": ["Reforçar", "Faisca", "Energia", "Energizar", "Projétil Metálico", "Onda Elétrica"],
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
    "MoveList": ["Seda", "Mordida", "Tesoura X", "Arranhar", "Esbravejar", "Treinar"],
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
    "MoveList": ["Teleporte", "Corrosão Psíquica", "Psicorte Duplo", "Ampliação Mental", "Mente Forte", "Cauda Violenta"],
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

# === Fim de Basicos.py ===

# === Início de Evo1.py ===
from Dados.Gen1.Mega import Mega_Gyarados
from Dados.Gen1.Evo2 import Venusaur,Charizard,Blastoise,Machamp,Gengar,Golem,Butterfree,Alakazam,Dragonite,Beedrill

Ivysaur = {
    "nome": "Ivysaur",
    "tipo": ["planta", "venenoso"],
    "evolução": Venusaur,
    "FF": None,
    "estagio": 2,
    "vida": 1.7375,
    "atk": 1.352941176,
    "atk SP": 1.416666667,
    "def": 1.666666667,
    "def SP": 1.5,
    "velocidade": 1.217391304,
    "XP": 55,
    "custo": 2,
    "movelist": ["Dreno", "Ácido", "Dança das Pételas", "Chicote de Vinha", "Cura Natural", "Bomba de Lodo"],
    "moves": 3,
    "H": 0.86,
    "W": 13
}

Charmeleon = {
    "nome": "Charmeleon",
    "tipo": ["fogo"],
    "evolução": Charizard,
    "FF": None,
    "estagio": 2,
    "vida": 1.8,
    "atk": 1.380952381,
    "atk SP": 1.434782609,
    "def": 1.411764706,
    "def SP": 1.5,
    "velocidade": 1.375,
    "XP": 55,
    "custo": 2,
    "movelist": ["Brasa", "Mordida", "Queimar", "Arranhar", "Bola de Fogo", "Ataque em Chamas"],
    "moves": 3,
    "H": 0.98,
    "W": 17
}

Wartortle = {
    "nome": "Wartortle",
    "tipo": ["agua"],
    "evolução": Blastoise,
    "FF": None,
    "estagio": 2,
    "vida": 1.792207792,
    "atk": 1.368421053,
    "atk SP": 1.470588235,
    "def": 1.52173913,
    "def SP": 1.454545455,
    "velocidade": 1.2,
    "XP": 55,
    "custo": 2,
    "movelist": ["Jato de Água", "Provocar", "Investida", "Golpe de Concha", "Soco", "Gota Pesada"],
    "moves": 3,
    "H": 0.83,
    "W": 21
}

Machoke = {
    "nome": "Machoke",
    "tipo": ["lutador"],
    "evolução": Machamp,
    "FF": None,
    "estagio": 2,
    "vida": 1.595744681,
    "atk": 1.5,
    "atk SP": 1.6,
    "def": 1.391304348,
    "def SP": 1.2,
    "velocidade": 1.3,
    "XP": 55,
    "custo": 2,
    "movelist": ["Soco", "Pedregulho", "Treinar", "Submissão", "Chamar para Briga", "Barragem"],
    "moves": 3,
    "H": 1.38,
    "W": 61

}

Haunter = {
    "nome": "Haunter",
    "tipo": ["fantasma", "venenoso"],
    "evolução": Gengar,
    "FF": None,
    "estagio": 2,
    "vida": 2.14516129,
    "atk": 1.5625,
    "atk SP": 1.444444444,
    "def": 1.333333333,
    "def SP": 1.5,
    "velocidade": 1.48,
    "XP": 55,
    "custo": 1,
    "movelist": ["Lambida", "Assombrar", "Acido", "Coleta Gananciosa", "Bomba de Lodo", "Mão Espectral"],
    "moves": 3,
    "H": 1.3,
    "W": 0.3
}

Graveler = {
    "nome": "Graveler",
    "tipo": ["pedra", "terrestre"],
    "evolução": Golem,
    "FF": None,
    "estagio": 2,
    "vida": 1.717647059,
    "atk": 1.363636364,
    "atk SP": 1.176470588,
    "def": 1.461538462,
    "def SP": 1.363636364,
    "velocidade": 1.176470588,
    "XP": 60,
    "custo": 3,
    "movelist": ["Tremor", "Provocar", "Soco", "Barragem Rochosa", "Quebra Chão", "Impacto Rochoso"],
    "moves": 3,
    "H": 1.12,
    "W": 102

}

Metapod = {
    "nome": "Metapod",
    "tipo": ["inseto"],
    "evolução": Butterfree,
    "FF": None,
    "estagio": 2,
    "vida": 1.661764706,
    "atk": 1.111111111,
    "atk SP": 1.210526316,
    "def": 1.882352941,
    "def SP": 1.333333333,
    "velocidade": 0.5555555556,
    "XP": 45,
    "custo": 2,
    "movelist": ["Crescer", "Seda", "Barragem"],
    "moves": 3,
    "H": 0.45,
    "W": 4.1

}

Kadabra = {
    "nome": "Kadabra",
    "tipo": ["psiquico"],
    "evolução": Alakazam,
    "FF": None,
    "estagio": 2,
    "vida": 2.245614035,
    "atk": 1.428571429,
    "atk SP": 1.448275862,
    "def": 1.384615385,
    "def SP": 1.473684211,
    "velocidade": 1.416666667,
    "XP": 55,
    "custo": 2,
    "movelist": ["Teleporte", "Ampliação Mental", "Psíquico Desgastante", "Mente Forte", "Bola Psíquica", "Transferência Psíquica"],
    "moves": 3,
    "H": 1.29,
    "W": 52

}

Dragonair = {
    "nome": "Dragonair",
    "tipo": ["dragao"],
    "evolução": Dragonite,
    "FF": None,
    "estagio": 2,
    "vida": 1.768292683,
    "atk": 1.454545455,
    "atk SP": 1.444444444,
    "def": 1.333333333,
    "def SP": 1.380952381,
    "velocidade": 1.428571429,
    "XP": 65,
    "custo": 2,
    "movelist": ["Ultraje", "Sopro do Dragão", "Esbravejar", "Pedra Especial", "Cauda de Ferro", "Bolhas"],
    "moves": 3,
    "H": 4.2,
    "W": 17.5
}

Raichu = {
    "nome": "Raichu",
    "tipo": ["eletrico"],
    "evolução": None,
    "FF": None,
    "estagio": 2,
    "vida": 1.608695652,
    "atk": 1.45,
    "atk SP": 1.321428571,
    "def": 1.136363636,
    "def SP": 1.35,
    "velocidade": 1.294117647,
    "XP": 0,
    "custo": 1,
    "movelist": ["Ultraje", "Eletrólise Hidrica", "Choque do Trovão", "Faisca", "Bola Elétrica", "Onda Elétrica"],
    "moves": 4,
    "H": 0.72,
    "W": 13.6

}

Zoroark = {
    "nome": "Zoroark",
    "tipo": ["sombrio"],
    "evolução": None,
    "FF": None,
    "estagio": 2,
    "vida": 1.802325581,
    "atk": 1.652173913,
    "atk SP": 1.555555556,
    "def": 1.315789474,
    "def SP": 1.263157895,
    "velocidade": 1.633333333,
    "XP": 0,
    "custo": 2,
    "movelist": ["Arranhar", "Nas Sombras", "Bola Sombria", "Corte Noturno", "Garra do Dragão", "Ataque Rápido"],
    "moves": 4,
    "H": 1.48,
    "W": 46

}

Gyarados = {
    "nome": "Gyarados",
    "tipo": ["agua", "voador"],
    "evolução": Mega_Gyarados,
    "FF": [Mega_Gyarados],
    "estagio": 2,
    "vida": 2.575757576,
    "atk": 5.545454545,
    "atk SP": 2.538461538,
    "def": 1.56,
    "def SP": 3,
    "velocidade": 1.653846154,
    "XP": 90,
    "custo": 3,
    "movelist": ["Rasante", "Cauda Violenta", "Cachoeira", "Jato de Água", "Bola de Água", "Esmagar"],
    "moves": 4,
    "H": 7.1,
    "W": 250

}

Wigglytuff = {
    "nome": "Wigglytuff",
    "tipo": ["fada", "normal"],
    "evolução": None,
    "FF": None,
    "estagio": 2,
    "vida": 1.378571429,
    "atk": 1.347826087,
    "atk SP": 1.5,
    "def": 1.3,
    "def SP": 1.333333333,
    "velocidade": 1.5,
    "XP": 0,
    "custo": 1,
    "movelist": ["Tapa", "Canto Alegre", "Brilho", "Tapa das Fadas", "Busca Alegre", "Vento Fada"],
    "moves": 4,
    "H": 1.01,
    "W": 13.5

}

Clefable = {
    "nome": "Clefable",
    "tipo": ["fada"],
    "evolução": None,
    "FF": None,
    "estagio": 2,
    "vida": 1.457943925,
    "atk": 1.529411765,
    "atk SP": 1.681818182,
    "def": 1.6,
    "def SP": 1.884615385,
    "velocidade": 1.5,
    "XP": 0,
    "custo": 3,
    "movelist": ["Constelação Mágica", "Vento Fada", "Brilho", "Benção", "Cura Natural", "Explosão Fada"],
    "moves": 4,
    "H": 1.2,
    "W": 48

}

Persian = {
    "nome": "Persian",
    "tipo": ["normal"],
    "evolução": None,
    "FF": None,
    "estagio": 2,
    "vida": 1.75308642,
    "atk": 1.545454545,
    "atk SP": 1.421052632,
    "def": 1.5,
    "def SP": 1.444444444,
    "velocidade": 1.482758621,
    "XP": 0,
    "custo": 1,
    "movelist": ["Arranhar", "Esbravejar", "Afinidade Territorial", "Corte Noturno", "Investida", "Ataque Rápido"],
    "moves": 4,
    "H": 0.89,
    "W": 35

}

Marowak = {
    "nome": "Marowak",
    "tipo": ["terrestre"],
    "evolução": None,
    "FF": None,
    "estagio": 2,
    "vida": 1.74025974,
    "atk": 1.684210526,
    "atk SP": 1.277777778,
    "def": 1.555555556,
    "def SP": 1.476190476,
    "velocidade": 1.368421053,
    "XP": 0,
    "custo": 1,
    "movelist": ["Tremor", "Esbravejar", "Osso Veloz", "Golpe Territorial", "Pedregulho", "Provocar"],
    "moves": 4,
    "H": 0.99,
    "W": 41

}

Cloyster = {
    "nome": "Cloyster",
    "tipo": ["agua", "gelo"],
    "evolução": None,
    "FF": None,
    "estagio": 2,
    "vida": 1.969230769,
    "atk": 1.48,
    "atk SP": 1.388888889,
    "def": 2.24137931,
    "def SP": 1.526315789,
    "velocidade": 1.523809524,
    "XP": 0,
    "custo": 2,
    "movelist": ["Confronto Trevoso", "Controle do Oceano", "Raio de Gelo", "Gelo Verdadeiro", "Golpe de Concha", "Lambida"],
    "moves": 4,
    "H": 1.45,
    "W": 138

}

Magneton = {
    "nome": "Magneton",
    "tipo": ["eletrico", "metal"],
    "evolução": None,
    "FF": None,
    "estagio": 2,
    "vida": 2.333333333,
    "atk": 1.421052632,
    "atk SP": 1.730769231,
    "def": 1.52,
    "def SP": 1.434782609,
    "velocidade": 1.55,
    "XP": 0,
    "custo": 1,
    "MoveList": ["Reforçar", "Eletrólise Hidrica", "Barragem", "Energizar", "Projétil Metalico", "Onda Elétrica"],
    "Moves": 2,
    "H": 0.96,
    "W": 55.5

}

Raticate = {
    "nome": "Raticate",
    "tipo": ["normal"],
    "evolução": None,
    "FF": None,
    "estagio": 2,
    "vida": 2.328358209,
    "atk": 1.454545455,
    "atk SP": 2.0,
    "def": 1.473684211,
    "def SP": 2.266666667,
    "velocidade": 1.321428571,
    "XP": 0,
    "custo": 3,
    "MoveList": ["Mordida", "Investida", "Nas Sombras", "Vasculhar", "Arranhar", "Envenenar"],
    "Moves": 2,
    "H": 0.85,
    "W": 26.2

}

Kakuna = {
    "nome": "Kakuna",
    "tipo": ["inseto", "venenoso"],
    "evolução": Beedrill,
    "FF": None,
    "estagio": 2,
    "vida": 1.568965517,
    "atk": 1.3,
    "atk SP": 1.157894737,
    "def": 1.555555556,
    "def SP": 1.315789474,
    "velocidade": 0.7647058824,
    "XP": 45,
    "custo": 2,
    "movelist": ["Crescer", "Seda", "Barragem"],
    "moves": 3,
    "H": 0.48,
    "W": 5.1

}




# === Fim de Evo1.py ===

# === Início de Evo2.py ===
import random
from Dados.Gen1.Mega import Mega_Alakazam,Mega_Charizard_X,Mega_Charizard_Y,Mega_Gengar,Mega_Beedrill,Mega_Blastoise,Mega_Venusaur
from Dados.Gen1.V import Venusaur_V,Blastoise_V,Charizard_V,Gengar_V,Machamp_V,Butterfree_V

Venusaur = {
    "nome": "Venusaur",
    "tipo": ["planta", "veneneno"],
    "evolução": Venusaur_V,
    "FF": [Mega_Venusaur],
    "estagio": 3,
    "vida": 1.302158273,
    "atk": 1.565217391,
    "atk SP": 1.558823529,
    "def": 1.4,
    "def SP": 1.545454545,
    "velocidade": 1.321428571,
    "XP": 90,
    "custo": 3,
    "movelist": ["Mega Dreno", "Ácido", "Raio Solar", "Folha Navalha", "Cura Natural", "Bomba de Lodo"],
    "moves": 4,
    "H": 1.77,
    "W": 110
}

Charizard = {
    "nome": "Charizard",
    "tipo": ["fogo", "voador"],
    "evolução": Charizard_V,
    "FF": random.choice([Mega_Charizard_X, Mega_Charizard_Y]),
    "estagio": 3,
    "vida": 1.288888889,
    "atk": 1.620689655,
    "atk SP": 1.575757576,
    "def": 1.375,
    "def SP": 1.333333333,
    "velocidade": 1.545454545,
    "XP": 90,
    "custo": 3,
    "movelist": ["Ataque de Asa", "Mordida", "Raio de Fogo", "Cauda Violenta", "Bola de Fogo", "Ataque de Chamas"],
    "moves": 4,
    "H": 1.83,
    "W": 92

}

Blastoise = {
    "nome": "Blastoise",
    "tipo": ["agua"],
    "evolução": Blastoise_V,
    "FF": [Mega_Blastoise],
    "estagio": 3,
    "vida": 1.275362319,
    "atk": 1.5,
    "atk SP": 1.56,
    "def": 1.514285714,
    "def SP": 1.53125,
    "velocidade": 1.333333333,
    "XP": 90,
    "custo": 3,
    "movelist": ["Jato Duplo", "Provocar", "Bola de Água", "Golpe de Concha", "Golpe Territorial", "Gota Pesada"],
    "moves": 4,
    "H": 1.69,
    "W": 106

}

Machamp = {
    "nome": "Machamp",
    "tipo": ["lutador"],
    "evolução": Machamp_V,
    "FF": None,
    "estagio": 3,
    "vida": 1.286666667,
    "atk": 1.472222222,
    "atk SP": 1.458333333,
    "def": 1.59375,
    "def SP": 1.5,
    "velocidade": 1.384615385,
    "XP": 90,
    "custo": 3,
    "movelist": ["Soco", "Combate Próximo", "Treinar", "Submissão", "Chamar para Briga", "Punho Missil"],
    "moves": 4,
    "H": 1.75,
    "W": 115

}

Gengar = {
    "nome": "Gengar",
    "tipo": ["fantasma", "venenoso"],
    "evolução": Gengar_V,
    "FF": [Mega_Gengar],
    "estagio": 3,
    "vida": 1.210526316,
    "atk": 1.36,
    "atk SP": 1.564102564,
    "def": 1.6,
    "def SP": 1.481481481,
    "velocidade": 1.324324324,
    "XP": 90,
    "custo": 2,
    "movelist": ["Maldade", "Bola Sombria", "Massacre Fantasmagórico", "Coleta Gananciosa", "Nas Sombras", "Extração"],
    "moves": 4,
    "H": 1.52,
    "W": 48

}

Golem = {
    "nome": "Golem",
    "tipo": ["pedra", "terrestre"],
    "evolução": None,
    "FF": None,
    "estagio": 3,
    "vida": 1.308219178,
    "atk": 1.433333333,
    "atk SP": 1.65,
    "def": 1.684210526,
    "def SP": 1.5,
    "velocidade": 1.35,
    "XP": 0,
    "custo": 5,
    "movelist": ["Terremoto", "Provocar", "Fúria Pétrea", "Barragem Rochosa", "Reforçar", "Pedra Colossal"],
    "moves": 4,
    "H": 1.58,
    "W": 390

}

Butterfree = {
    "nome": "Butterfree",
    "tipo": ["inseto", "voador"],
    "evolução": [Butterfree_V],
    "FF": None,
    "estagio": 3,
    "vida": 1.362831858,
    "atk": 1.65,
    "atk SP": 2.086956522,
    "def": 1.03125,
    "def SP": 1.666666667,
    "velocidade": 4.2,
    "XP": 80,
    "custo": 2,
    "movelist": ["Vento Forte", "Brilho", "Benção", "Cura Natural", "Seda", "Voar"],
    "moves": 4,
    "H": 1.16,
    "W": 31

}

Alakazam = {
    "nome": "Alakazam",
    "tipo": ["psiquico"],
    "evolução": None,
    "FF": [Mega_Alakazam],
    "estagio": 3,
    "vida": 1.2421875,
    "atk": 1.55,
    "atk SP": 1.642857143,
    "def": 1.722222222,
    "def SP": 1.714285714,
    "velocidade": 1.382352941,
    "XP": 95,
    "custo": 3,
    "movelist": ["Teletransporte", "Ampliação Mental", "Raio Psíquico", "Mente Forte", "Bola Psíquica", "Transferência Psíquica"],
    "moves": 4,
    "H": 1.59,
    "W": 43

}

Dragonite = {
    "nome": "Dragonite",
    "tipo": ["dragao", "voador"],
    "evolução": None,
    "FF": None,
    "estagio": 3,
    "vida": 1.413793103,
    "atk": 1.90625,
    "atk SP": 1.692307692,
    "def": 1.607142857,
    "def SP": 1.482758621,
    "velocidade": 1.1,
    "XP": 0,
    "custo": 4,
    "movelist": ["Ultraje", "Investida do Dragão", "Provocar", "Pedra Colossal", "Cauda Violenta", "Bola de Fogo"],
    "moves": 4,
    "H": 2.26,
    "W": 210
}

Beedrill = {
    "nome": "Beedrill",
    "tipo": ["inseto", "venenoso"],
    "evolução": None,
    "FF": [Mega_Beedrill],
    "estagio": 3,
    "vida": 1.604395604,
    "atk": 2.192307692,
    "atk SP": 1.363636364,
    "def": 1.071428571,
    "def SP": 1.24,
    "velocidade": 4.230769231,
    "XP": 75,
    "custo": 1,
    "movelist": ["Dor Falsa", "Envenenar", "Voar", "Rasante", "Picada", "Extraçao"],
    "moves": 4,
    "H": 1.14,
    "W": 28

}


# === Fim de Evo2.py ===

# === Início de Mega.py ===

Mega_Venusaur = {
    "nome": "Mega Venusaur",
    "tipo": ["planta", "veneneno"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.093922652,
    "atk": 1.083333333,
    "atk SP": 1.245283019,
    "def": 1.142857143,
    "def SP": 1.196078431,
    "velocidade": 1.135135135,
    "XP": 0,
    "custo": 3,
    "movelist": ["Mega Dreno", "Ácido", "Raio Solar", "Folha Navalha", "Morteiro de Pólem", "Bomba de Lodo"],
    "H": 2.02,
    "W": 115

}

Mega_Charizard_X = {
    "nome": "Mega Charizard X",
    "tipo": ["fogo", "dragao"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.120689655,
    "atk": 1.276595745,
    "atk SP": 1.038461538,
    "def": 1.303030303,
    "def SP": 1.166666667,
    "velocidade": 1.058823529,
    "XP": 0,
    "custo": 3,
    "movelist": ["Investida do Dragão", "Mordida", "Raio de Fogo", "Cauda Violenta", "Bola de Fogo", "Ataque em Chamas"],
    "H": 1.86,
    "W": 105

}

Mega_Charizard_Y = {
    "nome": "Mega Charizard Y",
    "tipo": ["fogo", "voador"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.063218391,
    "atk": 1.063829787,
    "atk SP": 1.365384615,
    "def": 1.090909091,
    "def SP": 1.111111111,
    "velocidade": 1.215686275,
    "XP": 0,
    "custo": 3,
    "movelist": ["Ataque de Asa", "Rasante", "Laser Incandescente", "Cauda Violenta", "Bola de Fogo", "Ataque em Chamas"],
    "H": 1.92,
    "W": 99
}

Mega_Blastoise = {
    "nome": "Mega Blastoise",
    "tipo": ["agua"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.090909091,
    "atk": 1.179487179,
    "atk SP": 1.282051282,
    "def": 1.113207547,
    "def SP": 1.163265306,
    "velocidade": 1.125,
    "XP": 0,
    "custo": 3,
    "movelist": ["Jato Triplo", "Provocar", "Bola de Água", "Golpe de Concha", "Golpe Territorial", "Gota Pesada"],
    "H": 1.73,
    "W": 112
}

Mega_Gengar = {
    "nome": "Mega Gengar",
    "tipo": ["fantasma", "veneneno"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.105590062,
    "atk": 1.205882353,
    "atk SP": 1.262295082,
    "def": 1.15625,
    "def SP": 1.175,
    "velocidade": 1.183673469,
    "XP": 0,
    "custo": 2,
    "movelist": ["Maldade", "Bola Sombria", "Massacre Fantasmagórico", "Coleta Gananciosa", "Nas Sombras", "Extração"],
    "H": 1.65,
    "W": 56
}

Mega_Alakazam = {
    "nome": "Mega Alakazam",
    "tipo": ["psiquico"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.012578616,
    "atk": 1.290322581,
    "atk SP": 1.173913043,
    "def": 1.096774194,
    "def SP": 1.208333333,
    "velocidade": 1.170212766,
    "XP": 0,
    "custo": 2,
    "movelist": ["Teletransporte", "Ampliação Mental", "Raio Psíquico", "Mente Forte", "Bola Psíquica", "Transferência Psíquica"],
    "H": 1.60,
    "W": 45
}

Mega_Gyarados = {
    "nome": "Mega Gyarados",
    "tipo": ["agua", "voador"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.141176471,
    "atk": 1.180327869,
    "atk SP": 1.212121212,
    "def": 1.076923077,
    "def SP": 1.066666667,
    "velocidade": 1.162790698,
    "XP": 0,
    "custo": 3,
    "movelist": ["Rasante", "Cauda Violenta", "Cachoeira", "Jato Duplo", "Cauda de Ferro", "Esmagar"],
    "H": 7.5,
    "W": 290

}

Mega_Mewtwo_X = {
    "nome": "Mega Mewtwo X",
    "tipo": ["psiquico"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.102040816,
    "atk": 1.28125,
    "atk SP": 1.0,
    "def": 1.18,
    "def SP": 1.053571429,
    "velocidade": 1.0,
    "XP": 0,
    "custo": 3,
    "movelist": ["Teleporte", "Corrosão Psíquica", "Psicorte Duplo", "Chamar para Briga", "Mente Forte", "Combate Próximo"],
    "H": 2,
    "W": 110

}

Mega_Mewtwo_Y = {
    "nome": "Mega Mewtwo Y",
    "tipo": ["psiquico"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.025510204,
    "atk": 1.046875,
    "atk SP": 1.197368421,
    "def": 1.06,
    "def SP": 1.071428571,
    "velocidade": 1.147058824,
    "XP": 0,
    "custo": 2,
    "movelist": ["Teleporte", "Raio Psíquico", "Agonia Mental", "Ampliação Mental", "Mente Forte", "Teletransporte"],
    "H": 1.7,
    "W": 78

}

Mega_Aerodactyl = {
    "nome": "Mega Aerodactyl",
    "tipo": ["pedra", "voador"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.185430464,
    "atk": 1.25,
    "atk SP": 1.28125,
    "def": 1.266666667,
    "def SP": 1.222222222,
    "velocidade": 1.5,
    "XP": 0,
    "custo": 3,
    "MoveList": ["Voar", "Ataque de Asa", "Investida Aérea", "Pedra Especial", "Barragem Rochosa", "Pedra Colossal"],
    "H": 2.09,
    "W": 85

}

Mega_Pinsir = {
    "nome": "Mega Pinsir",
    "tipo": ["Inseto", "voador"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.314516129,
    "atk": 1.4,
    "atk SP": 1.7,
    "def": 1.464285714,
    "def SP": 1.25,
    "velocidade": 1.44,
    "XP": 0,
    "custo": 2,
    "MoveList": ["Seda", "Mordida", "Tesoura X", "Arranhar", "Esbravejar", "Voar"],
    "H": 1.75,
    "W": 64

}

Mega_Beedrill = {
    "nome": "Mega Beedrill",
    "tipo": ["inseto", "voador"],
    "evolução": None,
    "FF": "Mega",
    "estagio": 4,
    "vida": 1.068493151,
    "atk": 1.087719298,
    "atk SP": 1.233333333,
    "def": 1.1,
    "def SP": 1.161290323,
    "velocidade": 1.545454545,
    "XP": 0,
    "custo": 1,
    "movelist": ["Dor Falsa", "Envenenar", "Voar", "Rasante", "Broca Perfuradora", "Extraçao"],
    "H": 1.29,
    "W": 35

}


# === Fim de Mega.py ===

# === Início de V.py ===
from Dados.Gen1.Vmax import Venusaur_Vmax,Charizard_Vmax,Blastoise_Vmax,Machamp_Vmax,Gengar_Vmax,Butterfree_Vmax,Snorlax_Vmax,Meowth_Vmax,Pikachu_Vmax
from Dados.Gen1.Vstar import Venusaur_Vstar,Charizard_Vstar,Blastoise_Vstar,Machamp_Vstar,Gengar_Vstar,Butterfree_Vstar,Snorlax_Vstar,Meowth_Vstar,Pikachu_Vstar

Venusaur_V = { 
    "nome": "Venusaur V", 
    "tipo": ["planta", "veneno"],
    "evolução": None,
    "FF": [Venusaur_Vmax, Venusaur_Vstar],
    "estagio": 4, 
    "vida": 1.08839779,
    "atk": 1.027777778,
    "atk SP": 1.018867925,
    "def": 1.028571429,
    "def SP": 1.019607843,
    "velocidade": 1.027027027,
    "XP": 120,
    "custo": 3,
    "movelist": ["Mega Dreno", "Ácido", "Raio Solar", "Folha Navalha", "Cura Natural", "Bomba de Lodo"],
}

Charizard_V = { 
    "nome": "Charizard V", 
    "tipo": ["fogo", "voador"],
    "evolução": None,
    "FF": [Charizard_Vmax, Charizard_Vstar],
    "estagio": 4, 
    "vida": 1.091954023,
    "atk": 1.021276596,
    "atk SP": 1.019230769,
    "def": 1.03030303,
    "def SP": 1.027777778,
    "velocidade": 1.019607843,
    "XP": 120,
    "custo": 3,
    "movelist": ["Ataque de Asa", "Mordida", "Raio de Fogo", "Cauda Violenta", "Bola de Fogo", "Ataque em Chamas"],
}

Blastoise_V = { 
    "nome": "Blastoise V", 
    "tipo": ["agua"],
    "evolução": None,
    "FF": [Blastoise_Vmax, Blastoise_Vstar],
    "estagio": 4, 
    "vida": 1.090909091,
    "atk": 1.025641026,
    "atk SP": 1.025641026,
    "def": 1.018867925,
    "def SP": 1.020408163,
    "velocidade": 1.03125,
    "XP": 120,
    "custo": 3,
    "movelist": ["Jato Duplo", "Provocar", "Bola de Água", "Golpe de Concha", "Golpe Territorial", "Gota Pesada"],
}

Machamp_V = { 
    "nome": "Machamp V", 
    "tipo": ["lutador"],
    "evolução": None,
    "FF": [Machamp_Vmax, Machamp_Vstar],
    "estagio": 4, 
    "vida": 1.082901554,
    "atk": 1.018867925,
    "atk SP": 1.028571429,
    "def": 1.019607843,
    "def SP": 1.027777778,
    "velocidade": 1.027777778,
    "XP": 120,
    "custo": 3,
    "movelist": ["Soco", "Combate Próximo", "Treinar", "Submissão", "Chamar para Briga", "Punho Missil"],
}

Gengar_V = { 
    "nome": "Gengar V", 
    "tipo": ["fantasma", "veneno"],
    "evolução": None,
    "FF": [Gengar_Vmax, Gengar_Vstar],
    "estagio": 4, 
    "vida": 1.099378882,
    "atk": 1.029411765,
    "atk SP": 1.016393443,
    "def": 1.03125,
    "def SP": 1.025,
    "velocidade": 1.020408163,
    "XP": 120,
    "custo": 2,
    "movelist": ["Maldade", "Bola Sombria", "Massacre Fantasmagórico", "Coleta Gananciosa", "Nas Sombras", "Extração"],
}

Butterfree_V = { 
    "nome": "Butterfree V", 
    "tipo": ["inseto", "voador"],
    "evolução": None,
    "FF": [Butterfree_Vmax, Butterfree_Vstar],
    "estagio": 4, 
    "vida": 1.103896104,
    "atk": 1.03030303,
    "atk SP": 1.020833333,
    "def": 1.03030303,
    "def SP": 1.025,
    "velocidade": 1.023809524,
    "XP": 100,
    "custo": 2,
    "movelist": ["Vento Forte", "Brilho", "Benção", "Cura Natural", "Seda", "Voar"],
}

Snorlax_V = { 
    "nome": "Snorlax V", 
    "tipo": ["normal"],
    "evolução": None,
    "FF": [Snorlax_Vmax, Snorlax_Vstar],
    "estagio": 4, 
    "vida": 1.065843621,
    "atk": 1.025641026,
    "atk SP": 1.033333333,
    "def": 1.032258065,
    "def SP": 1.03030303,
    "velocidade": 1.071428571,
    "XP": 100,
    "custo": 4,
    "movelist": ["Arranhar", "Tapa", "Tapa Especial", "Provocar", "Esmagar", "Descansar"],
}

Meowth_V = { 
    "nome": "Meowth V", 
    "tipo": ["normal"],
    "evolução": None,
    "FF": [Meowth_Vmax, Meowth_Vstar],
    "estagio": 4, 
    "vida": 1.197530864,
    "atk": 1.045454545,
    "atk SP": 1.052631579,
    "def": 1.055555556,
    "def SP": 1.055555556,
    "velocidade": 1.034482759,
    "XP": 70,
    "custo": 1,
    "movelist": ["Tapa", "Tapa Especial", "Vasculhar", "Arranhar", "Crescer", "Busca Gananciosa"],
}

Pikachu_V = { 
    "nome": "Pikachu V", 
    "tipo": ["eletrico"],
    "evolução": None,
    "FF": [Pikachu_Vmax, Pikachu_Vstar],
    "estagio": 4, 
    "vida": 1.173913043,
    "atk": 1.05,
    "atk SP": 1.035714286,
    "def": 1.045454545,
    "def SP": 1.05,
    "velocidade": 1.029411765,
    "XP": 75,
    "custo": 1,
    "movelist": ["Cauda de Ferro", "Ataque Rápido", "Choque do Trovão", "Faisca", "Bola Elétrica", "Energizar"],
}


# === Fim de V.py ===

# === Início de Vmax.py ===

Venusaur_Vmax = { 
    "nome": "Venusaur Vmax", 
    "tipo": ["planta", "veneno"],
    "evolução": None,
    "FF": "Vmax",
    "estagio": 5, 
    "vida": 2.081218274,
    "atk": 1.108108108,
    "atk SP": 1.074074074,
    "def": 1.083333333,
    "def SP": 1.038461538,
    "velocidade": 0.4473684211,
    "XP": 0,
    "custo": 6,
}

Charizard_Vmax = { 
    "nome": "Charizard Vmax", 
    "tipo": ["fogo", "voador"],
    "evolução": None,
    "FF": "Vmax",
    "estagio": 5, 
    "vida": 2.210526316,
    "atk": 1.145833333,
    "atk SP": 1.056603774,
    "def": 1.176470588,
    "def SP": 1.162162162,
    "velocidade": 0.2692307692,
    "XP": 0,
    "custo": 7,
}

Blastoise_Vmax = { 
    "nome": "Blastoise Vmax", 
    "tipo": ["agua"],
    "evolução": None,
    "FF": "Vmax",
    "estagio": 5, 
    "vida": 2.135416667,
    "atk": 1.2,
    "atk SP": 1.1,
    "def": 1.055555556,
    "def SP": 1.02,
    "velocidade": 0.303030303,
    "XP": 0,
    "custo": 7,

}

Machamp_Vmax = { 
    "nome": "Machamp Vmax", 
    "tipo": ["lutador"],
    "evolução": None,
    "FF": "Vmax",
    "estagio": 5, 
    "vida": 2.057416268,
    "atk": 1.111111111,
    "atk SP": 1.083333333,
    "def": 1.038461538,
    "def SP": 1.054054054,
    "velocidade": 0.3243243243,
    "XP": 0,
    "custo": 6,

}

Gengar_Vmax = { 
    "nome": "Gengar Vmax", 
    "tipo": ["fantasma", "veneno"],
    "evolução": None,
    "FF": "Vmax",
    "estagio": 5, 
    "vida": 2.203389831,
    "atk": 1.228571429,
    "atk SP": 1.064516129,
    "def": 1.090909091,
    "def SP": 1.097560976,
    "velocidade": 0.4,
    "XP": 0,
    "custo": 6,

}

Butterfree_Vmax = { 
    "nome": "Butterfree Vmax", 
    "tipo": ["inseto", "voador"],
    "evolução": None,
    "FF": "Vmax",
    "estagio": 5, 
    "vida": 2.176470588,
    "atk": 1.147058824,
    "atk SP": 1.12244898,
    "def": 1.058823529,
    "def SP": 1.024390244,
    "velocidade": 0.7441860465,
    "XP": 0,
    "custo": 5,

}

Snorlax_Vmax = { 
    "nome": "Snorlax Vmax", 
    "tipo": ["normal"],
    "evolução": None,
    "FF": "Vmax",
    "estagio": 5, 
    "vida": 2.200772201,
    "atk": 1.25,
    "atk SP": 1.161290323,
    "def": 1.0625,
    "def SP": 1.176470588,
    "velocidade": 0,
    "XP": 0,
    "custo": 0,

}

Meowth_Vmax = { 
    "nome": "Meowth Vmax", 
    "tipo": ["normal"],
    "evolução": None,
    "FF": "Vmax",
    "estagio": 5, 
    "vida": 2.577319588,
    "atk": 1.304347826,
    "atk SP": 1.15,
    "def": 1.157894737,
    "def SP": 1.210526316,
    "velocidade": 0.7666666667,
    "XP": 0,
    "custo": 4,

}

Pikachu_Vmax = { 
    "nome": "Pikachu Vmax", 
    "tipo": ["eletrico"],
    "evolução": None,
    "FF": "Vmax",
    "estagio": 5, 
    "vida": 2.592592593,
    "atk": 1.333333333,
    "atk SP": 1.172413793,
    "def": 1.086956522,
    "def SP": 1.19047619,
    "velocidade": 0.4857142857,
    "XP": 0,
    "custo": 4,

}


# === Fim de Vmax.py ===

# === Início de Vstar.py ===

Venusaur_Vstar = { 
    "nome": "Venusaur Vstar", 
    "tipo": ["planta", "veneno"],
    "evolução": None,
    "FF": "Vstar",
    "estagio": 5, 
    "vida": 1.060913706,
    "atk": 1.216216216,
    "atk SP": 1.166666667,
    "def": 1.222222222,
    "def SP": 1.173076923,
    "velocidade": 1.342105263,
    "XP": 0,
    "custo": 3,

}

Charizard_Vstar = { 
    "nome": "Charizard Vstar", 
    "tipo": ["fogo", "voador"],
    "evolução": None,
    "FF": "Vstar",
    "estagio": 5, 
    "vida": 1.063157895,
    "atk": 1.1875,
    "atk SP": 1.169811321,
    "def": 1.235294118,
    "def SP": 1.216216216,
    "velocidade": 1.25,
    "XP": 0,
    "custo": 3,

}

Blastoise_Vstar = { 
    "nome": "Blastoise Vstar", 
    "tipo": ["agua"],
    "evolução": None,
    "FF": "Vstar",
    "estagio": 5, 
    "vida": 1.0625,
    "atk": 1.2,
    "atk SP": 1.2,
    "def": 1.166666667,
    "def SP": 1.18,
    "velocidade": 1.393939394,
    "XP": 0,
    "custo": 3,

}

Machamp_Vstar = { 
    "nome": "Machamp Vstar", 
    "tipo": ["lutador"],
    "evolução": None,
    "FF": "Vstar",
    "estagio": 5, 
    "vida": 1.057416268,
    "atk": 1.166666667,
    "atk SP": 1.222222222,
    "def": 1.173076923,
    "def SP": 1.216216216,
    "velocidade": 1.351351351,
    "XP": 0,
    "custo": 3,

}

Gengar_Vstar = { 
    "nome": "Gengar Vstar", 
    "tipo": ["fantasma", "veneno"],
    "evolução": None,
    "FF": "Vstar",
    "estagio": 5, 
    "vida": 1.06779661,
    "atk": 1.228571429,
    "atk SP": 1.14516129,
    "def": 1.242424242,
    "def SP": 1.219512195,
    "velocidade": 1.26,
    "XP": 0,
    "custo": 2,

}

Butterfree_Vstar = { 
    "nome": "Butterfree Vstar", 
    "tipo": ["inseto", "voador"],
    "evolução": None,
    "FF": "Vstar",
    "estagio": 5, 
    "vida": 1.070588235,
    "atk": 1.235294118,
    "atk SP": 1.183673469,
    "def": 1.235294118,
    "def SP": 1.219512195,
    "velocidade": 1.302325581,
    "XP": 0,
    "custo": 2,

}

Snorlax_Vstar = { 
    "nome": "Snorlax Vstar", 
    "tipo": ["normal"],
    "evolução": None,
    "FF": "Vstar",
    "estagio": 5, 
    "vida": 1.046332046,
    "atk": 1.225,
    "atk SP": 1.258064516,
    "def": 1.25,
    "def SP": 1.264705882,
    "velocidade": 1.866666667,
    "XP": 0,
    "custo": 4,

}

Meowth_Vstar = { 
    "nome": "Meowth Vstar", 
    "tipo": ["normal"],
    "evolução": None,
    "FF": "Vstar",
    "estagio": 5, 
    "vida": 1.12371134,
    "atk": 1.391304348,
    "atk SP": 1.45,
    "def": 1.421052632,
    "def SP": 1.421052632,
    "velocidade": 1.433333333,
    "XP": 0,
    "custo": 1,

}

Pikachu_Vstar = { 
    "nome": "Pikachu Vstar", 
    "tipo": ["eletrico"],
    "evolução": None,
    "FF": "Vstar",
    "estagio": 5, 
    "vida": 1.111111111,
    "atk": 1.428571429,
    "atk SP": 1.310344828,
    "def": 1.347826087,
    "def SP": 1.380952381,
    "velocidade": 1.371428571,
    "XP": 0,
    "custo": 1,
}


# === Fim de Vstar.py ===

