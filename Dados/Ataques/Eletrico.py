from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Eletrolise_Hidrica(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.efeitosNega["Encharcado"] > 0:
        Dano = Dano * 2

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Eletrolise_Hidrica = {
    "nome": "Eletrolise_Hidrica",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela","azul"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Se o alvo estiver encharcado esse ataque causará 2 vezes o dano",
    "efeito": "EnergiaAzul",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Eletrolise_Hidrica
    }

Faisca = {
    "nome": "Faisca",
    "tipo": ["eletrico"],   
    "custo": ["amarela"],
    "estilo": "N",
    "dano": 1,
    "alcance": 10,
    "precisão": 125, 
    "descrição": "Uma faisca certeira no oponente",
    "efeito": "RajadaAmarela",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Onda_Eletrica(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Paralisado"] += 3

Onda_Eletrica = {
    "nome": "Onda Eletrica",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 36,
    "precisão": 100, 
    "descrição": "Deixe o alvo paralisado por 3 turnos",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": F_Onda_Eletrica,
    "irregularidade": None
    }

def F_Choque_do_Trovao(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 70:
        Alvo.efeitosNega["Paralisado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Choque_do_Trovao = {
    "nome": "Choque do Trovão",
    "tipo": ["eletrico"],   
    "custo": ["amarela","amarela","amarela","amarela"],
    "estilo": "E",
    "dano": 1.6,
    "alcance": 32,
    "precisão": 99, 
    "descrição": "Um grande raio que tem 30% de chance de paralisar o alvo por 3 turnos",
    "efeito": "SuperDescarga",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Choque_do_Trovao
    }

def F_Energizar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if PokemonV is not None:
        if PokemonV in player.pokemons:
            PokemonV.efeitosPosi["Energizado"] += 3
            return
 
    PokemonS.efeitosPosi["Energizado"] += 3

Energizar = {
    "nome": "Energizar",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 99, 
    "descrição": "Ganhe energizado por 3 turnos ou caso exista um pokemon aliado vizualisado, ele que ganhará o efeito",
    "efeito": "Estouro",
    "extra": "TV",
    "funçao": F_Energizar,
    "irregularidade": None
    }

def F_Bola_Eletrica(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)

    for inimigo in inimigos:
        inimigo.atacado(Dano/2,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_Eletrica = {
    "nome": "Bola Eletrica",
    "tipo": ["eletrico"],   
    "custo": ["amarela","amarela","amarela"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Bola_Eletrica
    }