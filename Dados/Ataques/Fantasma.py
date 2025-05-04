from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Assombrar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    efeitos_disponiveis = list(Alvo.efeitosNega.keys())
    if efeitos_disponiveis:
        efeito_escolhido = random.choice(efeitos_disponiveis)
        Alvo.efeitosNega[efeito_escolhido] += 2

Assombrar = {
    "nome": "Assombrar",
    "tipo": ["fantasma"],   
    "custo": ["preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 15,
    "precisão": 95, 
    "descrição": "Aplica um efeito negativo aleatorio por 2 turnos no alvo",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": F_Assombrar,
    "irregularidade": False
    }

def F_Lambida(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.Curar(Dano/10,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Lambida = {
    "nome": "Lambida",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Cure 10% do dano causado",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Lambida
    }
