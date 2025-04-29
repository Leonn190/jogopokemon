from Geradores.GeradorAtaques import padrao

Jato_de_Agua = {
    "nome": "Jato De Agua",
    "tipo": ["agua"],   
    "custo": ["normal","azul"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Lança um jato de agua intenso no oponente",
    "efeito": "EspiralAzul",
    "extra": False,
    "funçao": padrao
    }

Jato_duplo = {
    "nome": "Jato De Agua",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul"],
    "estilo": "E",
    "dano": 1.0,
    "alcance": 20,
    "precisão": 95, 
    "descrição": "Esse ataque tem 50% de chance de causar mais 50% de dano e deixar o oponente encharcado",
    "extra": None,
    "funçao": None
    }