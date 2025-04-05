import random
import Funções

def A(atacante,alvo,player,inimigo):
    Dano = atacante["atk"] * 1
    Tipo = ["fogo"]
    mitigação = 100 / (100 + alvo["def"])
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)

def B(atacante,alvo,player,inimigo):
    Dano = atacante["atk"] * 1.1
    Tipo = ["fogo"]
    mitigação = 100 / (100 + alvo["def"]) 
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)