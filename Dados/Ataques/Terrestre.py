from Geradores.GeradorAtaques import Regular, Irregular, Multi_Regular, Multi_Irregular
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

def Alv_Tremor(PokemonS,Alvo,player,inimigo,Mapa):
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

def Alv_Quebra_Chao(PokemonS,Alvo,player,inimigo,Mapa):
    if PokemonS.vel >= 30:
        aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,3,Mapa.Zona)
        return inimigos
    else:
        aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
        return inimigos

def F_Quebra_Chao(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano = Dano * PokemonS.Vida / 100
    PokemonS.atacado(Dano*0.15,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Quebra_Chão = {
    "nome": "Quebra Chão",
    "tipo": ["terrestre"],   
    "custo": ["amarela","amarela","amarela"],
    "estilo": "N",
    "dano": 0.7,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "A cada 1 de vida esse ataque causa mais 1% de dano, esse ataque atinge todos os inimigos ate 2 casas nos arredores e caso esse pokemon tenha mais de 30 de velocidade, atinge até 3 casas nos arredores. Esse ataque causa 15% do dano a si mesmo como perfuração",
    "efeito": "ImpactoRochoso",
    "extra": "MA",
    "alvos": Alv_Quebra_Chao,
    "funçao": Multi_Irregular,
    "irregularidade": F_Quebra_Chao
    }
