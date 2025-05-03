from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Tapa = {
    "nome": "Tapa",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "N",
    "dano": 0.8,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Um Tapa ofensivo no pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

Cabeçada = {
    "nome": "Cabeçada",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "N",
    "dano": 1.0,
    "alcance": 5,
    "precisão": 90, 
    "descrição": "Uma cabeçada ofensiva no pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Investida(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.Vida -= 10

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Investida = {
    "nome": "Investida",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 5,
    "precisão": 85, 
    "descrição": "Esse ataque causa 10 de dano a si mesmo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Investida
    }

def F_Vasculhar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    player.inventario.append(caixa())

Vasculhar = {
    "nome": "Vasculhar",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 150,
    "precisão": 100, 
    "descrição": "Vasculhe e ganhe 1 item aleatório",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Vasculhar,
    "irregularidade": False
    }

def F_Ataque_Rapido(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    
    if random.choice([True,False]) == True:
        PokemonS.Atacou = False

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Ataque_Rapido = {
    "nome": "Bola Eletrica",
    "tipo": ["normal"],   
    "custo": ["normal","normal"],
    "estilo": "N",
    "dano": 1,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Tem 50% de chance desse ataque não constar como um ataque e esse pokemon poder atacar novamente",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Ataque_Rapido
    }