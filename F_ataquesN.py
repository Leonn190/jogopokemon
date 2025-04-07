import random
import Funções

def A(atacante,alvo,player,inimigo,F):

    pagou = 0
    for i in range(len(F["custo"])):
        if F["custo"][i] == "normal":
            for j in range(len(player[4])):
                if player[3][player[4][j]] >= 1:
                    player[3][player[4][j]] = player[3][player[4][j]] - 1
                    pagou += 1
                    break
        else:
            if player[3][F["custo"][i]] >= 1:
                player[3][F["custo"][i]] = player[3][F["custo"][i]] - 1
                pagou += 1
    
    if pagou != len(F["custo"]):
        return 0

    Dano = atacante["atk"] * F["dano"]
    Tipo = F["tipo"]
    mitigação = 100 / (100 + alvo["def"])
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)
    return 1

def B(atacante,alvo,player,inimigo,F):
    
    pagou = 0
    for i in range(len(F["custo"])):
        if F["custo"][i] == "normal":
            for j in range(len(player[4])):
                if player[3][player[4][j]] >= 1:
                    player[3][player[4][j]] = player[3][player[4][j]] - 1
                    pagou += 1
                    break
        else:
            if player[3][F["custo"][i]] >= 1:
                player[3][F["custo"][i]] = player[3][F["custo"][i]] - 1
                pagou += 1
    
    if pagou != len(F["custo"]):
        return 0

    Dano = atacante["atk"] * F["dano"]
    Tipo = F["tipo"]
    mitigação = 100 / (100 + alvo["def"])
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)
    return 1