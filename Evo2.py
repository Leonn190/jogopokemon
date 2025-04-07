import random
from Ataques_N import A,B
from Ataques_S import C,D

Venusaur = {
    "nome": "Venusaur",
    "tipo": ["planta","veneno"],
    "evolução": "c",
    "estagio": "estagio 2",
    "vida": 30,
    "atk": 20,
    "atk SP": 30,
    "def": 20,
    "def SP": 30,
    "velocidade": 3,
    "XP": 3,
    "custo": 3,
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Charizard = {
    "nome": "",
    "tipo": ["fogo,voador"],
    "evolução": "c",
    "estagio": "estagio 2",
    "vida": 30,
    "atk": 20,
    "atk SP": 30,
    "def": 20,
    "def SP": 30,
    "velocidade": 3,
    "XP": 3,
    "custo": 3,
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}

Blastoise = {
    "nome": "blastoise",
    "tipo": ["agua"],
    "evolução": "c",
    "estagio": "estagio 2",
    "vida": 30,
    "atk": 20,
    "atk SP": 30,
    "def": 20,
    "def SP": 30,
    "velocidade": 3,
    "XP": 3,
    "custo": 3,
    "ataques normais": random.choice([B]),
    "ataques especiais": random.choice([C,D])
}