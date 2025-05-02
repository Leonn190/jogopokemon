from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Pedregulho = {
    "nome": "Pedregulho",
    "tipo": ["pedra"],   
    "custo": ["laranja"],
    "estilo": "N",
    "dano": 0.9,
    "alcance": 30,
    "precisão": 90, 
    "descrição": "Lança um pedregulho no inimigo",
    "efeito": "Estouro",
    "extra": False,
    "funçao": Regular,
    "irregularidade": False
    }