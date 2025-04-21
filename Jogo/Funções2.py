import Partida as P
import math
import pygame

Energias = ["vermelha", "azul", "amarela", "verde", "roxo", "rosa", "laranja", "marrom", "preta", "cinza"]

def efetividade(Tipo_do_ataque,Tipo_do_atacado,tela,atacado):
    
    tabela_tipos = {
    "normal":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "venenoso": 0, "terrestre": 0,
                  "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": -0.75, "dragao": 0, "sombrio": 0, "metal": 0, "fada": 0},

    "fogo":      {"normal": 0, "fogo": -0.25, "agua": -0.25, "eletrico": 0, "planta": 0.5, "gelo": 0.5, "lutador": 0, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0.5, "pedra": -0.25, "fantasma": 0, "dragao": -0.25, "sombrio": 0,
                  "metal": 0.5, "fada": 0},

    "agua":      {"normal": 0, "fogo": 0.5, "agua": -0.25, "eletrico": 0, "planta": -0.25, "gelo": 0, "lutador": 0, "venenoso": 0,
                  "terrestre": 0.5, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0.5, "fantasma": 0, "dragao": -0.25, "sombrio": 0,
                  "metal": 0, "fada": 0},

    "eletrico":  {"normal": 0, "fogo": 0, "agua": 0.5, "eletrico": -0.25, "planta": -0.25, "gelo": 0, "lutador": 0, "venenoso": 0,
                  "terrestre": -0.75, "voador": 0.5, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": -0.25, "sombrio": 0,
                  "metal": 0, "fada": 0},

    "planta":    {"normal": 0, "fogo": -0.25, "agua": 0.5, "eletrico": 0, "planta": -0.25, "gelo": 0, "lutador": 0, "venenoso": -0.25,
                  "terrestre": 0.5, "voador": -0.25, "psiquico": 0, "inseto": -0.25, "pedra": 0.5, "fantasma": 0, "dragao": -0.25,
                  "sombrio": 0, "metal": -0.25, "fada": 0},

    "gelo":      {"normal": 0, "fogo": -0.25, "agua": -0.25, "eletrico": 0, "planta": 0.5, "gelo": -0.25, "lutador": 0, "venenoso": 0,
                  "terrestre": 0.5, "voador": 0.5, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0.5, "sombrio": 0,
                  "metal": -0.25, "fada": 0},

    "lutador":   {"normal": 0.5, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0.5, "lutador": 0, "venenoso": -0.25,
                  "terrestre": 0, "voador": -0.25, "psiquico": -0.25, "inseto": -0.25, "pedra": 0.5, "fantasma": -0.75, "dragao": 0,
                  "sombrio": 0.5, "metal": 0.5, "fada": -0.25},

    "venenoso":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0.5, "gelo": 0, "lutador": 0, "venenoso": -0.25,
                  "terrestre": -0.25, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": -0.25, "fantasma": -0.25, "dragao": 0,
                  "sombrio": 0, "metal": -0.75, "fada": 0.5},

    "terrestre":     {"normal": 0, "fogo": 0.5, "agua": 0, "eletrico": 0.5, "planta": -0.25, "gelo": 0, "lutador": 0, "venenoso": 0.5,
                  "terrestre": 0, "voador": -0.75, "psiquico": 0, "inseto": -0.25, "pedra": 0.5, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "metal": 0.5, "fada": 0},

    "voador":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": -0.25, "planta": 0.5, "gelo": 0, "lutador": 0.5, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0.5, "pedra": -0.25, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "metal": -0.25, "fada": 0},

    "psiquico":  {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "venenoso": 0.5,
                  "terrestre": 0, "voador": 0, "psiquico": -0.25, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0,
                  "sombrio": -0.75, "metal": -0.25, "fada": 0},

    "inseto":    {"normal": 0, "fogo": -0.25, "agua": 0, "eletrico": 0, "planta": 0.5, "gelo": 0, "lutador": -0.25, "venenoso": -0.25,
                  "terrestre": 0, "voador": -0.25, "psiquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": -0.25, "dragao": 0,
                  "sombrio": 0.5, "metal": -0.25, "fada": -0.25},

    "pedra":     {"normal": 0, "fogo": 0.5, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0.5, "lutador": -0.25, "venenoso": 0,
                  "terrestre": -0.25, "voador": 0.5, "psiquico": 0, "inseto": 0.5, "pedra": 0, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "metal": -0.25, "fada": 0},

    "fantasma":  {"normal": -0.75, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": 0.5, "dragao": 0,
                  "sombrio": -0.25, "metal": 0, "fada": 0},

    "dragao":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0.5,
                  "sombrio": 0, "metal": -0.25, "fada": -0.75},

    "sombrio":   {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": -0.25, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": 0.5, "dragao": 0,
                  "sombrio": -0.25, "metal": 0, "fada": -0.25},

    "metal":       {"normal": 0, "fogo": -0.25, "agua": -0.25, "eletrico": -0.25, "planta": 0, "gelo": 0.5, "lutador": 0, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "metal": -0.25, "fada": 0.5},

    "fada":      {"normal": 0, "fogo": -0.25, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "venenoso": -0.25,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0.5,
                  "sombrio": 0.5, "metal": -0.25, "fada": 0},
    }
    
    multiplicador = 1
    for i in range(len(Tipo_do_ataque)):
        for j in range(len(Tipo_do_atacado)):
            multiplicador = multiplicador + tabela_tipos[Tipo_do_ataque[i]][Tipo_do_atacado[j]]
    if multiplicador < 0:
        multiplicador = 0
    
    
    if multiplicador > 1.5:
        texto = "Super Efetivo"
    elif multiplicador > 1:
        texto = "Efetivo"
    elif multiplicador == 1:
        return multiplicador
    elif multiplicador > 0.5:
        texto = "Pouco Efetivo"
    elif multiplicador > 0:
        texto = "Não Efetivo"
    else:
        texto = "Não Afeta"
    Fonte = pygame.font.SysFont(None, 30)
    P.adicionar_mensagem_passageira(tela,f"{texto}",(0,0,0),Fonte,((1365 - atacado.pos * 190),220))

    return multiplicador

def distancia_entre_pokemons(poke1, poke2, tamanho_casa):
    if poke1.local is None or poke2.local is None:
        return None

    linha1, coluna1 = map(int, poke1.local["id"])
    linha2, coluna2 = map(int, poke2.local["id"])

    dx = (linha1 - linha2) * tamanho_casa
    dy = (coluna1 - coluna2) * tamanho_casa

    return math.hypot(dx, dy)