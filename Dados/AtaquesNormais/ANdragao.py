Asa_de_Ferro = {
    "nome": "Asa de Ferro",
    "tipo": ["dragao"],
    "custo": ["marrom", "marrom"],
    "dano": 1.2,
    "alcance": 30,
    "precisão": 100,
    "descrição": "Golpe veloz com a asa de um dragão, causando impacto contundente",
    "função": [],
    "alvo": [],
    "valorAlvo": [], 
    "valores": []
}

Cauda_Desgastante = {
    "nome": "Cauda Desgastante",
    "tipo": ["dragao"],
    "custo": ["marrom", "marrom"],
    "dano": 1.4,
    "alcance": 35,
    "precisão": 95,
    "descrição": "Um golpe de cauda que perde força conforme o inimigo carrega mais itens.",
    "função": [],
    "alvo": [],
    "valorAlvo": [],
    "condicional": True,
    "valores": [
        ["ItensInimigo", 2, -0.2]  # A cada 2 itens do oponente, reduz 0.2 no dano final
    ]
}

Garras_Ferinas = {
    "nome": "Garras Ferinas",
    "tipo": ["dragao"],
    "custo": ["normal", "marrom", "marrom", "marrom"],
    "dano": 1.7,
    "alcance": 25,
    "precisão": 100,
    "descrição": "Ataca com garras afiadas e poderosas que rasgam a defesa inimiga",
    "função": [],
    "alvo": [],
    "valorAlvo": [],
    "valores": []
}

Fúria_do_Dragão = {
    "nome": "Fúria do Dragão",
    "tipo": ["dragao"],
    "custo": ["normal", "normal", "marrom", "marrom", "marrom", "marrom"],
    "dano": 2.2,
    "alcance": 35,
    "precisão": 80,
    "descrição": "Uma explosão de poder que canaliza toda a fúria do dragão, causando enorme dano ao oponente. Há 60% de chance de causar 35 de dano ao próprio usuário.",
    "chance": [60], 
    "função": ["DanoExtra"],
    "alvo": ["self"],
    "valorAlvo": [1], 
    "valores": [35]   
}
