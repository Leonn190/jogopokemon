from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Voar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Voando"] = 3

Voar = {
    "nome": "Voar",
    "tipo": ["voador"],   
    "custo": ["amarela"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "voe e ganhe o efeito voando por 3 turnos",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Voar,
    "irregularidade": False
    }

def F_Ataque_de_Asa(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if PokemonS.efeitosPosi["Voando"] > 0:
        Dano = Dano * 0.8
    
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Ataque_de_Asa = {
    "nome": "Ataque de Asa",
    "tipo": ["voador"],   
    "custo": ["normal","amarela","amarela"],
    "estilo": "N",
    "dano": 1.45,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque causa -25% de dano caso esse pokemon esteja voando",
    "efeito": "ChicoteMultiplo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Ataque_de_Asa
    }

def F_Investida_Aerea(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if PokemonS.efeitosPosi["Voando"] > 0:
        Dano = Dano * 1.25
    PokemonS.atacado(15,player,inimigo,tela,Mapa)
    
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Investida_Aerea = {
    "nome": "Investida Aérea",
    "tipo": ["voador"],   
    "custo": ["amarela","amarela"],
    "estilo": "N",
    "dano": 1.25,
    "alcance": 10,
    "precisão": 95, 
    "descrição": "Esse ataque causa 15 de dano a si mesmo, caso esse pokemon esteja voando esse ataque causará mais 25% de dano",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Investida_Aerea
    }

def F_Rasante(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    DanoV = PokemonS.vel * 1.35 * 0.9
    DanoN = PokemonS.Atk * 1.35 * 0.1
    Dano = DanoV + DanoN
    
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Rasante = {
    "nome": "Rasante",
    "tipo": ["voador"],   
    "custo": ["amarela","amarela"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 15,
    "precisão": 110, 
    "descrição": "Esse ataque escala apenas 10% com o dano o resto é com velocidade (90%)",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Investida_Aerea
    }

def F_Bico_Broca(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.49
    
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bico_Broca = {
    "nome": "Bico Broca",
    "tipo": ["voador"],   
    "custo": ["normal","amarela"],
    "estilo": "N",
    "dano": 1.05,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Bique seu oponente como uma verdadeira broca, ignorando 51% da defesa dele",
    "efeito": "Corte",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Bico_Broca
    }

def F_Vento_Forte(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    linhaS, colunaS = PokemonS.local["id"]
    linhaA, colunaA = Alvo.local["id"]

    intensidade = 2 if Alvo.Peso < 200 else 1

    deslocamento_linha = 0
    deslocamento_coluna = 0

    if colunaS == colunaA:

        if linhaA > linhaS:
            deslocamento_linha = intensidade  
        else:
            deslocamento_linha = -intensidade  

    elif linhaS == linhaA:
        if colunaA > colunaS:
            deslocamento_coluna = intensidade  
        else:
            deslocamento_coluna = -intensidade  

    else:

        if linhaA > linhaS:
            deslocamento_linha = intensidade  
        else:
            deslocamento_linha = -intensidade 

        if colunaA > colunaS:
            deslocamento_coluna = intensidade  
        else:
            deslocamento_coluna = -intensidade  

    nova_linha = linhaA + deslocamento_linha
    nova_coluna = colunaA + deslocamento_coluna

    Move(Alvo, nova_linha, nova_coluna, Mapa.Zona)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Vento_Forte = {
    "nome": "Vento Forte",
    "tipo": ["voador"],   
    "custo": ["amarela","amarela"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Mova o alvo 2 casas para longe, caso ele tenha mais de 200kg mova apenas 1 casa",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Vento_Forte
    }
