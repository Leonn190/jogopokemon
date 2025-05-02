from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Mordida = {
    "nome": "Mordida",
    "tipo": ["inseto"],   
    "custo": ["normal","verde"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 10,
    "precisão": 95, 
    "descrição": "Morda seu oponente com força",
    "efeito": "Mordida",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }