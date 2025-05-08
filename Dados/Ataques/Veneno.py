from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Envenenar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Envenenado"] = 3

Envenenar = {
    "nome": "Envenenar",
    "tipo": ["venenoso"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 25,
    "precisão": 80, 
    "descrição": "deixe o pokemon inimigo envenenado por 3 turnos",
    "efeito": "GasRoxo",
    "extra": "A",
    "funçao": F_Envenenar,
    "irregularidade": False
    }

def F_Acido(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.8
    if random.choice([True,False]) == True:
        Alvo.Def_spB -= 1

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Acido = {
    "nome": "Acido",
    "tipo": ["venenoso"],   
    "custo": ["roxa","roxa"],
    "estilo": "E",
    "dano": 1,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque ignora 20% da defesa especial e tem 50% de chance de remover 1 de defesa especial permanente",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Acido
    }

def Alv_Bomba_de_Lodo(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 2, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def F_Bomba_de_Lodo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosNega["Envenenado"]
    if Alvo != AlvoS:
        Dano = Dano * 0.0

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bomba_de_Lodo = {
    "nome": "Bomba de Lodo",
    "tipo": ["venenoso"],   
    "custo": ["roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 0.95,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa envenenamento por 3 turnos aos pokemons inimigos adjacentes até 2 casas",
    "efeito": "Fogo",
    "alvos": Alv_Bomba_de_Lodo,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Bomba_de_Lodo
    }

def F_Extraçao(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.efeitosNega["Envenenado"] > 0:
        PokemonS.curar(14 * Alvo.efeitosNega["Envenenado"],player,tela)
        Alvo.efeitosNega["Envenenado"] = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Extraçao = {
    "nome": "Extração",
    "tipo": ["venenoso"],   
    "custo": ["normal","roxa"],
    "estilo": "N",
    "dano": 1.05,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Esse ataque remove o efeito envenenar do oponente, para cada turno restante no efeito, cure 14 de vida",
    "efeito": "Mordida",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Extraçao
    }
