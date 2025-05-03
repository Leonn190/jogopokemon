from Geradores.GeradorAtaques import Regular, Irregular
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

def F_Bola_Sombria(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)

    for inimigo in inimigos:
        inimigo.atacado(Dano/2,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_Sombria = {
    "nome": "Bola Sombria",
    "tipo": ["sombrio"],   
    "custo": ["preta","preta","preta"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "EstouroMagico",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Bola_Sombria
    }
