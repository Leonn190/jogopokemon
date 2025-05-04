from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Brilho(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for pokemon in inimigo.pokemons:
        if pokemon.efeitosPosi["Furtivo"] > 0:
            pokemon.efeitosPosi["Furtivo"] = 0
            pokemon.atacado(10,player,inimigo,tela,Mapa)

Brilho = {
    "nome": "Brilho",
    "tipo": ["fada"],   
    "custo": ["normal","roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 15,
    "precisão": 80, 
    "descrição": "Remova o efeito furtivo de todos os inimigos que tiverem, quem tiver leva 10 de dano",
    "efeito": "MarcaBrilhosa",
    "extra": "A",
    "funçao": F_Brilho,
    "irregularidade": False
    }

Vento_Fada = {
    "nome": "Vento Fada",
    "tipo": ["fada"],   
    "custo": ["roxa","roxa"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Um vento fada ofensivo",
    "efeito": "FeixeMagenta",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Bençao(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonV.efeitosPosi["Abençoado"] += 3
    
Bençao = {
    "nome": "Benção",
    "tipo": ["fada"],   
    "custo": ["normal","roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Selecione um pokemon como vizualizado, ele será abençoado por 3 turnos",
    "efeito": "MarcaBrilhosa",
    "extra": "V",
    "funçao": F_Brilho,
    "irregularidade": False
    }
