from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover, verifica_colisao
import math
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Assombrar(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    efeitos_disponiveis = list(AlvoS.efeitosNega.keys())
    if efeitos_disponiveis:
        efeito_escolhido = random.choice(efeitos_disponiveis)
        AlvoS.efeitosNega[efeito_escolhido] = 2

Assombrar = {
    "nome": "Assombrar",
    "tipo": ["fantasma"],   
    "custo": ["preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 15,
    "precisão": 95, 
    "descrição": "Aplica um efeito negativo aleatorio por 2 turnos no alvo",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": F_Assombrar,
    "irregularidade": False
    }

def FI_Lambida(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    PokemonS.curar(Dano/15,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Lambida = {
    "nome": "Lambida",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Cure 15% do dano causado",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Lambida
    }

def FI_Atravessar(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    for chave,valor in PokemonS.efeitosNega.items():
        PokemonS.efeitosNega[chave] = 0
        Alvo.efeitosNega[chave] = valor

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Atravessar = {
    "nome": "Atravessar",
    "tipo": ["fantasma"],   
    "custo": ["preta","preta"],
    "estilo": "E",
    "dano": 0.5,
    "alcance": 9,
    "precisão": 100, 
    "descrição": "Atravessa o alvo, removendo todos os efeitos negativos de si mesmo e passando para o alvo",
    "efeito": "FeixeMagenta",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Atravessar
    }

saldo = 1

def FF_Coleta_Gananciosa(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,Escolha):
    global saldo
    if Escolha == "Mais":
        if random.randint(0,100) > saldo * 2:
            saldo += saldo
            EstadoDaPergunta["estado"] = False
            F_Coleta_Gananciosa(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta)
        else:   
            saldo = 0
            EstadoDaPergunta["estado"] = False
            return
    else:
        player.ouro += saldo
        saldo = 1
        EstadoDaPergunta["estado"] = False

def F_Coleta_Gananciosa(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I=None):
    global saldo
    saldo = 1
    EstadoDaPergunta["funçao"] = FF_Coleta_Gananciosa
    EstadoDaPergunta["info"] = PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Mais","Parar"]
    EstadoDaPergunta["estado"] = True

Coleta_Gananciosa = {
    "nome": "Coleta Gananciosa",
    "tipo": ["fantasma"],   
    "custo": ["preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe 1 de ouro, no entanto voce pode ganhar mais, porém toda vez que escolhe mais tem mais chance de perder tudo",
    "efeito": "!None",
    "extra": "TV",
    "funçao": F_Coleta_Gananciosa,
    "irregularidade": False
    }

def FI_Mao_Espectral(Dano, Defesa, PokemonS, PokemonV, AlvoS, Alvo, player, inimigo, Ataque, Mapa, tela, Baralho, AlvoLoc, EstadoDaPergunta):
    if PokemonS.local is None or Alvo.local is None:
        return

    xS, yS = PokemonS.local
    xA, yA = Alvo.local

    distancia = math.hypot(xA - xS, yA - yS)

    if distancia <= (PokemonS.raio + Alvo.raio):
        return  # Já estão colidindo ou próximos demais para puxar

    # Define o vetor unitário de direção do atacante para o alvo (sentido reverso pois queremos puxar)
    dx = xS - xA
    dy = yS - yA
    dist_total = math.hypot(dx, dy)

    if dist_total == 0:
        return  # Mesma posição, não faz sentido puxar

    direcao_x = dx / dist_total
    direcao_y = dy / dist_total

    # Tenta mover o alvo ao longo da direção contrária ao vetor
    passo = 1  # pixels por iteração
    nova_x = xA
    nova_y = yA

    for i in range(int(dist_total)):
        nova_x += direcao_x * passo
        nova_y += direcao_y * passo

        if math.hypot(nova_x - xS, nova_y - yS) <= (PokemonS.raio + Alvo.raio):
            break  # Próximo o suficiente, para antes de colidir

        if verifica_colisao(int(nova_x), int(nova_y), Alvo):
            # Encontrou posição válida mais próxima sem colisão
            mover(Alvo, (int(nova_x), int(nova_y)))
            break

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Mao_Espectral = {
    "nome": "Mão Espectral",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta","preta"],
    "estilo": "E",
    "dano": 1,
    "alcance": 40,
    "precisão": 100, 
    "descrição": "Puxe o inimigo para perto de você",
    "efeito": "ExplosaoRoxa",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Mao_Espectral
    }

def FF_Maldade(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,Escolha):
    AlvoS.efeitosNega[Escolha] = 4
    EstadoDaPergunta["estado"] = False

def F_Maldade(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I=None):
    opçoes = []
    for chave in PokemonS.efeitosNega:
        opçoes.append(chave)

    EstadoDaPergunta["funçao"] = FF_Maldade
    EstadoDaPergunta["info"] = PokemonS,PokemonV,AlvoS,player,Alvos,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc
    EstadoDaPergunta["opçoes"] = []
    EstadoDaPergunta["estado"] = True

    for i in range(4):
        EstadoDaPergunta["opçoes"].append(random.choice(opçoes))

Maldade = {
    "nome": "Maldade",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta","preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 50,
    "precisão": 100, 
    "descrição": "Escolha entre 4 efeitos negativos aleatorios para colocar no alvo por 4 turnos",
    "efeito": "ChuvaVermelha",
    "extra": "A",
    "funçao": F_Maldade,
    "irregularidade": False
    }

def FI_Massacre_Fantasmagorico(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    for chave in PokemonS.efeitosPosi:
        if Alvo.efeitosPosi[chave] > 1:
            return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

    Dano = Dano * 1.41
    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Massacre_Fantasmagorico = {
    "nome": "Massacre Fantasmagórico",
    "tipo": ["fantasma"],   
    "custo": ["preta","preta","preta","preta"],
    "estilo": "E",
    "dano": 1.4,
    "alcance": 10,
    "precisão": 99, 
    "descrição": "Se o alvo não tiver nenhum efeito positivo, esse ataque irá causar mais 41% de dano",
    "efeito": "RasgosRosa",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Massacre_Fantasmagorico
    }

def FF_Vasculhada_Trapaceira(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,Escolha):
    Escolha = int(Escolha)
    if player.ouro < Escolha:
        Escolha = 0
    player.ouro -= Escolha
    
    if Escolha == 0:
        item = Gera_item(Baralho.Comuns + Baralho.Incomuns,Baralho)
        player.ganhar_item(item,Baralho)
    elif Escolha == 5:
        item = Gera_item(Baralho.Raros,Baralho)
        player.ganhar_item(item,Baralho)
    elif Escolha == 10:
        item = Gera_item(Baralho.Epicos,Baralho)
        player.ganhar_item(item,Baralho)
    elif Escolha == 15:
        item = Gera_item(Baralho.Lendarios,Baralho)
        player.ganhar_item(item,Baralho)

    EstadoDaPergunta["estado"] = False

def F_Vasculhada_Trapaceira(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Vasculhada_Trapaceira
    EstadoDaPergunta["info"] = PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["0","5","10","15"]
    EstadoDaPergunta["estado"] = True

Vasculhada_Trapaceira = {
    "nome": "Vasculhada Trapaceira",
    "tipo": ["fantasma"],   
    "custo": ["preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Escolha o quanto de ouro quer gastar para vasculhar, 0 para comum/incomum, 5 para raro, 10 para epico e 15 para mitico",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Vasculhada_Trapaceira,
    "irregularidade": False
    }
