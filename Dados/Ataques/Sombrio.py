from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Nas_Sombras(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Furtivo"] += 5

Nas_Sombras = {
    "nome": "Nas Sombras",
    "tipo": ["sombrio"],   
    "custo": ["preta","preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "entre nas sombras e ganhe o efeito furtivo por 5 turnos",
    "efeito": "ChuvaBrilhante",
    "extra": None,
    "funçao": F_Nas_Sombras,
    "irregularidade": False
    }

def Alv_Bola_Sombria(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def F_Bola_Sombria(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_Sombria = {
    "nome": "Bola_Sombria",
    "tipo": ["sombrio"],   
    "custo": ["preta","preta","preta"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "Fogo",
    "alvos": Alv_Bola_Sombria,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Bola_Sombria
    }

def F_Corte_Noturno(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    linhaS, colunaS = PokemonS.local["id"]
    linhaA, colunaA = Alvo.local["id"]

    if linhaS == linhaA + 1:
        Dano = Dano * 1.7

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Corte_Noturno = {
    "nome": "Corte Noturno",
    "tipo": ["Sombrio"],   
    "custo": ["normal","preta","preta"],
    "estilo": "N",
    "dano": 0.95,
    "alcance": 5,
    "precisão": 100, 
    "descrição": "Esse ataque causa 70% a mais de dano caso voce esteja atras do pokemon",
    "efeito": "CorteDourado",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Corte_Noturno
    }
