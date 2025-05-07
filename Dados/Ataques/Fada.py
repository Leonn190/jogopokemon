from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa, coletor
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Brilho(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosPosi["Furtivo"] = 0

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

def Alv_Brilho(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = []
    for pokemon in inimigo.pokemons:
        if pokemon.efeitosPosi["Furtivo"] > 0:
            alvos.append(pokemon)

Brilho = {
    "nome": "Brilho",
    "tipo": ["fada"],   
    "custo": ["roxa","roxa"],
    "estilo": "E",
    "dano": 0.5,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ataca todos os pokemon com o efeito furtivo e remove esse efeito deles",
    "efeito": "MarcaBrilhosa",
    "extra": "MA",
    "alvos": Alv_Brilho,
    "funçao": Multi_Irregular,
    "irregularidade": F_Brilho
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
    "funçao": F_Bençao,
    "irregularidade": False
    }

def FF_Busca_Alegre(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    num = int(Escolha)
    if PokemonV is not None:
        PokemonV.curar(3*num,player,tela)
    else:
        PokemonS.curar(3*num,player,tela)
    
    for i in range(5-num):
        player.energias[coletor] += 1

def F_Busca_Alegre(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Busca_Alegre
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["1","2","3","4"]
    EstadoDaPergunta["estado"] = True

Busca_Alegre = {
    "nome": "Busca Alegre",
    "tipo": ["fada"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe 5 energias aleatorias, voce pode escolher descartar até 4 delas, para cada uma cure 3 de vida do pokemon visualizado ou de si mesmo",
    "efeito": "!None",
    "extra": "TV",
    "funçao": F_Busca_Alegre,
    "irregularidade": False
    }
