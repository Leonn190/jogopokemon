from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover, PosicionarGuardar
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Confusão(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    AlvoS.efeitosNega["Confuso"] = 3

Confusão = {
    "nome": "Confusão",
    "tipo": ["psiquico"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 10,
    "precisão": 90, 
    "descrição": "Deixe o inimigo confuso por 3 turnos",
    "efeito": "FeixeRoxo",
    "extra": "A",
    "funçao": F_Confusão,
    "irregularidade": False
    }

def Alv_Bola_Psíquica(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 3, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def FI_Bola_Psiquica(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Bola_Psiquica = {
    "nome": "Bola Psíquica",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 7,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "ExplosaoRoxa",
    "alvos": Alv_Bola_Psíquica,
    "extra": "MAA",
    "funçao": Regular,
    "irregularidade": FI_Bola_Psiquica
    }

def FI_Teleporte(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    xA, yA = Alvo.local
    xS, yS = PokemonS.local
    
    PosicionarGuardar(Alvo,1)
    PosicionarGuardar(Alvo,1)
    mover(PokemonS,(xA,yA))
    mover(Alvo,(xS,yS))

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Teleporte = {
    "nome": "Teleporte",
    "tipo": ["psiquico"],   
    "custo": ["roxa"],
    "estilo": "N",
    "dano": 0.4,
    "alcance": 12,
    "precisão": 100, 
    "descrição": "Troque de lugar com o alvo",
    "efeito": "FeixeMagenta",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Teleporte
    }

def FI_Ampliação_Mental(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    for efeito in PokemonS.efeitosNega:
        if Alvo.efeitosNega[efeito] > 0:
            Alvo.efeitosNega[efeito] += 1

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Ampliação_Mental = {
    "nome": "Ampliação Mental",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa"],
    "estilo": "E",
    "dano": 0.85,
    "alcance": 4,
    "precisão": 80, 
    "descrição": "Aumente 1 de todos os contadores de efeitos negativos do pokemon atingido",
    "efeito": "FeixeRoxo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Ampliação_Mental
    }

def FI_Psiquico_Desgastante(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    PokemonS.efeitosNega["Incapacitado"] += 3

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Psiquico_Desgastante = {
    "nome": "Psiquico Desgastante",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa"],
    "estilo": "E",
    "dano": 1.45,
    "alcance": 5,
    "precisão": 85, 
    "descrição": "Esse pokemon agora está incapacitado por 3 turnos",
    "efeito": "CorteRicocheteadoRoxo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Psiquico_Desgastante
    }

def FI_Mente_Forte(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if random.choice([True,False]) ==  True:
        PokemonS.efeitosPosi["Focado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Mente_Forte = {
    "nome": "Mente Forte",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa"],
    "estilo": "N",
    "dano": 1.15,
    "alcance": 5,
    "precisão": 100, 
    "descrição": "Esse ataque tem 50% de chance de te deixar focado",
    "efeito": "CorteRicocheteadoRoxo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Mente_Forte
    }

def FI_Corrosao_Psiquica(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Dano = Dano * Alvo.Vida // 100

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Corrosao_Psiquica = {
    "nome": "Corrosão Psíquica",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 5,
    "precisão": 100, 
    "descrição": "O dano desse ataque é a % da vida do inimigo",
    "efeito": "OrbesRoxos",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Corrosao_Psiquica
    }

def FI_Psicorte_Duplo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.7
    aliados, inimigos = pokemons_nos_arredores(Alvo,player,inimigo,2,Mapa.Zona)
    if PokemonV in inimigos:
        mitigação = 100 / (100 + PokemonV.Def)
        DanoV = Dano * mitigação
        PokemonV.atacado(DanoV,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Psicorte_Duplo = {
    "nome": "Psicorte Duplo",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa","roxa","roxa","roxa"],
    "estilo": "N",
    "dano": 1.5,
    "alcance": 2,
    "precisão": 95, 
    "descrição": "Esse ataque causa dano a um oponente selecionado caso esteja ate 2 casas adjacentes do alvo principal, esse ataque ignora 40% das defesas inimigas",
    "efeito": "CorteDuploRoxo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Psicorte_Duplo
    }

def FI_Transferencia_Psiquica(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    for efeito in PokemonV.efeitosNega:
        if PokemonV.efeitosNega[efeito] >= 1:
            Alvo.efeitosNega[efeito] += PokemonV.efeitosNega[efeito]
            PokemonV.efeitosNega[efeito] = 0
            break

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Transferencia_Psiquica = {
    "nome": "Tranferência Psíquica",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa"],
    "estilo": "E",
    "dano": 0.7,
    "alcance": 5,
    "precisão": 100, 
    "descrição": "Transfere um efeito negativo aleatorio do pokemon visualizado para o alvo",
    "efeito": "FeixeMagenta",
    "efeito2": "FluxoAzul",
    "extra": "AV",
    "funçao": Regular,
    "irregularidade": FI_Transferencia_Psiquica
    }

def FI_Teletransporte(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    xA, yA = Alvo.local
    xS, yS = PokemonV.local
    
    PosicionarGuardar(Alvo,1)
    PosicionarGuardar(Alvo,1)
    mover(PokemonS,(xA,yA))
    mover(Alvo,(xS,yS))

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Teletransporte = {
    "nome": "Teletransporte",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa"],
    "estilo": "E",
    "dano": 0.6,
    "alcance": 14,
    "precisão": 100, 
    "descrição": "O pokemon visualizado troca de lugar com o alvo",
    "efeito": "FeixeMagenta",
    "efeito2": "FeixeMagenta",
    "extra": "AV",
    "funçao": Regular,
    "irregularidade": FI_Teletransporte
    }

def FI_Raio_Psiquico(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    contador = 0
    for efeito in Alvo.efeitosNega:
        if Alvo.efeitosNega[efeito] > 0:
            contador += 1
    for efeito in Alvo.efeitosPosi:
        if Alvo.efeitosPosi[efeito] > 0:
            contador += 1
    Dano = Dano * (1 - 0.1 * contador)

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Raio_Psiquico = {
    "nome": "Raio Psíquico",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa","roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 2.1,
    "alcance": 6,
    "precisão": 100, 
    "descrição": "Esse ataque causa menos 10% de dano a cada efeito que o pokemon inimigo tiver",
    "efeito": "RasgoMagenta",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Raio_Psiquico
    }

def FI_Agonia_Mental(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosNega["Incapacitado"] = 5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Agonia_Mental = {
    "nome": "Agonia Mental",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa","roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.35,
    "alcance": 11,
    "precisão": 100, 
    "descrição": "Esse ataque deixa o alvo incapacitado por 5 turnos",
    "efeito": "OrbesRoxos",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Agonia_Mental
    }
