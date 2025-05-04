from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Mordida = {
    "nome": "Mordida",
    "tipo": ["inseto"],   
    "custo": ["normal","verde"],
    "estilo": "N",
    "dano": 1.25,
    "alcance": 10,
    "precisão": 95, 
    "descrição": "Morda seu oponente com força",
    "efeito": "Mordida",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Seda(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.Varvel_perm > -11:
        Alvo.Varvel_perm -= 12

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Seda = {
    "nome": "Seda",
    "tipo": ["Inseto"],   
    "custo": ["verde"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 20,
    "precisão": 90, 
    "descrição": "Esse ataque diminue 12 de velocidade do oponente, caso ja tenha -12 de velocidade, não diminue mais",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Seda
    }

def F_Picada(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.choice([True,False]) == True:
        Alvo.efeitosNega["Envenenado"] += 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Picada = {
    "nome": "Picada",
    "tipo": ["Inseto"],   
    "custo": ["verde"],
    "estilo": "N",
    "dano": 0.8,
    "alcance": 15,
    "precisão": 90, 
    "descrição": "Esse ataque tem 50% de chance de deixar o oponente envenenado por 3 turnos",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Picada
    }
