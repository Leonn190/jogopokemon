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
    return alvos

Brilho = {
    "nome": "Brilho",
    "tipo": ["fada"],   
    "custo": ["normal","roxa"],
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
    PokemonV.efeitosPosi["Abençoado"] = 3
    
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
        PokemonV.curar(4*num,player,tela)
    else:
        PokemonS.curar(4*num,player,tela)
    
    for i in range(5-num):
        player.energias[coletor()] += 1
    EstadoDaPergunta["estado"] = False

def F_Busca_Alegre(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Busca_Alegre
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["0","1","2","3"]
    EstadoDaPergunta["estado"] = True

Busca_Alegre = {
    "nome": "Busca Alegre",
    "tipo": ["fada"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe 5 energias aleatorias, voce pode escolher descartar até 3 delas, para cada uma cure 4 de vida do pokemon visualizado ou de si mesmo",
    "efeito": "!None",
    "extra": "TV",
    "funçao": F_Busca_Alegre,
    "irregularidade": False
    }

def F_Tapa_das_Fadas(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    contador = 0
    for efeito in Alvo.efeitosPosi:
        if Alvo.efeitosPosi[efeito] > 1:
            contador += 1
    Dano = Dano * (1 + 0.3 * contador)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Tapa_das_Fadas = {
    "nome": "Tapa das Fadas",
    "tipo": ["agua"],   
    "custo": ["normal","roxa","roxa"],
    "estilo": "N",
    "dano": 0.95,
    "alcance": 5,
    "precisão": 100, 
    "descrição": "Esse ataque causa 30% de dano a mais para cada efeito positivo que o alvo tiver",
    "efeito": "FacasRosas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Tapa_das_Fadas
    }

def F_Constelaçao_Magica(PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for alvo in Alvo:
        alvo.efeitosPosi["Furtivo"] = 3

def Alv_Constelaçao_Magica(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = []
    for pokemon in player.pokemons:
        if pokemon != PokemonS:
            alvos.append(pokemon)
    return alvos

Constelaçao_Magica = {
    "nome": "Constelação Mágica",
    "tipo": ["fada"],   
    "custo": ["roxa","roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Deixa todos os pokemon aliados menos a si mesmo em modo furtivo por 3 turnos",
    "efeito": "Fumaça",
    "extra": "MA",
    "alvos": Alv_Constelaçao_Magica,
    "funçao": F_Constelaçao_Magica,
    "irregularidade": False
    }

def Alv_Explosao_Lunar(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = [Alvo]
    for pokemon in inimigo.pokemons:
        if abs(pokemon.pos - Alvo.pos) == 1:
            alvos.append(pokemon)

    return alvos

def F_Explosao_Lunar(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.4

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Explosao_Lunar = {
    "nome": "Explosão Lunar",
    "tipo": ["agua"],   
    "custo": ["normal","roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.4,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque causa 40% do dano original aos pokemons nas duas posiçoes adjacentes",
    "efeito": "CorteRosa",
    "alvos": Alv_Explosao_Lunar,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Explosao_Lunar
    }
