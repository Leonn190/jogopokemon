from Geradores.GeradorAtaques import Regular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores, distancia_entre_pokemons
import random

def F_Queimar(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    AlvoS.efeitosNega["Queimado"] = 3

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

def Alv_Bola_de_Fogo(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def FI_Bola_de_Fogo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

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
    "alvos": Alv_Bola_de_Fogo,
    "extra": "MAA",
    "funçao": Regular,
    "irregularidade": FI_Bola_de_Fogo
    }

def FI_Superaquecer(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.efeitosNega["Queimado"] > 0:
        Alvo.efeitosNega["Queimado"] += 1
        Dano = Dano * 1.15
    if PokemonV in player.pokemons:
        PokemonV.efeitosNega["Congelado"] = 0
        PokemonV.efeitosNega["Encharcado"] = 0

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Superaquecer = {
    "nome": "Superaquecer",
    "tipo": ["fogo"],   
    "custo": ["vermelha","vermelha"],
    "estilo": "E",
    "dano": 0.5,
    "alcance": 20,
    "precisão": 99, 
    "descrição": "Caso o alvo ja esteja queimado, acrescente 1 contador no efeito e cause mais 15% de dano, selecione um pokemon aliado para remover o efeito congelado e encharcado",
    "efeito": "Fogo",
    "efeito2": "Fogo",
    "extra": "AV",
    "funçao": Regular,
    "irregularidade": FI_Superaquecer
    }

def FI_Brasa(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 85:
        Alvo.efeitosNega["Queimado"] += 2
    
    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Brasa = {
    "nome": "Brasa",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha"],
    "estilo": "E",
    "dano": 1.05,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque tem 15% de chance de deixar o alvo queimado por 2 turnos",
    "efeito": "Fogo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Brasa
    }

def F_Ondas_de_Calor(PokemonS,PokemonV,Alvo,Alvos,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for alvo in Alvos:
        alvo.efeitosNega["Queimado"] = 4

def Alv_Ondas_de_Calor(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = []
    for pokemon in inimigo.pokemons:
        dist = distancia_entre_pokemons(pokemon,PokemonS,Mapa.Metros)
        if random.randint(0,100) > dist + 5:
            alvos.append(pokemon)
    return alvos

Ondas_de_Calor = {
    "nome": "Ondas de Calor",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha","vermelha"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "qaunto mais perto os inimigos estiverem desse pokemon, mais chance eles tem de serem atingidos, todos os atingidos ficam queimados por 4 turnos",
    "efeito": "Fogo",
    "extra": "MA",
    "alvos": Alv_Ondas_de_Calor,
    "funçao": F_Ondas_de_Calor,
    "irregularidade": False
    }

def FI_Raio_de_Fogo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosNega["Congelado"] = 0
    Alvo.efeitosNega["Encharcado"] = 0
    
    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Raio_de_Fogo = {
    "nome": "Raio de Fogo",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha","vermelha","vermelha","vermelha"],
    "estilo": "E",
    "dano": 1.9,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Lança um raio de calor concentrado extremo que remove o efeito congelado e encharcado do oponente",
    "efeito": "LabaredaMultipla",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Raio_de_Fogo
    }

Ataque_de_Chamas = {
    "nome": "Ataque de Chamas",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 10,
    "precisão": 95, 
    "descrição": "Uma manobra poderosa onde se utiliza fogo",
    "efeito": "Fogo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def FI_Laser_Incandescente(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosNega["Congelado"] = 0
    Alvo.efeitosNega["Encharcado"] = 0
    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Laser_Incandescente = {
    "nome": "Laser Incandescente",
    "tipo": ["fogo"],   
    "custo": ["vermelha","vermelha","vermelha","vermelha","vermelha"],
    "estilo": "E",
    "dano": 2,
    "alcance": 28,
    "precisão": 100, 
    "descrição": "Lança um laser de calor concentrado extremo que remove o efeito congelado e encharcado do oponente",
    "efeito": "LabaredaMultipla",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Laser_Incandescente
    }
