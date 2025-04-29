from Geradores.GeradorAtaques import padrao
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Jato_de_Agua = {
    "nome": "Jato De Agua",
    "tipo": ["agua"],   
    "custo": ["normal","azul"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Lança um jato de agua intenso no oponente",
    "efeito": "EspiralAzul",
    "extra": False,
    "funçao": padrao
    }

def F_Jato_Duplo(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc):
    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    Aumento = random.choice([True,False])

    if Aumento is True:
        Dano = Dano * 1.5
        Alvo.efeitosNega["Encharcado"] = 3

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    Alvo.atacado(DanoF,player,inimigo,tela)

Jato_Duplo = {
    "nome": "Jato Duplo",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul"],
    "estilo": "E",
    "dano": 1.0,
    "alcance": 20,
    "precisão": 95, 
    "descrição": "Esse ataque tem 50% de chance de causar mais 50% de dano e deixar o oponente encharcado por 3 turnos",
    "efeito": "RedemoinhoAzul",
    "extra": None,
    "funçao": F_Jato_Duplo
    }
