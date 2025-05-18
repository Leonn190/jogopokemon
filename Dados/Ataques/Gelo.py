from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Cristalizar(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    if AlvoS.efeitosNega["Encharcado"] > 0:
        AlvoS.efeitosNega["Congelado"] += AlvoS.efeitosNega["Encharcado"] + 1
        AlvoS.efeitosNega["Encharcado"] = 0

Cristalizar = {
    "nome": "Cristalizar",
    "tipo": ["gelo"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 30,
    "precisão": 100, 
    "descrição": "Se o pokemon inimigo estiver encharcado, ele perde esse efeito e ganha congelar por 1 turno a mais",
    "efeito": "FluxoAzul",
    "extra": "A",
    "funçao": F_Cristalizar,
    "irregularidade": False
    }

def FI_Reinado_de_Gelo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    contador = 0
    for pokemon in player.pokemons + inimigo.pokemons:
        if pokemon.efeitosNega["Congelado"] > 0:
            contador += 1
    Dano = Dano * (1 + 0.5 * contador)

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Reinado_de_Gelo = {
    "nome": "Reinado de Gelo",
    "tipo": ["gelo"],   
    "custo": ["normal","azul","azul"],
    "estilo": "E",
    "dano": 0.6,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% a mais de dano para cada pokemon congelado na partida",
    "efeito": "FacasAzuis",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Reinado_de_Gelo
    }

def FF_Magia_de_Gelo(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,Escolha):
    Valor = int(Escolha)
    PokemonV.curar(20,player,tela)
    PokemonV.efeitosPosi["Regeneração"] = Valor
    PokemonV.efeitosPosi["Congelado"] = Valor
    EstadoDaPergunta["estado"] = False

def F_Magia_de_Gelo(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Magia_de_Gelo
    EstadoDaPergunta["info"] = PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["2","3","4","5"]
    EstadoDaPergunta["estado"] = True

Magia_de_Gelo = {
    "nome": "Magia de Gelo",
    "tipo": ["gelo"],  
    "custo": ["normal","azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Cure 20 de vida do pokemon Visualizado e escolha quantos turnos ele vai ganhar o efeito regeneração e congelado",
    "efeito": "MagiaAzul",
    "efeito2": "MagiaAzul",
    "extra": "V",
    "funçao": F_Magia_de_Gelo,
    "irregularidade": False
    }

def FI_Raio_de_Gelo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 80:
        Alvo.efeitosNega["Congelado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Raio_de_Gelo = {
    "nome": "Raio de Gelo",
    "tipo": ["gelo"],   
    "custo": ["normal","azul","azul","azul","azul"],
    "estilo": "E",
    "dano": 1.95,
    "alcance": 18,
    "precisão": 99, 
    "descrição": "Lança um raio de gelo extremamente potente que tem 20% de chance de congelar o alvo por 3 turnos",
    "efeito": "RaioAzul",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Raio_de_Gelo
    }

def FI_Gelo_Verdadeiro(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Defesa = 0

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Gelo_Verdadeiro = {
    "nome": "Gelo Verdadeiro",
    "tipo": ["gelo"],   
    "custo": ["azul","azul"],
    "estilo": "N",
    "dano": 1.15,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque ignora a defesa do pokemon inimigo",
    "efeito": "MarcaAzul",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Gelo_Verdadeiro
    }

