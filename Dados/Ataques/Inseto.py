from Geradores.GeradorAtaques import Regular
from Jogo.Tabuleiro import Move, GuardarPosicionar
from Geradores.GeradorOutros import caixa, coletor
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Mordida = {
    "nome": "Mordida",
    "tipo": ["inseto"],   
    "custo": ["normal","verde"],
    "estilo": "N",
    "dano": 1.25,
    "alcance": 10,
    "precisão": 95, 
    "descrição": "Morda seu oponente com força",
    "efeito": "Mordida",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def FI_Seda(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.Varvel_perm > -11:
        Alvo.Varvel_perm -= 12

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Seda = {
    "nome": "Seda",
    "tipo": ["inseto"],   
    "custo": ["verde"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 20,
    "precisão": 90, 
    "descrição": "Esse ataque diminue 12 de velocidade do oponente, caso ja tenha -12 de velocidade, não diminue mais",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Seda
    }

def FI_Picada(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.choice([True,False]) == True:
        Alvo.efeitosNega["Envenenado"] += 3

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Picada = {
    "nome": "Picada",
    "tipo": ["inseto"],   
    "custo": ["verde"],
    "estilo": "N",
    "dano": 0.8,
    "alcance": 15,
    "precisão": 90, 
    "descrição": "Esse ataque tem 50% de chance de deixar o oponente envenenado por 3 turnos",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Picada
    }

def FF_Minhocagem(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
        if Escolha == "Roubar":
            if inimigo.energias["verde"] > 2:
                 inimigo.energias["verde"] -= 2
                 player.energias["verde"] += 2
            else:
                 player.energias["verde"] += inimigo.energias["verde"]
                 inimigo.energias["verde"] = 0
        else:
            GuardarPosicionar(PokemonS,player,3,Mapa.Zona)

        Dano, Defesa = VEstilo(PokemonS,AlvoS,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],AlvoS.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,AlvoS,player,inimigo,DanoF,Ataque["estilo"],tela)

        EstadoDaPergunta["estado"] = False
        AlvoS.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Minhocagem(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Minhocagem
    EstadoDaPergunta["info"] = PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Guardar","Roubar"]
    EstadoDaPergunta["estado"] = True

Minhocagem = {
    "nome": "Minhocagem",
    "tipo": ["inseto"],   
    "custo": ["normal","normal","normal"],
    "estilo": "E",
    "dano": 0.7,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Com o movimento das minhocas voce pode escolher entre guardar esse pokemon ou roubar 2 energias verde do oponente",
    "efeito": "DomoVerde",
    "extra": "A",
    "funçao": F_Minhocagem,
    "irregularidade": False
    }

def F_Coleta(PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for i in range(4):
        player.energias[coletor()] += 1

Coleta = {
    "nome": "Coleta",
    "tipo": ["inseto"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe 4 energias aleatorias",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Coleta,
    "irregularidade": None
    }

Tesoura_X = {
    "nome": "Tesoura X",
    "tipo": ["inseto"],   
    "custo": ["verde","verde","verde"],
    "estilo": "N",
    "dano": 1.6,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Atinja com força o oponente",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def FI_Dor_Falsa(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosPosi["Regeneração"] = 3

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Dor_Falsa = {
    "nome": "Dor Falsa",
    "tipo": ["inseto"],   
    "custo": ["normal","verde"],
    "estilo": "N",
    "dano": 1.7,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Esse ataque aplica uma dor falsa no oponente pois deixa ele com regeneração por 3 turnos",
    "efeito": "ChicoteMultiplo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Dor_Falsa
    }
