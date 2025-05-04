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
    "alcance": 28,
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
    "nome": "Garra_do_Dragão",
    "tipo": ["dragao"],   
    "custo": ["normal","normal","vermelha"],
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
