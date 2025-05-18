from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

Arremesso_de_Terra = {
    "nome": "Arremesso de Terra",
    "tipo": ["terrestre"],   
    "custo": ["amarela"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 30,
    "precisão": 65, 
    "descrição": "Lança terra ofensiva com força no oponente",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def Alv_Tremor(PokemonS,Alvo,player,inimigo,Mapa):

    aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
    return inimigos  

Tremor = {
    "nome": "Tremor",
    "tipo": ["terrestre"],   
    "custo": ["amarela","amarela"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Atinge todos os inimigos que estiverem até 2 casas adjacentes, não precisa de alvo",
    "efeito": "ExplosaoPedra",
    "extra": "MA",
    "alvos": Alv_Tremor,
    "funçao": Regular,
    "irregularidade": False
    }

def Alv_Quebra_Chao(PokemonS,Alvo,player,inimigo,Mapa):
    if PokemonS.vel >= 30:
        aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,3,Mapa.Zona)
        return inimigos
    else:
        aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
        return inimigos

def FI_Quebra_Chao(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Dano = Dano * PokemonS.Vida / 100
    PokemonS.atacado(Dano*0.15,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Quebra_Chao = {
    "nome": "Quebra Chão",
    "tipo": ["terrestre"],   
    "custo": ["amarela","amarela","amarela"],
    "estilo": "N",
    "dano": 0.7,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "A cada 1 de vida esse ataque causa mais 1% de dano, esse ataque atinge todos os inimigos ate 2 casas nos arredores e caso esse pokemon tenha mais de 30 de velocidade, atinge até 3 casas nos arredores. Esse ataque causa 15% do dano a si mesmo como perfuração",
    "efeito": "ImpactoRochoso",
    "extra": "MA",
    "alvos": Alv_Quebra_Chao,
    "funçao": Regular,
    "irregularidade": FI_Quebra_Chao
    }

def F_Afinidade_Territorial(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Velocista"] = 3
    aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
    if inimigos == []:
        PokemonS.atacou = False

Afinidade_Territorial = {
    "nome": "Afinidade Territorial",
    "tipo": ["terrestre"],   
    "custo": ["amarela"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe o efeito velocista por 3 turnos, se não tiver nenhum inimigo até 2 casas adjacentes esse pokemon poderá atacar novamente",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Afinidade_Territorial,
    "irregularidade": False
    }

Osso_Veloz = {
    "nome": "Osso Veloz",
    "tipo": ["terrestre"],   
    "custo": ["amarela","amarela","amarela"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 55,
    "precisão": 75, 
    "descrição": "Lança um osso ofensivo com força no oponente, podendo viajar por muitos metros",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def FI_Golpe_Territorial(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if PokemonS.efeitosPosi["Provocando"] > 0:
        Dano = Dano * 1.2
        if Alvo.efeitosPosi["Provocando"] > 0:
            Dano = Dano * 1.1
            Alvo.efeitosPosi["Provocando"] = 0

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Golpe_Territorial = {
    "nome": "Golpe Territorial",
    "tipo": ["terrestre"],   
    "custo": ["normal","amarela","amarela"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Se esse pokemon estiver com o efeito provocando, esse ataque causará mais 20% de dano e caso o alvo também esteja provocando, esse golpe causa ainda mais 10% e remove o efeito de provocando do alvo",
    "efeito": "ExplosaoPedra",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Golpe_Territorial
    }

def Alv_Tremorr(PokemonS,Alvo,player,inimigo,Mapa):
    return inimigo.pokemons

Terremoto = {
    "nome": "Terremoto",
    "tipo": ["terrestre"],   
    "custo": ["normal","amarela","amarela","amarela","amarela"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Esse ataque atinge todos os pokemon inimigos",
    "efeito": "ExplosaoPedra",
    "extra": "MA",
    "alvos": Alv_Tremorr,
    "funçao": Regular,
    "irregularidade": False
    }
