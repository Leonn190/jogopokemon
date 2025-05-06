from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Queimar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Queimado"] += 3

Queimar = {
    "nome": "Queimar",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 15,
    "precisão": 90, 
    "descrição": "Queime o pokemon inimigo por 3 turnos",
    "efeito": "Fogo",
    "extra": "A",
    "funçao": F_Queimar,
    "irregularidade": False
    }

def F_Bola_de_Fogo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)

    for inimigo in inimigos:
        inimigo.atacado(Dano/2,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_de_Fogo = {
    "nome": "Bola de Fogo",
    "tipo": ["fogo"],   
    "custo": ["vermelha","vermelha","vermelha"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "Fogo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Bola_de_Fogo
    }

def F_Superaquecer(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.efeitosNega["Queimado"] > 0:
        Alvo.efeitosNega["Queimado"] += 1
        Dano = Dano * 1.15
    if PokemonV in player.pokemons:
        PokemonV.efeitosNega["Congelado"] = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Superaquecer = {
    "nome": "Superaquecer",
    "tipo": ["fogo"],   
    "custo": ["vermelha","vermelha"],
    "estilo": "E",
    "dano": 0.5,
    "alcance": 20,
    "precisão": 99, 
    "descrição": "Caso o alvo ja esteja queimado, acrescente 1 contador no efeito e cause mais 15% de dano, selecione um pokemon aliado para remover o efeito congelado",
    "efeito": "Fogo",
    "efeito2": "Fogo",
    "extra": "AV",
    "funçao": Irregular,
    "irregularidade": F_Superaquecer
    }

def F_Brasa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Queimado"] += 2

Brasa = {
    "nome": "Brasa",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha"],
    "estilo": "E",
    "dano": 1.05,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque tem 10% de chance de deixar o alvo queimado por 2 turnos",
    "efeito": "Fogo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }
