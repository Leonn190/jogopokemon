from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
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