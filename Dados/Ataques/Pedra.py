from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Pedregulho = {
    "nome": "Pedregulho",
    "tipo": ["pedra"],   
    "custo": ["laranja"],
    "estilo": "N",
    "dano": 0.9,
    "alcance": 30,
    "precisão": 90, 
    "descrição": "Lança um pedregulho no inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

Pedra_Especial = {
    "nome": "Pedra Especial",
    "tipo": ["pedra"],   
    "custo": ["normal","laranja"],
    "estilo": "N",
    "dano": 1.5,
    "alcance": 20,
    "precisão": 50, 
    "descrição": "Lança uma pedra especial no inimigo",
    "efeito": "ImpactoRochoso",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Barragem_Rochosa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.barreira += (PokemonS.Def + PokemonS.Def_sp) * 0.2

Barragem_Rochosa = {
    "nome": "Voar",
    "tipo": ["voador"],   
    "custo": ["cinza"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe 20% das somas das defesas como barreira",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Barragem_Rochosa,
    "irregularidade": False
    }

def F_Impacto_Rochoso(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano = PokemonS.Def * Ataque["dano"]
    PokemonS.efeitosNega["Quebrado"] = 2

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Impacto_Rochoso = {
    "nome": "Impacto Rochoso",
    "tipo": ["pedra"],   
    "custo": ["normal","laranja","laranja"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 5,
    "precisão": 100, 
    "descrição": "Esse ataque causa dano baseado apenas na Defesa, após esse ataque, esse pokemon fica quebrado por 2 turnos",
    "efeito": "ImpactoRochoso",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Impacto_Rochoso
    }

def F_Pedra_Colossal(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if inimigo.inventario != []:  
        item = random.choice(inimigo.inventario)
        inimigo.inventario.remove(item)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Pedra_Colossal = {
    "nome": "Pedra Colossal",
    "tipo": ["pedra"],   
    "custo": ["normal","laranja","laranja","laranja"],
    "estilo": "N",
    "dano": 1.55,
    "alcance": 15,
    "precisão": 95, 
    "descrição": "Esse ataque causa dano baseado apenas na Defesa, após esse ataque, esse pokemon fica quebrado por 2 turnos",
    "efeito": "ImpactoRochoso",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Pedra_Colossal
    }

def FF_Furia_Petrea(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    Valor = int(Escolha)
    
    PokemonS.efeitosPosi["Imortal"] = 2
    PokemonS.atacado(Valor * 35,player,inimigo,tela,Mapa)

    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    Dano = Dano * (1 + 0.35 * Valor)

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)
    
    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    EstadoDaPergunta["estado"] = False
    Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Furia_Petrea(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Furia_Petrea
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["1","2","3","4"]
    EstadoDaPergunta["estado"] = True

Furia_Petrea = {
    "nome": "Fúria Pétrea",
    "tipo": ["pedra"],  
    "custo": ["normal","laranja","laranja","laranja","laranja"],
    "estilo": "N",
    "dano": 1,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Ganhe importal por 2 turnos, Escolha um nivel de fúria, esse ataque causa 35% de dano a mais e 35 de dano a si mesmo como perfuraçao a cada nivel de fúria",
    "efeito": "ImpactoRochoso",
    "efeito2": "ImpactoRochoso",
    "extra": "A",
    "funçao": F_Furia_Petrea,
    "irregularidade": False
    }
