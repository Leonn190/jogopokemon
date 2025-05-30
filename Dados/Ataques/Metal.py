from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Reforçar(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    if PokemonV is not None:
        if PokemonV in player.pokemons:
            PokemonV.efeitosPosi["Reforçado"] = 3
            return
 
    PokemonS.efeitosPosi["Reforçado"] = 3

Reforçar = {
    "nome": "Reforçar",
    "tipo": ["metal"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe reforçado por 3 turnos, caso tenha um pokemon vizualisado aliado, ele que ganhará o efeito",
    "efeito": "Engrenagem",
    "efeito2": "Engrenagem",
    "extra": "TV",
    "funçao": F_Reforçar,
    "irregularidade": False
    }

def FI_Cauda_de_Ferro(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if random.choice([True,False]) == True:
        Alvo.Def_spB -= 1

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Cauda_de_Ferro = {
    "nome": "Cauda de Ferro",
    "tipo": ["metal"],   
    "custo": ["azul","azul"],
    "estilo": "N",
    "dano": 1.25,
    "alcance": 3,
    "precisão": 100, 
    "descrição": "Esse ataque tem 50% de chance de remover 1 de defesa normal permanente",
    "efeito": "Corte",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Cauda_de_Ferro
    }

Projetil_Metalico = {
    "nome": "Projétil Metálico",
    "tipo": ["metal"],   
    "custo": ["azul","azul"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 10,
    "precisão": 90, 
    "descrição": "Lança um projétil metalico intenso no oponente",
    "efeito": "Engrenagem",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Barragem(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    ganho = PokemonS.Atk_sp * 0.4
    if "metal" in PokemonS.tipo:
        ganho = ganho * 1.25
    PokemonS.barreira += ganho

Barragem = {
    "nome": "Barragem",
    "tipo": ["metal"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe barreira equivalente a 40% do dano especial, caso esse pokemon seja do tipo Metal, ganhe mais 25%",
    "efeito": "Engrenagem",
    "efeito2": "Engrenagem",
    "extra": None,
    "funçao": F_Barragem,
    "irregularidade": False
    }

def FI_Broca_Perfuradora(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.2

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Broca_Perfuradora = {
    "nome": "Broca Perfuradora",
    "tipo": ["metal"],   
    "custo": ["normal","azul","azul"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 1,
    "precisão": 100, 
    "descrição": "Esse ataque ignora 80% da armadura do Alvo",
    "efeito": "Corte",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Cauda_de_Ferro
    }
