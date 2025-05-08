from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Sopro_do_Dragao(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):

    efeitos_ativos = [chave for chave, valor in Alvo.efeitosPosi.items() if valor > 0]

    if efeitos_ativos:
        efeito_removido = random.choice(efeitos_ativos)
        Alvo.efeitosPosi[efeito_removido] = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Sopro_do_Dragao = {
    "nome": "Sopro do Dragão",
    "tipo": ["dragao"],   
    "custo": ["vermelha"],
    "estilo": "E",
    "dano": 0.7,
    "alcance": 26,
    "precisão": 90, 
    "descrição": "O sopro do dragão é capaz de remover um efeito positivo com o padrão draconico do pokemon atingido",
    "efeito": "Fumaça",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Sopro_do_Dragao
    }

def FF_Garra_do_Dragao(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
        Alvo.efeitosNega[Escolha] = 3

        Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

        EstadoDaPergunta["estado"] = False
        Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Garra_do_Dragao(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Garra_do_Dragao
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Quebrado","Fragilizado"]
    EstadoDaPergunta["estado"] = True

Garra_do_Dragao = {
    "nome": "Garra do Dragão",
    "tipo": ["dragao"],   
    "custo": ["normal","vermelha","vermelha"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Escolha entre deixar o oponente fragilizado ou quebrado por 3 turnos",
    "efeito": "Garra",
    "extra": "A",
    "funçao": F_Garra_do_Dragao,
    "irregularidade": False
    }

def F_Ultraje(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.atacado(22,player,inimigo,tela,Mapa)
    
Ultraje = {
    "nome": "Ultraje",
    "tipo": ["dragao"],   
    "custo": ["normal","vermelha"],
    "estilo": "N",
    "dano": 1,
    "alcance": 25,
    "precisão": 95, 
    "descrição": "Esse ataque causa sempre 22 de dano independente de qualquer efeito ou atributo",
    "efeito": "Corte",
    "extra": "A",
    "funçao": F_Ultraje,
    "irregularidade": False
    }

Cauda_Violenta = {
    "nome": "Cauda Violenta",
    "tipo": ["dragao"],   
    "custo": ["normal","vermelha","vermelha"],
    "estilo": "N",
    "dano": 1.4,
    "alcance": 20,
    "precisão": 85, 
    "descrição": "Use sua cauda para atingir o oponente com força",
    "efeito": "CorteRosa",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Investida_do_Dragao(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):

    PokemonS.atacado(40,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Investida_do_Dragao = {
    "nome": "Investida do Dragao",
    "tipo": ["dragao"],   
    "custo": ["vermelha","vermelha","vermelha","vermelha"],
    "estilo": "N",
    "dano": 2,
    "alcance": 16,
    "precisão": 100, 
    "descrição": "Esse ataque causa 36 de dano de perfuraçao em si mesmo",
    "efeito": "ExplosaoVermelha",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Investida_do_Dragao
    }
