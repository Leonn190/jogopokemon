import random

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