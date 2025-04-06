import random
import Funções

def C(atacante,alvo,player,inimigo,F):

    pagou = 0
    for i in range(len(F["custo"])):
        if F["custo"][i] == "normal":
            for j in range(len(player[9])):
                if player[8][player[9][j]] >= 1:
                    player[8][player[9][j]] = player[8][player[9][j]] - 1
                    pagou += 1
                    break
        else:
            if player[8][F["custo"][i]] >= 1:
                player[8][F["custo"][i]] = player[8][F["custo"][i]] - 1
                pagou += 1
    
    if pagou != len(F["custo"]):
        return 0

    Dano = atacante["atk SP"] * C["dano"]
    Tipo = C["tipo"]
    mitigação = 100 / (100 + alvo["def SP"]) 
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)

def D(atacante,alvo,player,inimigo,F):

    pagou = 0
    for i in range(len(F["custo"])):
        if F["custo"][i] == "normal":
            for j in range(len(player[9])):
                if player[8][player[9][j]] >= 1:
                    player[8][player[9][j]] = player[8][player[9][j]] - 1
                    pagou += 1
                    break
        else:
            if player[8][F["custo"][i]] >= 1:
                player[8][F["custo"][i]] = player[8][F["custo"][i]] - 1
                pagou += 1
    
    if pagou != len(F["custo"]):
        return 0


    Dano = atacante["atk SP"] * D["dano"]
    Tipo = D["tipo"]
    mitigação = 100 / (100 + alvo["def SP"]) 
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)