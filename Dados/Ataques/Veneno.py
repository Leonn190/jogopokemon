from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Envenenar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Envenenado"] += 3

Envenenar = {
    "nome": "Envenenar",
    "tipo": ["venenoso"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 25,
    "precisão": 80, 
    "descrição": "deixe o pokemon inimigo envenenado por 3 turnos",
    "efeito": "GasRoxo",
    "extra": None,
    "funçao": F_Envenenar,
    "irregularidade": False
    }