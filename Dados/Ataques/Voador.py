from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Voar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosNega["Voando"] += 3

Voar = {
    "nome": "Voar",
    "tipo": ["voador"],   
    "custo": ["cinza"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "voe e ganhe o efeito voando por 3 turnos",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Voar,
    "irregularidade": False
    }