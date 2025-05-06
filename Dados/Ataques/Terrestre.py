from Geradores.GeradorAtaques import Regular, Irregular, Multi_Regular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
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

def Alv_Tremor(PokemonS,player,inimigo,Mapa):
    aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
    return inimigos  

Tremor = {
    "nome": "Tremor",
    "tipo": ["terrestre"],   
    "custo": ["amarela","amarela"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Atinge todos os inimigos que estiverem até 2 casas adjacentes, não precisa de alvo",
    "efeito": "ExplosaoPedra",
    "extra": "MA",
    "alvos": Alv_Tremor,
    "funçao": Multi_Regular,
    "irregularidade": False
    }
