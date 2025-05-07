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
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

Pedra_Especial = {
    "nome": "Pedra Especial",
    "tipo": ["pedra"],   
    "custo": ["normal","laranja"],
    "estilo": "N",
    "dano": 1.5,
    "alcance": 20,
    "precisão": 50, 
    "descrição": "Lança uma pedra especial no inimigo",
    "efeito": "ImpactoRochoso",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Barragem_Rochosa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.barreira += (PokemonS.Def + PokemonS.Def_sp) * 0.2

Barragem_Rochosa = {
    "nome": "Voar",
    "tipo": ["voador"],   
    "custo": ["cinza"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe 20% das somas das defesas como barreira",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Barragem_Rochosa,
    "irregularidade": False
    }

def F_Impacto_Rochoso(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano = PokemonS.Def * Ataque["dano"]
    PokemonS.efeitosNega["Quebrado"] = 2

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Impacto_Rochoso = {
    "nome": "Seda",
    "tipo": ["pedra"],   
    "custo": ["normal","laranja","laranja"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 5,
    "precisão": 100, 
    "descrição": "Esse ataque causa dano baseado apenas na Defesa, após esse ataque, esse pokemon fica quebrado por 2 turnos",
    "efeito": "ImpactoRochoso",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Impacto_Rochoso
    }

