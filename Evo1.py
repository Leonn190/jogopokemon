import random
from Ataques_N import A,B
from Ataques_S import C,D
from Evo2 import Venusaur,Charizard,Blastoise,Machamp,Gengar,Golem,Butterfree,Alakazam,Dragonite

Ivysaur = {
    "nome": "ivysaur",
    "tipo": ["planta","veneno"],
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
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Charmeleon = {
    "nome": "charmeleon",
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
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Wartortle = {
    "nome": "wartortle",
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
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
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
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Haunter = {
    "nome": "haunter",
    "tipo": ["fantasma","veneno"],
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
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Graveler = {
    "nome": "graveler",
    "tipo": ["pedra","terra"],
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
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Metapod = {
    "nome": "metapod",
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
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Kadabra = {
    "nome": "kadabra",
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
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Dragonair = {
    "nome": "dragonair",
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
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Raichu = {
    "nome": "raichu",
    "tipo": ["eletrico"],
    "evolução": 0,
    "estagio": "estagio 1",
    "vida": 1.2,
    "atk": 1.1,
    "atk SP": 1.2,
    "def": 1.15,
    "def SP": 1.15,
    "velocidade": 6,
    "XP": 3,
    "custo": 1,
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Zoroark = {
    "nome": "zoroark",
    "tipo": ["sombrio"],
    "evolução": 0,
    "estagio": "estagio 1",
    "vida": 1.2,
    "atk": 1.2,
    "atk SP": 1.25,
    "def": 1.1,
    "def SP": 1.1,
    "velocidade": 5,
    "XP": 3,
    "custo": 2,
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Gyarados = {
    "nome": "gyarados",
    "tipo": ["agua"],
    "evolução": 0,
    "estagio": "estagio 1",
    "vida": 2.6,
    "atk": 4.5,
    "atk SP": 2.9,
    "def": 2.5,
    "def SP": 2.8,
    "velocidade": 4,
    "XP": 3,
    "custo": 4,
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Wigglytuff = {
    "nome": "wigglytuff",
    "tipo": ["fada,normal"],
    "evolução": 0,
    "estagio": "estagio 1",
    "vida": 1.35,
    "atk": 1.1,
    "atk SP": 1.15,
    "def": 1.1,
    "def SP": 1.1,
    "velocidade": 2,
    "XP": 3,
    "custo": 3,
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Magneton = {
    "nome": "magneton",
    "tipo": ["eletrico","aço"],
    "evolução": 0,
    "estagio": "estagio 1",
    "vida": 1.15,
    "atk": 1.1,
    "atk SP": 1.15,
    "def": 1.15,
    "def SP": 1.15,
    "velocidade": 3,
    "XP": 3,
    "custo": 1,
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

