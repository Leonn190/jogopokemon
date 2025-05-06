from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Assombrar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    efeitos_disponiveis = list(Alvo.efeitosNega.keys())
    if efeitos_disponiveis:
        efeito_escolhido = random.choice(efeitos_disponiveis)
        Alvo.efeitosNega[efeito_escolhido] += 2

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
    PokemonS.Curar(Dano/10,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Lambida = {
    "nome": "Lambida",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Cure 10% do dano causado",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Lambida
    }

def F_Atravessar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for chave,valor in PokemonS.efeitosNega:
        PokemonS.efeitosNega[chave] = 0
        Alvo.efeitosNega[chave] = valor

Atravessar = {
    "nome": "Atravessar",
    "tipo": ["fantasma"],   
    "custo": ["preta","preta"],
    "estilo": "E",
    "dano": 0.5,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Atravessa o alvo, removendo todos os efeitos negativos de si mesmo e passando para o alvo",
    "efeito": "FeixeMagenta",
    "extra": "A",
    "funçao": F_Assombrar,
    "irregularidade": False
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
