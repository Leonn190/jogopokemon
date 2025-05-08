from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Cristalizar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if Alvo.efeitosNega["Encharcado"] > 0:
        Alvo.efeitosNega["Congelado"] += Alvo.efeitosNega["Encharcado"] + 1
        Alvo.efeitosNega["Encharcado"] = 0

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

def F_Reinado_de_Gelo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    contador = 0
    for pokemon in player.pokemons + inimigo.pokemons:
        if pokemon.efeitosNega["Congelado"] > 0:
            contador += 1
    Dano = Dano * (1 + 0.5 * contador)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

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
    "funçao": Irregular,
    "irregularidade": F_Reinado_de_Gelo
    }

def FF_Magia_de_Gelo(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    Valor = int(Escolha)
    PokemonV.curar(20,player,tela)
    PokemonV.efeitosPosi["Regeneração"] = Valor
    PokemonV.efeitosPosi["Congelado"] = Valor
    EstadoDaPergunta["estado"] = False

def F_Magia_de_Gelo(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Magia_de_Gelo
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["2","3","4","5"]
    EstadoDaPergunta["estado"] = True

Magia_de_Gelo = {
    "nome": "Magia de Gelo",
    "tipo": ["gelo"],  
    "custo": ["normal","azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Cure 20 de vida do pokemon Visualizado e escolha quantos turnos ele vai ganhar o efeito cura e congelado",
    "efeito": "MagiaAzul",
    "efeito2": "MagiaAzul",
    "extra": "V",
    "funçao": F_Magia_de_Gelo,
    "irregularidade": False
    }

def F_Raio_de_Gelo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 80:
        Alvo.efeitosNega["Congelado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

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
    "funçao": Irregular,
    "irregularidade": F_Raio_de_Gelo
    }

def F_Gelo_Verdadeiro(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Defesa = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

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
    "funçao": Irregular,
    "irregularidade": F_Raio_de_Gelo
    }

