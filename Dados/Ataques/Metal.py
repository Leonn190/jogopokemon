from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Reforçar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if PokemonV is not None:
        if PokemonV in player.pokemons:
            PokemonV.efeitosPosi["Reforçado"] += 3
            return
 
    PokemonS.efeitosPosi["Reforçado"] += 3

Reforçar = {
    "nome": "Reforçar",
    "tipo": ["metal"],   
    "custo": ["cinza"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe reforçado por 3 turnos, caso tenha um pokemon vizualisado aliado, ele que ganhará o efeito",
    "efeito": "Engrenagem",
    "extra": "TV",
    "funçao": F_Reforçar,
    "irregularidade": False
    }