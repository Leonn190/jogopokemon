import random
import Funções

def C(atacante,alvo,player,inimigo):
    Dano = atacante["atk SP"] * 1.1
    Tipo = ["fogo"]
    mitigação = 100 / (100 + alvo["def SP"]) 
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)

def D(atacante,alvo,player,inimigo):
    Dano = atacante["atk SP"] * 1
    Tipo = ["fogo"]
    mitigação = 100 / (100 + alvo["def SP"]) 
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)