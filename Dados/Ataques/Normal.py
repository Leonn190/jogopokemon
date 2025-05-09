from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move, GuardarPosicionar
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Tapa = {
    "nome": "Tapa",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "N",
    "dano": 0.8,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Um Tapa ofensivo no pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

Cabeçada = {
    "nome": "Cabeçada",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "N",
    "dano": 1.0,
    "alcance": 9,
    "precisão": 90, 
    "descrição": "Uma cabeçada ofensiva no pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Investida(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.Vida -= 10

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Investida = {
    "nome": "Investida",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 9,
    "precisão": 85, 
    "descrição": "Esse ataque causa 10 de dano a si mesmo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Investida
    }

def F_Vasculhar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    item = caixa()
    if item["classe"] in ["pokebola","Fruta"]:
        player.Captura.append(item)
    else:
        player.inventario.append(item)

Vasculhar = {
    "nome": "Vasculhar",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 150,
    "precisão": 100, 
    "descrição": "Vasculhe e ganhe 1 item aleatório",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Vasculhar,
    "irregularidade": False
    }

def F_Ataque_Rapido(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    
    if random.choice([True,False]) == True:
        PokemonS.atacou = False

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Ataque_Rapido = {
    "nome": "Ataque Rápido",
    "tipo": ["normal"],   
    "custo": ["normal","normal"],
    "estilo": "N",
    "dano": 1,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Tem 50% de chance desse ataque não constar como um ataque e esse pokemon poder atacar novamente",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Ataque_Rapido
    }

def F_Provocar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Provocando"] = 3

Provocar = {
    "nome": "Provocar",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Provoque os inimigos e ganhe Provocar por 3 turnos",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Provocar,
    "irregularidade": False
    }

Energia = {
    "nome": "Energia",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 20,
    "precisão": 95, 
    "descrição": "Libere energia contra o pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

Arranhar = {
    "nome": "Arranhar",
    "tipo": ["normal"],   
    "custo": ["normal","normal","normal"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Arranhe o alvo com vontade",
    "efeito": "Garra",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Crescer(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.Ganhar_XP(4,player)

Crescer = {
    "nome": "Crescer",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe 4 de XP",
    "efeito": "BolhasVerdes",
    "extra": None,
    "funçao": F_Crescer,
    "irregularidade": False
    }

def F_Esbravejar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if PokemonS.Vida < PokemonS.VidaMax * 0.6:
        PokemonS.efeitosPosi["Ofensivo"] = 3

Esbravejar = {
    "nome": "Esbravejar",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Se esse pokemon estiver com menos de 60% da vida maxima, ele ganha Ofensivo por 3 turnos",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Esbravejar,
    "irregularidade": False
    }

Tapa_Especial = {
    "nome": "Tapa Especial",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "E",
    "dano": 0.8,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Um Tapa ofensivo no pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Esmagar(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    
    Dano = Dano + Dano * (1 + 0.1 * PokemonS.Peso // 100)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Esmagar = {
    "nome": "Esmagar",
    "tipo": ["normal"],   
    "custo": ["normal","normal","normal","normal","normal"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 9,
    "precisão": 99, 
    "descrição": "Esse ataque causa mais 10% de dano a cada 100kg que esse pokemon tiver",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Esmagar
    }

def F_Descansar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    GuardarPosicionar(PokemonS,player,4,Mapa.Zona)
    cura = (PokemonS.VidaMax - PokemonS.Vida) * 0.3
    PokemonS.curar(cura,player,tela)

Descansar = {
    "nome": "Descansar",
    "tipo": ["normal"],   
    "custo": ["normal","normal","normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 150,
    "precisão": 100, 
    "descrição": "Esse pokemon é guardado por 4 turnos mas regenera 30% da vida perdida",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Descansar,
    "irregularidade": False
    }

def F_Canto_Alegre(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for efeito in PokemonV.efeitosNega:
        PokemonV.efeitosNega[efeito] = 0
 
Canto_Alegre = {
    "nome": "Canto Alegre",
    "tipo": ["normal"],   
    "custo": ["normal","normal","normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Remove todos os efeitos negativos do pokemon visualizado",
    "efeito": "FeixeMagenta",
    "extra": "V",
    "funçao": F_Canto_Alegre,
    "irregularidade": False
    }
