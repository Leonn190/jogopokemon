from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Jato_de_Agua = {
    "nome": "Jato De Agua",
    "tipo": ["agua"],   
    "custo": ["normal","azul"],
    "estilo": "E",
    "dano": 1,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Lança um jato de agua intenso no oponente",
    "efeito": "EspiralAzul",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Jato_Duplo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Aumento = random.choice([True,False])

    if Aumento is True:
        Dano = Dano * 1.5
        Alvo.efeitosNega["Encharcado"] += 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Jato_Duplo = {
    "nome": "Jato Duplo",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 20,
    "precisão": 95, 
    "descrição": "Esse ataque tem 50% de chance de causar mais 50% de dano e deixar o oponente encharcado por 3 turnos",
    "efeito": "EspiralAzul",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Jato_Duplo
    }

def F_Bolhas(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    try:
        Dano = Dano * (1 + PokemonS.bolhas/6,6)
    except AttributeError:
        PokemonS.bolhas = 0
    
    PokemonS.bolhas += 1

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bolhas = {
    "nome": "Bolhas",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "N",
    "dano": 0.3,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Esse ataque causa mais 15% de dano por cada vez que o pokemon oponente foi atingido pelo ataque Bolhas",
    "efeito": "Agua",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Bolhas
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
        Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Controle_do_Oceano(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
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
    "extra": "A",
    "funçao": F_Controle_do_Oceano,
    "irregularidade": False
    }

Splash = {
    "nome": "Splash",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "N",
    "dano": 0.5,
    "alcance": 15,
    "precisão": 50, 
    "descrição": "A precisão do ataque é 50% pois esse ataque tem 50% de chance de não fazer nada",
    "efeito": "Agua",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Vasculhar_no_Rio(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Vezes = random.choice([1,2])
    for i in range(Vezes):
        player.inventario.append(caixa())

Vasculhar_no_Rio = {
    "nome": "Vasculhar no Rio",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 150,
    "precisão": 100, 
    "descrição": "Vasculhe até 2 itens no rio",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Vasculhar_no_Rio,
    "irregularidade": False
    }

def F_Golpe_de_Concha(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano += PokemonS.Def * Ataque["dano"]
    PokemonS.efeitosPosi["Reforçado"] = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Golpe_de_Concha = {
    "nome": "Golpe de Concha",
    "tipo": ["agua"],   
    "custo": ["normal","normal","azul"],
    "estilo": "N",
    "dano": 0.6,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Esse ataque causa dano baseado em defesa e em ataque, após esse ataque o pokemon perde o efeito reforçado caso tenha",
    "efeito": "HexagonoLaminas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Golpe_de_Concha
    }

def F_Gota_Pesada(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Encharcado"] += 4

Gota_Pesada = {
    "nome": "Gota Pesada",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 25,
    "precisão": 95, 
    "descrição": "Esse ataque deixa o oponente encharcado por 4 turnos mas sem dar dano nele",
    "efeito": "Agua",
    "extra": "A",
    "funçao": F_Gota_Pesada,
    "irregularidade": False
    }