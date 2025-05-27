import random
from Dados.Gen1.Mega import Mega_Alakazam,Mega_Charizard_X,Mega_Charizard_Y,Mega_Gengar,Mega_Beedrill,Mega_Blastoise,Mega_Venusaur
from Dados.Gen1.V import Venusaur_V,Blastoise_V,Charizard_V,Gengar_V,Machamp_V,Butterfree_V

Venusaur = {
    "nome": "Venusaur",
    "tipo": ["planta", "venenoso"],
    "evolução": None,
    "FF": [Mega_Venusaur],
    "vida": 155,
    "atk": 36,
    "atk SP": 58,
    "def": 35,
    "def SP": 57,
    "velocidade": 36,
    "XP": 80,
    "custo": 3,
    "moves": 4,
    "Tamanho": 1.9,
    "movelist": ["Mega Dreno", "Ácido", "Raio Solar", "Folha Navalha", "Cura Natural", "Bomba de Lodo"],
    "H": 1.77,
    "W": 110
}

Charizard = {
    "nome": "Charizard",
    "tipo": ["fogo", "voador"],
    "evolução": None,
    "FF": [Mega_Charizard_X, Mega_Charizard_Y],
    "vida": 147,
    "atk": 52,
    "atk SP": 57,
    "def": 32,
    "def SP": 37,
    "velocidade": 52,
    "XP": 80,
    "custo": 3,
    "moves": 4,
    "Tamanho": 1.8,
    "movelist": ["Ataque de Asa", "Mordida", "Raio de Fogo", "Cauda Violenta", "Bola de Fogo", "Ataque de Chamas"],
    "H": 1.83,
    "W": 92

}

Blastoise = {
    "nome": "Blastoise",
    "tipo": ["agua"],
    "evolução": None,
    "FF": [Mega_Blastoise],
    "vida": 151,
    "atk": 40,
    "atk SP": 39,
    "def": 59,
    "def SP": 54,
    "velocidade": 29,
    "XP": 80,
    "custo": 3,
    "moves": 4,
    "Tamanho": 1.8,
    "movelist": ["Jato Duplo", "Provocar", "Bola de Água", "Golpe de Concha", "Golpe Territorial", "Gota Pesada"],
    "H": 1.69,
    "W": 106

}

Machamp = {
    "nome": "Machamp",
    "tipo": ["lutador"],
    "evolução": None,
    "FF": None,
    "vida": 173,
    "atk": 55,
    "atk SP": 34,
    "def": 54,
    "def SP": 36,
    "velocidade": 37,
    "XP": 0,
    "custo": 3,
    "moves": 4,
    "Tamanho": 1.8,
    "movelist": ["Soco", "Combate Próximo", "Treinar", "Submissão", "Chamar para Briga", "Punho Míssil"],
    "H": 1.75,
    "W": 115
}

Gengar = {
    "nome": "Gengar",
    "tipo": ["fantasma", "venenoso"],
    "evolução": None,
    "FF": [Mega_Gengar],
    "vida": 134,
    "atk": 36,
    "atk SP": 65,
    "def": 32,
    "def SP": 46,
    "velocidade": 50,
    "XP": 80,
    "custo": 2,
    "moves": 4,
    "Tamanho": 1.7,
    "movelist": ["Maldade", "Bola Sombria", "Massacre Fantasmagórico", "Coleta Gananciosa", "Nas Sombras", "Extração"],
    "H": 1.52,
    "W": 48

}

Golem = {
    "nome": "Golem",
    "tipo": ["pedra", "terrestre"],
    "evolução": None,
    "FF": None,
    "vida": 168,
    "atk": 48,
    "atk SP": 34,
    "def": 66,
    "def SP": 48,
    "velocidade": 27,
    "XP": 80,
    "custo": 5,
    "moves": 4,
    "Tamanho": 2.0,
    "movelist": ["Terremoto", "Provocar", "Fúria Pétrea", "Barragem Rochosa", "Reforçar", "Pedra Colossal"],
    "H": 1.58,
    "W": 390

}

Butterfree = {
    "nome": "Butterfree",
    "tipo": ["inseto", "voador"],
    "evolução": None,
    "FF": None,
    "vida": 128,
    "atk": 32,
    "atk SP": 51,
    "def": 29,
    "def SP": 40,
    "velocidade": 43,
    "XP": 0,
    "custo": 2,
    "moves": 4,
    "Tamanho": 1.6,
    "movelist": ["Vento Forte", "Brilho", "Benção", "Cura Natural", "Seda", "Voar"],
    "H": 1.16,
    "W": 31

}

Alakazam = {
    "nome": "Alakazam",
    "tipo": ["psiquico"],
    "evolução": None,
    "FF": [Mega_Alakazam],
    "vida": 125,
    "atk": 32,
    "atk SP": 73,
    "def": 30,
    "def SP": 54,
    "velocidade": 48,
    "XP": 80,
    "custo": 3,
    "moves": 4,
    "Tamanho": 1.6,
    "movelist": ["Teletransporte", "Ampliação Mental", "Raio Psíquico", "Mente Forte", "Bola Psíquica", "Transferência Psíquica"],
    "H": 1.59,
    "W": 43

}

Dragonite = {
    "nome": "Dragonite",
    "tipo": ["dragao", "voador"],
    "evolução": None,
    "FF": None,
    "vida": 211,
    "atk": 65,
    "atk SP": 47,
    "def": 45,
    "def SP": 42,
    "velocidade": 31,
    "XP": 0,
    "custo": 4,
    "moves": 4,
    "Tamanho": 2.3,
    "movelist": ["Ultraje", "Investida do Dragão", "Provocar", "Pedra Colossal", "Cauda Violenta", "Bola de Fogo"],
    "H": 2.26,
    "W": 210
}

Beedrill = {
    "nome": "Beedrill",
    "tipo": ["inseto", "venenoso"],
    "evolução": None,
    "FF": [Mega_Beedrill],
    "vida": 106,
    "atk": 62,
    "atk SP": 30,
    "def": 30,
    "def SP": 32,
    "velocidade": 56,
    "XP": 70,
    "custo": 1,
    "moves": 4,
    "Tamanho": 1.5,
    "movelist": ["Dor Falsa", "Envenenar", "Voar", "Rasante", "Picada", "Extração"],
    "H": 1.14,
    "W": 28
}

Magnezone = {
    "nome": "Magnezone",
    "tipo": ["eletrico", "metal"],
    "evolução": None,
    "FF": None,
    "vida": 146,
    "atk": 30,
    "atk SP": 59,
    "def": 57,
    "def SP": 47,
    "velocidade": 35,
    "XP": 0,
    "custo": 3,
    "moves": 4,
    "Tamanho": 1.8,
    "movelist": [],
    "H": 0,
    "W": 0
}