from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Nas_Sombras(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Furtivo"] = 5

Nas_Sombras = {
    "nome": "Nas Sombras",
    "tipo": ["sombrio"],   
    "custo": ["preta","preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "entre nas sombras e ganhe o efeito furtivo por 5 turnos",
    "efeito": "ChuvaBrilhante",
    "extra": None,
    "funçao": F_Nas_Sombras,
    "irregularidade": False
    }

def Alv_Bola_Sombria(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 3, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def FI_Bola_Sombria(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Bola_Sombria = {
    "nome": "Bola Sombria",
    "tipo": ["sombrio"],   
    "custo": ["preta","preta","preta"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 7,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "ChuvaBrilhante",
    "alvos": Alv_Bola_Sombria,
    "extra": "MAA",
    "funçao": Regular,
    "irregularidade": FI_Bola_Sombria
    }

def FI_Corte_Noturno(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    linhaS, colunaS = PokemonS.local["id"]
    linhaA, colunaA = Alvo.local["id"]

    if linhaS == linhaA - 1:
        Dano = Dano * 1.7

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Corte_Noturno = {
    "nome": "Corte Noturno",
    "tipo": ["sombrio"],   
    "custo": ["normal","preta","preta"],
    "estilo": "N",
    "dano": 0.95,
    "alcance": 1,
    "precisão": 100, 
    "descrição": "Esse ataque causa 70% a mais de dano caso voce esteja atras do pokemon",
    "efeito": "CorteDourado",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Corte_Noturno
    }

def FI_Confronto_Trevoso(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    PokemonS.efeitosPosi["Provocando"] = 3
    Alvo.efeitosPosi["Provocando"] = 3

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Confronto_Trevoso = {
    "nome": "Confronto Trevoso",
    "tipo": ["sombrio"],   
    "custo": ["normal","preta","preta"],
    "estilo": "N",
    "dano": 1.05,
    "alcance": 7,
    "precisão": 100, 
    "descrição": "Deixe a si mesmo e o alvo provocando por 3 turnos",
    "efeito": "RedemoinhoCosmico",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Confronto_Trevoso
    }
