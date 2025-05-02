from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Chamar_para_Briga(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Provocando"] += 3
    PokemonS.efeitosPosi["Preparado"] += 3

Chamar_para_Briga = {
    "nome": "Chamar para Briga",
    "tipo": ["lutador"],   
    "custo": ["normal","laranja"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe preparado e provocar por 3 turnos",
    "efeito": "Karate",
    "extra": None,
    "funçao": F_Chamar_para_Briga,
    "irregularidade": False
    }

Soco = {
    "nome": "Soco",
    "tipo": ["lutador"],   
    "custo": ["laranja"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Um soco firme",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }