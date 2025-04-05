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

def fogo_puro(atacante, alvo):
    if alvo['def SP'] > 60:
        alvo['def SP'] = 60
    dano = 60 - alvo["def SP"]
    alvo["vida"] -= dano

def defesa_flamejante(atacante, alvo):
    if alvo['def SP'] > 60:
        alvo['def SP'] = 60
    dano = 40 - alvo["def SP"]
    alvo["vida"] -= dano
    atacante["def"] += 10