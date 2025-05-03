from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Confusão(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Queimado"] += 3

Confusão = {
    "nome": "Confusão",
    "tipo": ["psiquico"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 35,
    "precisão": 90, 
    "descrição": "Deixe o inimigo confuso por 3 turnos",
    "efeito": "FeixeRoxo",
    "extra": "A",
    "funçao": F_Confusão,
    "irregularidade": False
    }

def F_Bola_Psiquica(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)

    for inimigo in inimigos:
        inimigo.atacado(Dano/2,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_Psiquica = {
    "nome": "Bola Psiquica",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "ExplosaoRoxa",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Bola_Psiquica
    }
