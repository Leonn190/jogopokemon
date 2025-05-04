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
    "extra": "A",
    "funçao": F_Envenenar,
    "irregularidade": False
    }

def F_Acido(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.8
    if random.choice([True,False]) == True:
        Alvo.Def_spB -= 1


    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Acido = {
    "nome": "Acido",
    "tipo": ["venenoso"],   
    "custo": ["roxa","roxa"],
    "estilo": "E",
    "dano": 1,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque ignora 20% da defesa especial e tem 50% de chance de remover 1 de defesa especial permanente",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Acido
    }