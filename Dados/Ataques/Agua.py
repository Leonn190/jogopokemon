from Geradores.GeradorAtaques import Regular
from Jogo.Tabuleiro import Move, GuardarPosicionar
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
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

def FI_Jato_Duplo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Aumento = random.choice([True,False])

    if Aumento is True:
        Dano = Dano * 1.5
        Alvo.efeitosNega["Encharcado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

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
    "funçao": Regular,
    "irregularidade": FI_Jato_Duplo
    }

def FI_Bolhas(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    try:
        Dano = Dano * (1 + PokemonS.bolhas/5)
    except AttributeError:
        PokemonS.bolhas = 0
    
    PokemonS.bolhas += 1

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Bolhas = {
    "nome": "Bolhas",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "N",
    "dano": 0.3,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Esse ataque causa mais 20% de dano por cada vez que o pokemon oponente foi atingido pelo ataque Bolhas",
    "efeito": "Agua",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Bolhas
    }

def FF_Controle_do_Oceano(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,Escolha):
        
        linhaA, colunaA = AlvoS.local["id"]

        if Escolha == "Norte":
            Move(AlvoS,linhaA-2,colunaA,Mapa.Zona)
        elif Escolha == "Sul":
            Move(AlvoS,linhaA+2,colunaA,Mapa.Zona)
        elif Escolha == "Leste":
            Move(AlvoS,linhaA,colunaA+2,Mapa.Zona)
        elif Escolha == "Oeste":
            Move(AlvoS,linhaA,colunaA-2,Mapa.Zona)

        Dano, Defesa = VEstilo(PokemonS,AlvoS,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],AlvoS.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,AlvoS,player,inimigo,DanoF,Ataque["estilo"],tela)

        EstadoDaPergunta["estado"] = False
        AlvoS.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Controle_do_Oceano(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Controle_do_Oceano
    EstadoDaPergunta["info"] = PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Norte","Sul","Leste","Oeste"]
    EstadoDaPergunta["estado"] = True

Controle_do_Oceano = {
    "nome": "Controle do Oceano",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul"],
    "estilo": "E",
    "dano": 0.7,
    "alcance": 60,
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

def F_Vasculhar_no_Rio(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    Vezes = random.choice([1,2])
    for i in range(Vezes):
        item = Gera_item(Baralho.Comuns + Baralho.Incomuns,Baralho)
        player.ganhar_item(item,Baralho)

Vasculhar_no_Rio = {
    "nome": "Vasculhar no Rio",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Vasculhe até 2 itens no rio, podendo ser da raridade comum ou incomum",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Vasculhar_no_Rio,
    "irregularidade": False
    }

def FI_Golpe_de_Concha(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Dano += PokemonS.Def * Ataque["dano"]
    Dano += PokemonS.Def_sp * Ataque["dano"]
    PokemonS.efeitosPosi["Reforçado"] = 0

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Golpe_de_Concha = {
    "nome": "Golpe de Concha",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul"],
    "estilo": "N",
    "dano": 0.5,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Esse ataque causa dano baseado em defesa, defesa especial e em ataque, após esse ataque o pokemon perde o efeito reforçado caso tenha",
    "efeito": "HexagonoLaminas",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Golpe_de_Concha
    }

def F_Gota_Pesada(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    AlvoS.efeitosNega["Encharcado"] = 4

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

def Alv_Bola_de_Agua(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def FI_Bola_de_Agua(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Bola_de_Agua = {
    "nome": "Bola de Água",
    "tipo": ["agua"],   
    "custo": ["azul","azul","azul"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "EspiralAzul",
    "alvos": Alv_Bola_de_Agua,
    "extra": "MAA",
    "funçao": Regular,
    "irregularidade": FI_Bola_de_Agua
    }

def FI_Cachoeira(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) <= 25:
        GuardarPosicionar(Alvo,player,3,Mapa.Zona)

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Cachoeira = {
    "nome": "Cachoeira",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul","azul"],
    "estilo": "N",
    "dano": 1.55,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Uma manobra aquática poderosa que tem 25% de chance de fazer o pokemon alvo ser guardado por 3 turnos",
    "efeito": "TornadoAgua",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Cachoeira
    }

def FI_Jato_Triplo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Aumento = random.randint(0,100)

    if Aumento > 70:
        Dano = Dano * 1.55
        Alvo.efeitosNega["Encharcado"] = 3
    elif Aumento > 20:
        Dano = Dano * 2.1
        Alvo.efeitosNega["Encharcado"] = 5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Jato_Triplo = {
    "nome": "Jato Triplo",
    "tipo": ["agua"],   
    "custo": ["azul","azul","azul","azul"],
    "estilo": "E",
    "dano": 0.8,
    "alcance": 18,
    "precisão": 100, 
    "descrição": "Esse ataque tem 50% de chance de aumentar 55% de dano e deixar o alvo encharcado por 3 turnos e tem 30% de chance de aumentar 110% de dano e encharcar o alvo por 5 turnos, e 20% de chance de não fazer nada a mais",
    "efeito": "EspiralAzul",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Jato_Triplo
    }
