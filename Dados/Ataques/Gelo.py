from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Cristalizar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if Alvo.efeitosNega["Encharcado"] > 0:
        Alvo.efeitosNega["Congelado"] += Alvo.efeitosNega["Encharcado"] + 1
        Alvo.efeitosNega["Encharcado"] = 0

Cristalizar = {
    "nome": "Cristalizar",
    "tipo": ["gelo"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 30,
    "precisão": 100, 
    "descrição": "Se o pokemon inimigo estiver encharcado, ele perde esse efeito e ganha congelar por 1 turno a mais",
    "efeito": "FluxoAzul",
    "extra": None,
    "funçao": F_Cristalizar,
    "irregularidade": False
    }