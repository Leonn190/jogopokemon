import Dados.AllAtaques as A
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
    "ataques normais": [A.ANplanta.Golpe_Tropical],
    "ataques especiais": [A.ASplanta.Tiro_de_semente, A.ASplanta.Dreno]
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
    "ataques normais": [A.ANfogo.Labareda_Turbulenta],
    "ataques especiais": [A.ASfogo.Chama]
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
    "ataques normais": [A.ANagua.Jato_de_Agua],
    "ataques especiais": [A.ASnormal.Energia]
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
    "ataques normais": [A.ANlutador.Soco],
    "ataques especiais": [A.ASnormal.Vasculhar]
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
    "ataques normais": [A.ANfantasma.Toque_Espiritual],
    "ataques especiais": [A.ASvenenoso.Gás]
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
    "ataques normais": [A.ANpedra.Pedregulho],
    "ataques especiais": [A.ASterrestre.Desmoronamento]
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
    "ataques normais": [A.ANinseto.Mordida],
    "ataques especiais": [A.ASinseto.Danza_Larval]
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
    "ataques normais": [A.ANpsiquico.Toque_Mental],
    "ataques especiais": [A.ASnormal.Energia]
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
    "ataques normais": [A.ANnormal.Cabeçada],
    "ataques especiais": [A.ASdragao.Sopro_Dragão]
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
    "ataques normais": [A.ANeletrico.Faísca],
    "ataques especiais": [A.ASeletrico.Bola_de_Eletricidade]
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
    "ataques normais": [A.ANsombrio.Garras_Nebulosas],
    "ataques especiais": [A.ASsombrio.Sombra_Lisga]
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
    "ataques normais": [A.ANagua.Jato_de_Agua],
    "ataques especiais": [A.ASnormal.Vasculhar]
}

Jigglypuff = {
    "nome": "Jigglypuff",
    "raridade": 3,
    "dificuldade": 1,
    "code": 13,
    "tipo": ["fada", "normal"],
    "evolução": "Wigglytuff",
    "FF": None,
    "vida": 140,
    "atk": 23,
    "atk SP": 16,
    "def": 20,
    "def SP": 21,
    "velocidade": 20,
    "XP": 35,
    "custo": 1,
    "ataques normais": ["A.ANfada.Brilho"],
    "ataques especiais": ["A.ASfada.Encanto_Cintilante"]
}

Clefairy = {
    "nome": "Clefairy",
    "raridade": 3,
    "dificuldade": 1,
    "code": 14,
    "tipo": ["fada"],
    "evolução": "Clefable",
    "FF": None,
    "vida": 107,
    "atk": 17,
    "atk SP": 22,
    "def": 20,
    "def SP": 26,
    "velocidade": 14,
    "XP": 35,
    "custo": 2,
    "ataques normais": ["A.ANfada.Brilho"],
    "ataques especiais": ["A.ASfada.Encanto_Cintilante"]
}

Meowth = {
    "nome": "Meowth",
    "raridade": 2,
    "dificuldade": 2,
    "code": 15,
    "tipo": ["normal"],
    "evolução": ["Persian", "Meowth_V"],
    "FF": None,
    "vida": 81,
    "atk": 22,
    "atk SP": 19,
    "def": 18,
    "def SP": 18,
    "velocidade": 29,
    "XP": 35,
    "custo": 1,
    "ataques normais": ["A.ANnormal.Tapa"],
    "ataques especiais": ["A.ASnormal.Vasculhar"]
}

Cubone = {
    "nome": "Cubone",
    "raridade": 2,
    "dificuldade": 4,
    "code": 16,
    "tipo": ["terrestre"],
    "evolução": "Marowak",
    "FF": None,
    "vida": 77,
    "atk": 19,
    "atk SP": 18,
    "def": 27,
    "def SP": 21,
    "velocidade": 19,
    "XP": 30,
    "custo": 1,
    "ataques normais": ["A.ANterrestre.Terra"],
    "ataques especiais": ["A.ASterrestre.Desmoronamento"]
}

Shellder = {
    "nome": "Shellder",
    "raridade": 3,
    "dificuldade": 2,
    "code": 17,
    "tipo": ["agua"],
    "evolução": "Cloyster",
    "FF": None,
    "vida": 65,
    "atk": 25,
    "atk SP": 18,
    "def": 29,
    "def SP": 19,
    "velocidade": 21,
    "XP": 40,
    "custo": 1,
    "ataques normais": ["A.ANagua.Jato_de_Agua"],
    "ataques especiais": ["A.ASnormal.Energia"]
}

Magnemite = {
    "nome": "Magnemite",
    "raridade": 2,
    "dificuldade": 2,
    "code": 18,
    "tipo": ["eletrico", "metal"],
    "evolução": "Magneton",
    "FF": None,
    "vida": 51,
    "atk": 19,
    "atk SP": 26,
    "def": 25,
    "def SP": 23,
    "velocidade": 20,
    "XP": 35,
    "custo": 1,
    "ataques normais": ["A.ANmetal.Impacto"],
    "ataques especiais": ["A.ASeletrico.Bola_de_Eletricidade"]
}

Rattata = {
    "nome": "Rattata",
    "raridade": 1,
    "dificuldade": 1,
    "code": 19,
    "tipo": ["normal"],
    "evolução": "Raticate",
    "FF": None,
    "vida": 67,
    "atk": 22,
    "atk SP": 13,
    "def": 19,
    "def SP": 15,
    "velocidade": 28,
    "XP": 30,
    "custo": 0,
    "ataques normais": ["A.ANnormal.Tapa"],
    "ataques especiais": ["A.ASnormal.Vasculhar"]
}

Weedle = {
    "nome": "Weedle",
    "raridade": 1,
    "dificuldade": 1,
    "code": 20,
    "tipo": ["inseto"],
    "evolução": "Kakuna",
    "FF": None,
    "vida": 58,
    "atk": 20,
    "atk SP": 19,
    "def": 18,
    "def SP": 19,
    "velocidade": 17,
    "XP": 15,
    "custo": 1,
    "ataques normais": ["A.ANinseto.Mordida"],
    "ataques especiais": ["A.ASinseto.Danza_Larval"]
}

Snorlax = {
    "nome": "Snorlax",
    "raridade": 7,
    "dificuldade": 5,
    "code": 21,
    "tipo": ["normal"],
    "evolução": "Snorlax_V",
    "FF": None,
    "vida": 243,
    "atk": 39,
    "atk SP": 30,
    "def": 31,
    "def SP": 33,
    "velocidade": 14,
    "XP": 45,
    "custo": 4,
    "ataques normais": ["A.ANnormal.Tapa"],
    "ataques especiais": ["A.ASnormal.Energia"]
}

Aerodactyl = {
    "nome": "Aerodactyl",
    "raridade": 7,
    "dificuldade": 6,
    "code": 22,
    "tipo": ["pedra", "voador"],
    "evolução": None,
    "FF": "Mega_Aerodactyl",
    "vida": 151,
    "atk": 44,
    "atk SP": 32,
    "def": 30,
    "def SP": 27,
    "velocidade": 50,
    "XP": 50,
    "custo": 3,
    "ataques normais": ["A.ANpedra.Pancada_Rocha"],
    "ataques especiais": ["A.ASvoador.Rajada"]
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
    "ataques normais": ["A.ANgelo.Caco_de_Gelo"],
    "ataques especiais": ["A.ASpsiquico.Ondas_Mentais"]
}

Pinsir = {
    "nome": "Pinsir",
    "raridade": 6,
    "dificuldade": 4,
    "code": 24,
    "tipo": ["inseto"],
    "evolução": None,
    "FF": "Mega_Pinsir",
    "vida": 124,
    "atk": 50,
    "atk SP": 20,
    "def": 28,
    "def SP": 24,
    "velocidade": 25,
    "XP": 45,
    "custo": 2,
    "ataques normais": ["A.ANinseto.Mandíbula_Vingativa"],
    "ataques especiais": ["A.ASinseto.Bola_de_Insetos"]
}

Mewtwo = {
    "nome": "Mewtwo",
    "raridade": 10,
    "dificuldade": 9,
    "code": 25,
    "tipo": ["psiquico"],
    "evolução": None,
    "FF": ["Mega_Mewtwo_X", "Mega_Mewtwo_Y"],
    "vida": 196,
    "atk": 64,
    "atk SP": 76,
    "def": 50,
    "def SP": 56,
    "velocidade": 68,
    "XP": 55,
    "custo": 3,
    "ataques normais": ["A.ANpsiquico.Colapso_Psiquico"],
    "ataques especiais": ["A.ASpsiquico.Bola_Psiquica"]
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
    "ataques normais": ["A.ANgelo.Bola_de_Gelo"],
    "ataques especiais": ["A.ASvoador.Furacão_Gelado"]
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
    "ataques normais": [A.ANvoador.Lâmina_Aérea],
    "ataques especiais": [A.ASfogo.Bola_de_Fogo]
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
    "ataques normais": [A.ANvoador.Lâmina_Aérea],
    "ataques especiais": [A.ASeletrico.Bola_de_Eletricidade]
}

Pokedex = [0,
    Bulbasaur, Charmander, Squirtle, Machop, Gastly, Geodude, Caterpie, Abra, Dratini, Pikachu,
    Zorua, Magikarp, Jigglypuff, Clefairy, Meowth, Cubone, Shellder, Magnemite, Rattata, Weedle, Snorlax, Aerodactyl, Jynx, Pinsir, Mewtwo, Articuno,Moltres,Zapdos]