from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def FI_Dreno(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    PokemonS.curar(15,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Dreno = {
    "nome": "Dreno",
    "tipo": ["planta"],   
    "custo": ["normal","verde"],
    "estilo": "E",
    "dano": 0.8,
    "alcance": 4,
    "precisão": 100, 
    "descrição": "Esse ataque cura 15 de vida de si mesmo",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Dreno
    }

def FI_Chicote_de_Vinha(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 40:
        Dano = Dano * 1.2

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Chicote_de_Vinha = {
    "nome": "Chicote de Vinha",
    "tipo": ["planta"],   
    "custo": ["verde","verde"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 6,
    "precisão": 75, 
    "descrição": "Esse ataque tem 60% de chance de causar mais 20% de dano",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Chicote_de_Vinha
    }

Disparo_de_Semente = {
    "nome": "Disparo de Semente",
    "tipo": ["planta"],   
    "custo": ["normal","verde"],
    "estilo": "N",
    "dano": 0.9,
    "alcance": 11,
    "precisão": 100, 
    "descrição": "Lança um jato de agua intenso no oponente",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Cura_Natural(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
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
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe regeneração por 3 turnos, caso tenha um pokemon visualizado aliado, ele que ganhará o efeito",
    "efeito": "DomoVerde",
    "efeito2": "DomoVerde",
    "extra": "TV",
    "funçao": F_Cura_Natural,
    "irregularidade": False
    }

Raio_Solar = {
    "nome": "Raio Solar",
    "tipo": ["planta"],   
    "custo": ["normal","verde","verde","verde","verde"],
    "estilo": "E",
    "dano": 1.8,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Lança um raio canalisado pelo sol",
    "efeito": "BarreiraCelular",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def Alv_Dança_das_Petalas(PokemonS,Alvo,player,inimigo,Mapa):
    aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
    return aliados + [PokemonS]

def F_Dança_das_Petalas(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    for alvo in Alvos:
        cura = (alvo.VidaMax - alvo.Vida) * 0.15
        alvo.curar(cura,player,tela)
        alvo.efeitosPosi["Velocista"] = 3

Dança_das_Petalas = {
    "nome": "Dança das Pétalas",
    "tipo": ["planta"],   
    "custo": ["normal","verde","verde"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Num raio de 2 casas adjacentes, cure 15% da vida perdida dos aliados e deixe eles com o efeito velocista",
    "efeito": "DomoVerde",
    "extra": "MA",
    "alvos": Alv_Dança_das_Petalas,
    "funçao": F_Dança_das_Petalas,
    "irregularidade": None
    }

def FI_Mega_Dreno(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    PokemonS.curar(PokemonS.Atk_sp * 0.45,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Mega_Dreno = {
    "nome": "Mega Dreno",
    "tipo": ["planta"],   
    "custo": ["verde","verde","verde"],
    "estilo": "N",
    "dano": 1.15,
    "alcance": 5,
    "precisão": 100, 
    "descrição": "Esse ataque cura 45% do seu dano especial",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Mega_Dreno
    }

Folha_Navalha = {
    "nome": "Folha Navalha",
    "tipo": ["planta"],   
    "custo": ["normal","verde","verde"],
    "estilo": "N",
    "dano": 1.5,
    "alcance": 7,
    "precisão": 90, 
    "descrição": "Uma folha capaz de cortar como uma navalha, atirada no alvo",
    "efeito": "DomoVerde",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def Alv_Morteiro_de_Polem(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def FI_Morteiro_de_Polem(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Morteiro_de_Polem = {
    "nome": "Morteiro de Pólem",
    "tipo": ["planta"],   
    "custo": ["verde","verde","verde","verde","verde"],
    "estilo": "E",
    "dano": 1.45,
    "alcance": 16,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "Explosao",
    "alvos": Alv_Morteiro_de_Polem,
    "extra": "MAA",
    "funçao": Regular,
    "irregularidade": FI_Morteiro_de_Polem
    }
