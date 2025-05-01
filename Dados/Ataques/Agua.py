from Geradores.GeradorAtaques import padrao
from Jogo.Tabuleiro import Move
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Jato_de_Agua = {
    "nome": "Jato De Agua",
    "tipo": ["agua"],   
    "custo": ["normal","azul"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Lança um jato de agua intenso no oponente",
    "efeito": "EspiralAzul",
    "extra": False,
    "funçao": padrao
    }

def F_Jato_Duplo(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    Aumento = random.choice([True,False])

    if Aumento is True:
        Dano = Dano * 1.5
        Alvo.efeitosNega["Encharcado"] = 3

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    Alvo.atacado(DanoF,player,inimigo,tela)

Jato_Duplo = {
    "nome": "Jato Duplo",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul"],
    "estilo": "E",
    "dano": 1.0,
    "alcance": 20,
    "precisão": 95, 
    "descrição": "Esse ataque tem 50% de chance de causar mais 50% de dano e deixar o oponente encharcado por 3 turnos",
    "efeito": "RedemoinhoAzul",
    "extra": None,
    "funçao": F_Jato_Duplo
    }

def F_Bolhas(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    try:
        Dano = Dano * (1 + PokemonS.bolhas/10)
    except AttributeError:
        PokemonS.bolhas = 0
    
    PokemonS.bolhas += 1

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    Alvo.atacado(DanoF,player,inimigo,tela)

Bolhas = {
    "nome": "Bolhas",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "N",
    "dano": 0.3,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Esse ataque causa mais 10% de dano por cada vez que o pokemon oponente foi atingido pelo ataque Bolhas",
    "efeito": "Agua",
    "extra": None,
    "funçao": F_Bolhas
    }

def FF_Controle_do_Oceano(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
        
        linhaA, colunaA = Alvo.local["id"]

        if Escolha == "Norte":
            Move(Alvo,linhaA-2,colunaA,Mapa.Zona)
        elif Escolha == "Sul":
            Move(Alvo,linhaA+2,colunaA,Mapa.Zona)
        elif Escolha == "Leste":
            Move(Alvo,linhaA,colunaA+2,Mapa.Zona)
        elif Escolha == "Oeste":
            Move(Alvo,linhaA,colunaA-2,Mapa.Zona)

        Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

        EstadoDaPergunta["estado"] = False
        Alvo.atacado(DanoF,player,inimigo,tela)

def F_Controle_do_Oceano(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    
    EstadoDaPergunta["funçao"] = FF_Controle_do_Oceano
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Norte","Sul","Leste","Oeste"]
    EstadoDaPergunta["estado"] = True

Controle_do_Oceano = {
    "nome": "Controle do Oceano",
    "tipo": ["agua"],   
    "custo": ["normal","normal","azul","azul"],
    "estilo": "E",
    "dano": 0.7,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Escolha para qual direçao irá mover o pokemon inimigo em 2 posições",
    "efeito": "TornadoAgua",
    "extra": None,
    "funçao": F_Controle_do_Oceano
    }