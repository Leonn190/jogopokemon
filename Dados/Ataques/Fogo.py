from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Queimar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Queimado"] += 3

Queimar = {
    "nome": "Queimar",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 20,
    "precisão": 90, 
    "descrição": "Queime o pokemon inimigo por 3 turnos",
    "efeito": "Fogo",
    "extra": "A",
    "funçao": F_Queimar,
    "irregularidade": False
    }

