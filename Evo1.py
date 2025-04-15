import random
from Ataques_N import A,B
from Ataques_S import C,D
from Evo2 import Venusaur,Charizard,Blastoise,Machamp,Gengar,Golem,Butterfree,Alakazam,Dragonite

Ivysaur = {
    "nome": "Ivysaur",
    "tipo": ["planta","venenoso"],
    "evolução": Venusaur,
    "estagio": "estagio 1",
    "vida": 1.15,
    "atk": 1.1,
    "atk SP": 1.15,
    "def": 1.1,
    "def SP": 1.15,
    "velocidade": 3,
    "XP": 3,
    "custo": 2,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Charmeleon = {
    "nome": "Charmeleon",
    "tipo": ["fogo"],
    "evolução": Charizard,
    "estagio": "estagio 1",
    "vida": 1.1,
    "atk": 1.1,
    "atk SP": 1.2,
    "def": 1.1,
    "def SP": 1.15,
    "velocidade": 4,
    "XP": 3,
    "custo": 1,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Wartortle = {
    "nome": "Wartortle",
    "tipo": ["agua"],
    "evolução": Blastoise,
    "estagio": "estagio 1",
    "vida": 1.1,
    "atk": 1.1,
    "atk SP": 1.1,
    "def": 1.15,
    "def SP": 1.1,
    "velocidade": 3,
    "XP": 3,
    "custo": 2,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Machoke = {
    "nome": "Machoke",
    "tipo": ["lutador"],
    "evolução": Machamp,
    "estagio": "estagio 1",
    "vida": 1.1,
    "atk": 1.2,
    "atk SP": 1.05,
    "def": 1.1,
    "def SP": 1.1,
    "velocidade": 3,
    "XP": 3,
    "custo": 3,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Haunter = {
    "nome": "Haunter",
    "tipo": ["fantasma","venenoso"],
    "evolução": Gengar,
    "estagio": "estagio 1",
    "vida": 1.1,
    "atk": 1.05,
    "atk SP": 1.2,
    "def": 1.05,
    "def SP": 1.1,
    "velocidade": 4,
    "XP": 3,
    "custo": 1,
    "ataques normais": [B],
    "ataques especiais": [C,D]
}

Graveler = {
    "nome": "Graveler",
    "tipo": ["pedra","terrestre"],
    "evolução": Golem,
    "estagio": "estagio 1",
    "vida": 1.15,
    "atk": 1.1,
    "atk SP": 1.1,
    "def": 1.1,
    "def SP": 1.1,
    "velocidade": 2,
    "XP": 3,
    "custo": 4,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Metapod = {
    "nome": "Metapod",
    "tipo": ["inseto"],
    "evolução": Butterfree,
    "estagio": "estagio 1",
    "vida": 1.05,
    "atk": 1.025,
    "atk SP": 1.025,
    "def": 1.15,
    "def SP": 1.05,
    "velocidade": 2,
    "XP": 4,
    "custo": 3,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Kadabra = {
    "nome": "Kadabra",
    "tipo": ["psiquico"],
    "evolução": Alakazam,
    "estagio": "estagio 1",
    "vida": 1.15,
    "atk": 1.1,
    "atk SP": 1.1,
    "def": 1.1,
    "def SP": 1.1,
    "velocidade": 4,
    "XP": 3,
    "custo": 2,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Dragonair = {
    "nome": "Dragonair",
    "tipo": ["dragao"],
    "evolução": Dragonite,
    "estagio": "estagio 1",
    "vida": 1.15,
    "atk": 1.1,
    "atk SP": 1.1,
    "def": 1.1,
    "def SP": 1.15,
    "velocidade": 4,
    "XP": 4,
    "custo": 2,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Raichu = {
    "nome": "Raichu",
    "tipo": ["eletrico"],
    "evolução": None,
    "estagio": "estagio 1",
    "vida": 1.2,
    "atk": 1.1,
    "atk SP": 1.2,
    "def": 1.15,
    "def SP": 1.15,
    "velocidade": 6,
    "XP": 3,
    "custo": 1,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Zoroark = {
    "nome": "Zoroark",
    "tipo": ["sombrio"],
    "evolução": None,
    "estagio": "estagio 1",
    "vida": 1.2,
    "atk": 1.2,
    "atk SP": 1.25,
    "def": 1.1,
    "def SP": 1.1,
    "velocidade": 5,
    "XP": 3,
    "custo": 2,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Gyarados = {
    "nome": "Gyarados",
    "tipo": ["agua"],
    "evolução": None,
    "estagio": "estagio 1",
    "vida": 2.6,
    "atk": 4.5,
    "atk SP": 2.9,
    "def": 2.5,
    "def SP": 2.8,
    "velocidade": 4,
    "XP": 3,
    "custo": 4,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Wigglytuff = {
    "nome": "Wigglytuff",
    "tipo": ["fada,normal"],
    "evolução": None,
    "estagio": "estagio 1",
    "vida": 1.35,
    "atk": 1.1,
    "atk SP": 1.15,
    "def": 1.1,
    "def SP": 1.1,
    "velocidade": 2,
    "XP": 3,
    "custo": 3,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

Magneton = {
    "nome": "Magneton",
    "tipo": ["eletrico","metal"],
    "evolução": None,
    "estagio": "estagio 1",
    "vida": 1.15,
    "atk": 1.1,
    "atk SP": 1.15,
    "def": 1.15,
    "def SP": 1.15,
    "velocidade": 3,
    "XP": 3,
    "custo": 1,
    "ataques normais":[B],
    "ataques especiais":[C,D]
}

