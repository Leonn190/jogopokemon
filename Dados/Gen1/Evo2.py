import random
from Dados.Gen1.Mega import Mega_Alakazam,Mega_Charizard_X,Mega_Charizard_Y,Mega_Gengar,Mega_Beedrill,Mega_Blastoise,Mega_Venusaur
from Dados.Gen1.V import Venusaur_V,Blastoise_V,Charizard_V,Gengar_V,Machamp_V,Butterfree_V

Venusaur = {
    "nome": "Venusaur",
    "tipo": ["planta", "venenoso"],
    "evolução": Venusaur_V,
    "FF": [Mega_Venusaur],
    "estagio": 3,
    "vida": 181,
    "atk": 36,
    "atk SP": 53,
    "def": 35,
    "def SP": 51,
    "velocidade": 37,
    "custo": 3,
    "XP": 90,
    "movelist": ["Mega Dreno", "Ácido", "Raio Solar", "Folha Navalha", "Cura Natural", "Bomba de Lodo"],
    "moves": 4,
    "H": 1.77,
    "W": 110
}

Charizard = {
    "nome": "Charizard",
    "tipo": ["fogo", "voador"],
    "evolução": Charizard_V,
    "FF": [Mega_Charizard_X, Mega_Charizard_Y],
    "estagio": 3,
    "vida": 174,
    "atk": 47,
    "atk SP": 52,
    "def": 33,
    "def SP": 36,
    "velocidade": 51,
    "custo": 3,
    "XP": 90,
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
    "vida": 176,
    "atk": 39,
    "atk SP": 39,
    "def": 53,
    "def SP": 49,
    "velocidade": 32,
    "custo": 3,
    "XP": 90,
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
    "vida": 193,
    "atk": 53,
    "atk SP": 35,
    "def": 51,
    "def SP": 36,
    "velocidade": 36,
    "custo": 3,
    "XP": 90,
    "movelist": ["Soco", "Combate Próximo", "Treinar", "Submissão", "Chamar para Briga", "Punho Míssil"],
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
    "vida": 161,
    "atk": 34,
    "atk SP": 61,
    "def": 32,
    "def SP": 40,
    "velocidade": 49,
    "custo": 2,
    "XP": 90,
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
    "vida": 191,
    "atk": 43,
    "atk SP": 33,
    "def": 64,
    "def SP": 45,
    "velocidade": 27,
    "custo": 5,
    "XP": 0,
    "movelist": ["Terremoto", "Provocar", "Fúria Pétrea", "Barragem Rochosa", "Reforçar", "Pedra Colossal"],
    "moves": 4,
    "H": 1.58,
    "W": 390

}

Butterfree = {
    "nome": "Butterfree",
    "tipo": ["inseto", "voador"],
    "evolução": Butterfree_V,
    "FF": None,
    "estagio": 3,
    "vida": 154,
    "atk": 33,
    "atk SP": 48,
    "def": 33,
    "def SP": 40,
    "velocidade": 42,
    "custo": 2,
    "XP": 80,
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
    "vida": 159,
    "atk": 31,
    "atk SP": 69,
    "def": 31,
    "def SP": 48,
    "velocidade": 47,
    "custo": 3,
    "XP": 95,
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
    "vida": 205,
    "atk": 61,
    "atk SP": 44,
    "def": 45,
    "def SP": 43,
    "velocidade": 33,
    "custo": 4,
    "XP": 0,
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
    "vida": 146,
    "atk": 57,
    "atk SP": 30,
    "def": 30,
    "def SP": 31,
    "velocidade": 55,
    "custo": 1,
    "XP": 75,
    "movelist": ["Dor Falsa", "Envenenar", "Voar", "Rasante", "Picada", "Extração"],
    "moves": 4,
    "H": 1.14,
    "W": 28

}
