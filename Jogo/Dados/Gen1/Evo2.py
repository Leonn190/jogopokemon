import random
from Dados.Gen1.Mega import Mega_Alakazam,Mega_Charizard_X,Mega_Charizard_Y,Mega_Gengar,Mega_Beedrill,Mega_Blastoise,Mega_Venusaur
from Dados.Gen1.V import Venusaur_V,Blastoise_V,Charizard_V,Gengar_V,Machamp_V,Butterfree_V
import Dados.AllAtaques as A

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
    "ataques normais": [A.ANplanta.Folha_Navalha],
    "ataques especiais": [A.ASplanta.Raio_Solar]
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
    "ataques normais": [A.ANfogo.Lâmina_Ígnea],
    "ataques especiais": [A.ASfogo.Bola_de_Fogo]
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
    "ataques normais": [A.ANagua.Jato_de_Agua],
    "ataques especiais": [A.ASagua.Bola_de_Agua]
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
    "ataques normais": [A.ANlutador.Chave_de_Impulso],
    "ataques especiais": [A.ASlutador.Punho_Tornado]
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
    "ataques normais": [A.ANvenenoso.Vórtice_Venenoso],
    "ataques especiais": [A.ASfantasma.Bola_Fantasma]
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
    "ataques normais": [A.ANpedra.Pancada_Rocha],
    "ataques especiais": [A.ASpedra.Lança_de_Pedra]
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
    "ataques normais": [A.ANfada.Brilho],
    "ataques especiais": [A.ASinseto.Bola_de_Insetos]
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
    "ataques normais": [A.ANpsiquico.Colapso_Psiquico],
    "ataques especiais": [A.ASpsiquico.Bola_Psiquica]
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
    "ataques normais": [A.ANdragao.Garras_Ferinas],
    "ataques especiais": [A.ASdragao.Bola_Dragonica]
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
    "ataques normais": [A.ANinseto.Mandíbula_Vingativa],
    "ataques especiais": [A.ASinseto.Explosão_Criatura]
}


