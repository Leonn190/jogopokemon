from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Assombrar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    efeitos_disponiveis = list(Alvo.efeitosNega.keys())
    if efeitos_disponiveis:
        efeito_escolhido = random.choice(efeitos_disponiveis)
        Alvo.efeitosNega[efeito_escolhido] = 2

Assombrar = {
    "nome": "Assombrar",
    "tipo": ["fantasma"],   
    "custo": ["preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 15,
    "precisão": 95, 
    "descrição": "Aplica um efeito negativo aleatorio por 2 turnos no alvo",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": F_Assombrar,
    "irregularidade": False
    }

def F_Lambida(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.curar(Dano/15,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Lambida = {
    "nome": "Lambida",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Cure 15% do dano causado",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Lambida
    }

def F_Atravessar(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    for chave,valor in PokemonS.efeitosNega.items():
        PokemonS.efeitosNega[chave] = 0
        Alvo.efeitosNega[chave] = valor

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Atravessar = {
    "nome": "Atravessar",
    "tipo": ["fantasma"],   
    "custo": ["preta","preta"],
    "estilo": "E",
    "dano": 0.5,
    "alcance": 9,
    "precisão": 100, 
    "descrição": "Atravessa o alvo, removendo todos os efeitos negativos de si mesmo e passando para o alvo",
    "efeito": "FeixeMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Atravessar
    }

saldo = 1

def FF_Coleta_Gananciosa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    global saldo
    if Escolha == "Mais":
        if random.randint(0,100) > saldo * 2:
            saldo += saldo
            EstadoDaPergunta["estado"] = False
            F_Coleta_Gananciosa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta)
        else:   
            saldo = 0
            EstadoDaPergunta["estado"] = False
            return
    else:
        player.ouro += saldo
        saldo = 1
        EstadoDaPergunta["estado"] = False

def F_Coleta_Gananciosa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I=None):
    
    EstadoDaPergunta["funçao"] = FF_Coleta_Gananciosa
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Mais","Parar"]
    EstadoDaPergunta["estado"] = True

Coleta_Gananciosa = {
    "nome": "Coleta Gananciosa",
    "tipo": ["fantasma"],   
    "custo": ["preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe 1 de ouro, no entanto voce pode ganhar mais, porém toda vez que escolhe mais tem mais chance de perder tudo",
    "efeito": "!None",
    "extra": "TV",
    "funçao": F_Coleta_Gananciosa,
    "irregularidade": False
    }

def F_Mao_Espectral(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    linhaS, colunaS = PokemonS.local["id"]
    linhaA, colunaA = Alvo.local["id"]

    if linhaS > linhaA:
        Move(Alvo,linhaS - 1, colunaS,Mapa.Zona)
    else:
        Move(Alvo,linhaS + 1, colunaS,Mapa.Zona)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Mao_Espectral = {
    "nome": "Mão Espectral",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta","preta"],
    "estilo": "E",
    "dano": 1,
    "alcance": 40,
    "precisão": 100, 
    "descrição": "Puxe o inimigo para perto de você",
    "efeito": "ExplosaoRoxa",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Mao_Espectral
    }

def FF_Maldade(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    Alvo.efeitosNega[Escolha] = 4
    EstadoDaPergunta["estado"] = False

def F_Maldade(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I=None):
    opçoes = []
    for chave in PokemonS.efeitosNega:
        opçoes.append(chave)

    EstadoDaPergunta["funçao"] = FF_Maldade
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = []
    EstadoDaPergunta["estado"] = True

    for i in range(4):
        EstadoDaPergunta["opçoes"].append(random.choice(opçoes))

Maldade = {
    "nome": "Maldade",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta","preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 50,
    "precisão": 100, 
    "descrição": "Escolha entre 4 efeitos negativos aleatorios para colocar no alvo por 4 turnos",
    "efeito": "ChuvaVermelha",
    "extra": "A",
    "funçao": F_Maldade,
    "irregularidade": False
    }

def F_Massacre_Fantasmagorico(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    for chave in PokemonS.efeitosPosi:
        if Alvo.efeitosPosi[chave] > 1:
            return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

    Dano = Dano * 1.41
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Massacre_Fantasmagorico = {
    "nome": "Massacre Fantasmagórico",
    "tipo": ["fantasma"],   
    "custo": ["preta","preta","preta","preta"],
    "estilo": "E",
    "dano": 1.4,
    "alcance": 10,
    "precisão": 99, 
    "descrição": "Se o alvo não tiver nenhum efeito positivo, esse ataque irá causar mais 41% de dano",
    "efeito": "RasgosRosa",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Massacre_Fantasmagorico
    }

