from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover, verifica_colisao
from Geradores.GeradorOutros import Gera_item
import math
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Voar(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
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

def FI_Ataque_de_Asa(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if PokemonS.efeitosPosi["Voando"] > 0:
        Dano = Dano * 0.8
    
    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Ataque_de_Asa = {
    "nome": "Ataque de Asa",
    "tipo": ["voador"],   
    "custo": ["normal","amarela","amarela"],
    "estilo": "N",
    "dano": 1.45,
    "alcance": 4,
    "precisão": 100, 
    "descrição": "Esse ataque causa -25% de dano caso esse pokemon esteja voando",
    "efeito": "ChicoteMultiplo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Ataque_de_Asa
    }

def FI_Investida_Aerea(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    if PokemonS.efeitosPosi["Voando"] > 0:
        Dano = Dano * 1.25
    PokemonS.atacado(15,player,inimigo,tela,Mapa)
    
    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Investida_Aerea = {
    "nome": "Investida Aérea",
    "tipo": ["voador"],   
    "custo": ["amarela","amarela"],
    "estilo": "N",
    "dano": 1.25,
    "alcance": 3,
    "precisão": 95, 
    "descrição": "Esse ataque causa 15 de dano a si mesmo, caso esse pokemon esteja voando esse ataque causará mais 25% de dano",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Investida_Aerea
    }

def FI_Rasante(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    DanoV = PokemonS.vel * 1.35 * 0.9
    DanoN = PokemonS.Atk * 1.35 * 0.1
    Dano = DanoV + DanoN
    
    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Rasante = {
    "nome": "Rasante",
    "tipo": ["voador"],   
    "custo": ["amarela","amarela"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 3,
    "precisão": 110, 
    "descrição": "Esse ataque escala apenas 10% com o dano o resto é com velocidade (90%)",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Rasante
    }

def FI_Bico_Broca(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.49
    
    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Bico_Broca = {
    "nome": "Bico Broca",
    "tipo": ["voador"],   
    "custo": ["normal","amarela"],
    "estilo": "N",
    "dano": 1.05,
    "alcance": 1,
    "precisão": 100, 
    "descrição": "Bique seu oponente como uma verdadeira broca, ignorando 51% da defesa dele",
    "efeito": "Corte",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Bico_Broca
    }

def FI_Vento_Forte(Dano, Defesa, PokemonS, PokemonV, AlvoS, Alvo, player, inimigo, Ataque, Mapa, tela, Baralho, AlvoLoc, EstadoDaPergunta):
    # Verifica se algum dos Pokémon não está posicionado
    if PokemonS.local == [] or Alvo.local == []:
        return Dano, Defesa, PokemonS, PokemonV, AlvoS, Alvo, player, inimigo, Ataque, Mapa, tela, Baralho, AlvoLoc, EstadoDaPergunta

    xS = PokemonS.local[0]
    yS = PokemonS.local[1]
    xA = Alvo.local[0]
    yA = Alvo.local[1]

    dx = xA - xS
    dy = yA - yS
    dist_total = math.hypot(dx, dy)

    if dist_total == 0:
        return Dano, Defesa, PokemonS, PokemonV, AlvoS, Alvo, player, inimigo, Ataque, Mapa, tela, Baralho, AlvoLoc, EstadoDaPergunta

    direcao_x = dx / dist_total
    direcao_y = dy / dist_total

    # Define empurrão em metros baseado no peso
    peso = Alvo.Peso
    if peso > 400:
        return Dano, Defesa, PokemonS, PokemonV, AlvoS, Alvo, player, inimigo, Ataque, Mapa, tela, Baralho, AlvoLoc, EstadoDaPergunta
    elif peso > 300:
        metros = 2
    elif peso > 200:
        metros = 4
    elif peso > 100:
        metros = 6
    elif peso > 30:
        metros = 7
    else:
        metros = 8

    alcance_px = metros * Mapa.Metros

    # Gera lista de posições possíveis
    possiveis_posicoes = []
    nova_x = float(xA)
    nova_y = float(yA)

    for _ in range(int(alcance_px)):
        nova_x += direcao_x
        nova_y += direcao_y
        pos_int = [int(nova_x), int(nova_y)]
        if pos_int not in possiveis_posicoes:
            possiveis_posicoes.append(pos_int)

    # Testa da posição mais distante até a mais próxima
    for pos in reversed(possiveis_posicoes):
        if not verifica_colisao(pos[0], pos[1], Alvo):
            mover(Alvo, (pos[0],pos[1]))  # pos já está no formato [x, y]
            break

    return Dano, Defesa, PokemonS, PokemonV, AlvoS, Alvo, player, inimigo, Ataque, Mapa, tela, Baralho, AlvoLoc, EstadoDaPergunta

Vento_Forte = {
    "nome": "Vento Forte",
    "tipo": ["voador"],   
    "custo": ["amarela","amarela"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 7,
    "precisão": 100, 
    "descrição": "Mova o alvo para longe, o movimento varia do peso do inimigo, porém se ele tiver mais de 400kg ele não se move, se tiver menos de 30 se move 8 metros",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Vento_Forte
    }
