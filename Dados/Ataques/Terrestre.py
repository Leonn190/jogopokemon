from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Arremesso_de_Terra = {
    "nome": "Arremesso de Terra",
    "tipo": ["terrestre"],   
    "custo": ["amarela"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 30,
    "precisão": 65, 
    "descrição": "Lança terra ofensiva com força no oponente",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }