from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def FI_Eletrolise_Hidrica(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if Alvo.efeitosNega["Encharcado"] > 0:
        Dano = Dano * 2.25

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Eletrolise_Hidrica = {
    "nome": "Eletrólise Hidrica",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela","amarela"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Se o alvo estiver encharcado esse ataque causará 125% a mais de dano",
    "efeito": "EnergiaAzul",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Eletrolise_Hidrica
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

def F_Onda_Eletrica(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    AlvoS.efeitosNega["Paralisado"] = 3

Onda_Eletrica = {
    "nome": "Onda Elétrica",
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

def FI_Choque_do_Trovao(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) <= 30:
        Alvo.efeitosNega["Paralisado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

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
    "funçao": Regular,
    "irregularidade": FI_Choque_do_Trovao
    }

def F_Energizar(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    if PokemonV is not None:
        if PokemonV in player.pokemons:
            PokemonV.efeitosPosi["Energizado"] += 2
            return
 
    PokemonS.efeitosPosi["Energizado"] += 2

Energizar = {
    "nome": "Energizar",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 99, 
    "descrição": "Ganhe energizado por 2 turnos ou caso exista um pokemon aliado vizualisado, ele que ganhará o efeito",
    "efeito": "Estouro",
    "efeito2": "Estouro",
    "extra": "TV",
    "funçao": F_Energizar,
    "irregularidade": None
    }

def Alv_Bola_Eletrica(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def FI_Bola_Eletrica(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Bola_Eletrica = {
    "nome": "Bola Elétrica",
    "tipo": ["eletrico"],   
    "custo": ["amarela","amarela","amarela"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "FacasBrancas",
    "alvos": Alv_Bola_Eletrica,
    "extra": "MAA",
    "funçao": Regular,
    "irregularidade": FI_Bola_Eletrica
    }

def Alv_Tempestade_de_Raios(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = []
    for pokemon in inimigo.pokemons:
        if pokemon.efeitosNega["Encharcado"] > 0:
            alvos.append(pokemon)
    return alvos

Tempestade_de_Raios = {
    "nome": "Tempestade de Raios",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela","amarela"],
    "estilo": "E",
    "dano": 1.45,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Esse ataque atinge todos os pokemon encharcados inimigos",
    "efeito": "MarcaAmarela",
    "extra": "MA",
    "alvos": Alv_Tempestade_de_Raios,
    "funçao": Regular,
    "irregularidade": False
    }
