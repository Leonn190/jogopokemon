from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Confusão(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Queimado"] += 3

Confusão = {
    "nome": "Confusão",
    "tipo": ["psiquico"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 35,
    "precisão": 90, 
    "descrição": "Deixe o inimigo confuso por 3 turnos",
    "efeito": "FeixeRoxo",
    "extra": "A",
    "funçao": F_Confusão,
    "irregularidade": False
    }

def F_Bola_Psiquica(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)

    for inimigo in inimigos:
        inimigo.atacado(Dano/2,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_Psiquica = {
    "nome": "Bola Psiquica",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "ExplosaoRoxa",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Bola_Psiquica
    }

def F_Teleporte(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    linhaA, colunaA = Alvo.local["id"]
    linhaS, colunaS = PokemonS.local["id"]
    
    Move(PokemonS,linhaA,colunaA,Mapa.Zona)
    Move(Alvo,linhaS,colunaS,Mapa.Zona)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Teleporte = {
    "nome": "Teleporte",
    "tipo": ["psiquico"],   
    "custo": ["roxa"],
    "estilo": "E",
    "dano": 0.4,
    "alcance": 45,
    "precisão": 100, 
    "descrição": "Troque de lugar com o alvo",
    "efeito": "FeixeMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Teleporte
    }

def F_Ampliação_Mental(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    for efeito in PokemonS.efeitosNega:
        if PokemonS.efeitosNega[efeito] >= 1:
            PokemonS.efeitosNega[efeito] += 1

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Ampliação_Mental = {
    "nome": "Ampliação Mental",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa"],
    "estilo": "E",
    "dano": 0.85,
    "alcance": 15,
    "precisão": 90, 
    "descrição": "Aumente 1 de todos os contadores de efeitos negativos do pokemon atingido",
    "efeito": "FeixeRoxo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Ampliação_Mental
    }

def F_Psiquico_Desgastante(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.efeitosNega["Incapacitado"] += 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Psiquico_Desgastante = {
    "nome": "Psiquico Desgastante",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa"],
    "estilo": "E",
    "dano": 1.45,
    "alcance": 20,
    "precisão": 85, 
    "descrição": "Esse pokemon agora está incapacitado por 3 turnos",
    "efeito": "CorteRicocheteadoRoxo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Psiquico_Desgastante
    }

