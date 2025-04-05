import random

def golpe_de_fogo(atacante, alvo):
    if alvo['def'] > 50:
        alvo['def'] = 50
    dano = 50 - alvo["def"]
    alvo["vida"] -= dano

def disparo_quente(atacante, alvo):
    if alvo['def'] > 10:
        alvo['def'] = 10
    dano = 10 - alvo["def"]
    alvo["vida"] -= dano

def ataque_n(atacante,alvo,player,inimigo):
    