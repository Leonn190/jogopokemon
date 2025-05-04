from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Dreno(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.curar(15,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Dreno = {
    "nome": "Dreno",
    "tipo": ["planta"],   
    "custo": ["normal","verde"],
    "estilo": "E",
    "dano": 0.8,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque cura 15 de vida de si mesmo",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Dreno
    }

def F_Chicote_de_Vinha(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 40:
        Dano = Dano * 1.2

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Chicote_de_Vinha = {
    "nome": "Dreno",
    "tipo": ["planta"],   
    "custo": ["verde","verde"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 25,
    "precisão": 75, 
    "descrição": "Esse ataque tem 60% de chance de causar mais 20% de dano",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Chicote_de_Vinha
    }

Disparo_de_Semente = {
    "nome": "Disparo de Semente",
    "tipo": ["planta"],   
    "custo": ["normal","verde"],
    "estilo": "N",
    "dano": 0.9,
    "alcance": 38,
    "precisão": 100, 
    "descrição": "Lança um jato de agua intenso no oponente",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Cura_Natural(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if PokemonV is not None:
        if PokemonV in player.pokemons:
            PokemonV.efeitosPosi["Regeneração"] += 3
            return
 
    PokemonS.efeitosPosi["Regeneração"] += 3

Cura_Natural = {
    "nome": "Cura Natural",
    "tipo": ["planta"],   
    "custo": ["verde"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe regeneração por 3 turnos, caso tenha um pokemon vizualisado aliado, ele que ganhará o efeito",
    "efeito": "ExplosaoVerde",
    "extra": "TV",
    "funçao": F_Cura_Natural,
    "irregularidade": False
    }

Raio_Solar = {
    "nome": "Raio Solar",
    "tipo": ["planta"],   
    "custo": ["normal","normal","verde","verde","verde"],
    "estilo": "E",
    "dano": 1.8,
    "alcance": 30,
    "precisão": 100, 
    "descrição": "Lança um jato de agua intenso no oponente",
    "efeito": "BarreiraCelular",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }
