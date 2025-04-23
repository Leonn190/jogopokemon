Bomba_De_Xarope = {
    "nome": "Bomba De Xarope",
    "tipo": ["planta"],   
    "custo": ["normal","verde"],
    "dano": 1,
    "alcance": 30,
    "precisão": 100,
    
    "descrição": "Um disparo flamejante",
    "função": "AumentoCondicional",
    "alvo": "",
    "valores": ["Ouro", 30, 50],

    "função": "Mover",
    "alvo": "",
    "valores": ["Puxar",2]
}

Raio_Solar = {
    "nome": "Raio Solar",
    "tipo": ["planta"],   
    "custo": ["verde","verde","verde"],
    "dano": 1.5,
    "alcance": 50,
    "precisão": 100,
    "descrição": "Um raio poderoso canalisado pela luz do sol",
    "função": None,
    "valores": None
}

Dança_das_petalas = {
    "nome": "Dança das Pétalas",
    "tipo": ["planta"],   
    "custo": ["normal","verde"],
    "dano": 0.7,
    "alcance": 20,
    "precisão": 100,
    "descrição": "Ganhe permanentemente 1 de velocidade e conceda o efeito Velocista a um aliado aleatório",
    "função": None,
    "valores": None
}

Dreno = {
    "nome": "Dreno",
    "tipo": ["planta"],   
    "custo": ["verde"],
    "dano": 0.8,
    "alcance": 25,
    "precisão": 90,
    "descrição": "Drene o Pokemon inimigo curando 15 de vida",
    "função": "Autocura",
    "valores": 15
}